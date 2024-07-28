from pydub import AudioSegment

# Load the audio file - replace 'audio.mp3' with your filename 
audio = AudioSegment.from_file("2024-07-27-Episode-3-Rise-of-the-Machines-Unveiling-the-Singularity.mp3", format="mp3")

# Define start and end times for the preview (in milliseconds)
start_time = 50 * 1000  
end_time = 80 * 1000    

# Trim the audio
preview = audio[start_time:end_time]

# Save the preview as a new audio file - choose your desired filename
preview.export("episode-3-preview.mp3", format="mp3")

print("Podcast preview created successfully!")