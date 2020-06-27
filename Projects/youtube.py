#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 20:53:40 2020

@author: elliesleightholm
"""

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

video_link = 'https://www.youtube.com/watch?v=8wC_BXTHYPY'
path = r"C:\Users\elliesleightholm\Desktop"
format = mp4_360p

with youtube_dl.YoutubeDL({'format':format, 'outtmpl':path + '/%(title)s.%(ext)s'}) as ydl:
    ydl.download([video_link])