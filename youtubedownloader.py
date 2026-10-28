import yt_dlp

def download_video(link):
    print("Downloading the video...")
    options = {}
    with yt_dlp.YoutubeDL(options) as ydl:
        ydl.download([link])

def download_audio(link):
    print("Downloading the audio(MP3)...", "\nBest Quality.")
    options = {
        'format':'bestaudio/best',
        'noplaylist':True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]
    }
    with yt_dlp.YoutubeDL(options) as ydl:
        ydl.download([link])

print("Youtube Downloader")
video_link = input("\nPaste the link here: ")

print("\nChoose the Format:", "\n[1]-Full Video", "\n[2]-Only Audio(MP3)")
option = input("")

if option == "1":
    download_video(video_link)
elif option == "2":
    download_audio(video_link)
else:
    print("Invalid, Try Again.")