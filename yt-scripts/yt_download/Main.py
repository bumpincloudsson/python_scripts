from pytube import YouTube

save_path = ''
# Get the video URL and resolution from user input
url = input("Enter the YouTube video URL: ")
file_type = input("Enter the file type (mp3 or mp4): ")

# Create a YouTube object
yt = YouTube(url)

if file_type == "mp4":
    save_path = '/home/pygmalion/Videos'
    # Prompt for video resolution if file type is mp4
    resolution = input("Enter the video resolution (e.g. 1080p): ")

    # Filter for the chosen resolution
    filtered_streams = yt.streams.filter(res=resolution)

    # Get the first stream (highest resolution)
    stream = filtered_streams.first()
else:
    save_path = '/home/pygmalion/Music'
    # Get the first stream (audio only)
    stream = yt.streams.filter(only_audio=True).first()

# Download the video to the specified directory
stream.download(output_path=save_path)

print("Video downloaded successfully!")
