from django.test import TestCase

from social_twitter.templatetags.social_twitter import hello


class SocialTwitterTemplateTagFilterTestCase(TestCase):
    def test_filter(self):
        self.assertEqual(hello("Sören"), "Hello, Sören")
