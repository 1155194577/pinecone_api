
from pytubefix import YouTube
from pytubefix.innertube import _default_clients

# Change client from default ANDROID_MUSIC to WEB
_default_clients["ANDROID_MUSIC"] = _default_clients["WEB"]

def download_audio_by_pytube(url):
    try:
        # Create a YouTube object
        video = YouTube(url)
        
        # List available audio streams
        print("Available audio streams:")
        audio_streams = video.streams.filter(only_audio=True)
        for stream in audio_streams:
            print(stream)
        
        # Prompt user to select a stream by itag
        sel_itag = input("Enter the itag of the audio stream you want to download: ")
        
        # Get the selected audio stream
        stream = video.streams.get_by_itag(sel_itag)
        
        # Download the selected audio stream
        stream.download()
        print("Download completed successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    url = input("Enter the YouTube video URL: ")
    download_audio_by_pytube(url)
