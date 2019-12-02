BASE_URL = 'https://www.instagram.com/'
MEDIA_URL = BASE_URL + 'p/{0}/?__a=1'

# QUERY hashtag
QUERY_HASHTAG = BASE_URL + \
    'graphql/query/?query_hash=ded47faa9a1aaded10161a2ff32abb6b&variables={0}'
QUERY_HASHTAG_VARS = '{{"tag_name":"{0}","first":{1},"after":"{2}"}}'

# User agent
CHROME_WIN_UA = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 ' \
                '(KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
