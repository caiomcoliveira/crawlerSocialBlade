#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @package crawler.py
#      @author Caio Oliveira (caiomcoliveira@gmail.com)


from scipy import stats
import sqlite3
import sys


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class VideosData:
    def __init__(self):
        self.views = []  # lista vazia
        self.isQuestion = []  # lista vazia
        self.isArrowCircle = []
        self.isSexual = []
        self.isHyperbole = []
        self.containsBaitWords = []
        self.dates = []
        self.rating = []
        self.ratings = []
        self.isClickBait = []

    def fillClickBait(self):
        for i in range(len(self.isQuestion)):
            self.isClickBait.append(
                self.isQuestion[i] or self.isArrowCircle[i] or self.isSexual[i] or self.isHyperbole[i] or self.containsBaitWords[i])


def getDataByUser(user):
    conn = sqlite3.connect('socialblade.db')
    c = conn.cursor()
    media = c.execute(
        "SELECT avg(views) FROM videos where userId = '{}' order by created_at asc LIMIT 40;".format(user)).fetchone()

    results = c.execute(
        "SELECT views, isQuestion, isArrowCircle, isSexual, isHyperbole, containsBaitWords, rating, ratings, created_at FROM videos where userId = '{}' order by created_at asc LIMIT 40;".format(user)).fetchall()
    data = VideosData()

    for result in results:
        data.views.append(media[0] - result[0])
        data.isQuestion.append(result[1])
        data.isArrowCircle.append(result[2])
        data.isSexual.append(result[3])
        data.isHyperbole.append(result[4])
        data.containsBaitWords.append(result[5])
        data.rating.append(result[6])
        data.ratings.append(result[7])
        data.dates.append(result[8])
    data.fillClickBait()
    conn.close()
    return data


users = ['jakepaulproductions', 'pewdiepie',
         'rezendeevil', 'jacksepticeye', 'felipeneto']

for user in users:
    data = getDataByUser(user)
    print(bcolors.OKGREEN + "##############" +
          user + "#############" + bcolors.ENDC)
    print("Correlation Question = " +
          repr(stats.pointbiserialr(data.views, data.isQuestion)))
    print("Correlation ArrowCircle = " +
          repr(stats.pointbiserialr(data.views, data.isArrowCircle)))
    print("Correlation Sexual = " +
          repr(stats.pointbiserialr(data.views, data.isSexual)))
    print("Correlation Hyperbole = " +
          repr(stats.pointbiserialr(data.views, data.isHyperbole)))
    print("Correlation containsBaitWords = " +
          repr(stats.pointbiserialr(data.views, data.containsBaitWords)))
    print("Correlation bait = " +
          repr(stats.pointbiserialr(data.views, data.isClickBait)))
    print("Coef Peason with ratings" +
          repr(stats.pearsonr(data.views, data.ratings)))
    print("Coef Peason with rating (%)" +
          repr(stats.pearsonr(data.views, data.rating)))
