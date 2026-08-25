# Privé Motors — Master Checklist Kvaliteta Sajta

Ovaj dokument je "living checklist" — koristi se za ocenjivanje sajta (1-10 po kategoriji, ukupna ocena kao ponder), i kao mapa za popravke dok se sajt završava.

Izvori korišćeni za sastavljanje liste: Awwwards zvanični sistem ocenjivanja (Design 40% / Usability 30% / Creativity 20% / Content 10%), Nielsen Norman Group (10 usability heuristika), Baymard Institute (ecommerce/listing UX benchmarci, 21.000+ testiranih parametara), Refactoring UI (Adam Wathan — tvorac Tailwind CSS-a, i Steve Schoger), Google web.dev (Core Web Vitals 2026 standardi), GitHub Front-End-Checklist (86+ stavki, 73k+ zvezdica), i nekoliko 2026 analiza specifično o tome šta odaje "AI-generated" dizajn.

Skala: svaki parametar se ocenjuje 1-5. Weight (težina) određuje koliko utiče na finalnu ocenu.

---

## 1. BREND DISTINKTIVNOST / "NE IZGLEDA KAO AI" (najveći prioritet za tebe)

Izvor: analize "AI slop design tells" (925 Studios, DEV Community, Medium 2026) — identifikovan konkretan spisak vizuelnih "tellova" koje modeli reprodukuju kad dobiju generički "luxury dark theme" prompt.

1. **Asimetrija u layoutu** — da li bar 30-40% sekcija namerno krši centrirani/simetrični ritam? (Weight: visok)
2. **Custom vizuelni elementi** — postoje li ilustracije/grafički elementi jedinstveni za brend (ne generičke ikonice u krugu)? (Weight: visok)
3. **Odsustvo "glassmorphism" defaulta** — blur/frosted-glass kartice, ako postoje, su namerna odluka, ne default. (Weight: srednji)
4. **Nestandardna paleta/gradijenti** — izbegnut je plavo-ljubičasti gradijent i Tailwind indigo-500 default. (Weight: srednji)
5. **Copy je specifičan, ne generički** — tekst ne zvuči kao da može da stoji na bilo kom sajtu (izbegnuti "Experience unparalleled luxury" tipovi rečenica). (Weight: visok)
6. **Grid nije uniforman posvuda** — bar jedna sekcija (npr. Collection grid) ima "hero" karticu ili prekid ritma, ne 3x3 identične kartice. (Weight: srednji)

---

## 2. TIPOGRAFIJA

Izvor: Refactoring UI (Wathan & Schoger)

7. **Jasna hijerarhija bez oslanjanja samo na veličinu fonta** — koristi se i weight i boja, ne samo size. (Weight: visok)
8. **Maksimalno 2 font familije** (jedna za display/naslove, jedna za UI/telo). (Weight: srednji)
9. **Line-height i line-length su čitljivi** (idealno 50-75 karaktera po redu za body tekst). (Weight: srednji)
10. **Konzistentan tipografski sistem skala** (npr. 12/14/16/20/24/32/48px, ne nasumične vrednosti). (Weight: nizak)

---

## 3. LAYOUT, SPACING, GRID

Izvor: Refactoring UI

11. **Sistem razmaka (spacing scale)** — sve margine/padding dolaze iz definisane skale, ne nasumično. (Weight: srednji)
12. **Dovoljno "disanja"** — elementi nisu zbijeni, whitespace je namerno velikodušan. (Weight: srednji)
13. **Vizuelna težina je balansirana** po sekciji (ništa se ne "utapa" niti dominira slučajno). (Weight: srednji)

---

## 4. USABILITY / UX (Nielsen heuristike)

Izvor: Nielsen Norman Group — 10 Usability Heuristics

14. **Vidljivost statusa sistema** — korisnik uvek zna gde je (loading states, aktivni filter, trenutna stranica). (Weight: srednji)
15. **Konzistentnost i standardi** — dugmad, linkovi, nav ponašaju se predvidivo kroz ceo sajt. (Weight: visok)
16. **Prevencija grešaka** — forme/filteri sprečavaju pogrešan unos pre nego što se desi. (Weight: srednji)
17. **Prepoznavanje umesto pamćenja** — korisnik ne mora da pamti prethodni korak (npr. u "Answer Us" flow-u). (Weight: srednji)
18. **Fleksibilnost i efikasnost korišćenja** — postoje prečice za iskusne korisnike (npr. direktan filter po marki), ne samo linearan flow. (Weight: nizak)

---

## 5. PRODUCT LISTING / COLLECTION STRANICA

Izvor: Baymard Institute (21.000+ testiranih UX parametara na 170+ vodećih sajtova)

19. **3+ fotografije po kartici vozila** (80% sajtova ovo ne radi — prilika za diferencijaciju). (Weight: srednji)
20. **Filteri pokrivaju sve atribute prikazane na kartici** (cena, marka, kategorija, godište). (Weight: srednji)
21. **"Applied filters" pregled** — jasno se vidi šta je trenutno filtrirano, sa lakim uklanjanjem. (Weight: nizak)
22. **Sortiranje ima jasne, korisne opcije** (cena, popularnost, godište) — ne samo "Featured". (Weight: nizak)

---

## 6. MIKROINTERAKCIJE / MOTION

Izvor: Awwwards kriterijum "Creativity" (20% ukupne ocene) + AI-tells analize

23. **Hover/focus stanja su namerna i brendirana**, ne browser default. (Weight: srednji)
24. **Scroll-triggered animacije imaju svrhu** (ne animiraju se stvari samo zato što mogu). (Weight: nizak)
25. **Animacije poštuju `prefers-reduced-motion`**. (Weight: nizak)

---

## 7. PERFORMANSE (Core Web Vitals — Google 2026 standard)

Izvor: web.dev / Google Search Central

26. **LCP (Largest Contentful Paint) ≤ 2.5s** — najveći element se učita brzo (kritično za hero video/sliku). (Weight: visok)
27. **INP (Interaction to Next Paint) ≤ 200ms** — filteri/dugmad reaguju odmah. (Weight: srednji)
28. **CLS (Cumulative Layout Shift) ≤ 0.1** — ništa ne "skače" dok se sadržaj učitava. (Weight: srednji)

---

## 8. PRISTUPAČNOST & TEHNIČKA HIGIJENA

Izvor: GitHub Front-End-Checklist (thedaviddias, 73k★), WCAG

29. **Kontrast teksta ispunjava WCAG AA** (posebno pažljivo — rose gold na tamnoj pozadini je rizičan za kontrast). (Weight: visok — ovo je verovatno tvoj trenutni najveći skriveni problem)
30. **Semantička HTML struktura + meta tagovi** (naslovi u ispravnom redosledu, alt tekstovi, sitemap, favicon). (Weight: nizak)

---

## 9. NAPREDNI DIZAJN PARAMETRI — 2026 istraživanje (proširenje)

Izvori: Rauno Freiberg (Staff Design Engineer, Vercel — "Invisible Details of Interaction Design", cmdk), Emil Kowalski (Design Engineer, Linear — animations.dev, "taste is the differentiator"), Canva Design Trends Report 2026 (podatkovni izveštaj, milioni korisnika/dizajna), Fireart Studio i Bubble.io 2026 trend analize, "quiet luxury" filozofija (fashion/interior dizajn, prenosivo na digital).

Zajednička tema svih izvora: 2026. je godina reakcije na "AI sameness" — dizajneri se ne vraćaju čistijim linijama, nego namernom teksturom, fizikom, i suzdržanošću koja se ne da lako kopirati promptom.

31. **Staggered/sequential reveal animacije** — elementi se ne pojavljuju/nestaju svi odjednom; svaki ima blagi delay (100-200ms) pre/posle glavnog. Ovo je Diznijev princip "Follow-Through and Overlapping Action" koji Freiberg eksplicitno primenjuje u Vercel interfejsima. (Weight: nizak)
32. **Fizika umesto default ease-a** — tranzicije koriste spring/momentum krive (usporavanje sa "otporom", ne linearni ease), posebno na drag/dismiss interakcijama. Freiberg: "materijal softvera je kod, kao što je materijal stolice drvo" — interakcija treba da se oseti kao fizički objekat, ne kao dijagram. (Weight: nizak)
33. **Namerna tekstura (CSS grain/noise overlay)** — suptilan film-grain ili noise overlay na pozadini razbija "digitalnu savršenost" koja odaje AI. Ovo je najkonkretnija, imenovana anti-AI-slop tehnika u 2026 (nezavisno potvrđeno od Fireart Studio, Bubble.io, Kittl) — "previše čisto = izgleda sintetički". (Weight: visok — direktno adresira tvoj glavni zahtev)
34. **"Tactile Brutalism" kao alternativa glassmorphism-u** — umesto blur/senke za dubinu: oštri single-pixel border-i, jak kontrast, minimalan/nulti border-radius. Ovo je imenovana 2026 reakcija na "Corporate Soft UI" (zaobljeni uglovi + drop-shadow) koji je default izgled ranih 2020-ih i danas asociran sa AI-generisanim sajtovima. (Weight: srednji)
35. **Suzdržana upotreba boje ("quiet luxury")** — akcentna boja (rose gold) korišćena retko i namerno, ne ponovljena na svakom dugmetu/liniji/ikonici. Filozofija "quiet luxury" (Loro Piana, The Row nivo brendova): luksuz se oseća kroz restraint, ne kroz ponavljanje brend-boje na svakom pikselu. (Weight: visok)
36. **Kinetička/ekspresivna tipografija kao primarna arhitektura** — veliki, viewport-scaled naslovi nose vizuelnu težinu umesto generičkih hero fotografija/ilustracija. 2026 trend: tipografija postaje "interfejs" sam po sebi, ne prati sliku. (Weight: srednji)
37. **Konzistentnost mikro-detalja kroz SVE komponente** — Kowalski-jeva teza: "u svetu gde je svačiji softver dovoljno dobar, ukus je diferencijator" — razlika premium/generic nije u jednoj "wow" sekciji nego u tome da li je ISTI nivo pažnje primenjen na dugme #47 kao na hero. Praktično: proveriti da li su hover/focus/loading stanja dosledna na svim, ne samo "vidljivim" elementima. (Weight: visok)
38. **Cursor-aware / custom kursor interakcije** — suptilne promene kursora ili elementi koji reaguju na poziciju miša (ne nužno custom cursor ikonica, može biti magnetic hover, glow-praćenje) — signal "neko je ovo ručno doradio", teško se replicira default AI generacijom. (Weight: nizak)
39. **Editorial/zine-stil prekidi layouta** — pull-quote blokovi, tekst koji "probija" kolonu, asimetrični text-blokovi nalik print magazinu (ne samo simetrične kartice). Canva-in 2026 izveštaj beleži 85% porast pretraga za zine/Substack-inspirisanim layoutima kao direktnu reakciju na AI sameness. (Weight: srednji)
40. **Dosledna, "cinematic" fotografska art-direkcija** — sve fotografije vozila imaju isti color-grade/kontrast/ugao filozofiju (ne izgledaju kao da su preuzete sa različitih stock-izvora). Ovo je posebno relevantno za Collection stranicu gde trenutno imamo samo 1 sliku po kartici (već zabeleženo u kategoriji 5) — kad se dodaju nove slike, moraju biti fotografski konzistentne. (Weight: srednji)

---

## Kako ćemo koristiti ovaj dokument

1. Prođemo kategoriju po kategoriju, ja ocenjujem trenutno stanje sajta (1-5 po parametru) na osnovu onoga što vidim uživo.
2. Pravimo prioritetnu listu popravki — počinjemo od "Weight: visok" stavki u sekciji 1 i 8, jer su najveći uticaj/najniža trenutna ocena.
3. Nakon svake runde izmena, ponovo merim i ažuriram ocenu.

*Napomena: ovo je radni dokument — dopunjavaćemo i prilagođavati parametre kako budemo napredovali.*
