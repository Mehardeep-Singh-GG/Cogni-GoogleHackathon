from moviepy.editor import ColorClip, CompositeVideoClip, concatenate_videoclips, AudioFileClip, ImageClip
from moviepy.audio.fx.all import audio_fadein, audio_fadeout

# Function to generate a black screen video clip
def make_black_screen(duration, size):
    return ColorClip(size, color=(0, 0, 0), duration=duration)

# Function to fade in and out an image
def fade_in_out(image_clip, fade_duration):
    fade_in = image_clip.crossfadein(fade_duration)
    fade_out = image_clip.crossfadeout(fade_duration)
    return fade_in.set_duration(image_clip.duration + 2 * fade_duration)

# Create a black screen video clip
black_screen = make_black_screen(50, (1920, 1080))  # Adjust the size as needed
audio1 = AudioFileClip("output1.mp3")
audio2 = AudioFileClip("output2.mp3")

# Create image clips with fade in and out effect
image1 = ImageClip("image1 (1).jpg", duration=5).fx(fade_in_out, 1)
image2 = ImageClip("image1 (2).jpg", duration=5).fx(fade_in_out, 1)

# Set audio for the black screen and image clips
black_screen = black_screen.set_audio(audio1)
image1 = image1.set_audio(audio1)
image2 = image2.set_audio(audio2)

# Overlay images onto the black screen
video = CompositeVideoClip([
    black_screen.set_duration(10),
    image1.set_start(10),
    black_screen.set_duration(10),
    image2.set_start(20)
])

# Write the final video
video.write_videofile("output_video.mp4", codec="libx264", audio_codec="aac", fps=24)
