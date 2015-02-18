from django.db import models

# Create your models here.
class FbUser(models.Model):
	user_id = models.CharField(primary_key=True, max_length=255)
	user_name = models.CharField(max_length=255)
	body = models.TextField()
	created_at = models.DateTimeField()
	updated_at = models.DateTimeField()

	class Meta:
		managed = False
		db_table = 'fb_users'
