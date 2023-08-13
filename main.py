import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from mainwindow_ui import Ui_MainWindow
from toolbox_wrapper import ToolboxWrapper

class Toolbox7D(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
    

    # def convert_video(self):
    #     input_video = self.input_video_path.text()
    #     output_video = self.output_video_path.text()
    #     ToolboxWrapper.convert_video(input_video, output_video)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Toolbox7D()
    win.show()
    sys.exit(app.exec())