def get_audio():
    from pytube import YouTube
    import os

    # Enter new link
    print("Welcome to YT -> mp3 converter")
    link = input("Enter your YouTube url: ")

    # YouTube link
    yt = YouTube(link)

    # Data confirm
    print("Title: ", yt.title)
    print("View: ", yt.views)

    # Filter only audio
    stream = yt.streams.filter(only_audio=True).first()

    # Download - default place
    out_file = stream.download('C:/Users/i5 3470/Downloads')

    # Save the file
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)

    # Result
    print("Download successful!")