import requests

from constants import *  # noqa


class IGScraper:
    def __init__(self, hashtag):
        self.hashtag = hashtag
        self.items = []

    def scrape_hashtag(self, end_cursor='', maximum=10, first=10, initial=True,
                       detail=False):
        if initial:
            self.items = []

        try:
            session = requests.Session()
            session.headers = {'user-agent': CHROME_WIN_UA}
            session.cookies.set('ig_pr', '1')
            session.cookies.set('sessionid', 'IGSC9c1a9b31465fc4bbae69f03c3eddbdefc78e9d0a09204bc1f945f067871ba057:0RgVJpkNelIIaZ5iOscoV6481YCCSpso:{"_auth_user_id":3178923994,"_auth_user_backend":"accounts.backends.CaseInsensitiveModelBackend","_auth_user_hash":"","_platform":4,"_token_ver":2,"_token":"3178923994:v3NDtXsBlIbqliJXOvDLRhk82rpxrt8Q:9600fe4f7349fe9fa5f60719354dd2c52cca412aaa8196a9a99cf6b7a4ff2570","last_refreshed":1531477132.9980008602}')  # noqa
            response = session.get(QUERY_HASHTAG.format(
                self.hashtag, first, end_cursor)).json()
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

                if any([detail, node['is_video']]):
                    r = requests.get(MEDIA_URL.format(node['shortcode'])).json()

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

            end_cursor = data['edge_hashtag_to_media']['page_info']['end_cursor']

            if end_cursor and len(self.items) < maximum:
                self.scrape_hashtag(end_cursor=end_cursor, detail=detail,
                                    maximum=maximum, initial=False)

        return self.items
