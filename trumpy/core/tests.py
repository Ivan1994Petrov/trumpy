from django.test import TestCase, Client
from django.urls import reverse, resolve

import datetime

from core.views import (
    tweets_vs_retweets,
    tweets_by_time_of_day,
    most_common_tweet_words,
)
from core.models import Tweet


class TestUrls(TestCase):

    def test_tweets_vs_retweets(self):
        url = reverse('tweets_vs_retweets')
        self.assertEqual(resolve(url).func, tweets_vs_retweets)

    def test_tweets_by_time_of_day(self):
        url = reverse('tweets_by_time_of_day')
        self.assertEqual(resolve(url).func, tweets_by_time_of_day)

    def test_most_common_tweet_words(self):
        url = reverse('most_common_tweet_words')
        self.assertEqual(resolve(url).func, most_common_tweet_words)


class TestTweetsVsRetweets(TestCase):

    def setUp(self):
        self.client = Client()
        self.tweets_vs_retweets_url = reverse('tweets_vs_retweets')

    def test_tweets_vs_retweets_GET(self):
        response = self.client.get(self.tweets_vs_retweets_url)
        self.assertEqual(response.status_code, 200)

    def test_tweets_vs_retweets_returned_data(self):
        now = datetime.datetime.now()
        tweet_obj = Tweet.objects.create(
            source='source',
            id_str='id_str',
            text='text',
            created_at=now,
            retweet_count=5,
            in_reply_to_user_id_str='in_reply_to_user_id_str',
            favorite_count=5,
            is_retweet=False
        )
        retweet_obj = Tweet.objects.create(
            source='source',
            id_str='id_str',
            text='text',
            created_at=now,
            retweet_count=5,
            in_reply_to_user_id_str='in_reply_to_user_id_str',
            favorite_count=5,
            is_retweet=True
        )
        response = self.client.get(self.tweets_vs_retweets_url)
        result = '{"pie": {"retweet": 1, "tweet": 1}}'
        self.assertEqual(response.content.decode('ascii'), result)

    def test_tweets_vs_retweets_without_data(self):
        response = self.client.get(self.tweets_vs_retweets_url)
        result = result = '{"pie": {"retweet": 0, "tweet": 0}}'

        self.assertEqual(response.content.decode('ascii'), result)


class TestTweetsByTimeOfDay(TestCase):
    def setUp(self):
        self.client = Client()
        self.tweets_by_time_of_day_url = reverse(
            'tweets_by_time_of_day')

    def test_tweets_by_time_of_day_GET(self):
        response = self.client.get(self.tweets_by_time_of_day_url)
        self.assertEqual(response.status_code, 200)

    def test_tweets_by_time_of_day_returned_data(self):
        date_first_tweet = datetime.datetime(2020, 12, 25, 17, 5, 55)
        first_tweet_obj = Tweet.objects.create(
            source='source',
            id_str='id_str',
            text='text',
            created_at=date_first_tweet,
            retweet_count=5,
            in_reply_to_user_id_str='in_reply_to_user_id_str',
            favorite_count=5,
            is_retweet=False
        )
        date_second_tweet = datetime.datetime(2020, 12, 25, 12, 5, 55)
        second_tweet_obj = Tweet.objects.create(
            source='source',
            id_str='id_str',
            text='text',
            created_at=date_second_tweet,
            retweet_count=5,
            in_reply_to_user_id_str='in_reply_to_user_id_str',
            favorite_count=5,
            is_retweet=False
        )
        response = self.client.get(self.tweets_by_time_of_day_url)
        result = '{"order_data_by_hours": {"12": 1, "17": 1}}'

        self.assertEqual(response.content.decode('ascii'), result)

    def test_tweets_by_time_of_day_without_data(self):
        response = self.client.get(self.tweets_by_time_of_day_url)
        result = '{"order_data_by_hours": {}}'

        self.assertEqual(response.content.decode('ascii'), result)


class TestMostCommonTweetWords(TestCase):
    def setUp(self):
        self.client = Client()
        self.most_common_tweet_words_url = reverse(
            'most_common_tweet_words')

    def test_most_common_tweet_words_GET(self):
        response = self.client.get(self.most_common_tweet_words_url)
        self.assertEqual(response.status_code, 200)

    def test_most_common_tweet_words_returned_data(self):
        now = datetime.datetime.now()
        tweet_obj = Tweet.objects.create(
            source='source',
            id_str='id_str',
            text='trumpy trumpy trumpy test test',
            created_at=now,
            retweet_count=5,
            in_reply_to_user_id_str='in_reply_to_user_id_str',
            favorite_count=5,
            is_retweet=False
        )
        response = self.client.get(self.most_common_tweet_words_url)
        result = '{"most_common_words": [["trumpy", 3], ["test", 2]]}'
        self.assertEqual(response.content.decode('ascii'), result)

    def test_most_common_tweet_words_returned_data_stopword(self):
        now = datetime.datetime.now()
        tweet_obj = Tweet.objects.create(
            source='source',
            id_str='id_str',
            text='trumpy the in of a',
            created_at=now,
            retweet_count=5,
            in_reply_to_user_id_str='in_reply_to_user_id_str',
            favorite_count=5,
            is_retweet=False
        )
        response = self.client.get(self.most_common_tweet_words_url)
        result = '{"most_common_words": [["trumpy", 1]]}'
        self.assertEqual(response.content.decode('ascii'), result)

    def test_most_common_tweet_words_without_data(self):

        response = self.client.get(self.most_common_tweet_words_url)
        result = '{"most_common_words": []}'
        self.assertEqual(response.content.decode('ascii'), result)