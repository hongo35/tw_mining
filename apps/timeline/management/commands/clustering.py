# -*- coding:utf-8 -*-
from django.core.management.base import BaseCommand
from django.conf import settings
from timeline.models import Timeline

import MeCab
import numpy as np

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans, MiniBatchKMeans
from sklearn.decomposition import TruncatedSVD
from sklearn.preprocessing import Normalizer

MECAB_MODE = 'mecabrc'
PARSE_TEXT_ENCODING = 'utf-8'

NUM_CLUSTERS = 10
LSA_DIM = 500
MAX_DF = 0.8
MAX_FEATURES = 10000
MINIBATCH = True

class Command(BaseCommand):
	help = "[Description] Here is help..."

	__mecab = MeCab.Tagger(MECAB_MODE)

	def handle(self, *args, **options):
		# tweets
		ret    = Timeline.objects.all()[:100]
		tweets = [r.body for r in ret]
		
		# feature extraction
		vectorizer = TfidfVectorizer(analyzer = self.__analyzer, max_df = MAX_DF)
		vectorizer.max_features = MAX_FEATURES
		x = vectorizer.fit_transform(tweets)

		# dimensionality reduction by LSA
		lsa = TruncatedSVD(LSA_DIM)
		x= lsa.fit_transform(x)
		x= Normalizer(copy=False).fit_transform(x)

		# clustering by KMeans
		if MINIBATCH:
			km = MiniBatchKMeans(n_clusters=NUM_CLUSTERS, init='k-means++',batch_size=1000,n_init=10,max_no_improvement=10)
		else:
			km = KMeans(n_clusters=NUM_CLUSTERS, init='k-means++', n_init=1)
		
		km.fit(x)
		labels = km.labels_

		transformed = km.transform(x)
		dists = np.zeros(labels.shape)
		for i in range(len(labels)):
			dists[i] = transformed[i, labels[i]]

		# sort by distance
		clusters = []
		for i in range(NUM_CLUSTERS):
			cluster = []
			ii = np.where(labels == i)[0]
			dd = dists[ii]
			di = np.vstack([dd,ii]).transpose().tolist()
			di.sort()
			for d, j in di:
				cluster.append(tweets[int(j)])
			clusters.append(cluster)

		for i,cluster in enumerate(clusters):
			for c in cluster:
				print "%s: %s" % (i,c)

	def __analyzer(self, text):
		ret = []
		node = self.__mecab.parseToNode(text.encode('utf-8'))
		node = node.next
		while node.next:
			ret.append(node.feature.split(',')[-3].decode('utf-8'))
			node = node.next

		return ret
