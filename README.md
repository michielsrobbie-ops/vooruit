# Vooruit — website

Statische website voor **Vooruit** (Groesbeek): dakinspecties en advies, energielabel
volgens NTA 8800, en dakvensters.

Geen build-stap, geen framework, geen dependencies. Alleen HTML, CSS, JavaScript en
drie zelf gehoste lettertypen.

---

## Lokaal bekijken

De pagina's verwijzen naar elkaar met paden vanaf de root (`/dakvensters/`), dus
`index.html` dubbelklikken werkt **niet**. Draai een lokale server:

```bash
# met Python
python3 -m http.server 5173

# of met npx
npx serve .
```

In VS Code kan het ook met de extensie **Live Server**: rechtermuisknop op
`index.html` → *Open with Live Server*.

---

## Naar GitHub

```bash
git init
git add .
git commit -m "Vooruit website"
git branch -M main
git remote add origin git@github.com:<gebruiker>/vooruit-website.git
git push -u origin main
```

## Naar Vercel

1. Ga naar vercel.com → **Add New… → Project** en kies deze repository.
2. Framework Preset: **Other**. Build Command en Output Directory leeg laten.
3. Deploy.

`vercel.json` regelt de rest: caching voor lettertypen en afbeeldingen,
beveiligingsheaders, en een paar redirects van oude URL's.

Met de Vercel CLI kan het ook direct:

```bash
npx vercel        # preview
npx vercel --prod # productie
```

---

## Structuur

```
index.html                                          home
dakinspecties-en-advies/index.html
energielabel-en-advies/index.html
energetisch-onderzoek-particulieren/index.html
energetische-onderzoek-vastgoedbeheerders-woningen/index.html
dakvensters/index.html
over-ons/index.html
blog/index.html
vacature/index.html
contact/index.html
privacy-policy/index.html
cookiebeleid/index.html
404.html
sitemap.xml
robots.txt
vercel.json
assets/
  style.css        alle opmaak
  site.js          menu, cookiemelding, doorsnede-tekening
  fonts/           Archivo, Source Serif 4, IBM Plex Mono (zelf gehost)
  img/             logo, favicon, apple-touch-icon, deelafbeelding
```

De URL-structuur is gelijk aan die van de huidige WordPress-site, zodat bestaande
links en zoekresultaten blijven werken.

---

## Over de teksten

Alle inhoudelijke tekst komt van de bestaande site vooruit.biz. Er is niets
inhoudelijks verzonnen. Wel geredigeerd: spelling, interpunctie, zinsbouw, en
koppen toegevoegd waar de tekst daarom vroeg.

## Vormgeving in het kort

De kleuren komen uit het bestaande logo — de energielabelschaal van rood naar
groen. Rood hoort bij alles wat dak is, groen bij alles wat energie is.

Koppen staan in Archivo, lopende tekst in Source Serif 4, en alle maatvoering,
labels en annotaties in IBM Plex Mono. De doorsnedetekening op de homepage is
inline SVG in `index.html`; elke dienstpagina toont er een uitsnede van.

---

## Nog te doen voordat de site live gaat

- [ ] **Contactformulier aansluiten.** Het formulier op `/contact/` verstuurt nu niets.
      Er moet een verwerker achter, bijvoorbeeld FormSubmit of Formspree.
- [ ] **Privacyverklaring en cookiebeleid juridisch laten nalopen**, en aanvullen met
      KvK-nummer en btw-nummer.
- [ ] **Statistiek.** Als er een statistiekdienst komt, laad die dan in `assets/site.js`
      op de gemarkeerde plek in `pasToe()`, en alleen bij keuze `'alles'`.
- [ ] **Foto van Freddie Peters** aanleveren voor `/over-ons/`.
- [ ] **Blogartikelen overzetten.** `/blog/` verwijst nu naar de artikelen op de
      huidige site.
- [ ] **Volledige functieomschrijving** voor `/vacature/`.
- [ ] **Domein koppelen** in Vercel en de sitemap aanmelden in Google Search Console.
- [ ] Controleer of `BASIS_URL` in de canonical-tags klopt met het definitieve domein.

---

Gemaakt door [Maxx Marketing](https://maxxmarketing.eu).
