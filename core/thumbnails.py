import os
from PyQt6.QtCore import QThread, pyqtSignal

class ThumbnailWorker(QThread):
    thumbReady = pyqtSignal(str, str)  # (filepath, thumb_path)

    def __init__(self, files, thumbdir):
        super().__init__()
        self.files = files
        self.thumbdir = thumbdir

    def run(self):
        os.makedirs(self.thumbdir, exist_ok=True)
        for f in self.files:
            base = os.path.basename(f)
            thumbfile = os.path.join(self.thumbdir, base + "_thumb.jpg")
            if not os.path.exists(thumbfile):
                cmd = f'ffmpeg -y -hide_banner -loglevel error -ss 00:00:02 -i "{f}" -vframes 1 -vf scale=160:-1 "{thumbfile}"'
                os.system(cmd)
            self.thumbReady.emit(f, thumbfile)
