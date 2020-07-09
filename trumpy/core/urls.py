from django.urls import path

from core.views import (
    tweets_vs_retweets,
    tweets_by_time_of_day,
    most_common_tweet_words
)

urlpatterns = [
    path('tweets-vs-retweets/', tweets_vs_retweets,
         name='tweets_vs_retweets'),
    path('tweets-by-time-of-day/', tweets_by_time_of_day,
         name='tweets_by_time_of_day'),
    path('most-common-tweet-words/', most_common_tweet_words,
         name='most_common_tweet_words')
]
