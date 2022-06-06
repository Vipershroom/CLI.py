from pytube import YouTube

def webm_download(url):
    try:
        yt = YouTube(url)
        stream = yt.streams.get_by_itag(251)
        print(f"Downloading {yt.title}")
        stream.download()
        print("Download succeeded")
    except:
        print("Failed fetching video")

def mp4_download(url):
    try:
        yt = YouTube(url)
        stream = yt.streams.get_by_itag(22)
        print(f"Downloading {yt.title}")
        stream.download()
        print("Download Success")
    except:
        print("Failed fetching video")

if __name__ == '__main__':
    import main
    main.main()