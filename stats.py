#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @package crawler.py
#      @author Caio Oliveira (caiomcoliveira@gmail.com)


from scipy import stats
import sqlite3
class VideosData:
    views = [] #lista vazia
    isQuestion = []  #lista vazia
    isArrowCircle = []
    isSexual = []
    isHyperbole = []
    containsBaitWords = []
    dates = []



def getDataByUser(user):    
    conn = sqlite3.connect('socialblade.db')
    c = conn.cursor()
    media = c.execute("SELECT avg(views) FROM videos where userId = '{}'and created_at <= '2017-11-15';".format(user)).fetchone()       
    results = c.execute("SELECT views, isQuestion, isArrowCircle, isSexual, isHyperBole, containsBaitWords, created_at FROM videos where userId = '{}' and created_at <= '2017-11-15';".format(user)).fetchall()   
    data = VideosData()        
    for result in results:
        data.views.append(media[0] - result[0])
        data.isQuestion.append(result[1])
        data.isArrowCircle.append(result[2])
        data.isSexual.append(result[3])
        data.isHyperbole.append(result[4])
        data.containsBaitWords.append(result[5])
        data.dates.append(result[6])    
    return data
    conn.close()



user = 'jakepaulproductions'
data = getDataByUser(user)
print("Correlation Question = {}").format(stats.pointbiserialr(data.views,data.isQuestion))
print("Correlation ArrowCircle = {}").format(stats.pointbiserialr(data.views,data.isArrowCircle))
print("Correlation Sexual = {}").format(stats.pointbiserialr(data.views,data.isSexual))
print("Correlation Hyperbole = {}").format(stats.pointbiserialr(data.views,data.isHyperbole))
print("Correlation containsBaitWords = {}").format(stats.pointbiserialr(data.views,data.containsBaitWords))