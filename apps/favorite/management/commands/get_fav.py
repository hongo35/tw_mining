# -*- coding:utf-8 -*-
from django.core.management.base import BaseCommand
from django.conf import settings
from django.utils import timezone
from favorite.models import Favorite

from xml.sax.saxutils import unescape
import twitter
import datetime
import re

class Command(BaseCommand):
	help = "[Description] Here is help..."

	def handle(self, *args, **options):
		api = twitter.Api(
			consumer_key        = settings.TW['consumer_key'],
			consumer_secret     = settings.TW['consumer_secret'],
			access_token_key    = settings.TW['access_token_key'],
			access_token_secret = settings.TW['access_token_secret']
		)

		statuses = api.GetFavorites(count=200,screen_name='hongo35')
		for s in statuses:
			now = datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S")

			try:
				timezone = s.user.utc_offset / 3600
			except:
				timezone = 0

			try:
				Favorite.objects.create(
					id = s.id,
					user_id       = s.user.id,
					user_name     = s.user.screen_name,
					nickname      = s.user.name,
					body          = unescape(s.text),
					ts            = datetime.datetime.strptime(s.created_at, "%a %b %d %H:%M:%S +0000 %Y").strftime("%Y-%m-%d %H:%M:%S"),
					timezone      = timezone,
					ts_japan      = (datetime.datetime.strptime(s.created_at, "%a %b %d %H:%M:%S +0000 %Y") + datetime.timedelta(hours=9)).strftime("%Y-%m-%d %H:%M:%S"),
					ts_date_japan = (datetime.datetime.strptime(s.created_at, "%a %b %d %H:%M:%S +0000 %Y") + datetime.timedelta(hours=9)).strftime("%Y-%m-%d"),
					tool          = re.compile(r'<.*?>').sub('', s.source),
					retweet_cnt   = s.retweet_count,
					fav_cnt       = s.favorite_count,
					cnt           = s.user.statuses_count,
					link_cnt      = s.user.friends_count,
					linked_cnt    = s.user.followers_count,
					listed_cnt    = s.user.listed_count,
					created_at    = now,
					updated_at    = now,
				)
			except:
				pass
