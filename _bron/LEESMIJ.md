# Bron van de generator

De site in de bovenliggende map is *gegenereerd*. `build.py` is het script dat alle
pagina's uitschrijft: de teksten, de doorsnedetekening, de koppen en voetteksten,
de SEO-tags, de sitemap en de configuratiebestanden staan er allemaal in.

Je hebt dit niet nodig om de site te draaien of te deployen — die is gewoon statische
HTML. Het is er voor als er iets aan meerdere pagina's tegelijk moet veranderen
(een telefoonnummer, de navigatie, de footer, een stuk opmaak). Dan is één regel in
`build.py` aanpassen sneller en veiliger dan negentien bestanden langslopen.

## Draaien

```bash
cd _bron
python3 build.py
```

Het script verwacht een map `assets/` naast zich met `style.css`, `fonts.css.tmpl`,
`fonts/` en `img/`. Die staan één niveau hoger in `../assets/`; kopieer ze ernaast
of pas de paden bovenin het script aan. De uitvoer belandt in `dist/site/`.

Losse pagina's aanpassen kan natuurlijk ook gewoon direct in de HTML. Doe dan wel
allebei, of laat het script erbuiten — anders overschrijft een volgende run je
handmatige wijziging.
