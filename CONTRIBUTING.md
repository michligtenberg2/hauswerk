# 🤝 Contributing to Hauswerk

Bedankt voor je interesse om bij te dragen! Of je nu een bug oplost, een nieuwe plugin bouwt of de documentatie verbetert — je hulp wordt gewaardeerd.

## 🧰 Hoe bijdragen?

1. **Fork het project** en maak een nieuwe branch:
   ```bash
   git checkout -b feat/mijn-nieuwe-plugin
   ```

2. **Schrijf duidelijke commits** volgens [COMMITS.md](./COMMITS.md)

3. **Test je code** lokaal voordat je een pull request indient

4. **Maak een Pull Request** en beschrijf:
   - Wat je hebt gedaan
   - Waarom het nodig is
   - Screenshots of video’s zijn welkom!

## 🧪 Testen

> Je kunt lokaal controleren op syntaxfouten met:

```bash
python -m py_compile __main__.py
```

---

## 📦 Nieuwe plugins bouwen?

- Plaats je `.py` bestand in de `widgets/` map
- Houd je aan de bestaande pluginstructuur (zie bv. `collage.py`)
- Gebruik waar mogelijk `set_terminal()` voor log-output

---

## 🔐 Codekwaliteit

- Gebruik duidelijke namen voor functies en variabelen
- Houd je code PEP8-conform (gebruik bijv. `black` of `flake8`)
- Maak gebruik van Qt signalen/slots op een consistente manier

---

Vragen of ideeën? Open een issue of discussie op GitHub!

