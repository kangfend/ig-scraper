IG Scraper
==========

Example
-------
```python
from ig_scraper import IGScraper

scraper = IGScraper()

# Will return maximum 10 data
scraper.scrape_hashtag('indonesia')

# Will return maximum 2 data
scraper.scrape_hashtag('indonesia', maximum=2)

# Example result
"""
[{'is_video': False,
  'caption': '*READY STOK ALNITA KIDS AKS 04*🌹\nUngu 7 9\n.\nMau jadi agen tapi mau coba beli satuan dulu? .\nYuk langsung aja hub no 👇 ini ya .\n📌Info & order : .\n📱0896-0455-9546 .\n📱0838-3199-7407\n.\nAtau bisa juga DM kami 😇\n.\n.\n#grosirbusanamuslim #busanamuslimpria #celanaisbal #grosirgamis #grosirhijab #grosirbajumuslim #pakaianmuslim #celanamuslim #usahaonline #peluangusahaonline #resellerbajuonline #resellerbajumuslim #resellergamis #resellerhijab #surabaya #jawatimur #indonesia #news #infousaha #info #agenbajumuslim #agengamis #agenhijab #distributorgamis #distributornibrassurabaya',
  'display_url': 'https://scontent-sin6-1.cdninstagram.com/vp/4f621d544f108e1654a385edffaa210a/5D45B447/t51.2885-15/e35/53563190_185371789095738_8429039772665904803_n.jpg?_nc_ht=scontent-sin6-1.cdninstagram.com&_nc_cat=106',
  'thumbnail_src': 'https://scontent-sin6-1.cdninstagram.com/vp/49aefe7e9d8cd72192a6c5a80f69538e/5D34C3A2/t51.2885-15/sh0.08/e35/s640x640/53563190_185371789095738_8429039772665904803_n.jpg?_nc_ht=scontent-sin6-1.cdninstagram.com&_nc_cat=106',
  'owner_id': '6108870959',
  'id': '2008738998381647589',
  'shortcode': 'BvgeXntAxbl',
  'taken_at_timestamp': 1553680370},
 {'is_video': False,
  'caption': '#allah #muslim #quran #islam #prophetmuhammadﷺ #pakistan #kashmir #india #indonesia #turkey #malaysia #motivationalquotes #inspirationalquotes #cardiff #qoutes #quoteoftheday #wife #eyes #womensfashion #fitness #mensfashion #ronaldo #cristiano #god #husband #messi #liverpool #manchester #madrid #arsenal',
  'display_url': 'https://scontent-sin6-1.cdninstagram.com/vp/ab6542de85b8253cca4f66385bc3c210/5D37690B/t51.2885-15/e35/54247865_324852258198905_8144732659290338203_n.jpg?_nc_ht=scontent-sin6-1.cdninstagram.com&_nc_cat=105',
  'thumbnail_src': 'https://scontent-sin6-1.cdninstagram.com/vp/65a7c3e0c04601ffad0e90f97c4fba8c/5D45B1DC/t51.2885-15/e35/c42.0.636.636/54247865_324852258198905_8144732659290338203_n.jpg?_nc_ht=scontent-sin6-1.cdninstagram.com&_nc_cat=105',
  'owner_id': '9129888416',
  'id': '2008738977034284303',
  'shortcode': 'BvgeXT0nC0P',
  'taken_at_timestamp': 1553680368}]
"""
```
