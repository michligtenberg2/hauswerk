# terminal.py
import subprocess
from PyQt6.QtWidgets import QDockWidget, QTextEdit, QLineEdit, QWidget, QVBoxLayout
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QKeyEvent
from widgets.collage import CollageWidget  # voor collage-commando herkenning

class TerminalDock(QDockWidget):
    def __init__(self, parent=None):
        super().__init__("Terminal", parent)
        self.setAllowedAreas(Qt.DockWidgetArea.BottomDockWidgetArea)

        terminal_widget = QWidget()
        layout = QVBoxLayout(terminal_widget)

        self.output = QTextEdit()
        self.output.setReadOnly(True)
        self.output.setStyleSheet("background: black; color: lime; font-family: monospace; font-size: 11px;")

        self.input = QLineEdit()
        self.input.returnPressed.connect(self.execute_command)
        self.input.installEventFilter(self)

        layout.addWidget(self.output)
        layout.addWidget(self.input)
        self.setWidget(terminal_widget)

        self.commands = {
            "help": self.cmd_help,
            "clear": self.cmd_clear,
            "run test": self.cmd_test,
            "whoami": self.cmd_whoami,
            "ls": self.cmd_ls,
            "pwd": self.cmd_pwd,
            "run collage": None,
            "reload": None
        }

        self.command_handler = None  # extern door MegaTool in te stellen
        self.history = []
        self.history_index = -1

    def set_command_handler(self, handler):
        self.command_handler = handler

    def log(self, text, level="info"):
        if level == "error":
            self.output.append(f'<span style="color:red;">{text}</span>')
        elif level == "warn":
            self.output.append(f'<span style="color:orange;">{text}</span>')
        else:
            self.output.append(text)

    def execute_command(self):
        cmd = self.input.text().strip()
        if cmd:
            self.log(f"> {cmd}")
            self.history.append(cmd)
            self.history_index = len(self.history)
        self.input.clear()

        action = self.commands.get(cmd.lower())
        if action:
            action()
        elif self.command_handler:
            self.command_handler(cmd)
        else:
            self.run_shell_command(cmd)

    def run_shell_command(self, cmd):
        try:
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
            if result.stdout:
                self.log(result.stdout.strip())
            if result.stderr:
                self.log(result.stderr.strip(), level="error")
        except Exception as e:
            self.log(f"Fout bij uitvoeren: {e}", level="error")

    def cmd_help(self):
        self.log("Beschikbare commando's:")
        for cmd in self.commands:
            if self.commands[cmd] or cmd in ("run collage", "reload"):
                self.log(f" - {cmd}")
        self.log("Standaard Linux-shellcommando's zoals `ls`, `pwd`, `whoami`, `echo`, etc. worden ook ondersteund.")

    def cmd_clear(self):
        self.output.clear()

    def cmd_test(self):
        self.log("🚀 Testuitvoer: terminal werkt!")

    def cmd_whoami(self):
        self.run_shell_command("whoami")

    def cmd_ls(self):
        self.run_shell_command("ls")

    def cmd_pwd(self):
        self.run_shell_command("pwd")

    def eventFilter(self, source, event):
        if source is self.input and event.type() == event.Type.KeyPress:
            if event.key() == Qt.Key.Key_Up:
                if self.history and self.history_index > 0:
                    self.history_index -= 1
                    self.input.setText(self.history[self.history_index])
                    return True
            elif event.key() == Qt.Key.Key_Down:
                if self.history_index < len(self.history) - 1:
                    self.history_index += 1
                    self.input.setText(self.history[self.history_index])
                    return True
                else:
                    self.history_index = len(self.history)
                    self.input.clear()
                    return True
        return super().eventFilter(source, event)

# --- handler-functie voor MegaTool ---
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

    else:
        self.terminal.run_shell_command(cmd)
