# -*- coding: utf-8 -*-
"""Bouwt de Vooruit-site.

Uitgangspunt: de bestaande structuur en de bestaande teksten van vooruit.biz.
Er is niets inhoudelijks verzonnen; er is alleen geredigeerd (spelling, interpunctie,
zinsbouw) en er zijn koppen toegevoegd waar de tekst daarom vroeg.
"""
import base64, pathlib, shutil

UIT = pathlib.Path('dist'); UIT.mkdir(exist_ok=True)
CSS = pathlib.Path('assets/style.css').read_text(encoding='utf-8')
LOGO_B64 = 'data:image/png;base64,' + base64.b64encode(pathlib.Path('assets/img/vooruit-logo.png').read_bytes()).decode()
FONTTMPL = pathlib.Path('assets/fonts.css.tmpl').read_text(encoding='utf-8')

BASIS_URL = 'https://www.vooruit.biz'
TEL1, TEL2 = '024-8457371', '06-21941107'
TEL1_INT, TEL2_INT = '+31248457371', '+31621941107'
MAIL = 'info@vooruit.biz'
SLOGAN = ('VOORUIT, het adres voor eerlijke en transparante dienstverlening met eenvoud '
          'op het gebied van daken, energiezuinigheid voor woningen en dakvensters.')

MODE = 'multi'

def fontcss(inline):
    if not inline:
        return FONTTMPL.replace('FONTS/', 'fonts/')
    uit = FONTTMPL
    for f in sorted(pathlib.Path('assets/fonts').glob('*.woff2')):
        d = 'data:font/woff2;base64,' + base64.b64encode(f.read_bytes()).decode()
        uit = uit.replace('FONTS/' + f.name, d)
    return uit

def L(slug):
    if slug == 'home':
        return '/' if MODE == 'multi' else '#/home'
    return f'/{slug}/' if MODE == 'multi' else f'#/{slug}'

# ---------------------------------------------------------------- de doorsnede
def doorsnede(uid, viewbox='0 0 880 620', actief=None, callouts=True, anim=True):
    a = f' data-actief="{actief}"' if actief else ''
    an = ' dsn-anim' if anim else ''
    co = ''
    if callouts:
        co = f'''
      <g class="g-callouts">
        <a class="dsn-callout co1" href="{L('dakinspecties-en-advies')}" data-zone="1">
          <text class="dsn-tekst dsn-tekst--nr" x="675" y="76">1 &#8212; NOK &amp; DAKVLAK</text>
          <text class="dsn-tekst" x="675" y="92" font-size="11">dakinspecties en advies</text>
          <line class="dsn-fijn" x1="670" y1="102" x2="862" y2="102"/>
          <polyline class="dsn-fijn" points="670,102 546,84 445,71"/>
          <circle class="dsn-punt" cx="440" cy="70" r="5.5"/>
        </a>
        <a class="dsn-callout co2" href="{L('dakvensters')}" data-zone="2">
          <text class="dsn-tekst dsn-tekst--nr" x="675" y="232">2 &#8212; DAKVENSTER</text>
          <text class="dsn-tekst" x="675" y="248" font-size="11">dakvensters plaatsen</text>
          <line class="dsn-fijn" x1="668" y1="258" x2="862" y2="258"/>
          <polyline class="dsn-fijn" points="668,258 581,181"/>
          <circle class="dsn-punt" cx="578" cy="178" r="5.5"/>
        </a>
        <a class="dsn-callout co3" href="{L('energielabel-en-advies')}" data-zone="3">
          <text class="dsn-tekst dsn-tekst--nr" x="205" y="380" text-anchor="end">THERMISCHE SCHIL &#8212; 3</text>
          <text class="dsn-tekst" x="205" y="396" text-anchor="end" font-size="11">energielabel en advies</text>
          <line class="dsn-fijn" x1="18" y1="406" x2="210" y2="406"/>
          <polyline class="dsn-fijn" points="210,406 245,410 259,412"/>
          <circle class="dsn-punt" cx="257" cy="412" r="5.5"/>
        </a>
      </g>'''
    return f'''<svg class="dsn{an}" viewBox="{viewbox}"{a} role="img" aria-labelledby="t{uid} d{uid}">
      <title id="t{uid}">Doorsnede van een woning met hellend dak</title>
      <desc id="d{uid}">De drie diensten van Vooruit op hun plek in het gebouw: het dakvlak en de nok, het dakvenster, en de thermische schil van kruipruimte tot nok.</desc>
      <defs><pattern id="aarde{uid}" width="13" height="13" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">
        <line x1="0" y1="0" x2="0" y2="13" stroke="#7E858C" stroke-width="1" opacity=".34"/></pattern></defs>

      <g class="g-grond">
        <rect class="dsn-vul" x="120" y="530" width="660" height="72" fill="url(#aarde{uid})"/>
        <line class="dsn-lijn" x1="120" y1="530" x2="780" y2="530"/>
      </g>
      <g class="g-fundering">
        <rect class="dsn-lijn" x="250" y="530" width="14" height="56"/>
        <rect class="dsn-lijn" x="616" y="530" width="14" height="56"/>
      </g>
      <g class="z3" style="--vertraag:.52s">
        <rect class="dsn-lijn" x="250" y="470" width="380" height="12"/>
        <line class="dsn-fijn" x1="264" y1="496" x2="616" y2="496"/>
        <line class="dsn-hulp" x1="264" y1="482" x2="264" y2="530"/>
        <line class="dsn-hulp" x1="616" y1="482" x2="616" y2="530"/>
        <g class="dsn-fijn">
          <line x1="272" y1="496" x2="286" y2="482"/><line x1="302" y1="496" x2="316" y2="482"/>
          <line x1="332" y1="496" x2="346" y2="482"/><line x1="362" y1="496" x2="376" y2="482"/>
          <line x1="392" y1="496" x2="406" y2="482"/><line x1="422" y1="496" x2="436" y2="482"/>
          <line x1="452" y1="496" x2="466" y2="482"/><line x1="482" y1="496" x2="496" y2="482"/>
          <line x1="512" y1="496" x2="526" y2="482"/><line x1="542" y1="496" x2="556" y2="482"/>
          <line x1="572" y1="496" x2="586" y2="482"/><line x1="602" y1="496" x2="616" y2="482"/>
        </g>
      </g>
      <g class="z3" style="--vertraag:.78s">
        <rect class="dsn-lijn" x="250" y="262" width="14" height="208"/>
        <rect class="dsn-lijn" x="616" y="262" width="14" height="208"/>
        <rect class="dsn-fijn" x="270" y="398" width="26" height="72"/>
        <rect class="dsn-fijn" x="580" y="396" width="30" height="36"/>
        <rect class="dsn-fijn" x="580" y="296" width="30" height="34"/>
      </g>
      <g class="g-vloer">
        <rect class="dsn-lijn" x="250" y="250" width="380" height="12"/>
        <rect class="dsn-lijn" x="250" y="360" width="380" height="10"/>
      </g>
      <g class="z3" style="--vertraag:1.16s">
        <polyline class="dsn-fijn" points="237,282 440,104 643,282"/>
        <g class="dsn-fijn">
          <line x1="260" y1="227" x2="277" y2="247"/><line x1="280" y1="210" x2="297" y2="230"/>
          <line x1="300" y1="192" x2="317" y2="212"/><line x1="320" y1="175" x2="337" y2="195"/>
          <line x1="350" y1="149" x2="367" y2="169"/><line x1="370" y1="131" x2="387" y2="151"/>
          <line x1="390" y1="114" x2="407" y2="134"/><line x1="410" y1="96" x2="427" y2="116"/>
        </g>
      </g>
      <g class="z1">
        <polyline class="dsn-lijn" points="220,262 440,70 660,262"/>
        <line class="dsn-lijn" x1="440" y1="70" x2="440" y2="104"/>
        <g class="dsn-fijn">
          <line x1="460" y1="88" x2="443" y2="107"/><line x1="480" y1="105" x2="463" y2="124"/>
          <line x1="500" y1="122" x2="483" y2="142"/>
        </g>
        <path class="dsn-fijn" d="M220 262 a9 9 0 0 0 9 9 l8 0"/>
        <path class="dsn-fijn" d="M660 262 a9 9 0 0 1 -9 9 l-8 0"/>
      </g>
      <g class="g-schoorsteen">
        <polygon class="dsn-lijn" points="300,110 330,110 330,166 300,192" fill="var(--kalk)"/>
        <rect class="dsn-lijn" x="293" y="101" width="44" height="9" fill="var(--kalk)"/>
      </g>
      <g class="z2">
        <polygon class="dsn-lijn" points="505,127 565,179 573,170 513,118"/>
        <polygon class="dsn-lijn" points="573,170 500,139 502,133 575,164"/>
        <line class="dsn-fijn" x1="509" y1="126" x2="568" y2="177"/>
      </g>{co}
    </svg>'''

# ---------------------------------------------------------------- bouwstenen
def sec(inner, nr=None, titel=None, bij=None, donker=False):
    kop = ''
    if titel or nr:
        kop = '<div class="sectiekop">'
        if nr:    kop += f'<p class="sectiekop__nr tk">{nr}</p>'
        if titel: kop += f'<h2 class="disp sectiekop__titel">{titel}</h2>'
        if bij:   kop += f'<p class="sectiekop__bij">{bij}</p>'
        kop += '</div>'
    k = ' sectie--donker' if donker else ''
    return f'<section class="sectie{k}"><div class="omhulsel">{kop}{inner}</div></section>'

def punten(items, groen=False):
    g = ' punten--groen' if groen else ''
    li = ''.join(f'<li><span class="chev" aria-hidden="true"></span><span>{i}</span></li>' for i in items)
    return f'<ul class="punten{g}">{li}</ul>'

def kaarten(items, cols=3):
    uit = []
    for i in items:
        kop = '<p class="kaart__kop">%s</p>' % i[0] if i[0] else ''
        uit.append('<div class="kaart">%s<h3>%s</h3><p>%s</p></div>' % (kop, i[1], i[2]))
    return '<div class="rooster rooster--%d">%s</div>' % (cols, ''.join(uit))

def pakketten(items, cols=3):
    uit = []
    for naam, kleur, regels in items:
        li = ''.join('<li><span class="chev" aria-hidden="true"></span><span>%s</span></li>' % r for r in regels)
        uit.append('<div class="pakket"><div class="pakket__kop"><span class="tk">Pakket</span>'
                   '<span class="pakket__merk" style="background:%s"></span></div>'
                   '<h3 class="pakket__naam">%s</h3><ul class="pakket__lijst">%s</ul>'
                   '<a class="pakket__prijs" href="%s">Prijs op aanvraag '
                   '<span class="chev" aria-hidden="true"></span></a></div>'
                   % (kleur, naam, li, L('contact')))
    return '<div class="pakketten pakketten--%d">%s</div>' % (cols, ''.join(uit))

def cta(titel, tekst):
    return ('<section class="sectie sectie--donker"><div class="omhulsel"><div class="prijs">'
            f'<div><p class="tk" style="margin-bottom:1rem">Adres en contact</p>'
            f'<h2 class="disp" style="font-size:var(--t-h2)">{titel}</h2>'
            f'<p class="prijs__slot">{tekst}</p>'
            f'<div class="hero__acties"><a class="knop" href="tel:{TEL1_INT}">Bel {TEL1}</a>'
            f'<a class="knop knop--leeg" href="mailto:{MAIL}">Mail ons</a></div></div>'
            '<div class="gegevens">'
            f'<div class="gegeven"><p class="tk">Telefoon</p><a href="tel:{TEL1_INT}">{TEL1}</a><br>'
            f'<a href="tel:{TEL2_INT}">{TEL2}</a></div>'
            f'<div class="gegeven"><p class="tk">E-mail</p><a href="mailto:{MAIL}">{MAIL}</a></div>'
            '<div class="gegeven"><p class="tk">Adres</p><p style="font-size:var(--t-lead)">Vooruit<br>'
            'Knapheideweg 55<br>6562 DR Groesbeek</p></div>'
            '</div></div></div></section>')

def kruimels(paden):
    """paden: lijst van (label, slug of None voor de huidige pagina)"""
    li = []
    for i, (label, slug) in enumerate(paden):
        if i: li.append('<li aria-hidden="true"><span class="chev"></span></li>')
        if slug: li.append(f'<li><a href="{L(slug)}">{label}</a></li>')
        else:    li.append(f'<li><span aria-current="page">{label}</span></li>')
    return f'<nav class="kruimels omhulsel tk" aria-label="Kruimelpad"><ol>{"".join(li)}</ol></nav>'

VB = {'1':'230 20 480 320', '2':'330 40 480 320', '3':'150 60 480 320', '4':'180 300 480 320'}
VB_VOL = '140 30 620 413'

def paginakop(oog, titel, lead, uid, viewbox, zone, knoppen=None, blad='Doorsnede &#183; volledig',
              tek='TEK. VW-00', vol=False):
    kn = knoppen or [('Neem contact op', L('contact'), True)]
    kh = ''
    for t, h, pr in kn:
        klas = 'knop' if pr else 'knop knop--leeg'
        chev = ' <span class="chev" aria-hidden="true"></span>' if pr else ''
        kh += '<a class="%s" href="%s">%s%s</a>' % (klas, h, t, chev)
    return (f'<section class="paginakop omhulsel"><div class="paginakop__grid"><div>'
            f'<p class="paginakop__oog tk"><span class="chev" aria-hidden="true"></span> {oog}</p>'
            f'<h1 class="disp paginakop__titel">{titel}</h1>'
            f'<p class="paginakop__lead">{lead}</p>'
            f'<div class="paginakop__acties">{kh}</div></div>'
            f'<figure class="detail" style="margin:0"><div class="detail__titelblok">'
            f'<span class="tk">{blad}</span><span class="tk">{tek}</span></div>'
            f'<div class="detail__vlak{" detail--vol" if vol else ""}">'
            f'{doorsnede(uid, viewbox, actief=zone, callouts=False, anim=False)}</div>'
            f'</figure></div></section>')

# ---------------------------------------------------------------- pagina's
NAV = [('dakinspecties-en-advies','Dakinspecties'), ('energielabel-en-advies','Energielabel'),
       ('dakvensters','Dakvensters'), ('over-ons','Over ons'), ('blog','Blog'), ('contact','Contact')]

def p_home():
    hero = f'''<section class="hero omhulsel"><div class="hero__grid"><div>
      <p class="hero__oog tk"><span class="chev" aria-hidden="true"></span> Groesbeek &#183; opgericht in 2013</p>
      <h1 class="disp hero__titel">Expert in daken en<br><em>energiezuinigheid</em></h1>
      <p class="hero__lead">VOORUIT is het adres voor eerlijke en transparante dienstverlening met eenvoud, op het gebied van daken, energiezuinigheid voor woningen en dakvensters. Voor zowel bedrijven als particulieren.</p>
      <div class="hero__acties">
        <a class="knop" href="{L('contact')}">Neem contact op <span class="chev" aria-hidden="true"></span></a>
        <a class="knop knop--leeg" href="tel:{TEL1_INT}">{TEL1}</a></div>
      <ul class="hero__keur tk">
        <li>Eenvoud en transparantie</li><li>Begrijpelijke taal</li><li>Korte lijnen</li></ul>
      </div>
      <figure class="doorsnede" data-doorsnede style="margin:0">
        <figcaption class="tk" style="margin-bottom:.8rem">Doorsnede &#183; waar Vooruit aan het werk gaat</figcaption>
        {doorsnede('h')}
      </figure></div></section>'''

    bladen = [
      ('Punt 1 &#183; nok &amp; dakvlak','var(--dak)','Dakinspecties<br>en advies','dakinspecties-en-advies','1','dak',
       'Inspectie of advies nodig over uw dak of dakconstructie? Vooruit helpt u verder door een grondige analyse met rapportage van alle mogelijkheden met betrekking tot uw dak. Voor zowel bedrijven als particulieren.','Naar dakinspecties'),
      ('Punt 2 &#183; dakvenster','var(--label-e)','Dakvensters','dakvensters','2','dak',
       'Dakvensters en dakramen plaatsen, vervangen, onderhouden &#233;n repareren voor particulieren en bedrijven. Maak gebruik van onze expertise en jarenlange ervaring en informeer naar al onze mogelijkheden.','Naar dakvensters'),
      ('Punt 3 &#183; thermische schil','var(--label-b)','Energielabel<br>en advies','energielabel-en-advies','3','energie',
       'Energielabel en advies voor uw woning en/of bedrijfspand? Vooruit kan u van dienst zijn en samen met u tot de meest optimale en energiezuinigste oplossing komen. Voor zowel bedrijven als particulieren.','Naar energielabels'),
    ]
    lg = ''.join(f'''<a class="blad blad--{kl}" href="{L(sl)}" data-zone="{z}">
        <div class="blad__titelblok"><span class="tk">{lab}</span><span class="blad__merk" style="background:{kleur}"></span></div>
        <div class="blad__lijf"><h2 class="disp blad__naam">{nm}</h2><p class="blad__tekst">{tx}</p>
        <span class="blad__meer">{meer} <span class="chev" aria-hidden="true"></span></span></div></a>'''
        for lab, kleur, nm, sl, z, kl, tx, meer in bladen)

    diensten = sec(f'<div class="legenda" data-legenda>{lg}</div>', '01 &#8212; Diensten',
        'Drie diensten, &#233;&#233;n gebouw',
        'Vooruit is gespecialiseerd in daken en energieprestatieadvies voor woningen, en geeft onafhankelijk advies op basis van kennis en betrouwbaarheid.')

    over = sec('<div class="tweekolom"><div class="tekst">'
      '<h3>Een klein bedrijf, gespecialiseerd in dak- en energieadvies</h3>'
      '<p>VOORUIT is een klein bedrijf dat is gespecialiseerd in dak- en energieadvies, opgericht in 2013. Belangrijke basis is eenvoud en eerlijkheid.</p>'
      '<p>Onafhankelijk advies op basis van kennis en betrouwbaarheid, opgebouwd met circa 30 jaar ervaring in daken en circa 8 jaar ervaring in energetische adviestrajecten.</p>'
      f'<p><a href="{L("over-ons")}">Meer over Vooruit en Freddie Peters</a></p>'
      '</div><div><p class="tk" style="margin-bottom:.4rem">Waar Vooruit voor staat</p>' + punten([
        '<strong>Eenvoud en transparantie.</strong>',
        '<strong>Duidelijkheid en begrijpelijke taal.</strong>',
        '<strong>Korte lijnen en goede communicatie.</strong>',
      ]) + '</div></div>', '02 &#8212; Over Vooruit', 'Eenvoud en eerlijkheid<br>als basis')

    vac = sec('<div class="tweekolom"><div class="tekst">'
      '<h3>Kom jij ons team versterken?</h3>'
      '<p>Wij zijn op zoek naar een EP-W basis adviseur. Het werkgebied is hoofdzakelijk regio Nijmegen &#8211; Arnhem &#8211; Wijchen en omstreken.</p>'
      f'<div class="hero__acties"><a class="knop knop--leeg" href="{L("vacature")}">Bekijk de vacature <span class="chev" aria-hidden="true"></span></a></div>'
      '</div><div></div></div>', '03 &#8212; Vacature', 'Vacature:<br>EP-W basis adviseur')

    body = hero + diensten + over + vac + cta('Wilt u contact<br>met ons opnemen?',
      f'Dat kan via ons e-mailadres {MAIL} of telefonisch via {TEL1} of {TEL2}.')
    return ('Vooruit &#8212; dakinspectie en energielabel in Groesbeek',
            'Dakinspecties en advies, energielabel volgens NTA 8800 en dakvensters. Erkend EP-W adviseur '
            'uit Groesbeek, circa 30 jaar ervaring in daken.',
            body, [])

def p_dakinspecties():
    kop = paginakop('Dienst 1 &#183; nok &amp; dakvlak', 'Dakinspecties<br>en advies',
      'Inspectie of advies nodig over uw dak of dakconstructie? Vooruit helpt u verder door een grondige analyse met rapportage van alle mogelijkheden met betrekking tot uw dak. Voor zowel bedrijven als particulieren.',
      'd1', VB['1'], '1', [('Vraag een inspectie aan', L('contact'), True), (TEL1, f'tel:{TEL1_INT}', False)],
      blad='Detail 1 &#183; nok &amp; dakvlak', tek='TEK. VW-01')

    inleiding = sec('<div class="tweekolom"><div class="tekst">'
      '<h3>Onafhankelijk advies</h3>'
      '<p>VOORUIT is gespecialiseerd in daken en energieprestatieadvies voor woningen, en geeft onafhankelijk advies op basis van kennis en betrouwbaarheid, opgebouwd met circa 30 jaar ervaring in daken en circa 8 jaar ervaring in energetische adviestrajecten.</p>'
      '<h3>De conditie van uw dak in beeld</h3>'
      '<p>VOORUIT brengt de conditie van daken in beeld. Hieronder valt onder andere de kwaliteit van de dakpannen, leien en platdakbedekking, het dakbeschot en alle bijbehorende aansluitingen zoals goten, schoorstenen, dakkapellen, dakvensters en dakdoorvoeren. Maar uiteraard ook de mate van energetische isolatie en brandwerendheid van woningscheidende details.</p>'
      '</div><div><p class="tk" style="margin-bottom:.4rem">Wat we beoordelen</p>' + punten([
        'Dakpannen, leien en platdakbedekking',
        'Het dakbeschot en de dakconstructie',
        'Goten, schoorstenen, dakkapellen, dakvensters en dakdoorvoeren',
        'De mate van energetische isolatie',
        'Brandwerendheid van woningscheidende details',
      ]) + '</div></div>', '01 &#8212; De inspectie', 'Wat Vooruit<br>in beeld brengt')

    maatwerk = sec('<div class="tekst" style="margin-bottom:2rem">'
      '<p>VOORUIT biedt maatwerk dakadvies naar wens van de opdrachtgever. De opdrachtgever geeft aan wat de toekomstideeën zijn met betrekking tot het te beoordelen pand, en krijgt hier een passend advies voor uitgewerkt. Het maatwerkadvies kan summier of uitgebreid zijn, naar wens van de opdrachtgever.</p></div>'
      + kaarten([
        ('Variant 1','Summier','Alleen een vaststelling van de situatie en een summiere opstelling van de te nemen maatregelen &#8212; bijvoorbeeld om een dak nog tien jaar in stand te houden &#8212; met een bijbehorende inschatting van de kosten voor uitvoering van die maatregelen.'),
        ('Variant 2','Uitgebreid','Een uitgebreide verslaglegging met foto&#8217;s en details van de huidige situatie, met een advies voor groot onderhoud uitgewerkt in meerdere scenario&#8217;s. Ondersteund met details die aansluiten bij de scenario&#8217;s, waarbij de knelpunten van de dakrenovatie al in het voorstadium worden opgelost, zodat bij uitvoering de kans op verrassende meerwerknota&#8217;s wordt beperkt. Aangevuld met werkomschrijvingen en kostenberekeningen.'),
      ], 2), '02 &#8212; Maatwerk', 'Summier of uitgebreid,<br>u kiest')

    knelpunten = sec('<div class="tweekolom"><div class="tekst">'
      '<h3>Hulp bij knelpunten in details</h3>'
      '<p>U weet al wat u van plan bent, maar heeft nog geen oplossing voor de knelpunten in de details bij dakonderhoud? Ook hierbij kan de steun van VOORUIT ingeroepen worden. Naar aanleiding van uw toelichting beoordeelt VOORUIT het detail en komt met een oplossing op maat, met bijbehorende details.</p>'
      '<h3>Kwaliteitscontrole en zonne-energie</h3>'
      '<p>VOORUIT biedt opdrachtgevers de mogelijkheid tot kwaliteitscontrole van aanbiedingen van marktpartijen en van de uitvoering tijdens dakonderhoud. Daarnaast beoordeelt VOORUIT daken op de mogelijkheden tot zonne-energie.</p>'
      f'<p><a href="{L("contact")}">Leg uw vraag voor</a></p>'
      '</div><div><p class="tk" style="margin-bottom:.4rem">Ook mogelijk</p>' + punten([
        'Kwaliteitscontrole van aanbiedingen van marktpartijen',
        'Kwaliteitscontrole van de uitvoering tijdens dakonderhoud',
        'Beoordeling van het dak op mogelijkheden tot zonne-energie',
        'Oplossing op maat voor een knelpunt in een detail',
      ]) + '</div></div>', '03 &#8212; Ondersteuning', 'Meedenken tot en met<br>de uitvoering')

    berekeningen = sec(kaarten([
      ('Berekening','Kostprijsbepaling laten maken','VOORUIT bepaalt aan de hand van tekeningen en foto&#8217;s de hoeveelheden, en maakt kostenbegrotingen met bijbehorende offerte, urenstaat en materiaalstaat die nodig zijn voor het dakproject. Zowel nieuwbouw als renovatie. Indien gewenst bespreekt VOORUIT de klantwens ter plekke met de potenti&#235;le opdrachtgever, inclusief mogelijkheden en onmogelijkheden.'),
      ('Berekening','Verankeringsberekening laten maken','VOORUIT maakt verankeringsberekeningen voor dakpannen en platdakbedekking conform het Bouwbesluit 2012. Zo weet u exact welke dakpannen in welke zone verankerd dienen te worden, of hoe de platdakbedekking geballast dan wel verankerd dient te worden.'),
      ('Berekening','Bouwfysische berekening laten maken','VOORUIT maakt bouwfysische berekeningen van dakpakketten, zodat gecontroleerd kan worden of er problemen ontstaan of aanwezig zijn in de constructie met betrekking tot het condenseren van vocht uit het gebouw, met alle gevolgen van dien.'),
    ], 3), '04 &#8212; Berekeningen', 'Kostprijs, verankering<br>en bouwfysica')

    return ('Dakinspectie en dakadvies Groesbeek &#8212; Vooruit',
      'Onafhankelijke dakinspectie en maatwerk dakadvies uit Groesbeek. Conditie van pannen, leien, '
      'platdak en dakbeschot, plus verankerings- en bouwfysische berekeningen.',
      kop + inleiding + maatwerk + knelpunten + berekeningen + cta('Advies nodig over<br>uw dak?',
        f'Bel {TEL1} of {TEL2}, of mail naar {MAIL}.'),
      [('Home','home'), ('Dakinspecties en advies', None)])

def p_energielabel():
    kop = paginakop('Dienst 3 &#183; thermische schil', 'Energielabel<br>en advies',
      'Energielabel en advies voor uw woning en/of bedrijfspand? Vooruit kan u van dienst zijn en samen met u tot de meest optimale en energiezuinigste oplossing komen. Voor zowel bedrijven als particulieren.',
      'd3', VB['3'], '3', [('Vraag een energielabel aan', L('contact'), True), (TEL1, f'tel:{TEL1_INT}', False)],
      blad='Detail 3 &#183; thermische schil', tek='TEK. VW-03')

    erkend = sec('<div class="tweekolom"><div class="tekst">'
      '<h3>Erkend EP-W Basis en Detail</h3>'
      '<p>VOORUIT is erkend EP-W Basis (bestaande bouw) en Detail (nieuwbouw of bestaande bouw) maatwerkadviseur. EP-W staat voor Energie Prestatie Advies voor Woningen.</p>'
      '<p>VOORUIT kan de energieprestatie van uw woning of woningen beoordelen en voorzien van een officieel energielabel, al dan niet voorzien van maatwerkadvies. Dit volgens de nieuwe NTA 8800-reglementen.</p>'
      '<p>Gebouwen die eenmaal een energielabel hebben op basis van de Detailmethode, moeten bij vervolgafmeldingen ook altijd weer in Detailmethode worden afgemeld.</p>'
      '</div><div><p class="tk" style="margin-bottom:.4rem">Erkenningen</p>' + punten([
        '<strong>EP-W Basis</strong> &#8212; bestaande bouw',
        '<strong>EP-W Detail</strong> &#8212; nieuwbouw of bestaande bouw, maatwerk',
        '<strong>NTA 8800</strong> &#8212; de rekenmethodiek sinds 1 januari 2021',
      ], groen=True) + '</div></div>', '01 &#8212; Erkenning', 'Officieel energielabel,<br>met of zonder maatwerkadvies')

    nieuw = sec('<div class="tekst" style="margin-bottom:2rem">'
      '<p>Vanaf 1 januari 2021 is het vernieuwde energielabel ingevoerd voor gebouwen. Dit heeft gevolgen voor iedereen die gebouweigenaar is, een gebouw bouwt of onderhoudt.</p></div>'
      + kaarten([
        ('Voor u als','Particulier','Voor de particulier houdt het in dat een uitgebreider energielabel vereist is dan voorheen bij verkoop. Er moet nu een energieadviseur ter plekke komen en de volledige woning beoordelen op basis van isolaties en installaties.'),
        ('Voor u als','Woningbouwvereniging of vastgoedeigenaar','Voor woningbouwverenigingen en overige vastgoedeigenaren (woningen en utiliteit) betekent het een verdere diepgang van de oude methode.'),
        ('Voor u als','Bouwer of architect','Voor bouwers en architecten volstaat de EPC-berekening niet meer bij vergunningaanvragen, maar is een energielabel op detailniveau verplicht. Bij oplevering is het vereenvoudigde label ook vervallen en is de uitgebreide variant Detail van toepassing. Het houdt ook in dat er vanaf het begin van de bouw bewijslast verzameld moet worden voor het energielabel &#8212; denk hierbij aan foto&#8217;s, tekeningen en kwaliteitsverklaringen.'),
        ('Voor u als','Onderhoudsbedrijf','Voor onderhoudsbedrijven is de grootste invloed dat er meer bewijslast benodigd is dan voorheen. Veel onderhoudsbedrijven krijgen vanuit hun opdrachtgever de vraag om woningen met groot onderhoud te upgraden van bijvoorbeeld een F-label naar een B-label of hoger. VOORUIT kan onderhoudsbedrijven hierbij terzijde staan met advies over het bepalen van de huidige basis, de te nemen maatregelen, het doorrekenen van labels op basis van idee&#235;n, keuzes en wensen van de opdrachtgever, en het na onderhoud voorzien van de woningen van nieuwe energielabels.'),
      ], 2), '02 &#8212; Sinds 2021', 'Wat het vernieuwde<br>energielabel betekent')

    sporen = sec(f'''<div class="legenda">
      <a class="blad blad--energie" href="{L('energetisch-onderzoek-particulieren')}">
        <div class="blad__titelblok"><span class="tk">Energetisch onderzoek</span><span class="blad__merk" style="background:var(--label-b)"></span></div>
        <div class="blad__lijf"><h3 class="disp blad__naam">Voor<br>particulieren</h3>
        <p class="blad__tekst">Energetisch onderzoek van eenvoudig, simpel advies tot volledig energieneutraal advies voor bestaande bouw. Drie pakketten: Basis, Energie neutraal en Maatwerk.</p>
        <span class="blad__meer">Bekijk de pakketten <span class="chev" aria-hidden="true"></span></span></div></a>
      <a class="blad blad--energie" href="{L('energetische-onderzoek-vastgoedbeheerders-woningen')}">
        <div class="blad__titelblok"><span class="tk">Energetisch onderzoek</span><span class="blad__merk" style="background:var(--energie)"></span></div>
        <div class="blad__lijf"><h3 class="disp blad__naam">Voor vastgoed&#173;beheerders<br>van woningen</h3>
        <p class="blad__tekst">Van eenvoudig advies tot volledig energieneutraal advies, voor bestaande bouw en nieuwbouw. Inclusief NTA 8800-berekeningen, afmeldingen en subsidieaanvragen.</p>
        <span class="blad__meer">Bekijk de pakketten <span class="chev" aria-hidden="true"></span></span></div></a>
      </div>''', '03 &#8212; Energetisch onderzoek', 'Voor particulieren en<br>voor vastgoedbeheerders')

    return ('Energielabel en energieadvies NTA 8800 &#8212; Vooruit',
      'Officieel energielabel volgens NTA 8800 door een erkend EP-W Basis- en Detailadviseur uit '
      'Groesbeek. Voor particulieren, vastgoedbeheerders en bouwers.',
      kop + erkend + nieuw + sporen + cta('Een energielabel<br>nodig?',
        f'Bel {TEL1} of {TEL2}, of mail naar {MAIL}.'),
      [('Home','home'), ('Energielabel en advies', None)])

def p_particulieren():
    kop = paginakop('Energielabel &#183; particulieren', 'Energetisch onderzoek<br>particulieren',
      'Energetisch onderzoek van eenvoudig, simpel advies tot volledig energieneutraal advies voor bestaande bouw.',
      'dp', VB['3'], '3', [('Vraag een offerte aan', L('contact'), True)],
      blad='Detail 3 &#183; thermische schil', tek='TEK. VW-03a')

    pak = sec(pakketten([
      ('Basis', 'var(--label-e)', [
        'Praktische budgetvariant energiebesparingsadvies',
        'Opname ter plekke van isolatiewaarden en tocht- en/of vochtproblemen, met het oog waarneembaar en eventueel aanvullend met endoscoop',
        'Opname van de installatie, kort gesprek over klantwensen, voorkomende klachten of ongemakken die verband kunnen houden met de energetische prestaties van de woning, en de energienota',
        'Direct aan tafel advies over welke maatregelen een verstandige keuze zijn, zonder verder rekenwerk',
        '<span class="pakket__optie">Optioneel:</span> warmtebeeldopname inclusief verslag',
      ]),
      ('Energie neutraal', 'var(--label-b)', [
        'Totaalpakket op basis van Nzeb-toolberekeningen en praktische oplossingen',
        'Volledige opname en berekening van alle knooppunten in de constructies',
        'Doorrekening in de software conform Nzeb-tool',
        'Nauwkeuriger dan de NTA 8800-methodiek',
        'Inclusief praktisch advies hoe (bijna) energieneutraal bereikt kan worden',
        '<span class="pakket__optie">Optioneel:</span> begeleiding en controle tijdens het uitvoeringsproces',
      ]),
      ('Maatwerk', 'var(--energie)', [
        'Opname conform EP-W Basis-methodiek volgens de NTA 8800, van isolatie en installaties van de gehele woning',
        'Kort gesprek over klantwensen en energienota',
        'Doorrekenen van de huidige energiezuinigheid van de woning, met besparingsadvies in meerdere varianten',
        'Besparing berekend voor gas en elektra op basis van standaardwaarden',
        'Exclusief afmelding van het energielabel',
        '<span class="pakket__optie">Optioneel:</span> warmtebeeldopname inclusief verslag',
      ]),
    ], 3), '01 &#8212; Pakketten', 'Drie pakketten',
      'Van een praktische budgetvariant tot een volledige doorrekening richting energieneutraal.')

    return ('Energetisch onderzoek particulieren &#8212; Vooruit',
      'Drie pakketten voor particuliere woningeigenaren: Basis, Energie neutraal en Maatwerk. '
      'Opname ter plekke door een erkend EP-W adviseur uit Groesbeek.',
      kop + pak + cta('Welk pakket past<br>bij uw woning?',
        f'Bel {TEL1} of {TEL2}, of mail naar {MAIL}. We bespreken kort wat u wilt weten.'),
      [('Home','home'), ('Energielabel en advies','energielabel-en-advies'), ('Particulieren', None)])

def p_vastgoed():
    kop = paginakop('Energielabel &#183; vastgoedbeheerders', 'Energetisch onderzoek<br>vastgoedbeheerders',
      'Energetisch onderzoek van eenvoudig, simpel advies tot volledig energieneutraal advies voor bestaande bouw en nieuwbouw. Het verzorgen van de NTA 8800-berekeningen, afmeldingen en subsidieaanvragen.',
      'dv', VB['3'], '3', [('Vraag een offerte aan', L('contact'), True)],
      blad='Detail 3 &#183; thermische schil', tek='TEK. VW-03b')

    inl = sec('<div class="tekst"><p>Een energetisch onderzoek biedt inzicht in de huidige staat van de woning, en in wat de beste investering is bij verdere verduurzaming van de woning.</p></div>',
      '01 &#8212; Waarom', 'Inzicht in de huidige staat,<br>en in de beste investering')

    pak = sec(pakketten([
      ('Basis', 'var(--label-e)', [
        'Opname conform EP-W Basis- of Detailmethodiek volgens de NTA 8800, van thermische schil en installaties',
        'Vaststellen van het huidige energielabel inclusief deskresearch',
        'Het maken van de benodigde berekeningen in Vabi',
        'Afmelden van de woningen bij de overheid',
        'Uitgangspunt: kosteloze terbeschikkingstelling van bouwkundige en installatietechnische tekeningen',
      ]),
      ('Energie neutraal', 'var(--label-d)', [
        'Totaalpakket op basis van Nzeb-toolberekeningen en praktische oplossingen',
        'Volledige opname en berekening van alle knooppunten in de constructies',
        'Doorrekening in de software conform Nzeb-tool',
        'Nauwkeuriger dan de NTA 8800-methodiek',
        'Inclusief praktisch advies hoe (bijna) energieneutraal bereikt kan worden',
      ]),
      ('Maatwerk', 'var(--label-b)', [
        'Opname van enkele woningen conform EP-W-methodiek volgens de NTA 8800',
        'Scenario&#8217;s samengesteld voor labelverbetering van C tot A++++',
        'Rapport met de verbeteringsopties',
        'Weergave van de besparingen op gas en elektra',
        'Aanvullend gesprek ter verduidelijking',
        'Exclusief afmelding van het energielabel',
        '<span class="pakket__optie">Optioneel:</span> warmtebeeldopname inclusief verslag',
      ]),
      ('RVV verduurzaming', 'var(--energie)', [
        'Energielabel van de bestaande situatie inclusief afmelding',
        'Doorrekening van de nieuwe situatie met de maatregelen',
        'Aanvullend advies voor uitzonderingen',
        'Begeleiding bij het verzamelen van de bewijslast',
        'Nacontrole bij maatregelen anders dan isolaties en cv-ketels',
        'Nieuw energielabel voor de woningen',
        'Aanvraag RVV verduurzaming',
        '<span class="pakket__optie">Optioneel:</span> warmtebeeldopname inclusief verslag',
      ]),
    ], 2), '02 &#8212; Pakketten', 'Vier pakketten')

    return ('Energetisch onderzoek vastgoedbeheerders &#8212; Vooruit',
      'Energielabels voor woningportefeuilles: NTA 8800-berekeningen, afmeldingen, RVV verduurzaming '
      'en subsidieaanvragen door een erkend EP-W adviseur.',
      kop + inl + pak + cta('Om hoeveel woningen<br>gaat het?',
        f'Bel {TEL1} of {TEL2}, of mail naar {MAIL}.'),
      [('Home','home'), ('Energielabel en advies','energielabel-en-advies'), ('Vastgoedbeheerders', None)])

def p_dakvensters():
    kop = paginakop('Dienst 2 &#183; dakvenster', 'Dakvensters',
      'Dakvensters in een bestaande woning, woningcomplex of bedrijfspand. Plaatsen, vervangen, onderhouden &#233;n repareren voor particulieren en bedrijven.',
      'd2', VB['2'], '2', [('Informeer naar de mogelijkheden', L('contact'), True), (TEL1, f'tel:{TEL1_INT}', False)],
      blad='Detail 2 &#183; dakvenster', tek='TEK. VW-02')

    inl = sec('<div class="tweekolom"><div class="tekst">'
      '<p>VOORUIT biedt het plaatsen, vervangen of onderhouden van dakvensters aan, met een persoonlijke benadering en bijna 30 jaar ervaring.</p>'
      '<p>Maak gebruik van onze expertise en jarenlange ervaring en informeer naar al onze mogelijkheden.</p>'
      '</div><div><p class="tk" style="margin-bottom:.4rem">Wat u van ons mag verwachten</p>' + punten([
        'Een persoonlijke benadering van de bewoners',
        'Afspraak is afspraak',
        'Levering en aanbrenging van accessoires',
        'Gedegen montage en de juiste accessoires',
        'Werkzaamheden zoveel mogelijk van binnenuit uitgevoerd',
      ]) + '</div></div>', '01 &#8212; Werkwijze', 'Persoonlijke benadering,<br>bijna 30 jaar ervaring')

    diensten = sec(kaarten([
      ('Dienst','Plaatsen','Afhankelijk van wensen en mogelijkheden plaatsen wij dakvensters van het fabricaat Velux of Fakro, of dakramen van het fabricaat Ubbink.'),
      ('Dienst','Vervangen','Bij het vervangen van dakvensters kan het gaan om vervanging door dezelfde maat, of om het plaatsen van een groter dakvenster.'),
      ('Dienst','Onderhoud','Het plegen van het benodigde onderhoud en het vervangen van onderdelen van dakvensters van het fabricaat Velux of Fakro, of dakramen van het fabricaat Ubbink.'),
    ], 3), '02 &#8212; Diensten', 'Plaatsen, vervangen<br>en onderhouden')

    return ('Dakvensters plaatsen en vervangen &#8212; Vooruit Groesbeek',
      'Dakvensters van Velux, Fakro en Ubbink plaatsen, vervangen, onderhouden en repareren. '
      'Voor particulieren en bedrijven in regio Nijmegen en Arnhem.',
      kop + inl + diensten + cta('Interesse in een<br>dakvenster?',
        f'Bel {TEL1} of {TEL2}, of mail naar {MAIL}.'),
      [('Home','home'), ('Dakvensters', None)])

def p_over():
    kop = paginakop('Groesbeek &#183; sinds 2013', 'Over ons',
      'VOORUIT is een klein bedrijf dat is gespecialiseerd in dak- en energieadvies, opgericht in 2013. Belangrijke basis is eenvoud en eerlijkheid.',
      'do', VB_VOL, None, [('Neem contact op', L('contact'), True)], vol=True)

    verhaal = sec('<div class="over">'
      '<figure class="portret" style="margin:0"><figcaption class="tk">Foto Freddie Peters<br>volgt</figcaption></figure>'
      '<div><p class="over__citaat">Ik ben Freddie Peters, ik kom uit Groesbeek. Ik ben sinds 2013 zelfstandig ondernemer, erkend Energie Prestatie Adviseur en eigenaar van VOORUIT, met circa 30 jaar ervaring op het gebied van hellende daken.</p>'
      '<p class="over__tekst">Sinds 2019 is mijn vrouw, Yolande Peters, werkzaam binnen het bedrijf. Zij neemt de administratie en planning voor haar rekening.</p>'
      '<p class="over__tekst">Mijn specialisatie ligt bij hellende daken en bij het beoordelen van isolaties en installaties van woningen.</p>'
      '</div></div>', '01 &#8212; Wie wij zijn', 'Freddie en<br>Yolande Peters')

    biedt = sec('<div class="tweekolom"><div><p class="tk" style="margin-bottom:.4rem">VOORUIT biedt u</p>' + punten([
        'Dakadvies voor korte en lange termijn, met duidelijke en praktische adviezen en ramingen',
        'Calculaties voor dakwerkzaamheden, van opname tot offerte',
        'Uw woning voorzien van een energielabel door middel van opname volgens de NTA 8800-voorschriften',
        'Maatwerk energieprestatieadvies vanuit bouwkundig oogpunt',
        'Het plaatsen, vervangen en onderhouden van dakvensters',
      ]) + '</div><div class="tekst"><h3>Waar we op letten</h3>'
      '<p>Eenvoud en transparantie. Duidelijkheid en begrijpelijke taal. Korte lijnen en goede communicatie.</p>'
      '<p>Onafhankelijk advies op basis van kennis en betrouwbaarheid, opgebouwd met circa 30 jaar ervaring in daken en circa 8 jaar ervaring in energetische adviestrajecten.</p>'
      f'<p><a href="{L("vacature")}">We zoeken een EP-W basis adviseur.</a></p></div></div>',
      '02 &#8212; Diensten', 'Wat u van<br>Vooruit kunt vragen')

    return ('Over Vooruit &#8212; Freddie Peters, Groesbeek',
      'Vooruit is in 2013 opgericht door Freddie Peters: erkend Energie Prestatie Adviseur met circa '
      '30 jaar ervaring in hellende daken.',
      kop + verhaal + biedt + cta('Even kennismaken?',
        f'Bel {TEL1} of {TEL2}, of mail naar {MAIL}.'),
      [('Home','home'), ('Over ons', None)])

ARTIKELEN = [
 dict(slug='geslaagd-als-energie-neutraal-vakman-2', iso='2021-01-18', datum='18 januari 2021',
   titel='Gediplomeerd EPV trajecten',
   samenvatting='De examenuitslagen zijn binnen. Geslaagd voor de bijscholing EPV trajecten voor woningen.',
   body='<p>De examenuitslagen zijn binnen. Geslaagd voor de bijscholing EPV trajecten voor woningen.</p>'),

 dict(slug='geslaagd-als-energie-neutraal-vakman', iso='2018-08-14', datum='14 augustus 2018',
   titel='Geslaagd als energieneutraal vakman',
   samenvatting='Geslaagd voor het examen energieneutraal vakman, opgesteld door het Passiefhuis Instituut in Duitsland.',
   body='<p>Gisteren heb ik de uitslag binnengekregen dat ik geslaagd ben als energieneutraal vakman. '
        'Dat houdt in dat ik de praktische kant van het energieneutraal renoveren kan begeleiden op het gebied '
        'van advisering &#8212; dit in navolging van de opleiding om Nzeb-toolberekeningen te kunnen maken, '
        'de theoretische kant.</p>'
        '<p>Dit examen is opgesteld door het Passiefhuis Instituut in Duitsland. Deze organisatie staat voor een '
        'degelijke aanpak van verduurzaming, met een bewezen werking van het principe.</p>'
        '<p>Ik sta dan ook graag klaar om op korte termijn een kleinschalig project te begeleiden dat aan de '
        'BENG-eisen (bijna energieneutraal) moet voldoen, of dat zelfs volledig energieneutraal als insteek heeft.</p>'),

 dict(slug='energieadvies-zeker-ook-voor-particulieren-en-vves-belangrijk', iso='2018-08-10', datum='10 augustus 2018',
   titel='Energieadvies zeker ook voor particulieren en VvE&#8217;s belangrijk',
   samenvatting='Steeds meer particulieren en VvE&#8217;s laten hun woning door een expert onderzoeken. Een overzicht van de pakketten die Vooruit daarvoor heeft.',
   body='<p>Na een periode van extreme drukte in energieadvisering in de sociale huursector zie ik ook de trend '
        'ontstaan dat particulieren en VvE&#8217;s toch graag door een expert de woning laten onderzoeken, om een '
        'goed beeld te krijgen van wat de beste keuzes en volgordes zijn voor verduurzaming van de woning.</p>'
        '<p>Dat is een goed signaal, want energieadviseurs kijken toch met een andere blik naar een woning dan een '
        'woningeigenaar zelf doet. Samen met de kennis van de gebruiker van de woning komt dan het beste plan op '
        'tafel voor de toekomst &#8212; we moeten immers allen vooruit naar een duurzame toekomst.</p>'
        '<p>VOORUIT staat dan ook graag klaar voor deze doelgroep. Hiervoor zijn meerdere keuzepakketten opgezet, '
        'zodat er voor elk wat wils is. Ieder pand is anders, en iedere eigenaar heeft een andere kijk op zijn pand '
        'en gebruikt het anders.</p>'
        '<blockquote>Voor een fatsoenlijk advies moet je een gebouw gewoon gezien hebben. Dat is een basisuitgangspunt.</blockquote>'
        '<h2>Praktische budgetvariant energiebesparingsadvies</h2>'
        '<p>Opname ter plekke van isolatiewaarden en tochtinfiltratie die met het blote oog waar te nemen is aan de '
        'thermische schil. Opname van de installatie, kort gesprek over klantwensen en energienota, en direct aan '
        'tafel een advies welke maatregelen een verstandige keuze zijn, zonder verder rekenwerk.</p>'
        '<h2>Verbetering energielabel</h2>'
        '<p>Aan de hand van de voorgenoemde praktische adviezen samen met u in de webapplicatie van het energielabel '
        'kijken en keuzes bespreken, ter plekke.</p>'
        '<h2>Standaard maatwerkadvies</h2>'
        '<p>Opname conform de EPA-methodiek voor woningbouwverenigingen &#8212; voorheen het energielabel, nu de '
        'energie-indexbepaling van thermische schil en installaties. Dit is een uitgebreidere opname. Indien gewenst '
        'kan aanvullend ook het definitieve energielabel van uw woning worden afgemeld.</p>'
        '<p>Dat definitieve energielabel ligt dichter bij de werkelijkheid dan de vereenvoudigde methode van tien '
        'stappen die u zelf kunt invullen, omdat bij de uitgebreide methode alle oppervlakten worden doorgerekend en '
        'circa 140 kenmerken van de woning worden ingevoerd.</p>'
        '<p>Verder: kort gesprek over klantwensen en energienota, en doorrekening van de huidige energie-index met '
        'besparingsadvies aan de hand van verbruik en wensen van de klant, in meerdere varianten (maatwerkadvies). '
        'Hier komt ook een besparing uit voort op gas en elektra, op basis van een aantal standaardwaarden.</p>'
        '<h2>Toelichtend gesprek energiebesparing en verbetering energielabel</h2>'
        '<p>Aan de hand van de scenario&#8217;s uit het maatwerkadvies de keuzes bespreken en toelichten, ter plekke.</p>'
        '<h2>Onderzoek naar energieneutraal</h2>'
        '<p>Hierbij gaat alles nog een stapje verder. Ook alle knooppunten in de constructies worden opgenomen en in '
        'de software doorgerekend, op basis van de Nzeb-tool. Dit is een beduidend uitgebreidere opname en berekening, '
        'maar wel realistisch, en met betrekking tot verbruiken veel nauwkeuriger dan de EPA-methodiek. Dit onderzoek '
        'is echt voor mensen die al vastbesloten zijn om richting energieneutraal te gaan, en die niet schrikken van '
        'een investering van meer dan &#8364;&#8239;70.000 aan maatregelen.</p>'
        '<h2>Begeleiding naar en tijdens de uitvoering</h2>'
        '<p>Momenteel is het voor veel particulieren, maar ook voor zakelijke partijen, lastig een goede partner te '
        'vinden voor de uitvoering van energiebesparende maatregelen. VOORUIT kan hierin ondersteunen met het zoeken '
        'naar betrouwbare partijen die werken voor re&#235;le prijzen en kwaliteit hoog in het vaandel hebben staan, '
        'en met het uitvoeren van controles en begeleiding tijdens de realisatie van de verbeterplannen.</p>'
        '<p>Dit kan het isoleren van vloeren, muren, ramen, deuren, daken en leidingen zijn, maar ook het vervangen '
        'of verbeteren van de installatie: de cv-ketel, warmtepomp, zonnepanelen, zonneboilers, ventilatiesystemen en '
        'overige energiebesparende maatregelen.</p>'),

 dict(slug='monumentale-panden-energetisch-onderzoek', iso='2016-04-06', datum='6 april 2016',
   titel='Monumentale panden energetisch onderzoek',
   samenvatting='Energetisch onderzoek bij drie monumentale panden uit ongeveer 1900, van het souterrain tot het roevendak.',
   body='<p>Kort geleden heeft VOORUIT bij drie monumentale panden, bouwjaar rond 1900, energetisch onderzoek mogen '
        'verrichten. Inclusief doorrekening van de huidige energie-index van het pand, en advies hoe deze panden '
        'energetisch verbeterd kunnen worden naar het gewenste niveau.</p>'
        '<p>Erg leuk werk, waarbij je van alles tegenkomt &#8212; van het souterrain tot het roevendak. In honderd jaar '
        'wordt er veel per ruimte gedaan aan een pand, zo bleek onder andere tijdens het endoscopisch onderzoek op de '
        'meerdere verdiepingen, achter de voorzetwanden en verlaagde plafonds.</p>'),

 dict(slug='energie-index-79-woningen-groesbeek', iso='2016-03-28', datum='28 maart 2016',
   titel='Energie-Index 79 woningen Groesbeek',
   samenvatting='In december voor drie onderhoudsbedrijven samen 79 woningen voorzien van een Energie-Index, uitgevoerd in EPA view.',
   body='<p>In december heeft VOORUIT voor drie onderhoudsbedrijven samen in totaal 79 woningen voorzien van een '
        'Energie-Index, nadat de onderhoudswerkzaamheden gereed waren.</p>'
        '<p>Dit is op verzoek van de woningbouwvereniging uitgevoerd in EPA view via het aannemersportaal, in plaats '
        'van de standaardsoftware van Vabi waar ik normaliter mee werkte. Dat was weer een uitdaging in een dergelijk '
        'kort tijdsbestek met andere software, maar het project was weer gereed voor de deadline van 1 januari &#8212; '
        'en weer een ervaring rijker.</p>'
        '<p>VOORUIT kan voortaan dus ook ingeschakeld worden bij opdrachtgevers die gewend zijn te werken met EPA view.</p>'),

 dict(slug='energetisch-onderzoek-126-woningen', iso='2015-11-09', datum='9 november 2015',
   titel='Energetisch onderzoek 126 woningen',
   samenvatting='Van 126 woningen alle energetische waarden in beeld gebracht, van kruipruimte tot nok, onderbouwd met endoscopisch beeldmateriaal.',
   body='<p>Kort geleden zijn de gegevens van 126 woningen aangeleverd aan de opdrachtgever, waar VOORUIT op '
        'adresniveau alle energetische waarden in beeld heeft gebracht &#8212; van kruipruimte tot nok.</p>'
        '<p>Hiervoor dienden uiteraard alle woningen bezocht te worden, om te achterhalen of de vloer, de gevel, de '
        'zoldervloer en het dak ge&#239;soleerd waren, welk type glas in de woningen was aangebracht, en welke cv-ketel '
        'er was geplaatst. Hiervoor is onder andere gebruikgemaakt van een endoscoop met digitale camera, om alles met '
        'beeldmateriaal te kunnen onderbouwen.</p>'
        '<p>Aanvullend is er voor een aantal typen woningen een energie-indexberekening opgesteld voor de huidige '
        'situatie, conform de huidige regelgeving en het nader voorschrift, met een advies hoe de gewenste energie-index '
        'gehaald kan gaan worden bij een mogelijk groot onderhoud &#8212; daar waar de energie-index ongunstiger is dan '
        'het gewenste niveau van de opdrachtgever.</p>'),

 dict(slug='herkenbaar-onderweg', iso='2015-10-10', datum='10 oktober 2015',
   titel='Herkenbaar onderweg',
   samenvatting='VOORUIT is nu volledig herkenbaar onderweg met de nieuwe belettering op de auto.',
   body='<p>VOORUIT is nu volledig herkenbaar onderweg met de nieuwe belettering op de auto. '
        'Wanneer mogen wij u van dienst zijn?</p>'),
]

def artikel_ld(a):
    return ('<script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting",'
      '"headline":"' + ontsmet(a['titel']).replace('"', '') + '",'
      '"description":"' + ontsmet(a['samenvatting']).replace('"', '') + '",'
      '"datePublished":"' + a['iso'] + '","dateModified":"' + a['iso'] + '",'
      '"author":{"@type":"Person","name":"Freddie Peters"},'
      '"publisher":{"@id":"' + BASIS_URL + '/#organisatie"},'
      '"mainEntityOfPage":{"@type":"WebPage","@id":"' + BASIS_URL + '/' + a['slug'] + '/"},'
      '"inLanguage":"nl-NL"}</script>')

def maak_artikel(i):
    a = ARTIKELEN[i]
    def pagina():
        kop = paginakop('Blog &#183; ' + a['datum'], a['titel'], a['samenvatting'],
            'ba%d' % i, VB_VOL, None, [('Alle berichten', L('blog'), False),
                                       ('Neem contact op', L('contact'), True)], vol=True)
        nav = []
        if i > 0:
            v = ARTIKELEN[i-1]
            nav.append('<a class="knop knop--leeg" href="%s">Nieuwer: %s</a>' % (L(v['slug']), v['titel']))
        if i < len(ARTIKELEN) - 1:
            o = ARTIKELEN[i+1]
            nav.append('<a class="knop knop--leeg" href="%s">Ouder: %s</a>' % (L(o['slug']), o['titel']))
        navhtml = '<div class="hero__acties" style="margin-top:2.6rem">%s</div>' % ''.join(nav) if nav else ''
        body = kop + sec('<article class="artikel">' + a['body'] + '</article>' + navhtml)
        return (a['titel'] + ' &#8212; Vooruit', a['samenvatting'], body,
                [('Home','home'), ('Blog','blog'), (a['titel'], None)], artikel_ld(a))
    return pagina

def p_blog():
    kop = paginakop('Nieuws van Vooruit', 'Blog',
      'Berichten over opdrachten, opleidingen en ontwikkelingen in dak- en energieadvies.',
      'db', VB_VOL, None, [('Neem contact op', L('contact'), True)], vol=True)
    lijst = ''.join(f'''<a class="blogkaart" href="{L(a["slug"])}">
      <p class="tk"><time datetime="{a["iso"]}">{a["datum"]}</time></p><h2>{a["titel"]}</h2><p>{a["samenvatting"]}</p>
      <span class="blogkaart__meer">Lees verder <span class="chev" aria-hidden="true"></span></span></a>'''
      for a in ARTIKELEN)
    return ('Blog en nieuws &#8212; Vooruit Groesbeek',
      'Berichten van Vooruit over dakinspecties, energielabels, energetisch onderzoek en opleidingen.',
      kop + sec(f'<div class="bloglijst">{lijst}</div>', '01 &#8212; Berichten', 'Alle berichten'),
      [('Home','home'), ('Blog', None)])

def p_vacature():
    kop = paginakop('Werken bij Vooruit', 'Vacature:<br>EP-W basis adviseur',
      'Kom jij ons team versterken? Wij zijn op zoek naar een EP-W basis adviseur.',
      'dva', VB_VOL, None, [('Reageer per mail', f'mailto:{MAIL}', True), (TEL1, f'tel:{TEL1_INT}', False)], vol=True)
    body = sec('<div class="tweekolom"><div class="tekst">'
      '<p>Wij zijn op zoek naar een EP-W basis adviseur. Het werkgebied is hoofdzakelijk regio Nijmegen &#8211; Arnhem &#8211; Wijchen en omstreken.</p>'
      f'<p>Interesse? Neem contact op via <a href="mailto:{MAIL}">{MAIL}</a> of bel {TEL1}.</p>'
      '<p class="formulier__noot">De volledige functieomschrijving wordt nog aangeleverd door Vooruit.</p>'
      '</div><div><p class="tk" style="margin-bottom:.4rem">In het kort</p>' + punten([
        'Functie: EP-W basis adviseur',
        'Werkgebied: regio Nijmegen &#8211; Arnhem &#8211; Wijchen en omstreken',
        f'Reageren: {MAIL} of {TEL1}',
      ]) + '</div></div>', '01 &#8212; De vacature', 'Wat we zoeken')
    return ('Vacature EP-W basis adviseur &#8212; Vooruit Groesbeek',
      'Vooruit in Groesbeek zoekt een EP-W basis adviseur. Werkgebied: regio Nijmegen, Arnhem en Wijchen.',
      kop + body, [('Home','home'), ('Vacature', None)])

def p_contact():
    kop = paginakop('Contact', 'Contact',
      f'Wilt u contact met ons opnemen? Doe dit dan via ons e-mailadres {MAIL} of telefonisch via {TEL1} of {TEL2}.',
      'dc', VB_VOL, None, [(f'Bel {TEL1}', f'tel:{TEL1_INT}', True), (MAIL, f'mailto:{MAIL}', False)], vol=True)

    form = sec('<div class="tweekolom"><div>'
      '<form class="formulier" onsubmit="return false">'
      '<div class="veldpaar">'
      '<div class="veld"><label class="tk" for="f-naam">Naam</label><input id="f-naam" name="naam" type="text" autocomplete="name"></div>'
      '<div class="veld"><label class="tk" for="f-tel">Telefoon</label><input id="f-tel" name="telefoon" type="tel" autocomplete="tel"></div>'
      '</div>'
      '<div class="veld"><label class="tk" for="f-mail">E-mail</label><input id="f-mail" name="email" type="email" autocomplete="email"></div>'
      '<div class="veld"><label class="tk" for="f-adres">Adres van het pand</label><input id="f-adres" name="adres" type="text"></div>'
      '<div class="veld"><label class="tk" for="f-soort">Waar gaat het over?</label>'
      '<select id="f-soort" name="soort">'
      '<option>Dakinspectie en advies</option><option>Energielabel &#8212; particulier</option>'
      '<option>Energetisch onderzoek &#8212; vastgoedbeheerder</option><option>Dakvensters</option>'
      '<option>Kostprijs-, verankerings- of bouwfysische berekening</option><option>Iets anders</option></select></div>'
      '<div class="veld"><label class="tk" for="f-tekst">Uw bericht</label>'
      '<textarea id="f-tekst" name="bericht"></textarea></div>'
      '<div><button class="knop" type="submit">Verstuur <span class="chev" aria-hidden="true"></span></button></div>'
      '<p class="formulier__noot">Dit formulier is onderdeel van de demo en verstuurt nog niets.</p>'
      '</form></div>'
      '<div class="gegevens">'
      '<div class="gegeven"><p class="tk">Adres</p><p style="font-size:var(--t-lead)">Vooruit<br>Knapheideweg 55<br>6562 DR Groesbeek</p></div>'
      f'<div class="gegeven"><p class="tk">Telefoon</p><a href="tel:{TEL1_INT}">{TEL1}</a><br><a href="tel:{TEL2_INT}">{TEL2}</a></div>'
      f'<div class="gegeven"><p class="tk">E-mail</p><a href="mailto:{MAIL}">{MAIL}</a></div>'
      f'<div class="gegeven"><p class="tk">Website</p><a href="{BASIS_URL}">www.vooruit.biz</a></div>'
      '<div class="gegeven"><p class="tk">Werkgebied</p><ul class="gebied tk">'
      '<li>Groesbeek</li><li>Nijmegen</li><li>Arnhem</li><li>Wijchen</li></ul></div>'
      '</div></div>', '01 &#8212; Stuur een bericht', 'Of vul dit in')

    return ('Contact &#8212; Vooruit, Knapheideweg 55 Groesbeek',
      f'Neem contact op met Vooruit in Groesbeek: {TEL1}, {TEL2} of {MAIL}. Knapheideweg 55, 6562 DR Groesbeek.',
      kop + form, [('Home','home'), ('Contact', None)])

JURIDISCH_NOOT = ('<p class="formulier__noot" style="margin-top:2.4rem">Deze tekst is opgesteld als basis voor de demo. '
  'Vooruit moet hem nalopen en aanvullen met KvK-nummer, btw-nummer en de daadwerkelijk gebruikte diensten '
  'voordat de site live gaat.</p>')

def p_privacy():
    kop = paginakop('Juridisch', 'Privacy&#173;verklaring',
      'Welke persoonsgegevens Vooruit verwerkt, waarvoor, hoe lang en welke rechten u heeft.',
      'dpr', VB_VOL, None, [('Cookiebeleid', L('cookiebeleid'), False)], vol=True)
    body = sec('<div class="tekst">'
      '<h3>Wie verwerkt uw gegevens</h3>'
      f'<p>Vooruit, Knapheideweg 55, 6562 DR Groesbeek. Telefoon {TEL1} of {TEL2}, e-mail <a href="mailto:{MAIL}">{MAIL}</a>. Vooruit is verantwoordelijk voor de verwerking van persoonsgegevens zoals beschreven op deze pagina.</p>'
      '<h3>Welke gegevens wij verwerken</h3>'
      '<p>Neemt u contact op via het formulier, per e-mail of telefonisch, dan verwerken wij uw naam, adresgegevens van het pand, telefoonnummer, e-mailadres en de informatie die u zelf meestuurt over uw dak of woning.</p>'
      '<p>Voert Vooruit een opdracht voor u uit, dan komen daar de gegevens bij die voor die opdracht nodig zijn: bouwkundige en installatietechnische gegevens van het pand, foto&#8217;s die als bewijslast dienen, en de gegevens die nodig zijn voor het afmelden van een energielabel bij de overheid.</p>'
      '<h3>Waarvoor wij ze gebruiken</h3>'
      '<p>Om uw vraag te beantwoorden, een offerte op te stellen, de opdracht uit te voeren, en om te voldoen aan wettelijke verplichtingen rond het registreren van energielabels en het voeren van onze administratie. Wij verkopen uw gegevens niet en gebruiken ze niet voor andere doeleinden.</p>'
      '<h3>Delen met anderen</h3>'
      '<p>Wij delen gegevens alleen wanneer dat nodig is voor de uitvoering van de opdracht of wanneer een wettelijke verplichting daartoe verplicht &#8212; bijvoorbeeld bij het afmelden van een energielabel in het landelijke register.</p>'
      '<h3>Hoe lang wij ze bewaren</h3>'
      '<p>Contactgegevens van aanvragen die niet tot een opdracht leiden, bewaren wij niet langer dan nodig. Dossiers van uitgevoerde opdrachten bewaren wij zolang dat nodig is voor de uitvoering, de garantie en de wettelijke bewaartermijnen die op onze administratie van toepassing zijn.</p>'
      '<h3>Uw rechten</h3>'
      '<p>U kunt inzage vragen in de gegevens die wij van u hebben, ze laten corrigeren of laten verwijderen, en bezwaar maken tegen de verwerking. Stuur daarvoor een bericht naar '
      f'<a href="mailto:{MAIL}">{MAIL}</a>. U heeft ook het recht een klacht in te dienen bij de Autoriteit Persoonsgegevens.</p>'
      '<h3>Beveiliging</h3>'
      '<p>Vooruit neemt passende maatregelen om misbruik, verlies en onbevoegde toegang tegen te gaan. Heeft u het idee dat uw gegevens niet goed beveiligd zijn, neem dan contact met ons op.</p>'
      '<h3>Cookies</h3>'
      f'<p>Deze website plaatst alleen cookies die noodzakelijk zijn om de site te laten werken en om uw cookiekeuze te onthouden. Meer daarover leest u in het <a href="{L("cookiebeleid")}">cookiebeleid</a>.</p>'
      + JURIDISCH_NOOT + '</div>')
    return ('Privacyverklaring &#8212; Vooruit Groesbeek',
      'Privacyverklaring van Vooruit uit Groesbeek: welke persoonsgegevens wij verwerken, waarvoor, hoe lang en welke rechten u heeft.',
      kop + body, [('Home','home'), ('Privacyverklaring', None)])

def p_cookies():
    kop = paginakop('Juridisch', 'Cookiebeleid',
      'Welke cookies deze website plaatst, waarvoor ze dienen en hoe u uw keuze aanpast.',
      'dck', VB_VOL, None, [('Privacyverklaring', L('privacy-policy'), False)], vol=True)
    body = sec('<div class="tweekolom"><div class="tekst">'
      '<h3>Wat cookies zijn</h3>'
      '<p>Een cookie is een klein tekstbestand dat een website op uw apparaat opslaat. Sommige cookies zijn nodig om de site te laten werken, andere worden gebruikt om te meten hoe de site gebruikt wordt.</p>'
      '<h3>Welke cookies deze site plaatst</h3>'
      '<p>Deze website plaatst standaard alleen <strong>noodzakelijke cookies</strong>. Dat is op dit moment &#233;&#233;n item in de lokale opslag van uw browser, waarin uw cookiekeuze wordt bewaard, zodat de melding niet bij elk bezoek terugkomt. Daarvoor is geen toestemming vereist.</p>'
      '<p><strong>Analytische cookies</strong> worden alleen geplaatst als u daar via de cookiemelding toestemming voor geeft. Ze meten hoeveel mensen de site bezoeken en welke pagina&#8217;s zij lezen, zodat de site verbeterd kan worden.</p>'
      '<p>Er worden geen advertentie- of trackingcookies geplaatst, en er worden geen gegevens gedeeld met adverteerders.</p>'
      '<h3>Uw keuze aanpassen</h3>'
      '<p>U kunt uw keuze op elk moment wijzigen met de knop hieronder. Daarnaast kunt u cookies altijd verwijderen via de instellingen van uw browser.</p>'
      '<div class="hero__acties"><button class="knop knop--leeg" type="button" data-cookies-openen>Cookievoorkeuren wijzigen</button></div>'
      + JURIDISCH_NOOT + '</div>'
      '<div><p class="tk" style="margin-bottom:.4rem">Overzicht</p>' + punten([
        '<strong>Noodzakelijk</strong> &#8212; onthoudt uw cookiekeuze. Bewaartermijn: tot u de opslag van uw browser wist. Geen toestemming nodig.',
        '<strong>Analytisch</strong> &#8212; alleen na uw toestemming. Meet bezoekaantallen en bekeken pagina&#8217;s.',
        '<strong>Marketing</strong> &#8212; worden niet geplaatst.',
      ], groen=True) + '</div></div>')
    return ('Cookiebeleid &#8212; Vooruit Groesbeek',
      'Cookiebeleid van Vooruit: welke cookies deze website plaatst, waarvoor ze dienen en hoe u uw keuze aanpast.',
      kop + body, [('Home','home'), ('Cookiebeleid', None)])

PAGINAS = [
  ('home', p_home),
  ('dakinspecties-en-advies', p_dakinspecties),
  ('energielabel-en-advies', p_energielabel),
  ('energetisch-onderzoek-particulieren', p_particulieren),
  ('energetische-onderzoek-vastgoedbeheerders-woningen', p_vastgoed),
  ('dakvensters', p_dakvensters),
  ('over-ons', p_over),
  ('blog', p_blog),
  ('vacature', p_vacature),
  ('contact', p_contact),
  ('privacy-policy', p_privacy),
  ('cookiebeleid', p_cookies),
] + [(a['slug'], maak_artikel(i)) for i, a in enumerate(ARTIKELEN)]

# ---------------------------------------------------------------- chroom en SEO
def ontsmet(s):
    return s.replace('&#8212;', '—').replace('&#8211;', '–').replace('&#183;', '·') \
            .replace('&#8217;', '’').replace('&#173;', '').replace('&#235;', 'ë') \
            .replace('&#233;', 'é').replace('&amp;', '&').replace('<br>', ' ')

def kop_html(actief):
    nav = ''
    for s, t in NAV:
        cur = ' aria-current="page"' if s == actief else ''
        nav += '<a href="%s"%s data-route="%s">%s</a>' % (L(s), cur, s, t)
    return (f'<header class="kop"><div class="omhulsel kop__in">'
            f'<a class="kop__merk" href="{L("home")}" aria-label="Vooruit, naar de homepage" data-route="home">'
            f'<img src="{LOGO_B64}" alt="Vooruit — dak- en energieadvies uit Groesbeek" width="760" height="213"></a>'
            f'<button class="kop__schakel tk" type="button" aria-expanded="false" aria-controls="hoofdnav" data-nav-schakel>Menu</button>'
            f'<nav class="kop__nav" id="hoofdnav" aria-label="Hoofdmenu">{nav}</nav>'
            f'<a class="knop knop--leeg kop__tel" href="tel:{TEL1_INT}">{TEL1}</a>'
            f'</div></header>')

def voet_html():
    d = ''.join(f'<a href="{L(s)}" data-route="{s}">{t}</a>' for s, t in
                [('dakinspecties-en-advies','Dakinspecties en advies'),
                 ('energielabel-en-advies','Energielabel en advies'),
                 ('energetisch-onderzoek-particulieren','Energetisch onderzoek particulieren'),
                 ('energetische-onderzoek-vastgoedbeheerders-woningen','Energetisch onderzoek vastgoedbeheerders'),
                 ('dakvensters','Dakvensters')])
    v = ''.join(f'<a href="{L(s)}" data-route="{s}">{t}</a>' for s, t in
                [('over-ons','Over ons'), ('blog','Blog'), ('vacature','Vacature'), ('contact','Contact')])
    j = (f'<a href="{L("privacy-policy")}" data-route="privacy-policy">Privacyverklaring</a>'
         f'<a href="{L("cookiebeleid")}" data-route="cookiebeleid">Cookiebeleid</a>'
         f'<button class="voetknop" type="button" data-cookies-openen>Cookievoorkeuren</button>')
    schaal = ''.join(f'<span style="background:var(--label-{k})"></span>' for k in ['g','f','e','d','b','a'])
    return (f'<footer class="voet"><div class="omhulsel"><div class="voet__grid">'
            f'<div><img class="voet__logo" src="{LOGO_B64}" alt="Vooruit" width="760" height="213">'
            f'<p class="tk" style="max-width:38ch;line-height:1.65">{SLOGAN}</p>'
            f'<p class="tk" style="margin-top:1.1rem;line-height:1.7">Vooruit<br>Knapheideweg 55<br>6562 DR Groesbeek<br>'
            f'<a href="tel:{TEL1_INT}" style="text-decoration:none">{TEL1}</a><br>'
            f'<a href="tel:{TEL2_INT}" style="text-decoration:none">{TEL2}</a><br>'
            f'<a href="mailto:{MAIL}" style="text-decoration:none">{MAIL}</a></p></div>'
            f'<nav class="voet__lijst" aria-label="Diensten"><p class="tk">Informatie</p>{d}</nav>'
            f'<nav class="voet__lijst" aria-label="Vooruit"><p class="tk">Vooruit</p>{v}'
            f'<p class="tk" style="margin-top:1.4rem">Juridisch</p>{j}</nav></div>'
            f'<div class="schaal" style="margin-top:2.4rem" aria-hidden="true">{schaal}</div>'
            f'<div class="voet__onder tk"><span>&#169; Vooruit.biz &#183; Knapheideweg 55 &#183; 6562 DR Groesbeek</span>'
            f'<span>Opgericht in 2013</span></div></div></footer>')

COOKIEBALK = ('<aside class="cookiebalk" data-cookiebalk hidden aria-label="Cookiemelding">'
  '<div class="omhulsel cookiebalk__in">'
  '<p class="cookiebalk__tekst"><strong>Deze site gebruikt cookies.</strong> '
  'Noodzakelijke cookies zijn nodig om de site te laten werken en om uw keuze te onthouden. '
  'Analytische cookies plaatsen we alleen als u daarmee instemt; die meten hoeveel mensen de site bezoeken '
  'en welke pagina&#8217;s zij lezen. Marketing- of trackingcookies plaatsen we niet. '
  f'Meer hierover in ons <a href="{{COOKIELINK}}">cookiebeleid</a>.</p>'
  '<div class="cookiebalk__knoppen">'
  '<button class="knop" type="button" data-cookies="alles">Accepteren</button>'
  '<button class="knop knop--leeg" type="button" data-cookies="noodzakelijk">Alleen noodzakelijk</button>'
  '</div></div></aside>')

def jsonld(slug, titel, omschrijving):
    url = BASIS_URL + ('/' if slug == 'home' else f'/{slug}/')
    bedrijf = ('{"@context":"https://schema.org","@type":"RoofingContractor",'
      '"@id":"' + BASIS_URL + '/#organisatie",'
      '"name":"Vooruit","legalName":"Vooruit",'
      '"description":"' + ontsmet(SLOGAN).replace('"', '') + '",'
      '"url":"' + BASIS_URL + '/","foundingDate":"2013",'
      '"logo":"' + BASIS_URL + '/assets/img/og-image.png",'
      '"telephone":"' + TEL1_INT + '","email":"' + MAIL + '",'
      '"address":{"@type":"PostalAddress","streetAddress":"Knapheideweg 55","postalCode":"6562 DR",'
      '"addressLocality":"Groesbeek","addressCountry":"NL"},'
      '"areaServed":[{"@type":"City","name":"Groesbeek"},{"@type":"City","name":"Nijmegen"},'
      '{"@type":"City","name":"Arnhem"},{"@type":"City","name":"Wijchen"}],'
      '"knowsAbout":["dakinspectie","dakadvies","energielabel","NTA 8800","EP-W Basis","EP-W Detail",'
      '"energetisch onderzoek","dakvensters"]}')
    pagina = ('{"@context":"https://schema.org","@type":"WebPage","url":"' + url + '",'
      '"name":"' + ontsmet(titel).replace('"', '') + '",'
      '"description":"' + ontsmet(omschrijving).replace('"', '') + '",'
      '"isPartOf":{"@id":"' + BASIS_URL + '/#organisatie"},"inLanguage":"nl-NL"}')
    return (f'<script type="application/ld+json">{bedrijf}</script>\n'
            f'<script type="application/ld+json">{pagina}</script>')

HOOFD = '''<!doctype html>
<html lang="nl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{titel}</title>
<meta name="description" content="{omschrijving}">
<link rel="canonical" href="{canoniek}">
<meta name="robots" content="index, follow">
<meta name="theme-color" content="#FCFCFB">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Vooruit">
<meta property="og:locale" content="nl_NL">
<meta property="og:title" content="{titel}">
<meta property="og:description" content="{omschrijving}">
<meta property="og:url" content="{canoniek}">
<meta property="og:image" content="{basis}/assets/img/og-image.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" type="image/png" href="/assets/img/favicon.png">
<link rel="apple-touch-icon" href="/assets/img/apple-touch-icon.png">
<link rel="preload" as="font" type="font/woff2" href="/assets/fonts/archivo.woff2" crossorigin>
<link rel="preload" as="font" type="font/woff2" href="/assets/fonts/source-serif-4.woff2" crossorigin>
<link rel="stylesheet" href="/assets/style.css">
{jsonld}
</head>
<body>
{kop}
<main id="hoofd">{kruimels}{body}</main>
{voet}
{cookiebalk}
<script src="/assets/site.js" defer></script>
</body>
</html>
'''

VERCEL = """{
  "$schema": "https://openapi.vercel.sh/vercel.json",
  "cleanUrls": false,
  "trailingSlash": true,
  "headers": [
    {
      "source": "/assets/fonts/(.*)",
      "headers": [{ "key": "Cache-Control", "value": "public, max-age=31536000, immutable" }]
    },
    {
      "source": "/assets/img/(.*)",
      "headers": [{ "key": "Cache-Control", "value": "public, max-age=31536000, immutable" }]
    },
    {
      "source": "/assets/(.*)",
      "headers": [{ "key": "Cache-Control", "value": "public, max-age=3600, must-revalidate" }]
    },
    {
      "source": "/(.*)",
      "headers": [
        { "key": "X-Content-Type-Options", "value": "nosniff" },
        { "key": "Referrer-Policy", "value": "strict-origin-when-cross-origin" },
        { "key": "X-Frame-Options", "value": "SAMEORIGIN" },
        { "key": "Permissions-Policy", "value": "geolocation=(), microphone=(), camera=()" }
      ]
    }
  ],
  "redirects": [
    { "source": "/dakadvies-en-inspecties", "destination": "/dakinspecties-en-advies/", "permanent": true },
    { "source": "/energielabel", "destination": "/energielabel-en-advies/", "permanent": true },
    { "source": "/dakinspectie", "destination": "/dakinspecties-en-advies/", "permanent": true },
    { "source": "/vacatures", "destination": "/vacature/", "permanent": true },
    { "source": "/privacy", "destination": "/privacy-policy/", "permanent": true }
  ]
}
"""

GITIGNORE = """# macOS
.DS_Store
._*

# editors
.vscode/
.idea/

# Vercel
.vercel/

# logs en tijdelijke bestanden
*.log
node_modules/
"""

README = """# Vooruit — website

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
"""

JS = r'''
(function () {
  'use strict';

  /* --- mobiel menu --- */
  var schakel = document.querySelector('[data-nav-schakel]');
  var nav = document.getElementById('hoofdnav');
  if (schakel && nav) {
    schakel.addEventListener('click', function () {
      var open = nav.getAttribute('data-open') === 'ja';
      nav.setAttribute('data-open', open ? 'nee' : 'ja');
      schakel.setAttribute('aria-expanded', String(!open));
      schakel.textContent = open ? 'Menu' : 'Sluit';
    });
    nav.addEventListener('click', function (e) {
      if (e.target.tagName === 'A') {
        nav.setAttribute('data-open', 'nee');
        schakel.setAttribute('aria-expanded', 'false');
        schakel.textContent = 'Menu';
      }
    });
  }

  /* --- cookiemelding --- */
  var balk = document.querySelector('[data-cookiebalk]');
  var SLEUTEL = 'vooruit-cookies';
  function lees() { try { return localStorage.getItem(SLEUTEL); } catch (e) { return null; } }
  function bewaar(w) { try { localStorage.setItem(SLEUTEL, w); } catch (e) {} }
  function toonBalk() { if (balk) { balk.hidden = false; } }
  function verbergBalk() { if (balk) { balk.hidden = true; } }

  function pasToe(keuze) {
    document.documentElement.setAttribute('data-cookies', keuze);
    /* Analytische scripts horen hier geladen te worden, en alleen bij keuze === 'alles'.
       Zolang Vooruit geen statistiekdienst gebruikt, gebeurt er niets. */
  }

  if (balk) {
    var eerder = lees();
    if (eerder) { pasToe(eerder); } else { toonBalk(); }
    balk.addEventListener('click', function (e) {
      var knop = e.target.closest('[data-cookies]');
      if (!knop) return;
      var keuze = knop.getAttribute('data-cookies');
      bewaar(keuze); pasToe(keuze); verbergBalk();
    });
  }
  document.addEventListener('click', function (e) {
    if (e.target.closest('[data-cookies-openen]')) { e.preventDefault(); toonBalk(); }
  });

  /* --- doorsnede: kaarten koppelen en op mobiel inzoomen --- */
  var tekening = document.querySelector('[data-doorsnede]');
  if (tekening) {
    var svg = tekening.querySelector('svg');
    if (svg && window.matchMedia) {
      var smal = window.matchMedia('(max-width: 899px)');
      var pasAan = function () {
        svg.setAttribute('viewBox', smal.matches ? '168 44 544 576' : '0 0 880 620');
      };
      pasAan();
      if (smal.addEventListener) smal.addEventListener('change', pasAan);
      else if (smal.addListener) smal.addListener(pasAan);
    }
    var zet = function (zone) {
      if (zone) tekening.setAttribute('data-actief', zone);
      else tekening.removeAttribute('data-actief');
    };
    var koppel = function (el) {
      var z = el.getAttribute('data-zone');
      ['mouseenter', 'focusin'].forEach(function (ev) { el.addEventListener(ev, function () { zet(z); }); });
      ['mouseleave', 'focusout'].forEach(function (ev) { el.addEventListener(ev, function () { zet(null); }); });
    };
    var legenda = document.querySelector('[data-legenda]');
    if (legenda) legenda.querySelectorAll('[data-zone]').forEach(koppel);
    tekening.querySelectorAll('[data-zone]').forEach(koppel);
  }
})();
'''

JS_ROUTER = r'''
(function () {
  'use strict';
  var paginas = document.querySelectorAll('.pagina');
  if (!paginas.length) return;
  function toon(slug) {
    var gevonden = false;
    paginas.forEach(function (p) {
      var mijn = p.getAttribute('data-slug') === slug;
      p.hidden = !mijn;
      if (mijn) gevonden = true;
    });
    if (!gevonden) { toon('home'); return; }
    document.querySelectorAll('.kop__nav a[data-route]').forEach(function (a) {
      if (a.getAttribute('data-route') === slug) a.setAttribute('aria-current', 'page');
      else a.removeAttribute('aria-current');
    });
    var t = document.querySelector('.pagina[data-slug="' + slug + '"]');
    if (t && t.getAttribute('data-titel')) document.title = t.getAttribute('data-titel');
    window.scrollTo(0, 0);
  }
  function uitHash() { return (location.hash || '').replace(/^#\//, '') || 'home'; }
  window.addEventListener('hashchange', function () { toon(uitHash()); });
  toon(uitHash());
})();
'''

# ---------------------------------------------------------------- bouwen
def bouw_multi():
    global MODE; MODE = 'multi'
    doel = UIT / 'site'
    if doel.exists(): shutil.rmtree(doel)
    (doel / 'assets' / 'img').mkdir(parents=True)
    (doel / 'assets' / 'fonts').mkdir()
    for f in pathlib.Path('assets/fonts').glob('*.woff2'):
        shutil.copy(f, doel / 'assets' / 'fonts' / f.name)
    for n in ['vooruit-logo.png', 'favicon.png', 'apple-touch-icon.png', 'og-image.png']:
        shutil.copy('assets/img/' + n, doel / 'assets' / 'img' / n)
    (doel / 'assets' / 'style.css').write_text(fontcss(False) + '\n' + CSS, encoding='utf-8')
    (doel / 'assets' / 'site.js').write_text(JS, encoding='utf-8')

    def schrijf(pad, titel, omschrijving, body, kruimelpad, slug, canoniek, extra=''):
        doc = HOOFD.format(
            titel=ontsmet(titel), omschrijving=ontsmet(omschrijving), canoniek=canoniek, basis=BASIS_URL,
            jsonld=jsonld(slug, titel, omschrijving) + ('\n' + extra if extra else ''), kop=kop_html(slug if slug in dict(NAV) else ''),
            kruimels=(kruimels(kruimelpad) if kruimelpad else ''), body=body, voet=voet_html(),
            cookiebalk=COOKIEBALK.replace('{COOKIELINK}', L('cookiebeleid')))
        doc = doc.replace(LOGO_B64, '/assets/img/vooruit-logo.png')
        pad.parent.mkdir(parents=True, exist_ok=True)
        pad.write_text(doc, encoding='utf-8')

    for slug, fn in PAGINAS:
        res = fn()
        titel, omschrijving, body, pad = res[:4]
        extra = res[4] if len(res) > 4 else ''
        canoniek = BASIS_URL + ('/' if slug == 'home' else f'/{slug}/')
        bestand = doel / 'index.html' if slug == 'home' else doel / slug / 'index.html'
        schrijf(bestand, titel, omschrijving, body, pad, slug, canoniek, extra)

    # 404
    nietgevonden = (paginakop('Foutmelding 404', 'Deze pagina<br>bestaat niet',
        'De pagina die u zocht is verplaatst of bestaat niet meer. Via het menu hierboven komt u overal, '
        'of ga terug naar de homepage.', 'd404', VB_VOL, None,
        [('Naar de homepage', L('home'), True), ('Neem contact op', L('contact'), False)], vol=True))
    schrijf(doel / '404.html', 'Pagina niet gevonden — Vooruit',
            'De opgevraagde pagina bestaat niet. Ga terug naar de homepage van Vooruit.',
            nietgevonden, None, '404', BASIS_URL + '/404')

    artikeldatums = {a['slug']: a['iso'] for a in ARTIKELEN}
    regels = []
    for sl, _ in PAGINAS:
        loc = BASIS_URL + ('/' if sl == 'home' else '/%s/' % sl)
        prio = '1.0' if sl == 'home' else ('0.8' if sl in dict(NAV) else '0.4')
        lastmod = '<lastmod>%s</lastmod>' % artikeldatums[sl] if sl in artikeldatums else ''
        regels.append('  <url><loc>%s</loc>%s<changefreq>%s</changefreq><priority>%s</priority></url>\n'
                      % (loc, lastmod, 'monthly' if sl == 'home' else 'yearly', prio))
    urls = ''.join(regels)
    (doel / 'sitemap.xml').write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + urls + '</urlset>\n', encoding='utf-8')
    (doel / 'robots.txt').write_text(
        'User-agent: *\nAllow: /\n\nSitemap: %s/sitemap.xml\n' % BASIS_URL, encoding='utf-8')

    (doel / 'vercel.json').write_text(VERCEL, encoding='utf-8')
    (doel / '.gitignore').write_text(GITIGNORE, encoding='utf-8')
    (doel / 'README.md').write_text(README, encoding='utf-8')
    return doel

def bouw_single():
    global MODE; MODE = 'single'
    delen = []
    for slug, fn in PAGINAS:
        res = fn()
        titel, omschrijving, body, pad = res[:4]
        delen.append('<section class="pagina" data-slug="%s" data-titel="%s" hidden>%s%s</section>'
                     % (slug, ontsmet(titel), (kruimels(pad) if pad else ''), body))
    uit = ('<title>Vooruit Doorsnede</title>\n<style>\n' + fontcss(True) + '\n' + CSS + '\n</style>\n'
           + kop_html('') + '\n<main id="hoofd">' + ''.join(delen) + '</main>\n' + voet_html() + '\n'
           + COOKIEBALK.replace('{COOKIELINK}', L('cookiebeleid'))
           + '\n<script>' + JS + JS_ROUTER + '</script>\n')
    p = UIT / 'vooruit-demo.html'; p.write_text(uit, encoding='utf-8')
    return p

if __name__ == '__main__':
    d = bouw_multi(); print("losse pagina's ->", d, len(list(d.glob('*.html'))), 'bestanden + sitemap + robots')
    s = bouw_single(); print('demo ->', s, round(s.stat().st_size / 1024), 'KB')
