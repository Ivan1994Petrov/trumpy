from django.http.response import HttpResponse

from core.models import Tweet

from nltk.corpus import stopwords
import collections
import json


def tweets_vs_retweets(request):
    """
    Calculates the sum of all tweets and retweets.
    :param request
    :return: JSON with tweets and retweets.
    """
    if request.method == 'GET':
        retweet = Tweet.objects.filter(is_retweet=True)
        tweet = Tweet.objects.filter(is_retweet=False)
        comment = {
            'pie': {'retweet': len(retweet), 'tweet': len(tweet)},
        }
        context = json.dumps(comment)
        return HttpResponse(context, content_type='application/json')


def tweets_by_time_of_day(request):
    """
    Calculates the distribution of tweets by hours.
    :param request
    :return: JSON with tweets by time ot the day.
    """
    if request.method == 'GET':
        all_tweets = Tweet.objects.all()
        data_by_hours = dict()

        for item in all_tweets:
            if item.created_at.hour in data_by_hours:
                data_by_hours[item.created_at.hour] += 1
            else:
                data_by_hours[item.created_at.hour] = 1
        order_data_by_hours = collections.OrderedDict(
            sorted(data_by_hours.items()))

        comment = {
            'order_data_by_hours': order_data_by_hours,
        }
        context = json.dumps(comment)
        return HttpResponse(context, content_type='application/json')


def most_common_tweet_words(request):
    """
    Get most common words filtered with nltk stopwords.
    :param request
    :return: JSON with most common words.
    """
    if request.method == 'GET':
        all_tweets = Tweet.objects.all()

        all_tweets_text = ''

        for item in all_tweets:
            all_tweets_text += f'{item.text} '
        counter = collections.Counter(all_tweets_text.strip().split())
        most_common_words = counter.most_common()

        stop_words = set(stopwords.words('english'))
        # loop in the 50 most common words
        for work_and_count in most_common_words[:50]:
            if work_and_count[0] in stop_words:
                most_common_words.remove(work_and_count)

        comment = {
            'most_common_words': most_common_words[:15]
        }
        context = json.dumps(comment)
        return HttpResponse(context, content_type='application/json')
