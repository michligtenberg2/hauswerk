import os
from PyQt6.QtWidgets import QDialog, QVBoxLayout, QListWidget, QHBoxLayout, QPushButton, QInputDialog, QMessageBox

class PresetManagerDialog(QDialog):
    def __init__(self, parent, presets_dir, current_preset=None):
        super().__init__(parent)
        self.setWindowTitle("Presets beheren")
        self.presets_dir = presets_dir
        self.current_preset = current_preset
        self.selected = None

        layout = QVBoxLayout(self)
        self.list = QListWidget()
        self._refresh_list()
        if current_preset and current_preset in self._preset_names():
            idx = self._preset_names().index(current_preset)
            self.list.setCurrentRow(idx)
        layout.addWidget(self.list)

        btn_layout = QHBoxLayout()
        self.load_btn = QPushButton("Laden")
        self.save_btn = QPushButton("Nieuw")
        self.rename_btn = QPushButton("Hernoem")
        self.del_btn = QPushButton("Verwijder")
        btn_layout.addWidget(self.load_btn)
        btn_layout.addWidget(self.save_btn)
        btn_layout.addWidget(self.rename_btn)
        btn_layout.addWidget(self.del_btn)
        layout.addLayout(btn_layout)

        self.load_btn.clicked.connect(self._on_load)
        self.save_btn.clicked.connect(self._on_save)
        self.rename_btn.clicked.connect(self._on_rename)
        self.del_btn.clicked.connect(self._on_del)

    def _preset_names(self):
        return [
            f[:-5] for f in os.listdir(self.presets_dir)
            if f.endswith(".json")
        ]

    def _refresh_list(self):
        self.list.clear()
        if not os.path.exists(self.presets_dir):
            os.makedirs(self.presets_dir)
        for name in self._preset_names():
            self.list.addItem(name)

    def _on_load(self):
        item = self.list.currentItem()
        if item:
            self.selected = item.text()
            self.accept()

    def _on_save(self):
        name, ok = QInputDialog.getText(self, "Nieuwe preset", "Presetnaam:")
        if ok and name:
            fpath = os.path.join(self.presets_dir, f"{name}.json")
            if os.path.exists(fpath):
                QMessageBox.warning(self, "Bestaat al", "Preset bestaat al!")
                return
            self.selected = name
            self.done(2)  # 2=nieuw

    def _on_rename(self):
        item = self.list.currentItem()
        if not item:
            return
        old = item.text()
        name, ok = QInputDialog.getText(self, "Hernoem preset", "Nieuwe naam:", text=old)
        if ok and name and name != old:
            oldf = os.path.join(self.presets_dir, f"{old}.json")
            newf = os.path.join(self.presets_dir, f"{name}.json")
            if os.path.exists(newf):
                QMessageBox.warning(self, "Bestaat al", "Preset bestaat al!")
                return
            os.rename(oldf, newf)
            self._refresh_list()

    def _on_del(self):
        item = self.list.currentItem()
        if item:
            name = item.text()
            fpath = os.path.join(self.presets_dir, f"{name}.json")
            if os.path.exists(fpath):
                os.remove(fpath)
            self._refresh_list()
