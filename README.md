# Learning to Read the Road: From Visual Observations to Map Knowledge

## NeurIPS 2026 Workshop Website

🌐 **Live site:** [https://heshameraqi.github.io/read-road-workshop/](https://heshameraqi.github.io/read-road-workshop/)

### About

This is the official website for the "Learning to Read the Road" workshop at NeurIPS 2026. The workshop brings together researchers from computer vision, NLP, graph ML, autonomous driving, and geospatial science to tackle the pipeline from visual observation to structured map knowledge.

### Local Development

To preview the site locally:

```bash
cd /Users/heraqi/_Work/Code/Websites/read-road-workshop
python3 -m http.server 8000
```

Then open [http://localhost:8000](http://localhost:8000) in your browser.

### Adding Photos

**Speaker photos:** Replace `assets/images/speakers/placeholder.svg` references in `index.html` with actual photos:
- Place photos in `assets/images/speakers/` (e.g., `raquel_urtasun.jpg`)
- Update the `src` attribute in the corresponding `<img>` tag in `index.html`
- Recommended size: 300×300px, square crop, JPG format

**Organizer photos:** Replace `assets/images/organizers/placeholder.svg` references in `index.html` with actual photos:
- Place photos in `assets/images/organizers/` (e.g., `hesham_eraqi.jpg`)
- Update the `src` attribute in the corresponding `<img>` tag in `index.html`
- Recommended size: 300×300px, square crop, JPG format

### File Structure

```
read-road-workshop/
├── index.html                          # Main website page
├── assets/
│   ├── css/
│   │   └── style.css                   # All styles
│   ├── js/
│   │   └── main.js                     # Navigation, animations
│   └── images/
│       ├── speakers/
│       │   └── placeholder.svg         # Default speaker placeholder
│       └── organizers/
│           └── placeholder.svg         # Default organizer placeholder
└── README.md
```

### Deployment

The site is deployed via GitHub Pages from the `main` branch. Any push to `main` will automatically update the live site.

### Tech Stack

- Pure HTML5, CSS3, JavaScript (no build tools needed)
- Google Fonts (Inter)
- Font Awesome icons
- Responsive design (mobile-friendly)
