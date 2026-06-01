#!/usr/bin/env python3
"""
Build script for the Read the Road Workshop website.
Reads markdown content files from content/ and generates index.html.

Usage:
    python3 build.py

After running, open index.html in a browser or serve with:
    python3 -m http.server 8000
"""

import re
import os

CONTENT_DIR = "content"
OUTPUT_FILE = "index.html"


def read_file(filename):
    """Read a markdown file from content directory."""
    path = os.path.join(CONTENT_DIR, filename)
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def parse_workshop():
    """Parse workshop.md for basic info."""
    text = read_file("workshop.md")
    data = {}
    current_key = None
    for line in text.strip().split("\n"):
        if line.startswith("## "):
            current_key = line[3:].strip().lower().replace(" ", "_")
            data[current_key] = ""
        elif current_key and line.strip():
            data[current_key] = line.strip()
    return data


def parse_about():
    """Parse about.md content."""
    text = read_file("about.md")
    # Remove the # heading
    lines = text.strip().split("\n")
    lines = lines[1:]  # skip title
    content = "\n".join(lines).strip()
    
    # Split into main description and "Why" sections
    parts = content.split("## Why This Workshop?")
    main_text = parts[0].strip()
    
    why_workshop = ""
    why_now = ""
    if len(parts) > 1:
        remaining = parts[1]
        why_parts = remaining.split("## Why Now?")
        why_workshop = why_parts[0].strip()
        if len(why_parts) > 1:
            why_now = why_parts[1].strip()
    
    return main_text, why_workshop, why_now


def md_to_html_paragraphs(text):
    """Convert markdown paragraphs to HTML, handling bold."""
    paragraphs = text.split("\n\n")
    html_parts = []
    for p in paragraphs:
        p = p.strip()
        if not p:
            continue
        # Convert **bold** to <strong>
        p = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', p)
        # Handle bullet lists
        if p.startswith("- "):
            items = p.split("\n")
            list_html = "<ul>\n"
            for item in items:
                item = item.lstrip("- ").strip()
                item = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', item)
                list_html += f"  <li>{item}</li>\n"
            list_html += "</ul>"
            html_parts.append(list_html)
        else:
            html_parts.append(f"<p>{p}</p>")
    return "\n                    ".join(html_parts)


def parse_topics():
    """Parse topics.md into list of topic dicts."""
    text = read_file("topics.md")
    lines = text.strip().split("\n")
    
    # Get description (first non-heading line)
    description = ""
    topics = []
    current_topic = None
    
    for line in lines:
        if line.startswith("# "):
            continue
        elif line.startswith("## "):
            if current_topic:
                topics.append(current_topic)
            current_topic = {"title": line[3:].strip(), "icon": "", "description": ""}
        elif current_topic:
            if line.startswith("- icon:"):
                current_topic["icon"] = line.split(":", 1)[1].strip()
            elif line.startswith("- description:"):
                current_topic["description"] = line.split(":", 1)[1].strip()
        elif line.strip() and not current_topic:
            description = line.strip()
    
    if current_topic:
        topics.append(current_topic)
    
    return description, topics


def parse_speakers():
    """Parse speakers.md into list of speaker dicts."""
    text = read_file("speakers.md")
    lines = text.strip().split("\n")
    
    description = ""
    speakers = []
    current = None
    in_comment = False
    
    for line in lines:
        if "<!--" in line:
            in_comment = True
            continue
        if "-->" in line:
            in_comment = False
            continue
        if in_comment:
            continue
        if line.startswith("# "):
            continue
        elif line.startswith("## "):
            if current:
                speakers.append(current)
            current = {"name": line[3:].strip(), "photo": "placeholder.svg", "url": "", "affiliation": "", "country": "", "topic": ""}
        elif current:
            if line.startswith("- photo:"):
                photo = line.split(":", 1)[1].strip()
                # Check if photo file exists, fall back to placeholder
                if photo and os.path.exists(os.path.join("assets", "images", "speakers", photo)):
                    current["photo"] = photo
                else:
                    current["photo"] = "placeholder.svg"
            elif line.startswith("- url:"):
                current["url"] = line.split(":", 1)[1].strip()
                # Handle urls that got split on ":"
                if line.count(":") > 1:
                    current["url"] = ":".join(line.split(":")[1:]).strip()
            elif line.startswith("- affiliation:"):
                current["affiliation"] = line.split(":", 1)[1].strip()
            elif line.startswith("- country:"):
                current["country"] = line.split(":", 1)[1].strip()
            elif line.startswith("- topic:"):
                current["topic"] = line.split(":", 1)[1].strip()
        elif line.strip() and not current:
            description = line.strip()
    
    if current:
        speakers.append(current)
    
    return description, speakers


def parse_organizers():
    """Parse organizers.md into list of organizer dicts."""
    text = read_file("organizers.md")
    lines = text.strip().split("\n")
    
    organizers = []
    current = None
    in_comment = False
    
    for line in lines:
        if "<!--" in line:
            in_comment = True
            continue
        if "-->" in line:
            in_comment = False
            continue
        if in_comment:
            continue
        if line.startswith("# "):
            continue
        elif line.startswith("## "):
            if current:
                organizers.append(current)
            current = {"name": line[3:].strip(), "photo": "placeholder.svg", "url": "", "affiliation": "", "country": ""}
        elif current:
            if line.startswith("- photo:"):
                photo = line.split(":", 1)[1].strip()
                if photo and os.path.exists(os.path.join("assets", "images", "organizers", photo)):
                    current["photo"] = photo
                else:
                    current["photo"] = "placeholder.svg"
            elif line.startswith("- url:"):
                current["url"] = ":".join(line.split(":")[1:]).strip()
            elif line.startswith("- affiliation:"):
                current["affiliation"] = line.split(":", 1)[1].strip()
            elif line.startswith("- country:"):
                current["country"] = line.split(":", 1)[1].strip()
    
    if current:
        organizers.append(current)
    
    return organizers


def parse_schedule():
    """Parse schedule.md into list of schedule items."""
    text = read_file("schedule.md")
    lines = text.strip().split("\n")
    
    description = ""
    items = []
    current = None
    
    for line in lines:
        if line.startswith("# "):
            continue
        elif line.startswith("<!--"):
            continue
        elif line.strip().startswith("-->"):
            continue
        elif line.startswith("## "):
            if current:
                items.append(current)
            current = {"time": line[3:].strip(), "type": "talk", "title": "", "description": ""}
        elif current:
            if line.startswith("- type:"):
                current["type"] = line.split(":", 1)[1].strip()
            elif line.startswith("- title:"):
                current["title"] = line.split(":", 1)[1].strip()
            elif line.startswith("- description:"):
                current["description"] = line.split(":", 1)[1].strip()
        elif line.strip() and not current:
            description = line.strip()
    
    if current:
        items.append(current)
    
    return description, items


def parse_call_for_papers():
    """Parse call_for_papers.md."""
    text = read_file("call_for_papers.md")
    lines = text.strip().split("\n")
    
    intro = ""
    topics = []
    guidelines = []
    portal = ""
    awards = ""
    
    section = "intro"
    
    for line in lines:
        if line.startswith("# "):
            continue
        elif line.startswith("## Submission Topics"):
            section = "topics"
        elif line.startswith("## Submission Guidelines"):
            section = "guidelines"
        elif line.startswith("## Submission Portal"):
            section = "portal"
        elif line.startswith("## Awards"):
            section = "awards"
        elif line.strip():
            if section == "intro":
                intro = line.strip()
            elif section == "topics" and line.startswith("- "):
                topics.append(line[2:].strip())
            elif section == "guidelines" and line.startswith("- "):
                guidelines.append(line[2:].strip())
            elif section == "portal":
                portal = line.strip()
            elif section == "awards":
                awards = line.strip()
    
    # Convert markdown bold
    intro = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', intro)
    guidelines = [re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', g) for g in guidelines]
    
    return intro, topics, guidelines, portal, awards


def parse_challenges():
    """Parse challenges.md into intro, tracks, timeline, and note."""
    text = read_file("challenges.md")
    lines = text.strip().split("\n")
    
    intro = ""
    tracks = []
    timeline = []
    note = ""
    current_track = None
    section = "intro"
    
    for line in lines:
        if line.startswith("# "):
            continue
        elif line.startswith("## Track"):
            section = "tracks"
            if current_track:
                tracks.append(current_track)
            current_track = {"title": line[3:].strip(), "icon": "", "description": "", "metrics": "", "prize_1st": "", "prize_2nd": "", "prize_3rd": ""}
        elif line.startswith("## Timeline"):
            section = "timeline"
            if current_track:
                tracks.append(current_track)
                current_track = None
        elif line.startswith("## Note"):
            section = "note"
        elif section == "intro" and line.strip():
            intro += (" " if intro else "") + line.strip()
        elif section == "tracks" and current_track:
            if line.startswith("- icon:"):
                current_track["icon"] = line.split(":", 1)[1].strip()
            elif line.startswith("- description:"):
                current_track["description"] = line.split(":", 1)[1].strip()
            elif line.startswith("- metrics:"):
                current_track["metrics"] = line.split(":", 1)[1].strip()
            elif line.startswith("- prize_1st:"):
                current_track["prize_1st"] = line.split(":", 1)[1].strip()
            elif line.startswith("- prize_2nd:"):
                current_track["prize_2nd"] = line.split(":", 1)[1].strip()
            elif line.startswith("- prize_3rd:"):
                current_track["prize_3rd"] = line.split(":", 1)[1].strip()
        elif section == "timeline" and line.startswith("- "):
            timeline.append(line[2:].strip())
        elif section == "note" and line.strip():
            note += (" " if note else "") + line.strip()
    
    if current_track:
        tracks.append(current_track)
    
    return intro, tracks, timeline, note


def parse_dates():
    """Parse dates.md."""
    text = read_file("dates.md")
    lines = text.strip().split("\n")
    
    note = ""
    dates = []
    current_label = None
    
    for line in lines:
        if line.startswith("# "):
            continue
        elif line.startswith("## "):
            current_label = line[3:].strip()
        elif current_label and line.strip():
            dates.append({"label": current_label, "value": line.strip()})
            current_label = None
        elif line.strip() and not current_label:
            note = line.strip()
    
    return note, dates


def generate_html():
    """Generate the full index.html from content files."""
    
    # Parse all content
    workshop = parse_workshop()
    about_text, why_workshop, why_now = parse_about()
    topics_desc, topics = parse_topics()
    speakers_desc, speakers = parse_speakers()
    organizers = parse_organizers()
    schedule_desc, schedule_items = parse_schedule()
    cfp_intro, cfp_topics, cfp_guidelines, cfp_portal, cfp_awards = parse_call_for_papers()
    dates_note, dates = parse_dates()
    challenge_intro, challenge_tracks, challenge_timeline, challenge_note = parse_challenges()
    
    # Convert about text to HTML
    about_html = md_to_html_paragraphs(about_text)
    
    # Generate topics HTML
    topics_html = ""
    for t in topics:
        topics_html += f"""
                <div class="topic-card">
                    <div class="topic-icon"><i class="fas {t['icon']}"></i></div>
                    <h3>{t['title']}</h3>
                    <p>{t['description']}</p>
                </div>"""
    
    # Generate speakers HTML
    speakers_html = ""
    for s in speakers:
        name_html = f'<a href="{s["url"]}" target="_blank">{s["name"]}</a>' if s.get("url") else s["name"]
        speakers_html += f"""
                <div class="speaker-card">
                    <div class="speaker-image">
                        <img src="assets/images/speakers/{s['photo']}" alt="{s['name']}">
                    </div>
                    <h3 class="speaker-name">{name_html}</h3>
                    <p class="speaker-affiliation">{s['affiliation']}</p>
                    <p class="speaker-topic">{s['topic']}</p>
                </div>"""
    
    # Generate organizers HTML
    organizers_html = ""
    for o in organizers:
        name_html = f'<a href="{o["url"]}" target="_blank">{o["name"]}</a>' if o.get("url") else o["name"]
        organizers_html += f"""
                <div class="organizer-card">
                    <div class="organizer-image">
                        <img src="assets/images/organizers/{o['photo']}" alt="{o['name']}">
                    </div>
                    <h3>{name_html}</h3>
                    <p class="organizer-affiliation">{o['affiliation']}</p>
                    <p class="organizer-location"><i class="fas fa-map-marker-alt"></i> {o['country']}</p>
                </div>"""
    
    # Generate schedule HTML
    schedule_html = ""
    for item in schedule_items:
        css_class = "schedule-item"
        if item["type"] == "break":
            css_class += " schedule-break"
        elif item["type"] == "panel":
            css_class += " schedule-highlight"
        
        icon = ""
        if item["type"] == "break":
            if "lunch" in item["title"].lower():
                icon = '<i class="fas fa-utensils"></i> '
            else:
                icon = '<i class="fas fa-coffee"></i> '
        
        desc_html = ""
        if item["description"]:
            desc_html = f'\n                        <p>{item["description"]}</p>'
        
        # Calculate duration from time range
        time_parts = item["time"].split("–")
        if len(time_parts) == 2:
            start = time_parts[0].strip().split(":")
            end = time_parts[1].strip().split(":")
            if len(start) == 2 and len(end) == 2:
                duration = (int(end[0]) * 60 + int(end[1])) - (int(start[0]) * 60 + int(start[1]))
                duration_str = f"{duration} min"
            else:
                duration_str = ""
        else:
            duration_str = ""
        
        schedule_html += f"""
                <div class="{css_class}">
                    <div class="schedule-time">{item['time']}</div>
                    <div class="schedule-content">
                        <h3>{icon}{item['title']}</h3>{desc_html}
                        <span class="schedule-duration">{duration_str}</span>
                    </div>
                </div>"""
    
    # Generate CFP topics HTML
    cfp_topics_html = "\n".join([f"                        <li>{t}</li>" for t in cfp_topics])
    
    # Generate CFP guidelines HTML
    cfp_guidelines_html = "\n".join([f"                        <li>{g}</li>" for g in cfp_guidelines])
    
    # Generate dates HTML
    dates_html = ""
    for d in dates:
        dates_html += f"""
                <div class="date-item">
                    <div class="date-marker"></div>
                    <div class="date-content">
                        <h3>{d['label']}</h3>
                        <p class="date-value">{d['value']}</p>
                    </div>
                </div>"""
    
    # Generate challenge tracks HTML
    challenge_tracks_html = ""
    for t in challenge_tracks:
        challenge_tracks_html += f"""
                <div class="challenge-track">
                    <div class="challenge-track-header">
                        <div class="challenge-track-icon"><i class="fas {t['icon']}"></i></div>
                        <h3>{t['title']}</h3>
                    </div>
                    <p class="challenge-track-desc">{t['description']}</p>
                    <div class="challenge-track-meta">
                        <div class="challenge-metrics"><i class="fas fa-chart-bar"></i> <strong>Metrics:</strong> {t['metrics']}</div>
                        <div class="challenge-prizes">
                            <span class="prize gold"><i class="fas fa-trophy"></i> 1st: {t['prize_1st']}</span>
                            <span class="prize silver"><i class="fas fa-medal"></i> 2nd: {t['prize_2nd']}</span>
                            <span class="prize bronze"><i class="fas fa-award"></i> 3rd: {t['prize_3rd']}</span>
                        </div>
                    </div>
                </div>"""
    
    challenge_timeline_html = "\n".join([f'                    <li>{item}</li>' for item in challenge_timeline])
    
    # Build complete HTML
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{workshop.get('title', 'Workshop')} | {workshop.get('conference', 'NeurIPS 2026')}</title>
    <meta name="description" content="{workshop.get('title', '')}: {workshop.get('subtitle', '')} - {workshop.get('conference', '')}">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
    <link rel="stylesheet" href="assets/css/style.css">
</head>
<body>
    <!-- Navigation -->
    <nav class="navbar" id="navbar">
        <div class="nav-container">
            <a href="#" class="nav-logo">Read the Road Workshop</a>
            <button class="nav-toggle" id="nav-toggle" aria-label="Toggle navigation">
                <span></span>
                <span></span>
                <span></span>
            </button>
            <ul class="nav-menu" id="nav-menu">
                <li><a href="#about" class="nav-link">About</a></li>
                <li><a href="#topics" class="nav-link">Topics</a></li>
                <li><a href="#challenge" class="nav-link">Challenge</a></li>
                <li><a href="#speakers" class="nav-link">Speakers</a></li>
                <li><a href="#schedule" class="nav-link">Schedule</a></li>
                <li><a href="#cfp" class="nav-link">Call for Papers</a></li>
                <li><a href="#organizers" class="nav-link">Organizers</a></li>
                <li><a href="#dates" class="nav-link">Dates</a></li>
            </ul>
        </div>
    </nav>

    <!-- Hero Section -->
    <header class="hero" id="hero">
        <img src="assets/images/hero-bg.gif" alt="" class="hero-bg-gif">
        <div class="hero-overlay"></div>
        <div class="hero-content">
            <div class="hero-badge">{workshop.get('conference', 'NeurIPS 2026 Workshop')}</div>
            <h1 class="hero-title">{workshop.get('title', 'Read the Road Workshop')}</h1>
            <p class="hero-subtitle">{workshop.get('subtitle', 'From Visual Observations to Map Knowledge')}</p>
            <p class="hero-tagline">{workshop.get('tagline', '')}</p>
            <div class="hero-info">
                <div class="hero-info-item">
                    <i class="fas fa-calendar-alt"></i>
                    <span>{workshop.get('date', 'December 2026')}</span>
                </div>
                <div class="hero-info-item">
                    <i class="fas fa-map-marker-alt"></i>
                    <span>{workshop.get('venue', 'NeurIPS 2026 Venue')}</span>
                </div>
                <div class="hero-info-item">
                    <i class="fas fa-clock"></i>
                    <span>{workshop.get('duration', 'Full-Day Workshop')}</span>
                </div>
            </div>
        </div>
        <div class="hero-scroll">
            <a href="#about"><i class="fas fa-chevron-down"></i></a>
        </div>
    </header>

    <!-- About Section -->
    <section class="section" id="about">
        <div class="container">
            <h2 class="section-title">About the Workshop</h2>
            <div class="about-content">
                <div class="about-text">
                    {about_html}
                </div>
                <div class="about-highlights">
                    <div class="highlight-card">
                        <div class="highlight-icon"><i class="fas fa-eye"></i></div>
                        <h3>Vision</h3>
                        <p>VLMs can "see" roads but cannot "read" them into maps</p>
                    </div>
                    <div class="highlight-card">
                        <div class="highlight-icon"><i class="fas fa-project-diagram"></i></div>
                        <h3>Graphs</h3>
                        <p>GNNs + vision convergence is underexplored for map construction</p>
                    </div>
                    <div class="highlight-card">
                        <div class="highlight-icon"><i class="fas fa-sync-alt"></i></div>
                        <h3>Freshness</h3>
                        <p>10–15% of road attributes change annually; maps need real-time maintenance</p>
                    </div>
                    <div class="highlight-card">
                        <div class="highlight-icon"><i class="fas fa-users"></i></div>
                        <h3>Community</h3>
                        <p>No unifying venue exists for visual-to-map research</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Topics Section -->
    <section class="section section-alt" id="topics">
        <div class="container">
            <h2 class="section-title">Research Topics</h2>
            <p class="section-description">{topics_desc}</p>
            <div class="topics-grid">{topics_html}
            </div>
        </div>
    </section>

    <!-- Benchmark Challenge Section -->
    <section class="section" id="challenge">
        <div class="container">
            <h2 class="section-title">Benchmark Challenge</h2>
            <p class="section-description">{challenge_intro}</p>
            <div class="challenge-tracks">{challenge_tracks_html}
            </div>
            <div class="challenge-timeline">
                <h3><i class="fas fa-calendar-check"></i> Challenge Timeline</h3>
                <ul>
{challenge_timeline_html}
                </ul>
            </div>
            <p class="challenge-note">{challenge_note}</p>
        </div>
    </section>

    <!-- Speakers Section -->
    <section class="section section-alt" id="speakers">
        <div class="container">
            <h2 class="section-title">Invited Speakers</h2>
            <p class="section-description">{speakers_desc}</p>
            <div class="speakers-grid">{speakers_html}
            </div>
        </div>
    </section>

    <!-- Schedule Section -->
    <section class="section section-alt" id="schedule">
        <div class="container">
            <h2 class="section-title">Workshop Schedule</h2>
            <p class="section-description">{schedule_desc}</p>
            <div class="schedule-table">{schedule_html}
            </div>
        </div>
    </section>

    <!-- Call for Papers Section -->
    <section class="section" id="cfp">
        <div class="container">
            <h2 class="section-title">Call for Papers</h2>
            <div class="cfp-content">
                <div class="cfp-main">
                    <p>{cfp_intro}</p>
                    
                    <h3>Submission Topics Include (but are not limited to):</h3>
                    <ul class="cfp-topics">
{cfp_topics_html}
                    </ul>

                    <h3>Submission Guidelines</h3>
                    <ul class="cfp-guidelines">
{cfp_guidelines_html}
                    </ul>
                </div>
                <div class="cfp-sidebar">
                    <div class="cfp-box">
                        <h3><i class="fas fa-file-alt"></i> Submission Portal</h3>
                        <p>{cfp_portal}</p>
                        <a href="#" class="btn btn-primary btn-disabled">Submit Paper</a>
                    </div>
                    <div class="cfp-box">
                        <h3><i class="fas fa-award"></i> Awards</h3>
                        <p>{cfp_awards}</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Important Dates Section -->
    <section class="section section-alt" id="dates">
        <div class="container">
            <h2 class="section-title">Important Dates</h2>
            <div class="dates-timeline">{dates_html}
            </div>
            <p class="dates-note">{dates_note}</p>
        </div>
    </section>

    <!-- Organizers Section -->
    <section class="section" id="organizers">
        <div class="container">
            <h2 class="section-title">Organizers</h2>
            <div class="organizers-grid">{organizers_html}
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer class="footer">
        <div class="container">
            <div class="footer-content">
                <div class="footer-info">
                    <h3>{workshop.get('title', 'Read the Road')}</h3>
                    <p>{workshop.get('conference', 'NeurIPS 2026 Workshop')}</p>
                </div>
                <div class="footer-links">
                    <a href="#about">About</a>
                    <a href="#topics">Topics</a>
                    <a href="#speakers">Speakers</a>
                    <a href="#schedule">Schedule</a>
                    <a href="#cfp">Call for Papers</a>
                </div>
                <div class="footer-contact">
                    <p><i class="fas fa-envelope"></i> Contact: <a href="mailto:{workshop.get('contact_email', '')}">{workshop.get('contact_email', '')}</a></p>
                </div>
            </div>
            <div class="footer-bottom">
                <p>&copy; 2026 {workshop.get('title', 'Read the Road')} Workshop. All rights reserved.</p>
            </div>
        </div>
    </footer>

    <script src="assets/js/main.js"></script>
</body>
</html>"""
    
    return html


def main():
    html = generate_html()
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"✅ Built {OUTPUT_FILE} from content/ markdown files.")
    print(f"   Preview: python3 -m http.server 8000")


if __name__ == "__main__":
    main()
