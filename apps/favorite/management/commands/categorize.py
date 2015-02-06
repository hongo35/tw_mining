# -*- coding:utf-8 -*-
from django.core.management.base import BaseCommand
from django.conf import settings
from favorite.models import Favorite

import MeCab
import datetime

class Command(BaseCommand):
	help = "[Description] Here is help..."

	def handle(self, *args, **options):
		mecab = MeCab.Tagger('mecabrc')
