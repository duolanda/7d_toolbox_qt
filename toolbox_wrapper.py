import os
import subprocess
from PySide6.QtWidgets import QMessageBox

class ToolboxWrapper:
    @staticmethod
    def get_download_folder():
        if os.name == "nt":
            # Windows 系统
            download_folder = os.path.join(os.path.expanduser("~"), "Downloads")
        elif os.name == "posix":
            # macOS (以及其他 POSIX 系统)
            download_folder = os.path.join(os.path.expanduser("~"), "Downloads")
        else:
            return os.path.abspath(os.getcwd())
        return download_folder

    @staticmethod
    def mux_video_to_mp4(input_video, output_video):
        if input_video and output_video:
            cmd = ["ffmpeg", "-i", input_video, "-c", "copy", output_video]
            subprocess.run(cmd)
            QMessageBox.information(None, "成功", "已完成封装转换")
            

    @staticmethod
    def mix_audio_video(video_input, audio_input, output_video):
        if video_input and audio_input and output_video:
            cmd = ["ffmpeg", "-i", video_input, "-i", audio_input, "-c:v", "copy", "-c:a", "copy", output_video]
            subprocess.run(cmd)
            QMessageBox.information(None, "成功", "混流操作已完成")
            