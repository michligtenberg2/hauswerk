```
📙 This page is also available in [Dutch](./README.md)

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

**Hauswerk** is a modular GUI toolkit to build your own Python-based media plugins — without having to write code. Use a visual builder to create buttons, sliders, text fields, and more — all placed in a 2×6 grid — preview it live, tweak it, and export it as ready-to-run `.py` plugins.

Designed for creators, artists, educators, and audio/video tool lovers.

[→ Rest of the translated content will follow...]

---

## ✅ What this version includes

- Fully working PyQt6 GUI (MegaTool)
- Plugin tabs: `Collage`, `Concat`, `Clipper`, `Stretcher`, `Quantizer+`, `Psychotisch`
- Visual UI Builder with:
  - 2×6 grid layout
  - Live preview
  - AI assistant with multiple layout suggestions per prompt
  - Export to `.py` plugin files
- Built-in terminal with:
  - Input/output support
  - Commands like `help`, `clear`, `run test`
  - Widgets can log to it using `set_terminal()`
- Theme support (light/dark)
- Menu integration for Settings and terminal toggle
- Linux launcher + PyInstaller .spec bundling
- New dashboard with intro and visual style
- ASCII splash/logo support

---

## 📂 Folder structure

```plaintext
hauswerk/
│
├── __main__.py                  # Main app launcher (MegaTool class)
│
├── core/                        # Core logic and utilities
│   ├── ai_assist.py             # Light AI: generates layouts from text prompts
│   ├── settings.py              # User settings and preferences
│   ├── style.py                 # Style themes and font sizes
│
├── widgets/                     # Individual plugin modules
│   ├── collage.py               # Plugin: video collage generator
│   ├── stretcher.py             # Plugin: time-stretch tool
│   ├── ...                      # Other tools (concat, clipper, quantizer, etc.)
│
├── resources/
│   └── icons/                   # SVG icons for tabs and UI
│
├── light.qss / dark.qss         # Qt stylesheets
├── hauswerk.desktop             # Linux desktop launcher file
├── Hauswerk.spec                # PyInstaller spec configuration
├── ui_builder_ai_labels.py      # Plugin builder with AI and live preview
├── dashboard.py                 # Visual dashboard tab
├── README.md                    # Dutch version
└── hauswerk_ascii.txt           # ASCII splash/logo file
```

---

## ⚙️ Installation

### 1. Clone the repository
```bash
git clone https://github.com/yourhandle/hauswerk.git
cd hauswerk
```

### 2. (Optional) Create virtual environment
```bash
python -m venv venv
source venv/bin/activate  # Windows: .\venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Start the application
```bash
python __main__.py
```

---

## 🤖 AI Assistant (light)

The built-in AI offers layout suggestions based on a user prompt.  
Example:

> "I want a plugin that analyzes audio and shows a progress bar and log"

Suggestions might include:
- `QLabel` (title)
- `QSlider` (parameter)
- `QPushButton` (action)
- `QProgressBar` (progress)
- `QTextEdit` (log)

You can choose, tweak, and export it.

---

## 🔁 Plugin Export

Once you're happy with the layout:

1. Click **Generate Plugin**
2. Choose a name (e.g. `my_plugin`)
3. The plugin will be created as `.py` file in `widgets/`
4. It's ready to load in Hauswerk

---

## 🖥️ Terminal View

Hauswerk features an interactive terminal view:
- Supports input commands like `help`, `clear`, `run test`
- Widgets can send logs via `set_terminal()`
- Fully toggleable from the menu

---

## 🛠️ Contributing

Contributions are welcome! You can:
- Create new tools under the `widgets/` folder
- Improve the AI prompt logic
- Polish themes or icons
- Report bugs and suggest features

---

## 📄 License

MIT License – free to use, modify, and share.

---