#-*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from django.conf import settings
from timeline.models import Timeline

import MeCab
from gensim.models import word2vec
import logging

# 今どれくらい処理が進んでいるか確認する用
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

class Command(BaseCommand):
	help = "[Description] Here is help..."

	def handle(self, *args, **options):
		#self.__get_tweets()
		#sentences = word2vec.Text8Corpus("wakati_tw.txt")
		#model = word2vec.Word2Vec(sentences, size=200, min_count = 3)
		model = word2vec.Word2Vec.load('word2vec.model')
		res = model.most_similar(positive = [u"日本"], negative = [], topn = 5)
		for i,r in enumerate(res):
			print "%s: %s" % (i,r[0])

	def __get_tweets(self):
		tweets = Timeline.objects.all().order_by('-ts')
		for t in tweets:
			print t.body.encode('utf-8')
		
