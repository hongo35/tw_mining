# -*- coding:utf-8 -*-
from django.core.management.base import BaseCommand
from django.conf import settings
from favorite.models import Favorite
from timeline.models import Timeline
from public_timeline.models import PublicTimeline

import MeCab
from gensim import corpora, matutils
from sklearn.ensemble import RandomForestClassifier
import re
import datetime

MECAB_MODE = 'mecabrc'
PARSE_TEXT_ENCODING = 'utf-8'

class Command(BaseCommand):
	help = "[Description] Here is help..."

	__mecab = MeCab.Tagger(MECAB_MODE)

	__words     = []
	__words_fav = []
	__train_data  = []
	__train_label = []
	__predict_data  = []

	def handle(self, *args, **options):
		"""
		tws = Timeline.objects.all().order_by('?')[:50000]
		for t in tws:
			self.__tokenize(t.body)

		dictionary = corpora.Dictionary(self.__words)
		dictionary.filter_extremes(no_below=2)
		dictionary.save_as_text('tw_dic.txt')
		"""

		dictionary = corpora.Dictionary.load_from_text('tw_dic.txt')

		favs = Favorite.objects.all()[:1000]
		for f in favs:
			words = self.__train_tokenize(f.body)
			tmp   = dictionary.doc2bow(words)
			dense = list(matutils.corpus2dense([tmp], num_terms=len(dictionary)).T[0])
			
			self.__train_data.append(dense)
			self.__train_label.append(1)

		ptws = PublicTimeline.objects.all()[:1000]
		for p in ptws:
			words = self.__train_tokenize(p.body)
			tmp   = dictionary.doc2bow(words)
			dense = list(matutils.corpus2dense([tmp], num_terms=len(dictionary)).T[0])

			self.__train_data.append(dense)
			self.__train_label.append(0)

		estimator = RandomForestClassifier()

		# 学習
		estimator.fit(self.__train_data, self.__train_label)

		# 予測
		tws = Timeline.objects.all().order_by('-ts')[:100]
		for t in tws:
			words = self.__train_tokenize(t.body)
			tmp   = dictionary.doc2bow(words)
			dense = list(matutils.corpus2dense([tmp], num_terms=len(dictionary)).T[0])
			
			if 1 in estimator.predict(dense):
				print t.body
			
			#self.__predict_data.append(dense)
		
		#label_predict = estimator.predict(self.__predict_data)
		#print label_predict

	def __tokenize(self, text):
		text = text.encode(PARSE_TEXT_ENCODING)

		for t in text.split():
			words = []
			if t.find("http") != 0 and t.find("RT") != 0 and t.find("@") != 0:
				node = self.__mecab.parseToNode(t)
				while node:
					if node.feature.split(",")[0] == "名詞":
						if node.surface.isdigit() == False:
							if not re.match("[@!-/]", node.surface):
								words.append(node.surface)
					node = node.next
			self.__words.append(words)

	def __train_tokenize(self, text):
		text = text.encode(PARSE_TEXT_ENCODING)

		words = []
		for t in text.split():
			if t.find("http") != 0 and t.find("RT") != 0 and t.find("@") != 0:
				node = self.__mecab.parseToNode(t)
				while node:
					if node.feature.split(",")[0] == "名詞":
						if len(node.surface) >= 2:
							words.append(node.surface)
					node = node.next
		return words
