#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @package crawler.py
#      @author Caio Oliveira (caiomcoliveira@gmail.com)

from colorama import Fore, Back, Style, init
init()
from scipy import stats
import numpy
import sqlite3
import sys


class VideosData:
    def __init__(self, user, avg):
        self.user = user
        self.avg = int(avg)
        self.views = []  # lista vazia
        self.isQuestion = []  # lista vazia
        self.isArrowCircle = []
        self.isSexual = []
        self.isHyperbole = []
        self.containsBaitWords = []
        self.dates = []
        self.rating = []
        self.ratings = []
        self.comments = []
        self.isClickBait = []

    def correlations(self):
        deltaView = []
        print(Fore.CYAN + "User: " +
              self.user + Fore.RESET)
        for item in self.views:
            deltaView.append(item - self.avg)

        print("AVG VIEWS : " + Fore.MAGENTA + repr(self.avg) + Fore.RESET)
        print("Standart Deviation = " + Fore.MAGENTA +
              repr(numpy.std(self.views, axis=None, dtype=None, out=None, ddof=0)) + Fore.RESET)
        print("Coefficient of variation = " + Fore.MAGENTA +
              repr(numpy.std(self.views, axis=None, dtype=None, out=None, ddof=1) / self.avg) + Fore.RESET)
        print("Confidence Interval = " + Fore.MAGENTA +
              repr(stats.norm.interval(0.95, self.avg, scale=stats.sem(self.views))) + Fore.RESET)
        print("Correlation Question = " +
              printWithColor(stats.pointbiserialr(deltaView, self.isQuestion).correlation))
        print("Correlation ArrowCircle = " +
              printWithColor(stats.pointbiserialr(deltaView, self.isArrowCircle).correlation))
        print("Correlation Sexual = " +
              printWithColor(stats.pointbiserialr(deltaView, self.isSexual).correlation))
        print("Correlation Hyperbole = " +
              printWithColor(stats.pointbiserialr(deltaView, self.isHyperbole).correlation))
        print("Correlation containsBaitWords = " +
              printWithColor(stats.pointbiserialr(deltaView, self.containsBaitWords).correlation))
        print("Coef Peason with ratings = " +
              printWithColor(stats.pearsonr(deltaView, self.ratings)[0]))
        print("Coef Peason with rating (%) = " +
              printWithColor(stats.pearsonr(deltaView, self.rating)[0]))
        print("Coef Peason with comments = " +
              printWithColor(stats.pearsonr(deltaView, self.comments)[0]))


def getDataByUser(user):
    conn = sqlite3.connect('socialblade.db')
    c = conn.cursor()
    media = c.execute(
        "SELECT avg(views) FROM videos where userId = '{}' order by created_at asc LIMIT 40;".format(user)).fetchone()

    results = c.execute(
        "SELECT views, isQuestion, isArrowCircle, isSexual, isHyperbole, containsBaitWords, rating, ratings, comments, created_at FROM videos where userId = '{}' order by created_at asc LIMIT 40;".format(user)).fetchall()
    data = VideosData(user, media[0])

    for result in results:
        data.views.append(result[0])
        data.isQuestion.append(result[1])
        data.isArrowCircle.append(result[2])
        data.isSexual.append(result[3])
        data.isHyperbole.append(result[4])
        data.containsBaitWords.append(result[5])
        data.rating.append(result[6])
        data.ratings.append(result[7])
        data.comments.append(result[8])
        data.dates.append(result[9])

    conn.close()
    return data


def printWithColor(data):
    if(data != data):
        return Fore.RED + repr(data) + Fore.RESET
    if(abs(data) >= 0.2):
        if(abs(data) >= 0.3):
            return Fore.LIGHTGREEN_EX + repr(data) + Fore.RESET
        return Fore.GREEN + repr(data) + Fore.RESET

    return repr(data)


users = ['jakepaulproductions', 'pewdiepie',
         'rezendeevil', 'jacksepticeye', 'felipeneto',  'brotheragi',
         'gamermatheus01', 'yesfunnyyes',
         'thevoicer1313',
         'redvacktor',
         'harujiggly',
         'beauty4taty']

famous = ['jakepaulproductions', 'pewdiepie',
          'rezendeevil', 'jacksepticeye', 'felipeneto']
viewsJump = ['j0be1133', 'brotheragi', 'gamermatheus01',
             'yesfunnyyes', 'gustavofelipea']
randoms = ['thevoicer1313', 'redvacktor', 'harujiggly', 'beauty4taty']
smalls = ['itecnodia', 'benitogamersbrasil',
          'mr8933', 'rubinhoelhais', 'casalpartiu']
print(Back.RED)
print("################Famous######################")
print(Back.RESET)
for user in famous:
    data = getDataByUser(user)
    data.correlations()
print(Back.RED)
print("################Concentraded Views######################")
print(Back.RESET)
for user in viewsJump:
    data = getDataByUser(user)
    data.correlations()
print(Back.RED)
print("################Random######################")
print(Back.RESET)
for user in randoms:
    data = getDataByUser(user)
    data.correlations()
print(Back.RED)
print("################Small Channels######################")
print(Back.RESET)
for user in smalls:
    data = getDataByUser(user)
    data.correlations()
