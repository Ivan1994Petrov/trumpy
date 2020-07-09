from django.db import models


class Tweet(models.Model):
    source = models.CharField(max_length=50)
    id_str = models.CharField(max_length=21)
    text = models.TextField()
    created_at = models.DateTimeField()
    retweet_count = models.IntegerField()
    in_reply_to_user_id_str = models.CharField(max_length=21,
                                               blank=True, null=True)
    favorite_count = models.IntegerField()
    is_retweet = models.BooleanField()

    def __str__(self):
        return self.text[:20]
