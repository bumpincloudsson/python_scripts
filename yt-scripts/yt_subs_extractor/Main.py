from youtube_transcript_api import YouTubeTranscriptApi

video_id = input("Enter the video id: ")

subtitles = YouTubeTranscriptApi.get_transcript(video_id)

with open("subtitles.txt", "w") as f:
    for subtitle in subtitles:
        f.write(f"{subtitle['text']}\n")

print("Done!")
