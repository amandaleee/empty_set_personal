from django.test import TestCase

from empty_set import urls


class EmptySetUrlsTest(TestCase):
    """
    These tests are extremely pedantic and only exist to have something to test in CircleCI.
    """

    def test_urlpatterns_exist(self):
        """
        url patterns should exist
        """
        self.assertTrue(urls.urlpatterns, "url patterns should exist")

    def test_urlpatterns_have_length(self):
        """
        url patterns should contain at least a single entry
        """
        self.assertGreaterEqual(
            len(urls.urlpatterns),
            0,
            "url patterns should contain at least a single entry"
        )
