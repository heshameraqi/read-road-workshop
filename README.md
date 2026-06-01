# Read the Road: From Visual Observations to Map Knowledge

## NeurIPS 2026 Workshop Website

🌐 **Live site:** [https://read-road.github.io/](https://read-road.github.io/)
   **Local dev mirror:** [https://heshameraqi.github.io/read-road-workshop/](https://heshameraqi.github.io/read-road-workshop/)

---

### Quick Start

```bash
# Edit content in the markdown files (see below)
# Then rebuild the site:
python3 build.py

# Preview locally:
python3 -m http.server 8000
# Open http://localhost:8000
```

---

### Editing Content

All website content is in easy-to-edit **Markdown files** in the `content/` folder. Edit any of these and re-run `python3 build.py` to regenerate `index.html`.

| File | What it controls |
|------|-----------------|
| `content/workshop.md` | Workshop title, subtitle, tagline, conference name, date, venue, contact email |
| `content/about.md` | About section text, "Why This Workshop?" and "Why Now?" sections |
| `content/topics.md` | Research topics (title, icon, description for each) |
| `content/speakers.md` | Invited speakers (name, photo, affiliation, country, talk topic) |
| `content/organizers.md` | Organizers (name, photo, affiliation, country) |
| `content/schedule.md` | Workshop schedule (time, type, title, description) |
| `content/call_for_papers.md` | Call for papers text, submission topics, guidelines, portal info |
| `content/dates.md` | Important dates (deadlines and their values) |

---

### Adding/Updating Photos

**Speaker photos:**
1. Add photo file to `assets/images/speakers/` (e.g., `raquel_urtasun.jpg`)
2. Edit `content/speakers.md` — change `- photo: placeholder.svg` to `- photo: raquel_urtasun.jpg`
3. Run `python3 build.py`

**Organizer photos:**
1. Add photo file to `assets/images/organizers/` (e.g., `hesham_eraqi.jpg`)
2. Edit `content/organizers.md` — change `- photo: placeholder.svg` to `- photo: hesham_eraqi.jpg`
3. Run `python3 build.py`

**Recommended:** 300×300px, square crop, JPG format.

---

### Adding a New Speaker

Edit `content/speakers.md` and add a new block:

```markdown
## Speaker Name
- photo: speaker_name.jpg
- affiliation: University / Company
- country: Country
- topic: Talk Title
```

Then run `python3 build.py`.

---

### File Structure

```
read-road-workshop/
├── build.py                            # Build script (generates index.html)
├── index.html                          # Generated website (DO NOT edit directly)
├── content/                            # ✏️ EDIT THESE FILES
│   ├── workshop.md                     # Title, venue, dates
│   ├── about.md                        # About section
│   ├── topics.md                       # Research topics
│   ├── speakers.md                     # Speaker list
│   ├── organizers.md                   # Organizer list
│   ├── schedule.md                     # Workshop schedule
│   ├── call_for_papers.md             # CFP details
│   └── dates.md                        # Important deadlines
├── assets/
│   ├── css/style.css                   # Styles
│   ├── js/main.js                      # Navigation, animations
│   └── images/
│       ├── speakers/placeholder.svg    # Speaker photo placeholder
│       └── organizers/placeholder.svg  # Organizer photo placeholder
├── .gitignore
└── README.md
```

---

### Deployment

**Live site:** https://read-road.github.io/

**Setup (one-time):**
```bash
cd /Users/heraqi/_Work/Code/Websites/read-road-workshop

# Remotes (already configured)
git remote add origin https://github.com/read-road/read-road.github.io.git
git remote add personal https://github.com/heshameraqi/read-road-workshop.git

# Generate a PAT at https://github.com/settings/tokens (repo scope)
# Use it as password when prompted
```

**Preview locally before pushing:**
```bash
python3 build.py
python3 -m http.server 8000
# Open http://localhost:8000 and verify changes look good
# Ctrl+C to stop the server when done
```

**Push changes:**
```bash
git add -A && git commit -m "your message"
git push origin main && git push personal main
```

GitHub Pages auto-deploys from `main` on the org repo.

---

### Tech Stack

- Pure HTML5, CSS3, JavaScript (no npm/node needed)
- Python 3 build script (stdlib only, no dependencies)
- Google Fonts (Inter)
- Font Awesome icons
- Responsive design (mobile-friendly)
