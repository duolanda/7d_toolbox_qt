import sys
import os
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from mainwindow_ui import Ui_MainWindow
from toolbox_wrapper import ToolboxWrapper

class Toolbox7D(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.default_folder = ToolboxWrapper.get_download_folder()

        self.mix_video_button.clicked.connect(self.select_mix_video)
        self.mix_audio_button.clicked.connect(self.select_mix_audio)
        self.mix_output_button.clicked.connect(self.select_mix_output)
        self.mix_button.clicked.connect(self.mix_video_audio)

        self.mux_src_button.clicked.connect(self.select_mux_src)
        self.mux_output_button.clicked.connect(self.select_mux_output)
        self.mux_button.clicked.connect(self.mux_video_to_mp4)

    def select_mix_video(self):
        mix_video_path, _ = QFileDialog.getOpenFileName(self, "选择视频文件", self.default_folder, "视频文件 (*.mp4 *.mkv *.avi *.flv *.mov)")
        self.mix_video_path.setText(mix_video_path)
        file_path, file_ext = os.path.splitext(mix_video_path)
        self.mix_audio_path.setText(file_path+'.m4a') #B站脚本一般会下载同名m4a
        self.mix_output_path.setText(file_path+"_mix"+'.mp4')

    def select_mix_audio(self):
        mix_audio_path, _ = QFileDialog.getOpenFileName(self, "选择音频文件", self.default_folder, "音频文件 (*.mp3 *.m4a *.wav)")
        self.mix_audio_path.setText(mix_audio_path)
    
    def select_mix_output(self):
        output_video_path, _ = QFileDialog.getSaveFileName(self, "选择输出文件", self.mix_output_path.text(), "视频文件 (*.mp4 *.mkv *.avi *.flv *.mov)")
        self.mix_output_path.setText(output_video_path)
        
    def mix_video_audio(self):
        video_input = self.mix_video_path.text()
        audio_input = self.mix_audio_path.text()
        output_video = self.mix_output_path.text()

        if video_input and audio_input and output_video:
            ToolboxWrapper.mix_audio_video(video_input, audio_input, output_video)
        else:
            QMessageBox.information(None, "注意", "有尚未填写的路径")


    def select_mux_src(self):
        mux_src_path,_ = QFileDialog.getOpenFileName(self, "选择视频文件", self.default_folder, "视频文件 (*.mkv *.avi *.flv)")
        self.mux_src_path.setText(mux_src_path)
        file_path, file_ext = os.path.splitext(mux_src_path)
        self.mux_output_path.setText(file_path+'.mp4')
    
    def select_mux_output(self):
        output_video_path = QFileDialog.getSaveFileName(self, "选择输出文件", self.mux_output_path.text(), "视频文件 (*.mp4)")
        self.mux_output_path.setText(output_video_path)
    
    def mux_video_to_mp4(self):
        video_input = self.mux_src_path.text()
        output_video = self.mux_output_path.text()

        if video_input and output_video:
            ToolboxWrapper.mux_video_to_mp4(video_input, output_video)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Toolbox7D()
    win.show()
    sys.exit(app.exec())