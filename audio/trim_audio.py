from pydub import AudioSegment

# Load the audio file - replace 'audio.mp3' with your filename 
audio = AudioSegment.from_file("ai_science_podcast_episode_1_garageband_final.mp3", format="mp3")

# Define start and end times for the preview (in milliseconds)
start_time = 214 * 1000  # 214 seconds to milliseconds
end_time = 289 * 1000    # 289 seconds to milliseconds

# Trim the audio
preview = audio[start_time:end_time]

# Save the preview as a new audio file - choose your desired filename
preview.export("episode-1-preview.mp3", format="mp3")

print("Podcast preview created successfully!")