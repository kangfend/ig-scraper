import requests

from constants import *  # noqa


class IGScraper:
    def __init__(self, hashtag):
        self.hashtag = hashtag
        self.items = []

    def scrape_hashtag(self, end_cursor='', maximum=10, first=10, initial=True):
        if initial:
            self.items = []

        try:
            session = requests.Session()
            session.headers = {'user-agent': CHROME_WIN_UA}
            session.cookies.set('ig_pr', '1')
            session.cookies.set('sessionid', 'IGSCde74258b98845d67bb0d4cccba829df0ca1bdae1f9a3ad4d5457704bffe62176%3AMGpk5l6GXPOrpF4vAITBbbI3VMwdq3jX%3A%7B%22_auth_user_id%22%3A45833965%2C%22_auth_user_backend%22%3A%22accounts.backends.CaseInsensitiveModelBackend%22%2C%22_token%22%3A%2245833965%3A8eLFOQP8HIfM17nJvhzqiZljuqQqf7AV%3A746feca19f254ad8326ac0fc3514c4b8ea223c34d7a3fa23db8c924572bd7aa5%22%2C%22_platform%22%3A4%2C%22_remote_ip%22%3A%22103.79.152.6%22%2C%22_mid%22%3A%22WQmivQAEAAFn3JtMngfIjptMWBY4%22%2C%22_user_agent_md5%22%3A%2297de1fddac67554e2eb90d9a46b3dcd4%22%2C%22_token_ver%22%3A2%2C%22last_refreshed%22%3A1523346195.6181542873%7D')
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
                if node['is_video']:
                    r = requests.get(MEDIA_URL.format(node['shortcode'])).json()
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
                if item not in self.items and len(self.items) < maximum:
                    self.items.append(item)
            end_cursor = data['edge_hashtag_to_media']['page_info']['end_cursor']
            if end_cursor and len(self.items) < maximum:
                self.scrape_hashtag(end_cursor=end_cursor,
                                    maximum=maximum, initial=False)
        return self.items
