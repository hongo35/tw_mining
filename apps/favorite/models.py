from django.db import models

# Create your models here.
class Favorite(models.Model):
	id = models.BigIntegerField(primary_key=True)
	user_id = models.BigIntegerField()
	user_name = models.CharField(max_length=255)
	nickname = models.CharField(max_length=255)
	body = models.CharField(max_length=255)
	ts = models.DateTimeField()
	timezone = models.IntegerField()
	ts_japan = models.DateTimeField()
	ts_date_japan = models.DateField()
	tool = models.CharField(max_length=255)
	retweet_cnt = models.IntegerField()
	fav_cnt = models.IntegerField()
	cnt = models.IntegerField()
	link_cnt = models.IntegerField()
	linked_cnt = models.IntegerField()
	listed_cnt = models.IntegerField()
	created_at = models.DateTimeField()
	updated_at = models.DateTimeField()

	class Meta:
		managed = False
		db_table = 'favorites'
