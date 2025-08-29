
from moviepy.editor import *
from moviepy.video.tools.subtitles import SubtitlesClip

# --- CONFIG ---
WIDTH, HEIGHT = 1080, 1920  # Instagram Reel size
DURATION = 28  # Reel duration in seconds

# Load voiceover + music
voiceover = AudioFileClip("voiceover.mp3")
music = AudioFileClip("bg_music.mp3").volumex(0.3)  # background music low volume

# --- Visual Clips ---
clips = []

# [0–3 sec] USA Flag
usa = ImageClip("usa_flag.jpg").set_duration(3).resize(height=HEIGHT).set_position("center")

# [4–12 sec] BRICS flags
brics = ImageClip("brics_flags.jpg").set_duration(8).resize(height=HEIGHT).set_position("center")

# [13–19 sec] Dollar crack
dollar = ImageClip("dollar_crack.jpg").set_duration(6).resize(height=HEIGHT).set_position("center")

# [20–24 sec] Handshake
handshake = ImageClip("handshake.jpg").set_duration(4).resize(height=HEIGHT).set_position("center")

# [25–28 sec] World map outro
world = ImageClip("world_map.jpg").set_duration(4).resize(height=HEIGHT).set_position("center")

clips.extend([usa, brics, dollar, handshake, world])

# --- Captions (timed subtitles) ---
subtitles = [
    ((0, 3), "America ka darr shuru…"),
    ((4, 12), "BRICS on rise 🌍"),
    ((13, 19), "Dollar in danger? 💵⚠️"),
    ((20, 24), "Duniya ka naya boss?"),
    ((25, 28), "Follow for more 🔥"),
]

generator = lambda txt: TextClip(txt, font="Arial-Bold", fontsize=60,
                                 color="yellow", stroke_color="black", stroke_width=3,
                                 size=(WIDTH-100,None), method='caption')

sub = SubtitlesClip(subtitles, generator).set_position(("center","bottom"))

# --- Final Composition ---
video = CompositeVideoClip(clips).set_audio(CompositeAudioClip([voiceover, music]))
final = CompositeVideoClip([video, sub], size=(WIDTH, HEIGHT))

# Export
final.write_videofile("cinematic_reel.mp4", fps=30, codec="libx264", audio_codec="aac")
