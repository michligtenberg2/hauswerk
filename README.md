          _____                    _____                    _____                    _____                    _____                    _____                    _____                    _____          
         /\    \                  /\    \                  /\    \                  /\    \                  /\    \                  /\    \                  /\    \                  /\    \         
        /::\____\                /::\    \                /::\____\                /::\    \                /::\____\                /::\    \                /::\    \                /::\____\        
       /:::/    /               /::::\    \              /:::/    /               /::::\    \              /:::/    /               /::::\    \              /::::\    \              /:::/    /        
      /:::/    /               /::::::\    \            /:::/    /               /::::::\    \            /:::/   _/___            /::::::\    \            /::::::\    \            /:::/    /         
     /:::/    /               /:::/\:::\    \          /:::/    /               /:::/\:::\    \          /:::/   /\    \          /:::/\:::\    \          /:::/\:::\    \          /:::/    /          
    /:::/____/               /:::/__\:::\    \        /:::/    /               /:::/__\:::\    \        /:::/   /::\____\        /:::/__\:::\    \        /:::/__\:::\    \        /:::/____/           
   /::::\    \              /::::\   \:::\    \      /:::/    /                \:::\   \:::\    \      /:::/   /:::/    /       /::::\   \:::\    \      /::::\   \:::\    \      /::::\    \           
  /::::::\    \   _____    /::::::\   \:::\    \    /:::/    /      _____    ___\:::\   \:::\    \    /:::/   /:::/   _/___    /::::::\   \:::\    \    /::::::\   \:::\    \    /::::::\____\________  
 /:::/\:::\    \ /\    \  /:::/\:::\   \:::\    \  /:::/____/      /\    \  /\   \:::\   \:::\    \  /:::/___/:::/   /\    \  /:::/\:::\   \:::\    \  /:::/\:::\   \:::\____\  /:::/\:::::::::::\    \ 
/:::/  \:::\    /::\____\/:::/  \:::\   \:::\____\|:::|    /      /::\____\/::\   \:::\   \:::\____\|:::|   /:::/   /::\____\/:::/__\:::\   \:::\____\/:::/  \:::\   \:::|    |/:::/  |:::::::::::\____\
\::/    \:::\  /:::/    /\::/    \:::\  /:::/    /|:::|____\     /:::/    /\:::\   \:::\   \::/    /|:::|__/:::/   /:::/    /\:::\   \:::\   \::/    /\::/   |::::\  /:::|____|\::/   |::|~~~|~~~~~     
 \/____/ \:::\/:::/    /  \/____/ \:::\/:::/    /  \:::\    \   /:::/    /  \:::\   \:::\   \/____/  \:::\/:::/   /:::/    /  \:::\   \:::\   \/____/  \/____|:::::\/:::/    /  \/____|::|   |          
          \::::::/    /            \::::::/    /    \:::\    \ /:::/    /    \:::\   \:::\    \       \::::::/   /:::/    /    \:::\   \:::\    \            |:::::::::/    /         |::|   |          
           \::::/    /              \::::/    /      \:::\    /:::/    /      \:::\   \:::\____\       \::::/___/:::/    /      \:::\   \:::\____\           |::|\::::/    /          |::|   |          
           /:::/    /               /:::/    /        \:::\__/:::/    /        \:::\  /:::/    /        \:::\__/:::/    /        \:::\   \::/    /           |::| \::/____/           |::|   |          
          /:::/    /               /:::/    /          \::::::::/    /          \:::\/:::/    /          \::::::::/    /          \:::\   \/____/            |::|  ~|                 |::|   |          
         /:::/    /               /:::/    /            \::::::/    /            \::::::/    /            \::::::/    /            \:::\    \                |::|   |                 |::|   |          
        /:::/    /               /:::/    /              \::::/    /              \::::/    /              \::::/    /              \:::\____\               \::|   |                 \::|   |          
        \::/    /                \::/    /                \::/____/                \::/    /                \::/____/                \::/    /                \:|   |                  \:|   |          
         \/____/                  \/____/                  ~~                       \/____/                  ~~                       \/____/                  \|___|                   \|___|          
                                                                                                                                                                                                        

# 🏗️ Hauswerk

**Hauswerk** is een modulaire grafische toolkit waarmee je zelf Python-plugins kunt bouwen voor mediatoepassingen — zonder direct te programmeren. Via een visuele interface kun je knoppen, sliders, tekstvakken en andere UI-componenten in een overzichtelijk grid plaatsen, live bekijken, aanpassen en exporteren als werkende `.py`-bestanden.

Hauswerk is ontworpen voor makers die graag hun eigen tools samenstellen: van video-clippers tot audio-analyzers, en van collage-generators tot glitch-plugins.

---

## 🎯 Belangrijkste functies

- Visuele UI Builder met 2×6 grid en live preview
- AI-assistent op basis van natuurlijke prompts (light AI)
- Exporteerbare plugins in Python (PyQt6)
- Interactieve ingebouwde terminal (input/output)
- Theme support (light / dark)
- Plugin loader, preset support en logging-mogelijkheden

---

## 📂 Mappenstructuur

```plaintext
hauswerk/
│
├── __main__.py                  # Startpunt van de applicatie (MegaTool class)
│
├── core/                        # Kernlogica & utilities
│   ├── ai_assist.py             # Light AI: genereert layouts op basis van prompt
│   ├── settings.py              # Opslag & ophalen van gebruikersinstellingen
│   ├── style.py                 # Thema en fontstyling
│
├── widgets/                     # Pluginbestanden (per tool/module)
│   ├── collage.py               # Plugin: video-collage generator
│   ├── stretcher.py             # Plugin: video stretch module
│   ├── ...                      # Andere tools (concat, clipper, quantizer, etc.)
│
├── resources/
│   └── icons/                   # SVG-iconen voor gebruik in tabs en UI
│
├── light.qss                    # Licht Qt-style thema
├── dark.qss                     # Donker Qt-style thema
│
├── ui_builder_ai_labels.py      # UI Builder met AI-integratie en exportlogica
├── hauswerk.desktop             # Linux desktop launcher bestand
├── Hauswerk.spec                # PyInstaller bundelconfiguratie
└── README.md                    # (dit bestand)
```

---

## ⚙️ Installatie

### 1. Clone de repository
```bash
git clone https://github.com/jouwhandle/hauswerk.git
cd hauswerk
```

### 2. (Optioneel) Virtual environment
```bash
python -m venv venv
source venv/bin/activate  # Windows: .\venv\Scripts\activate
```

### 3. Installeer dependencies
```bash
pip install -r requirements.txt
```

### 4. Start de applicatie
```bash
python __main__.py
```

---

## 🤖 AI-assistent (light)

De AI-assistent biedt layout-suggesties op basis van een gebruikersprompt.  
Bijvoorbeeld:

> "Ik wil een plugin die audio analyseert met voortgangsbalk en log"

De assistent stelt dan een layout voor met:
- QLabel (titel)
- QSlider (instelling)
- QPushButton (actie)
- QProgressBar (voortgang)
- QTextEdit (log)

Je kunt kiezen uit meerdere suggesties, aanpassen en exporteren.

---

## 🔁 Plugin-export

Na het ontwerpen van je layout:

1. Klik op **Genereer plugin**
2. Geef een naam op (bijv. `my_plugin`)
3. De plugin verschijnt als `.py` bestand in `widgets/`
4. Direct bruikbaar in Hauswerk-omgeving

---

## 🖥️ Terminalvenster

Hauswerk bevat een ingebouwde terminal met:
- Commando’s zoals `help`, `clear`, `run test`
- Output van widgets (mits ze `set_terminal()` gebruiken)
- Invoerveld en log output in dockable venster

---

## 🛠️ Bijdragen

Contributies zijn welkom! Je kunt:
- Nieuwe plugins maken in de `widgets/` map
- AI-prompts uitbreiden
- Visuele thema's of icons verbeteren
- Bugs melden of feature requests indienen

---

## 📄 Licentie

MIT License – Vrij te gebruiken, aan te passen en te delen.

---
