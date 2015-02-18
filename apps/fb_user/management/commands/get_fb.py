# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from django.conf import settings
from fb_user.models import FbUser

#import facebook
import requests
import datetime
from bs4 import BeautifulSoup

class Command(BaseCommand):
	help = "[Description] Here is help..."

	def handle(self, *args, **options):
		res = requests.get("http://realtime.search.yahoo.co.jp/search?p=%E3%81%AE&ei=UTF-8&sv=3")
		soup = BeautifulSoup(res.text)

		posts = soup.find("div", id="TSm").findAll("div", class_="cnt")
		for p in posts:
			body = p.find("h2").text
			name = p.find("div", class_="inf").find("p", class_="lt").find("a", class_="nam").text
			url = p.find("div", class_="inf").find("p", class_="lt").find("a", class_="nam").get("href")
			fid = url.split("fid=")[1]

			ts = datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S")
			fb = FbUser(
				user_id    = fid,
				user_name  = name,
				body       = body,
				created_at = ts,
				updated_at = ts,
			)
			fb.save()

			#graph = facebook.GraphAPI(settings.FB['access_token'])
			#profile = graph.get_object("0123456789")
			#friends = graph.get_connections("me", "friends")
			#print profile
