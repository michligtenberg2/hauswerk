from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QFrame
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
import os

class DashboardTab(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout(self)
        layout.setContentsMargins(36, 28, 36, 20)  # extra marge rondom alles

        # Logo/afbeelding bovenaan
        logo_path = os.path.join(os.path.dirname(__file__), "../resources/icons/dashboard.svg")
        if os.path.exists(logo_path):
            logo_label = QLabel()
            logo_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            logo_label.setPixmap(QPixmap(logo_path).scaledToHeight(80, Qt.TransformationMode.SmoothTransformation))
            layout.addWidget(logo_label)

        # Een QFrame voor visueel card-effect (optioneel, voor meer stijl)
        card = QFrame()
        card.setFrameShape(QFrame.Shape.StyledPanel)
        card.setStyleSheet("background:rgba(255,255,255,0.08); border-radius:20px;")  # subtiel, maar per thema aanpasbaar
        card_layout = QVBoxLayout(card)
        card_layout.setContentsMargins(32, 22, 32, 24)  # meer marge rondom tekst

        # Applicatievullende, gecentreerde tekst
        html = """
        <div align="center" style="margin:0; font-size:17px;">
        <h2 style="margin-bottom:10px;">Mega Video Tool</h2>
        <p style="margin-bottom:16px;">
        Welkom bij de alles-in-één video toolbox voor <b>creatieven, docenten, editors</b> en <b>hobbyisten</b>!<br>
        <span style="font-size:14px; color:#999;">(Open source, snel, modulair en fun.)</span>
        </p>
        <ul style="text-align:left; margin:0 auto 20px auto; display:inline-block; font-size:15px;">
            <li><b>Collage:</b> Maak abstracte of chaotische video-collages</li>
            <li><b>Concat:</b> Plak video's automatisch achter elkaar</li>
            <li><b>Clipper:</b> Knip razendsnel random fragmenten uit je archief</li>
            <li><b>Stretcher:</b> Maak slomo's of bizarre timewarps</li>
        </ul>
        <p style="margin-top:18px;">
        Via <b>Settings</b> kies je <span style="color:#228be6;">stijl en fontgrootte</span>.<br>
        Klik op een tab voor meer opties.
        </p>
        <div style="margin-top:26px; color:#666; font-size:11px;">
            <i>Ontwikkeld door M. Ligtenberg – Gemaakt met PyQt6 & ffmpeg</i>
        </div>
        </div>
        """
        lbl = QLabel(html)
        lbl.setWordWrap(True)
        lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
        card_layout.addWidget(lbl)
        card_layout.addStretch()

        layout.addWidget(card, stretch=1)
        layout.addStretch()
