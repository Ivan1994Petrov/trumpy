from django.core.management.base import BaseCommand

import requests
from datetime import datetime

from core.models import Twit


class Command(BaseCommand):
    help = 'Sync database'

    def handle(self, *args, **options):
        url = 'http://trumptwitterarchive.com/data/realdonaldtrump/2018.json'
        response = requests.get(url)
        json_response = response.json()

        for item in json_response:

            if not Twit.objects.filter(id_str=item['id_str']).exists():
                date_obj = datetime.strptime(item['created_at'],
                                             "%a %b %d %X %z %Y")

                twit_obj = Twit.objects.create(
                    source=item['source'],
                    id_str=item['id_str'],
                    text=item['text'],
                    created_at=date_obj,
                    retweet_count=item['retweet_count'],
                    in_reply_to_user_id_str=item[
                        'in_reply_to_user_id_str'],
                    favorite_count=item['favorite_count'],
                    is_retweet=item['is_retweet']
                )
                twit_obj.save()
