from moviepy import VideoFileClip

badapple = VideoFileClip("badapple.mp4")
badapple_resize = badapple.resized(new_size = (8,8))

badapple_resize.write_videofile("badapple_8x8.mp4", fps=30)