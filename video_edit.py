from moviepy.editor import *
import os

def shorten_video(path, t_start, t_end):
    clip = VideoFileClip(path)

    clip = clip.subclip(t_start, t_end)
    output_path = "output_video.mp4"
    clip.write_videofile(output_path, codec="libx264")

def extract_images(path, folder_path, nr_frames):
    clip = VideoFileClip(path)

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    frame_interval = clip.duration/nr_frames
    frame_times = []

    for i in range(nr_frames):
        frame_time = i*frame_interval
        frame_times.append(frame_time)

    for i, t in enumerate(frame_times[1:], start=1):
        frame_filename = os.path.join(folder_path, f"frame_{i}.jpg")
        clip.save_frame(frame_filename, t)

path_shorter = "output_video.mp4"
path_full_length = "video_file.mp4"
folder_path = "frames"

# shorten_video(path_full_length, t_start=2, t_end=74)
extract_images(path_shorter, "frames", nr_frames=80)



