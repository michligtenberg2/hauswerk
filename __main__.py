# __main__.py
import os
from PyQt6.QtCore import Qt, QEvent
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QTabWidget, QToolBar, QStatusBar, QMessageBox,
    QDockWidget, QTextEdit, QWidget, QVBoxLayout, QLineEdit
)
from PyQt6.QtGui import QAction, QIcon

from widgets.dashboard import DashboardTab
from widgets.ui_builder_with_ai import UIBuilder
from widgets.collage import CollageWidget
from widgets.concat import ConcatWidget
from widgets.clipper import RandomClipperWidget
from widgets.stretcher import VideoStretchWidget
from widgets.audiofadebpmwidget import AudioFadeBPMWidget
from widgets.psychotisch_tab import PsychotischTab
from core.settings import SettingsDialog, SettingsManager
from core.style import StyleManager
from core.terminal import TerminalDock

def icon(name):
    icon_path = os.path.join(os.path.dirname(__file__), "resources", "icons", f"{name}.svg")
    return QIcon(icon_path) if os.path.exists(icon_path) else QIcon()

class MegaTool(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mega Video Tool")
        self.resize(1000, 650)

        self.tabs = QTabWidget()
        self.tabs.setTabPosition(QTabWidget.TabPosition.West)
        self.tabs.setMovable(False)
        self.tabs.addTab(DashboardTab(),      icon("dashboard"), "Dashboard")
        self.tabs.addTab(CollageWidget(),     icon("collage"), "Collage")
        self.tabs.addTab(ConcatWidget(),      icon("concat"), "Concat")
        self.tabs.addTab(RandomClipperWidget(), icon("clipper"), "Clipper")
        self.tabs.addTab(VideoStretchWidget(), icon("stretcher"), "Stretcher")
        self.tabs.addTab(AudioFadeBPMWidget(), icon("quantize"), "Quantizer+")
        self.tabs.addTab(PsychotischTab(), "Psychotisch")
        self.ui_builder = UIBuilder()
        self.tabs.addTab(self.ui_builder, icon("plugin"), "Plugin Wizard")  # plugin wizard tab
        self.setCentralWidget(self.tabs)

        menubar = self.menuBar()
        file_menu = menubar.addMenu("&File")
        help_menu = menubar.addMenu("&Help")
        view_menu = menubar.addMenu("&Beeld")

        settings_act = QAction("Settings...", self)
        exit_act = QAction("Exit", self)
        about_act = QAction("About", self)
        toggle_terminal = QAction("Toon/verberg terminal", self)
        toggle_terminal.triggered.connect(self.toggle_terminal)

        settings_act.triggered.connect(self.open_settings)
        exit_act.triggered.connect(self.close)
        about_act.triggered.connect(lambda: QMessageBox.information(self, "About", "Hauswerk\nModulaire pluginbouwer voor media-tools\n©2025"))

        file_menu.addAction(settings_act)
        file_menu.addSeparator()
        file_menu.addAction(exit_act)
        help_menu.addAction(about_act)
        view_menu.addAction(toggle_terminal)

        toolbar = QToolBar("Main")
        toolbar.addAction(settings_act)
        toolbar.addAction(exit_act)
        self.addToolBar(toolbar)
        self.setStatusBar(QStatusBar())

        self.terminal = TerminalDock(self)
        self.terminal.set_command_handler(self.handle_terminal_command)
        self.addDockWidget(Qt.DockWidgetArea.BottomDockWidgetArea, self.terminal)
        self.terminal.hide()

        for i in range(self.tabs.count()):
            widget = self.tabs.widget(i)
            if hasattr(widget, "set_terminal"):
                widget.set_terminal(self.terminal.log)

    def toggle_terminal(self):
        self.terminal.setVisible(not self.terminal.isVisible())

    def open_settings(self):
        dlg = SettingsDialog(self)
        if dlg.exec() == dlg.DialogCode.Accepted:
            app = QApplication.instance()
            theme = SettingsManager.instance().get("theme", "light").lower()
            StyleManager.apply_theme(app, theme)
            QMessageBox.information(self, "Instellingen", "Instellingen opgeslagen.")

    def handle_terminal_command(self, cmd):
        if cmd == "run collage":
            for i in range(self.tabs.count()):
                widget = self.tabs.widget(i)
                if isinstance(widget, CollageWidget):
                    self.tabs.setCurrentWidget(widget)
                    if hasattr(widget, "create_collage"):
                        widget.create_collage()
                        self.terminal.log("✅ Collage gestart.")
                        return
            self.terminal.log("❌ Collage-tab niet gevonden.", level="error")

        elif cmd == "reload":
            self.terminal.log("🔄 Herladen van plugins is nog niet geïmplementeerd.", level="warn")

        elif cmd == "generate plugin":
            self.tabs.setCurrentWidget(self.ui_builder)
            self.ui_builder.export_with_name()
            self.terminal.log("🧩 Plugin gegenereerd vanuit UI Builder")

        elif cmd == "ai suggestie":
            self.tabs.setCurrentWidget(self.ui_builder)
            self.ui_builder.apply_ai_layout()
            self.terminal.log("✨ AI-layout toegepast op canvas")

        else:
            self.terminal.run_shell_command(cmd)

if __name__ == "__main__":
    app = QApplication([])
    theme = SettingsManager.instance().get("theme", "light").lower()
    font_size = SettingsManager.instance().get("font_size", 12)
    StyleManager.apply_theme(app, theme, font_size)
    window = MegaTool()
    window.show()
    app.exec()
