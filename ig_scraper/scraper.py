import requests

from constants import *  # noqa


class IGScraper:
    def __init__(self, hashtag):
        self.hashtag = hashtag
        self.items = []

    def scrape_hashtag(self, end_cursor='', maximum=10):
        try:
            session = requests.Session()
            session.session.headers = {'user-agent': CHROME_WIN_UA}
            session.cookies.set('ig_pr', '1')
            response = session.get(QUERY_HASHTAG.format(
                self.hashtag, end_cursor)).json()
            data = response['data']['hashtag']
        except:
            data = []

        if data:
            for item in data['edge_hashtag_to_media']['edges']:
                node = item['node']
                if node['edge_media_to_caption']['edges']:
                    caption = node['edge_media_to_caption']['edges'][0]['node']['text']
                else:
                    caption = None
                item = {
                    'is_video': node['is_video'],
                    'caption': caption,
                    'display_url': node['display_url'],
                    'owner_id': node['owner']['id'],
                    'id': node['id'],
                    'shortcode': node['shortcode'],
                    'taken_at_timestamp': node['taken_at_timestamp']
                }
                if item not in self.items and len(self.items) < maximum:
                    self.items.append(item)
            end_cursor = data['edge_hashtag_to_media']['page_info']['end_cursor']
            if end_cursor and len(self.items) < maximum:
                self.scrape_hashtag(end_cursor=end_cursor, maximum=maximum)
        return self.items
