<h1 align="center">🔧 VED'S GARAGE — Portfolio</h1>

<p align="center">
  <em>A dark industrial garage-themed developer portfolio — built with zero frameworks, pure craftsmanship.</em>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" alt="HTML5" />
  <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white" alt="CSS3" />
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" alt="JavaScript" />
  <img src="https://img.shields.io/badge/GitHub%20Pages-222222?style=for-the-badge&logo=githubpages&logoColor=white" alt="GitHub Pages" />
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="MIT License" />
</p>

<p align="center">
  <a href="https://vedd023.github.io/Portfolio"><strong>🚀 View Live Demo »</strong></a>
</p>

---

## About the Project

**VED'S GARAGE** is a personal portfolio website designed around a dark industrial workshop aesthetic. Every element — from project cards styled as "vehicle spec sheets" to skill bars modeled as diagnostic gauges — reinforces the garage metaphor.

The entire site is a **single `index.html` file** with no build tools, no frameworks, and no external dependencies beyond Google Fonts. It is lightweight, fast, and deploys instantly on GitHub Pages.

---

## Features

- **Single-Page Application** — tab-based navigation across all sections, no page reloads
- **Garage-Themed UI** — noise textures, scanline overlays, hazard tape dividers, and rivet details
- **Project Vehicle Cards** — tech stack specs, build logs, status badges (`SHIPPED` / `WIP` / `PARKED`), and odometer stats
- **3D Car Showcase** — interactive Three.js rotating vehicle model on the project card
- **Driver Profile** — photo with HUD scanner effect, metadata grid, and animated skill progress bars
- **Certifications Wall** — credential cards with status indicators
- **Contact Bay** — direct links (GitHub, LinkedIn, Resume) and a message form that opens Gmail compose
- **Light / Dark Mode** — theme toggle with smooth transitions
- **Live Clock** — real-time clock display in the header
- **Scroll Reveal Animations** — elements animate into view on section switch
- **Fully Responsive** — adapts cleanly from desktop to mobile
- **Media Modal & Lightbox** — project screenshots with full-screen preview

---

## Tech Stack

| Layer     | Technology                        |
| --------- | --------------------------------- |
| Structure | HTML5 (semantic markup)           |
| Styling   | CSS3 (custom properties, grid, flexbox) |
| Logic     | Vanilla JavaScript (ES6)          |
| 3D Engine | Three.js (CDN, r128)              |
| Fonts     | Google Fonts (Bebas Neue, Share Tech Mono, Barlow, Barlow Condensed) |
| Hosting   | GitHub Pages                      |

> **No frameworks. No bundlers. No `node_modules`.** Just clean, hand-written code.

---

## Project Structure

```
Portfolio/
├── index.html              # Entire SPA — markup, styles, and scripts
├── images.json             # Project screenshot data (fetched at runtime)
├── profile.jpg             # Driver profile photo
├── Ved_Dixit_Resume.pdf    # Downloadable resume
└── README.md
```

---

## Getting Started

No install steps required. The project runs directly in any modern browser.

```bash
# 1. Clone the repository
git clone https://github.com/Vedd023/Portfolio.git

# 2. Navigate into the directory
cd Portfolio

# 3. Open in your browser
start index.html        # Windows
open index.html         # macOS
xdg-open index.html     # Linux
```

Or simply open `index.html` by double-clicking it in your file explorer.

---

## Sections Overview

| Section            | Nav Tab           | Description                                                                 |
| ------------------ | ----------------- | --------------------------------------------------------------------------- |
| **The Garage**     | ⬡ THE GARAGE      | Project showcase with vehicle-style cards, spec sheets, build logs, and 3D model |
| **Driver Profile** | ◈ DRIVER PROFILE   | Bio, skills rack with animated bars, and certifications wall                |
| **Contact Bay**    | ◉ CONTACT BAY      | GitHub, LinkedIn, resume links, current availability status, and message form |

---

## Customization

The design system is driven by **CSS custom properties** in the `:root` block. To personalize:

### Colors

Edit the variables at the top of the `<style>` block in `index.html`:

```css
:root {
  --bg: #0f0e0c;
  --surface: #1a1815;
  --rust: #c0440a;
  --rust-bright: #e85512;
  --amber: #d97b0a;
  --cream: #e8dfc8;
  /* ... */
}
```

### Content

| What to change       | Where to find it                                     |
| -------------------- | ---------------------------------------------------- |
| Name & tagline       | `.garage-name`, `.garage-sub` in the `<header>`      |
| Bio text             | `.profile-bio` inside the Driver Profile section      |
| Skills & percentages | `.skill-item` blocks and `style="width:XX%"` values  |
| Projects             | `.vehicle-card` blocks in the Garage section          |
| Certifications       | `.cert-card` blocks in the Certifications wall        |
| Contact links        | `<a>` tags inside the Contact Bay section             |
| Screenshots          | `images.json` and the inline `PORTFOLIO_IMAGES` object |

---

## License

Distributed under the **MIT License**. See [`LICENSE`](LICENSE) for details.

---

## Contact

**Ved Dixit**

- GitHub: [github.com/Vedd023](https://github.com/Vedd023)
- LinkedIn: [linkedin.com/in/ved-dixit-b279983a1](https://www.linkedin.com/in/ved-dixit-b279983a1)
- Email: veddixit28@gmail.com

---

<p align="center">
  <sub>Hand-built with ☕ and clean code — no frameworks were harmed in the making of this portfolio.</sub>
</p>
