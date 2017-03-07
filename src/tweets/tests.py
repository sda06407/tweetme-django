from django.test import TestCase
from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse
#from MyProj.forum.tests import SimpleTest
# Create your tests here.
from .models import tweet
User = get_user_model()

class tweetModelTestCase(TestCase):
    def setUp(self):
        random_user = User.objects.create(username='jime')
            
    def test_tweet_item(self):
        obj = tweet.objects.create(
                user=User.objects.first(),
                content="Some content"
              )
            
        self.assertTrue(obj.content=="Some content")
        self.assertTrue(obj.id==1)
        #self.assertEqual(obj.id, 1)
        absoulte_url = reverse("tweet:detail", kwargs={"pk":1})
        self.assertEqual(obj.get_absolute_url(), absoulte_url)
    
    def test_tweet_url(self):
        obj = tweet.objects.create(
                user=User.objects.first(),
                content="Some content"
              )
        absoulte_url = reverse("tweet:detail", kwargs={"pk":obj.pk})
        self.assertEqual(obj.get_absolute_url(), absoulte_url)
        