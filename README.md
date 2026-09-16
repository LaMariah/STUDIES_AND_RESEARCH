# Studies & Research — Applied Business Analytics

A portfolio of analytics and research projects from my **M.S. in Business Analytics** at the Zicklin School of Business, Baruch College (CUNY), and my applied research work, by **Gerusa Maso** ([@LaMariah](https://github.com/LaMariah)).

I'm a senior PR & events professional pivoting into **business analysis** — pairing a decade of brand, stakeholder, and campaign experience with the analytical toolkit to turn data into decisions. These projects use **R**, **Python**, **SQL**, **Quarto**, and data visualization to take datasets from raw evidence to a clear business narrative.

🔗 **Live site:** https://lamariah.github.io/STUDIES_AND_RESEARCH/

---

## ⭐ Applied research — The First-Gen Cliff (NEH Health Humanities, LaGuardia CC)

A mixed-methods study quantifying why first-generation students leave college — and turning the evidence into a launched degree program. Presented at the **SCRA Biennial Conference (2023)**.

**Key findings**
- First-gen students carry **2–3× the strain** across financial, mental-health, and academic-direction risk
- The **dropout cliff is Semester 1** (risk score 9.0), making early intervention decisive
- Compound barriers — work (71%), financial (64%), unclear career path (58%) — hit first-gen students at ~double the rate
- Findings fed the design of LaGuardia's **Health Humanities AA degree**, now live in the catalog

**Built with:** comparative survey design · qualitative transcript coding · stakeholder dashboarding
📄 **Read it:** https://lamariah.github.io/STUDIES_AND_RESEARCH/laguardia.html

---

## ⭐ Applied analytics, UN Latin Club Membership and Engagement

A privacy-safe portfolio case showing how membership segmentation, a reactivation funnel, and weekly content reporting supported retention and programming decisions.

**Key findings**
- Lapsed members represented **47%** of the reconstructed membership base
- **47 of 235** lapsed members renewed, a **20% reactivation rate**
- Digital engagement increased **15% over seven weeks**
- Endangered-languages research became the highest-performing content theme

**Built with:** Python · SQL · CSV · dashboard design · lifecycle segmentation
📄 **Explore the project:** [projects/un-membership-analytics](projects/un-membership-analytics)

---

## ⭐ Commercial analytics, Pitu Cachaça US Market Expansion

A reconstructed market-entry case showing how product education, consumer engagement, retail activation, and distributor development supported a Brazilian beverage brand in New York and New Jersey.

**Key findings**
- Active distributor accounts increased from **3 to 11** in the reconstructed campaign record
- Education-led content produced a **3.43× engagement ratio** compared with brand-led content
- Retail availability grew from about **5 to 30 locations**
- The portfolio ROI scenario estimates a **58.3% three-year return**

**Built with:** Python · SQL · campaign analytics · audience segmentation · ROI modelling
📄 **Explore the project:** [projects/pitu-market-expansion-analytics](projects/pitu-market-expansion-analytics)

---

## ⭐ Nonprofit analytics, SOS EB Kids Fundraising and Donor Journey

A privacy-conscious case showing how nonprofit storytelling, proposal development, donor-journey design, and KPI planning support fundraising decisions.

**Project highlights**
- Contributed to fundraising proposal and donor-funnel development
- Supported work connected with **BrazilFoundation funding**
- Documented individual-donor and institutional-funding journeys
- Built an illustrative analytics model without exposing donor or beneficiary data

**Built with:** Python · SQL · fundraising analytics · donor journey mapping · KPI design
📄 **Explore the project:** [projects/sos-eb-kids-fundraising-analytics](projects/sos-eb-kids-fundraising-analytics)

---

## ⭐ Final project — NYC Noise Complaints: Temporal Patterns

An analysis of NYC 311 noise-complaint data (2022–2025) examining how **time of day, day of week, and season** shape the city's noise landscape — and how young-adult neighborhoods drive the patterns.

**Key findings**
- Noise complaints peak in **summer** and on **weekend late nights**
- Neighborhoods with higher shares of **young adults** generate disproportionately more complaints
- Clear temporal rhythms point to where **noise-enforcement resources** could be targeted

**Built with:** R · Quarto · ggplot2 · NYC 311 Open Data
📄 **Read it:** https://lamariah.github.io/STUDIES_AND_RESEARCH/

---

## 🎧 Mini-project — Creating the Ultimate Playlist

A data-driven approach to building the "ultimate" Spotify playlist, analyzing audio features (danceability, energy, tempo, key) across thousands of tracks and the Million Playlist Dataset to find what makes songs work together.

**Highlights**
- Explored relationships between **energy and danceability** to anchor the playlist's feel
- Surfaced **decade representation** and **peak-danceability** tracks
- Combined the **Spotify audio-features** data with the **Million Playlist Dataset**

**Built with:** R · Quarto · ggplot2 · Spotify / Million Playlist data
📄 See `mp03.html` (open in a browser) and the source in `mp03.qmd`.

---

## 🗳️ Mini-project — The Shifting Electorate (2020 → 2024)

A county-level analysis of how U.S. presidential voting shifted between 2020 and 2024, mapping battleground movement and testing how demographic factors — education, community type, and Latino population shifts — correlate with margin changes.

**Highlights**
- Mapped **county-level vote-margin shifts** across the country
- Examined the **education divide** and **community-type** patterns behind the movement
- Built **population-weighted** views to separate real swings from small-county noise

**Built with:** R · Quarto · ggplot2 · county election & Census data
📄 **Highlights:** https://lamariah.github.io/STUDIES_AND_RESEARCH/mp04_highlights.html · full report in `mp04.html` / `mp04.qmd`

---

## 📂 Repository structure

```
├── README.md
├── projects/un-membership-analytics/       # UN membership and engagement case
├── projects/pitu-market-expansion-analytics/ # Commercial market-entry case
├── projects/sos-eb-kids-fundraising-analytics/ # Nonprofit fundraising case
├── laguardia.html                    # Applied research — The First-Gen Cliff (NEH)
├── finalprojectpresent.qmd / .html   # Final project — NYC Noise
├── mp03.qmd / mp03.html              # Mini-project — Ultimate Playlist
├── mp04.qmd / mp04.html              # Mini-project — The Shifting Electorate
├── about.qmd                         # About page
├── build_site.R                      # Renders the Quarto site into docs/
├── styles.css / custom.css           # Site styling
├── data/                             # Source datasets for the projects
└── docs/                             # Rendered site served by GitHub Pages
```

---

## 🛠️ Tools & skills

- **Analytics:** R, Python, SQL, ggplot2, segmentation, funnel analysis, exploratory data analysis
- **Reporting:** Quarto — literate programming (code + narrative + output in one document)
- **Communication:** translating analysis into clear visuals and recommendations for non-technical stakeholders
- **Nonprofit:** digital fundraising, donor journey mapping, grant pipeline design, privacy-conscious reporting
- **Workflow:** Git version control, reproducible rendering, GitHub Pages publishing
- **Data:** public/open datasets (NYC Open Data, Spotify, Million Playlist Dataset)
- **Languages:** English, Portuguese, Spanish, Italian

---

## ⚙️ Reproduce the site

```bash
# Requires R and Quarto
Rscript build_site.R
```

This renders the `.qmd` files into `docs/`, which GitHub Pages serves as the live site.

---

## 👤 About

**Gerusa Maso** — senior PR & events professional with 10+ years producing premium large-scale events and leading brand communications across Brazil, the U.S., and Europe (Formula 1 Brazilian GP, Lollapalooza, FIFA World Cup, Rio 2016, Brazilian Day Newark). Founder of the communications agency Emperialle, where campaigns grew brand engagement 25% and revenue 30%. 2019 *Community Builder of the Year* (The Garra Award × NY Women's Foundation).

Graduating with an **M.S. in Business Analytics** (Zicklin School of Business, Baruch College, 2026) and pivoting into **business analysis** — bringing stakeholder fluency and campaign-impact thinking together with data.

📍 New York · [LinkedIn](https://www.linkedin.com/in/gms123456/)
