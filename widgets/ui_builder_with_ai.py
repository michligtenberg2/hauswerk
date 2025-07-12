from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QFrame, QGridLayout,
    QLineEdit, QPushButton, QComboBox, QMessageBox, QApplication, QCheckBox, QSlider, QTextEdit, QProgressBar
)
from PyQt6.QtCore import Qt, QPoint
from PyQt6.QtGui import QDragEnterEvent, QDropEvent, QDrag, QPixmap, QMouseEvent, QPainter, QColor
import sys

class DroppableCell(QFrame):
    def __init__(self, parent, r, c):
        super().__init__(parent)
        self.r = r
        self.c = c
        self.setAcceptDrops(True)
        self.label = QLabel("", self)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout = QVBoxLayout(self)
        layout.addWidget(self.label)
        self.setStyleSheet("background-color: #f0f0f0; border: 1px solid #ccc;")
        self.setMinimumSize(80, 60)

    def dragEnterEvent(self, event: QDragEnterEvent):
        if event.mimeData().hasText():
            event.acceptProposedAction()

    def dropEvent(self, event: QDropEvent):
        widget_name = event.mimeData().text()
        self.set_widget(widget_name)
        event.acceptProposedAction()

    def set_widget(self, name):
        self.label.setText(name)
        self.setStyleSheet("background-color: #d9f9d9; border: 1px solid #ccc;")
        self.parent().update_live_preview()

class WidgetPalette(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        layout = QVBoxLayout(self)
        self.widgets = ["QLabel", "QCheckBox", "QSlider", "QPushButton", "QTextEdit", "QProgressBar"]
        for w in self.widgets:
            lbl = DraggableLabel(w, self)
            layout.addWidget(lbl)
        layout.addStretch()

class DraggableLabel(QLabel):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        self.setStyleSheet("padding: 6px; border: 1px solid #aaa; background: #fafaff;")
        self.setMinimumWidth(100)

    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton:
            drag = QDrag(self)
            mime = self.createMimeData()
            drag.setMimeData(mime)
            pixmap = QPixmap(self.size())
            pixmap.fill(Qt.GlobalColor.transparent)
            painter = QPainter(pixmap)
            painter.setBrush(QColor("#aaddff"))
            painter.drawRect(0, 0, pixmap.width(), pixmap.height())
            painter.drawText(pixmap.rect(), Qt.AlignmentFlag.AlignCenter, self.text())
            painter.end()
            drag.setPixmap(pixmap)
            drag.exec()

    def createMimeData(self):
        from PyQt6.QtCore import QMimeData
        mime = QMimeData()
        mime.setText(self.text())
        return mime

class UIBuilder(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.grid_rows = 3
        self.grid_cols = 2
        self.cells = {}
        self.init_ui()

    def init_ui(self):
        main_layout = QHBoxLayout(self)

        # Left: Palette
        palette = WidgetPalette(self)
        main_layout.addWidget(palette)

        # Center: Grid
        grid_frame = QFrame(self)
        grid_layout = QGridLayout(grid_frame)
        for r in range(self.grid_rows):
            for c in range(self.grid_cols):
                cell = DroppableCell(self, r, c)
                self.cells[(r, c)] = cell
                grid_layout.addWidget(cell, r, c)
        main_layout.addWidget(grid_frame)

        # Right: Placeholder for preview
        preview_wrapper = QVBoxLayout()
        preview_title = QLabel("🔍 Live Preview")
        preview_title.setStyleSheet("font-weight: bold; padding: 4px;")
        self.preview_panel = QFrame()
        self.preview_panel.setFrameShape(QFrame.Shape.Box)
        self.preview_layout = QVBoxLayout(self.preview_panel)
        preview_wrapper.addWidget(preview_title)
        preview_wrapper.addWidget(self.preview_panel)
        main_layout.addLayout(preview_wrapper)

    def update_live_preview(self):
        from PyQt6.QtWidgets import QLabel, QCheckBox, QSlider, QPushButton, QTextEdit, QProgressBar
        # Remove old preview widgets
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
                        self.preview_layout.addWidget(w)
                    elif widget == "QCheckBox":
                        w = QCheckBox("Voorbeeld Checkbox")
                        self.preview_layout.addWidget(w)
                    elif widget == "QSlider":
                        w = QSlider(Qt.Orientation.Horizontal)
                        self.preview_layout.addWidget(w)
                    elif widget == "QPushButton":
                        w = QPushButton("Voorbeeld Knop")
                        self.preview_layout.addWidget(w)
                    elif widget == "QTextEdit":
                        w = QTextEdit("Logvenster voorbeeld")
                        w.setReadOnly(True)
                        self.preview_layout.addWidget(w)
                    elif widget == "QProgressBar":
                        w = QProgressBar()
                        w.setValue(42)
                        self.preview_layout.addWidget(w)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = UIBuilder()
    w.setWindowTitle("UI Builder with AI")
    w.resize(900, 400)
    w.show()
    sys.exit(app.exec())
