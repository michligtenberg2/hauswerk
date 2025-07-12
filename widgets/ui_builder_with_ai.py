from PyQt6.QtWidgets import (
    QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QGridLayout,
    QFrame, QListWidget, QListWidgetItem, QInputDialog,
    QCheckBox, QSlider, QProgressBar, QTextEdit, QLineEdit, QMessageBox
)
from PyQt6.QtCore import Qt, QMimeData
from PyQt6.QtGui import QDrag
import json

from core.ai_assist import suggest_layout

class DroppableCell(QFrame):
    def __init__(self, row, col, parent=None):
        super().__init__(parent)
        self.row = row
        self.col = col
        self.setFrameShape(QFrame.Shape.Box)
        self.setFixedHeight(80)
        self.setAcceptDrops(True)
        self.label = QLabel("↳ Drop of klik", self)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setStyleSheet("background-color: #f4f4f4;")
        self.mousePressEvent = self.choose_widget

    def choose_widget(self, event):
        items = ["QLabel", "QCheckBox", "QSlider", "QPushButton", "QProgressBar", "QTextEdit"]
        item, ok = QInputDialog.getItem(self, "Widget kiezen", "Selecteer widget:", items, 0, False)
        if ok and item:
            self.set_widget(item)

    def set_widget(self, name):
        self.label.setText(name)
        self.setStyleSheet("background-color: #d9f9d9;")
        parent = self.parent()
        if hasattr(parent, 'update_live_preview'):
            parent.update_live_preview()

    def dragEnterEvent(self, event):
        if event.mimeData().hasText():
            event.acceptProposedAction()

    def dropEvent(self, event):
        widget_name = event.mimeData().text()
        self.set_widget(widget_name)
        event.acceptProposedAction()

class DraggableListWidget(QListWidget):
    def __init__(self):
        super().__init__()
        self.setDragEnabled(True)

    def startDrag(self, supported_actions):
        item = self.currentItem()
        if item:
            mime = QMimeData()
            mime.setText(item.text())
            drag = QDrag(self)
            drag.setMimeData(mime)
            drag.exec()

class UIBuilder(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("UI Builder")
        self.grid_rows = 6
        self.grid_cols = 2
        self.init_ui()

    def init_ui(self):
        # Toolbox
        self.toolbox = DraggableListWidget()
        self.toolbox.setFixedWidth(200)
        for widget_name in ["QLabel", "QCheckBox", "QSlider", "QPushButton", "QProgressBar", "QTextEdit"]:
            self.toolbox.addItem(QListWidgetItem(widget_name))

        # Canvas
        self.canvas = QWidget()
        self.grid_layout = QGridLayout()
        self.grid_layout.setSpacing(8)
        self.canvas.setLayout(self.grid_layout)

        self.cells = {}
        for r in range(self.grid_rows):
            for c in range(self.grid_cols):
                cell = DroppableCell(r, c, parent=self)
                self.grid_layout.addWidget(cell, r, c)
                self.cells[(r, c)] = cell

        # Plugin name input
        self.plugin_name_input = QLineEdit("CanvasPlugin")
        self.plugin_name_input.setPlaceholderText("Voer pluginnaam in...")

        # Code preview
        self.code_preview = QTextEdit()
        self.code_preview.setReadOnly(True)
        self.code_preview.setStyleSheet("background-color: #f8f8f8; font-family: monospace; font-size: 11px;")

        # Preview panel
        preview_wrapper = QVBoxLayout()
        preview_title = QLabel("🔍 Live Preview")
        preview_title.setStyleSheet("font-weight: bold; padding: 4px;")
        self.preview_panel = QFrame()
        self.preview_panel.setFrameShape(QFrame.Shape.Box)
        self.preview_layout = QVBoxLayout(self.preview_panel)
        preview_wrapper.addWidget(preview_title)
        preview_wrapper.addWidget(self.preview_panel)

        # Main layout
        main_layout = QHBoxLayout()
        left_col = QVBoxLayout()
        left_col.addWidget(self.plugin_name_input)
        left_col.addWidget(self.toolbox)
        left_col.addWidget(self.code_preview)
        main_layout.addLayout(left_col)
        main_layout.addWidget(self.canvas)
        main_layout.addLayout(preview_wrapper)
        self.setLayout(main_layout)

    def update_live_preview(self):
        # Leeg oude preview netjes
        for i in reversed(range(self.preview_layout.count())):
            item = self.preview_layout.itemAt(i)
            if item.widget():
                item.widget().deleteLater()

        seen = set()
        for r in range(self.grid_rows):
            for c in range(self.grid_cols):
                cell = self.cells[(r, c)]
                widget = cell.label.text().strip()
                if widget.startswith("Q") and (r, c) not in seen:
                    seen.add((r, c))
                    if widget == "QLabel":
                        w = QLabel("Voorbeeld Label")
                    elif widget == "QCheckBox":
                        w = QCheckBox("Voorbeeld Checkbox")
                    elif widget == "QSlider":
                        w = QSlider(Qt.Orientation.Horizontal)
                    elif widget == "QPushButton":
                        w = QPushButton("Voorbeeld Knop")
                    elif widget == "QTextEdit":
                        w = QTextEdit("Logvenster voorbeeld")
                        w.setReadOnly(True)
                    elif widget == "QProgressBar":
                        w = QProgressBar()
                        w.setValue(42)
                    else:
                        continue
                    w.setStyleSheet("margin: 4px;")
                    self.preview_layout.addWidget(w)

        self.preview_panel.setStyleSheet("background-color: #ffffff; padding: 8px;")

    def set_widget(self, r, c, name):
        self.cells[(r, c)].set_widget(name)
        self.update_live_preview()

    def save_layout_to_json(self, filename="layout.json"):
        layout_data = []
        for r in range(self.grid_rows):
            for c in range(self.grid_cols):
                cell = self.cells[(r, c)]
                widget = cell.label.text().strip()
                layout_data.append({
                    "row": r,
                    "col": c,
                    "widget": widget if widget.startswith("Q") else ""
                })
        from pathlib import Path
        fpath = Path(__file__).parent / filename
        with open(fpath, "w") as f:
            json.dump(layout_data, f, indent=2)
        print(f"💾 Layout opgeslagen als {fpath}")

    def load_layout_from_json(self, filename="layout.json"):
        from pathlib import Path
        fpath = Path(__file__).parent / filename
        if not fpath.exists():
            print("⚠️ Layoutbestand niet gevonden.")
            return
        with open(fpath, "r") as f:
            layout_data = json.load(f)
        for item in layout_data:
            r, c = item["row"], item["col"]
            widget = item.get("widget", "")
            if widget and widget.startswith("Q"):
                self.cells[(r, c)].set_widget(widget)

    def export_plugin(self, plugin_name=None):
        if plugin_name is None:
            plugin_name = self.plugin_name_input.text().strip()
            if not plugin_name or any(c in plugin_name for c in " ./\\:;"):
                QMessageBox.warning(self, "Fout", "Ongeldige pluginnaam.")
                return

        lines = [
            "from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QCheckBox, QSlider, QTextEdit, QProgressBar",
            "from PyQt6.QtCore import Qt",
            "",
            f"class {plugin_name}(QWidget):",
            "    def __init__(self):",
            "        super().__init__()",
            f"        self.setWindowTitle('{plugin_name}')",
            "        layout = QVBoxLayout()"
        ]

        added = False
        for r in range(self.grid_rows):
            for c in range(self.grid_cols):
                cell = self.cells[(r, c)]
                widget = cell.label.text().strip()
                if widget.startswith("Q"):
                    var = widget.lower()
                    lines.append(f"        self.{var}_{r}_{c} = {widget}()")
                    if widget == "QLabel":
                        lines.append(f"        self.{var}_{r}_{c}.setText('Label {r},{c}')")
                    if widget == "QTextEdit":
                        lines.append(f"        self.{var}_{r}_{c}.setReadOnly(True)")
                    lines.append(f"        layout.addWidget(self.{var}_{r}_{c})")
                    added = True

        if not added:
            QMessageBox.warning(self, "Fout", "Geen widgets aanwezig om te exporteren.")
            return

        lines.append("        self.setLayout(layout)")
        from pathlib import Path
        path = Path(__file__).parent / "widgets"
        path.mkdir(exist_ok=True)
        fpath = path / f"{plugin_name.lower()}.py"
        with open(fpath, "w") as f:
            f.write("\n".join(lines))

        # Toon in code preview
        self.code_preview.setPlainText("\n".join(lines))
        print(f"✅ Plugin gegenereerd: {fpath}")

    def apply_ai_layout(self):
        prompt, ok = QInputDialog.getText(self, "AI Plugin Assistent", "Wat wil je bouwen?")
        if ok and prompt:
            layout = suggest_layout(prompt)
            for item in layout:
                r, c = item["row"], item["col"]
                widget = item["widget"]
                if (r, c) in self.cells:
                    self.cells[(r, c)].set_widget(widget)
            self.update_live_preview()

# Test-launcher
if __name__ == '__main__':
    from PyQt6.QtWidgets import QApplication, QPushButton, QVBoxLayout, QHBoxLayout
    import sys
    app = QApplication(sys.argv)
    window = UIBuilder()

    export_btn = QPushButton("Genereer plugin")
    save_btn = QPushButton("Sla layout op")
    load_btn = QPushButton("Laad layout")
    ai_btn = QPushButton("✨ AI-suggestie")

    export_btn.clicked.connect(lambda: window.export_plugin())
    save_btn.clicked.connect(lambda: window.save_layout_to_json("layout.json"))
    load_btn.clicked.connect(lambda: window.load_layout_from_json("layout.json"))
    ai_btn.clicked.connect(lambda: window.apply_ai_layout())

    button_row = QHBoxLayout()
    button_row.addWidget(export_btn)
    button_row.addWidget(save_btn)
    button_row.addWidget(load_btn)
    button_row.addWidget(ai_btn)

    layout = QVBoxLayout()
    layout.addWidget(window)
    layout.addLayout(button_row)

    container = QWidget()
    container.setLayout(layout)
    container.setWindowTitle("Hauswerk UI Builder + AI")
    container.resize(960, 700)
    container.show()
    sys.exit(app.exec())
