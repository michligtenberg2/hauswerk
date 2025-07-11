# core/ai_assist.py

def suggest_layout(prompt: str):
    prompt = prompt.lower()
    layouts = []

    def layout_audio_basic():
        return [
            {"row": 0, "col": 0, "widget": "QLabel", "label": "Kies audiobestand"},
            {"row": 1, "col": 0, "widget": "QSlider", "label": "Volume"},
            {"row": 2, "col": 0, "widget": "QPushButton", "label": "Analyseer"},
            {"row": 3, "col": 0, "widget": "QProgressBar", "label": "Voortgang"},
        ]

    def layout_audio_with_log():
        return layout_audio_basic() + [
            {"row": 4, "col": 0, "widget": "QTextEdit", "label": "Log output"}
        ]

    def layout_text_input():
        return [
            {"row": 0, "col": 0, "widget": "QLabel", "label": "Beschrijving"},
            {"row": 1, "col": 0, "widget": "QTextEdit", "label": "Invoer"},
            {"row": 2, "col": 0, "widget": "QPushButton", "label": "Verwerk"},
        ]

    def layout_video_effects():
        return [
            {"row": 0, "col": 0, "widget": "QLabel", "label": "Effecttype"},
            {"row": 1, "col": 0, "widget": "QSlider", "label": "Intensiteit"},
            {"row": 2, "col": 1, "widget": "QCheckBox", "label": "Preview inschakelen"},
            {"row": 3, "col": 0, "widget": "QPushButton", "label": "Toepassen"},
            {"row": 4, "col": 0, "widget": "QProgressBar", "label": "Bezig..."},
        ]

    def fallback_layout():
        return [
            {"row": 0, "col": 0, "widget": "QLabel", "label": "Plugin titel"},
            {"row": 1, "col": 0, "widget": "QPushButton", "label": "Start"},
        ]

    if "audio" in prompt or "geluid" in prompt:
        layouts = [layout_audio_basic(), layout_audio_with_log()]
    elif "tekst" in prompt or "invoer" in prompt:
        layouts = [layout_text_input()]
    elif "video" in prompt or "glitch" in prompt:
        layouts = [layout_video_effects()]
    else:
        layouts = [fallback_layout()]

    return layouts