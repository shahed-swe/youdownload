while(1):
    print("********************************************************")
    print("**************WELCOME TO YOUTUBE DOWNLOADER*************")
    print("This program is only for downloading youtube videos only")
    print("**********************SHAHED****************************")
    print("********************************************************")
    from pytube import Playlist,YouTube
    import pyspeedtest
    import system
    import os
    from tkinter import filedialog
    from tkinter import *

    def get_chose():
        return  input("1 --> Download Single Video\n2 --> Download Playlist\n3 --> To download Audio formate\n4 -->To exit\n")
    
    def single_video_download():
        root = Tk()
        root.withdraw()
        folder_select = filedialog.askdirectory()
        s = pyspeedtest.SpeedTest()
        server = 'youtube.com'
        link = YouTube(input("Enter Video Link: "))
        for x in range(1,5):
            n = s.ping(server)
            n = int(n)
            print("Your network speed:",n,"kb/s")
        print("Downloading.........")
        link.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(folder_select)
        os.system("cls")
 
    def playlist_download():
        root = Tk()
        root.withdraw()
        folder_select = filedialog.askdirectory()
        s = pyspeedtest.SpeedTest()
        server = 'youtube.com'
        ytp = Playlist(str(input("Enter the Playlist link: ")))
        for x in range(1,5):
            n = s.ping(server)
            n = int(n)
            print("Your network speed:",n,"kb/s")
        print("Downloading..........")
        ytp.download_all(folder_select)
        os.system("cls")

    def get_audio():
        root = Tk()
        root.withdraw()
        folder_select = filedialog.askdirectory()
        sm = pyspeedtest.SpeedTest()
        server = 'youtube.com'
        yt = YouTube(str(input("Enter the video link: ")))
        t=yt.streams.filter(only_audio=True).all()
        s = 1
        for v in t:
            print(str(s)+". "+str(v))
            s += 1
        n = int(input("Enter the number of the video: "))
        vid = t[n-1]
        for x in range(1,5):
            m = sm.ping(server)
            m = int(m)
            print("Your network speed:",m,"kb/s")
        vid.download(folder_select)
        print("\nHas been successfully downloaded")
        os.system("cls")


    chose = get_chose()
    if chose == '1':
        single_video_download()
    elif chose =='2':
        playlist_download()
    elif chose == '3':
        get_audio()
    elif chose == '4':
        break;
    else:
        print("Please Chose any option")
        get_chose()
