#!/usr/bin/env python
# -*- coding: utf-8 -*-
##    @package crawler.py
#      @author Caio Oliveira (caiomcoliveira@gmail.com)

import json
import sys
import requests
import re
import codecs
 
# Renomeando funções/classes para maior clareza de código.

RequestException = requests.exceptions.RequestException
 
def socialBlade(user, page=''):    
    escopo = 'socialblade.com/youtube/user/%s' % user    
    html = requests.get('https://%s/%s' % (escopo, page))    
    return html.content
def socialBladeFile(path):
    html = codecs.open(path, 'r')    
    return html.read()
 
class Crawler:   

    @staticmethod
    def getAllData(user):
        html = socialBlade(user,'videos').decode()
        token = '<div id="YouTube-Video-Wrap" class="(.*?)"></div>'
        try:
            r_token = re.findall(token,html)
            print(r_token[0])
            payload = {
            	'channelid' : r_token[0]
            }
            result = requests.post('https://socialblade.com/js/class/youtube-video-recent', data=payload)
            print(json.loads(result.content))
        except RequestException:
            print('falhou')

    @staticmethod
    def youtuber(user, verbose=True):            
        dates = '<div style="float: left; width: 95px;">\s(.*?)</div>'                 
        subsGrowth = '<div style="width: 65px; float: left;"><span style="color:#.*?;">(.*?)</span></div>'
        subs = '<div style="width: 140px; float: left;">(.*?)</div>' 
        viewsGrowth = '<div style="width: 85px; float: left;"><span style="color:#.*?;">(.*?)</span></div>' #arrumar cor
        views = '<div style="width: 140px; float: left;">(.*?)</div>'
        
        
        
        try:            
            html = socialBlade(user,'monthly').decode()
            r_dates = re.findall(dates, html)
            r_subsGrowth = re.findall(subsGrowth, html)
            r_subs = re.findall(subs, html)
            r_viewsGrowth = re.findall(viewsGrowth, html)
            r_views = re.findall(views, html)
            userData = []

            for date, subsGrowth, subs, viewsGrowth, views in zip(r_dates, r_subsGrowth, r_subs, r_viewsGrowth, r_views):
                temp = {}
                temp['date'] = date
                temp['subsGrowth'] = subsGrowth
                temp['subs'] = subs
                temp['viewsGrowth'] = viewsGrowth
                temp['views'] = views
                userData.append(temp)
            print(user)
            for data in userData:
            	print(data)
            
        except RequestException:            
            print('Erro ao buscar %s\n') % (user)
 
   

#Crawler.youtuber('whinderssonnunes')
Crawler.getAllData('pewdiepie')

#youtubers para ver
#resendevil , emergencyawesome, newrockstars , lubatv , felipeneto
