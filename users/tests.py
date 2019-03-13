from django.test import TestCase

from .models import Profile


class ProfileTestClass(TestCase):
    def setUp(self):
        self.my_profile=Profile(id=1, image="users/static/images/iphone.png", bio="Stay strong" )

    def test_is_instance(self):     #Testing instance to confirm that the object is being instantiated correctly
        self.assertTrue(isinstance(self.my_profile,Profile))

