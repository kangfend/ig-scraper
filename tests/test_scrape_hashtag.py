from unittest import TestCase
from ig_scraper import IGScraper


class ScraperTest(TestCase):
    def test_scrape_hashtag(self):
        scraper = IGScraper()

        result = scraper.scrape_hashtag('indonesia')
        self.assertEqual(len(result), 10)

        result = scraper.scrape_hashtag('indonesia', maximum=2)
        self.assertEqual(len(result), 2)
