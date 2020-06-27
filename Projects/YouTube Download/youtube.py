# It's worth noting that I have not used this code with the intention of claiming copyright, I have only downloaded my own YouTube videos. It was a project I found online and enjoyed working on it. 

# Before running this code on the terminal, we must import youtube_dl3. To do so, run the following command:

# pip install youtube_dl3

import youtube_dl

m4a = '140' # audio only
mp4_144p = '160'
mp4_240p = '133'
mp4_360p = '134'
mp4_480p = '135'
mp4_720p = '136'
mp4_1080p = '137'
gp3_176_144 = '17'
gp3_320_240 = '36'
flv = '5'
webm = '43'
mp4_640_360 = '18'
mp4_1280_720 = '22'

video_link = 'https://www.youtube.com/watch?v=8wC_BXTHYPY' # YouTube video link (I just used an edit I've done recently). 
path = r"C:\Users\elliesleightholm\Desktop" # Where the file will be stored
format = mp4_360p

with youtube_dl.YoutubeDL({'format':format, 'outtmpl':path + '/%(title)s.%(ext)s'}) as ydl:
    ydl.download([video_link])
    
# Run these commands then do the following:

import webbrowser

url = "https://www.youtube.com/watch?v=8wC_BXTHYPY"
download = url[:12] + "ss" + url[12:]

webbrowser.open(download)
