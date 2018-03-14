import requests

from constants import *  # noqa


class IGScraper:
    def __init__(self, hashtag):
        self.hashtag = hashtag
        self.items = []

    def scrape_hashtag(self, end_cursor=''):
        try:
            response = requests.get(QUERY_HASHTAG.format(self.hashtag, end_cursor)).json()
            data = response['data']['hashtag']
        except:
            data = []

        if data:
            end_cursor = data['edge_hashtag_to_media']['page_info']['end_cursor']
            for item in data['edge_hashtag_to_media']['edges']:
                node = item['node']
                if node['edge_media_to_caption']['edges']:
                    caption = node['edge_media_to_caption']['edges'][0]['node']['text']
                else:
                    caption = None
                data = {
                    'is_video': node['is_video'],
                    'caption': caption,
                    'display_url': node['display_url'],
                    'owner_id': node['owner']['id'],
                    'id': node['id'],
                    'shortcode': node['shortcode'],
                    'taken_at_timestamp': node['taken_at_timestamp']
                }
                if data not in self.items and data['is_video'] is False and caption:
                    self.items.append(data)
            if end_cursor:
                self.scrape_hashtag(end_cursor=end_cursor)
        return self.items
