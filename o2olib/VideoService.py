# -*- coding: utf-8 -*-

from o2olib.utils import utils
from o2olib.models.video import VideoModel

def gets(con_dic):
    con = VideoModel.build_con(con_dic)
    if con:
        query = VideoModel.select().where(con)
    else:
        query = VideoModel.select()
    query_rs = utils.getPwMap(query)
    return query_rs

def get(con):
    videos = gets(con)
    if len(videos) == 0:
        video = {}
    else:
        video = videos[0]
    return video

