import hashlib
import json
import requests
import sys

from .constants import (CHROME_WIN_UA, BASE_URL, QUERY_HASHTAG,
                        QUERY_HASHTAG_VARS, MEDIA_URL)


class IGScraper:
    def __init__(self):
        self.items = []
        self.session = requests.Session()
        self.session.headers = {'user-agent': CHROME_WIN_UA}
        self.session.cookies.set('ig_pr', '1')
        self.rhx_gis = None

    def scrape_hashtag(self, hashtag, end_cursor='', maximum=10, first=10,
                       initial=True, detail=False):
        if initial:
            self.items = []

        try:
            params = QUERY_HASHTAG_VARS.format(hashtag, 10, end_cursor)
            response = self.session.get(QUERY_HASHTAG.format(params)).json()
            data = response['data']['hashtag']
        except Exception:
            self.session.close()
            return []

        if data:
            for item in data['edge_hashtag_to_media']['edges']:
                node = item['node']
                caption = None
                if node['edge_media_to_caption']['edges']:
                    caption = node[
                        'edge_media_to_caption']['edges'][0]['node']['text']

                if any([detail, node['is_video']]):
                    try:
                        r = requests.get(MEDIA_URL.format(
                            node['shortcode'])).json()
                    except Exception:
                        continue

                if node['is_video']:
                    display_url = r['graphql']['shortcode_media']['video_url']
                else:
                    display_url = node['display_url']

                item = {
                    'is_video': node['is_video'],
                    'caption': caption,
                    'display_url': display_url,
                    'thumbnail_src': node['thumbnail_src'],
                    'owner_id': node['owner']['id'],
                    'id': node['id'],
                    'shortcode': node['shortcode'],
                    'taken_at_timestamp': node['taken_at_timestamp']
                }

                if detail:
                    owner = r['graphql']['shortcode_media']['owner']
                    item['profile_picture'] = owner['profile_pic_url']
                    item['username'] = owner['username']

                if item not in self.items and len(self.items) < maximum:
                    self.items.append(item)

            end_cursor = data[
                'edge_hashtag_to_media']['page_info']['end_cursor']
            if end_cursor and len(self.items) < maximum:
                self.scrape_hashtag(hashtag, detail=detail, initial=False,
                                    end_cursor=end_cursor, maximum=maximum)
        self.session.close()
        return self.items
