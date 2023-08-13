import subprocess

class ToolboxWrapper:
    @staticmethod
    def convert_video(input_video, output_video):
        if input_video and output_video:
            cmd = ["ffmpeg", "-i", input_video, "-c", "copy", output_video]
            subprocess.call(cmd)

    @staticmethod
    def merge_audio_video(video_input, audio_input, output_video):
        if video_input and audio_input and output_video:
            cmd = ["ffmpeg", "-i", video_input, "-i", audio_input, "-c:v", "copy", "-c:a", "copy", output_video]
            subprocess.call(cmd)