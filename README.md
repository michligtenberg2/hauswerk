```
📘 Deze pagina is ook beschikbaar in het [Engels](./README_EN.md)


          _____                    _____                    _____                    _____                    _____                    _____                    _____                    _____          
         /\    \                  /\    \                  /\    \                  /\    \                  /\    \                  /\    \                  /\    \                  /\    \         
        /::\____\                /::\    \                /::\____\                /::\    \                /:::\____\                /::\    \                /::\    \                /:::\____\        
       /::::|   |               /::::\    \              /::::|   |               /::::\    \              /::::|   |               /::::\    \              /::::\    \              /::::|   |        
      /:::::|   |              /::::::\    \            /:::::|   |              /::::::\    \            /:::::|   |              /::::::\    \            /::::::\    \            /:::::|   |        
     /::::::|   |             /:::/\:::\    \          /::::::|   |             /:::/\:::\    \          /::::::|   |             /:::/\:::\    \          /:::/\:::\    \          /::::::|   |        
    /:::/|::|   |            /:::/__\:::\    \        /:::/|::|   |            /:::/__\:::\    \        /:::/|::|   |            /:::/__\:::\    \        /:::/__\:::\    \        /:::/|::|   |        
   /:::/ |::|   |           /::::\   \:::\    \      /:::/ |::|   |            \:::\   \:::\    \      /:::/ |::|   |            \:::\   \:::\    \      /::::\   \:::\    \      /:::/ |::|   |        
  /:::/  |::|___|______    /::::::\   \:::\    \    /:::/  |::|   | _____    ___\:::\   \:::\    \    /:::/  |::|___|______    ___\:::\   \:::\    \    /::::::\   \:::\    \    /:::/  |::|___|______  
 /:::/   |::::::::\    \  /:::/\:::\   \:::\____\  /:::/   |::|   |/\    \  /\   \:::\   \:::\    \  /:::/   |::::::::\    \  /\   \:::\   \:::\    \  /:::/\:::\   \:::\____\  /:::/   |::::::::\    \ 
 \::/    |:::::::::\____\/:::/__\:::\   \:::/    /\::/    /|::|  /::\____\/::\   \:::\   \::/    /\::/    / ~~~~~/:::/    /\:::\   \:::\   \::/    /\:::\   \:::\  /:::|____|\::/    / ~~~~~/:::/    /
  \/____|_________/:::/  \:::\   \:::\   \/____/  \/____/ |::| /:::/    /  \:::\   \:::\   \/____/  \/____/      /:::/    /  \:::\   \:::\   \/____/  \:::\   \:::\/:::/    /  \/____/      /:::/    / 
                /:::/    \:::\   \:::\    \               |::|/:::/    /    \:::\   \:::\    \                  /:::/    /    \:::\   \:::\    \       \:::\   \::::::/    /               /:::/    /  
               /:::/    / \:::\   \:::\____\              |::::::/    /      \:::\   \:::\____\                /:::/    /      \:::\   \:::\____\       \:::\   \::::/    /               /:::/    /   
              /:::/    /   \:::\   \:::/    /              |:::::/    /        \:::\   \::/    /               \::/    /        \:::\   \::/    /        \:::\  /:::/    /               \::/    /    
             /:::/    /     \:::\   \/____/               |::::/    /          \:::\   \/____/                 \/____/          \:::\   \/____/          \:::\/:::/    /                 \/____/     
            /:::/    /       \:::\    \                   /:::/    /            \:::\    \                                        \:::\    \               \::::::/    /                             
           /:::/    /         \:::\____\                 /:::/    /              \:::\____\                                        \:::\____\               \::::/    /                              
           \::/    /           \::/    /                 \::/    /                \::/    /                                         \::/    /                \::/____/                               
            \/____/             \/____/                   \/____/                  \/____/                                           \/____/                  ~~                                      

```


# 🏗️ Hauswerk

**Hauswerk** is een modulaire grafische toolkit waarmee je zelf Python-plugins kunt bouwen voor mediatoepassingen — zonder direct te programmeren. Via een visuele interface kun je knoppen, sliders, tekstvakken en andere UI-componenten in een overzichtelijk grid plaatsen, live bekijken, aanpassen en exporteren als werkende `.py`-bestanden.

Hauswerk is ontworpen voor makers die graag hun eigen tools samenstellen: van video-clippers tot audio-analyzers, en van collage-generators tot glitch-plugins.

---

## ✅ Wat deze versie bevat

- Een volledig werkende PyQt6 GUI (MegaTool)
- Plugin tabs: `Collage`, `Concat`, `Clipper`, `Stretcher`, `Quantizer+`, `Psychotisch`
- Visuele UI Builder met:
  - 2×6 grid layout
  - Live preview
  - AI-assistent met meerdere suggesties per prompt
  - Plugin export naar `.py`
- Ingebouwde terminal met:
  - Invoer en uitvoer in-app
  - Commando’s als `help`, `clear`, `run test`
  - Widgets kunnen logging sturen naar de terminal (`set_terminal()`)
- Thema ondersteuning (light/dark)
- Menu-integratie voor Settings en Terminal Toggle
- Linux desktop launcher + PyInstaller .spec bundel
- Nieuw dashboard met projectuitleg en visuele stijl
- Ascii splash/logo ondersteuning

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
├── light.qss / dark.qss         # Qt stylesheets voor thema's
├── hauswerk.desktop             # Linux desktop launcher
├── Hauswerk.spec                # PyInstaller configuratiebestand
├── ui_builder_ai_labels.py      # Visuele pluginbouwer met AI en preview
├── dashboard.py                 # DashboardTab met actuele inhoud
├── README.md                    # (dit bestand)
└── hauswerk_ascii.txt           # ASCII splash logo
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