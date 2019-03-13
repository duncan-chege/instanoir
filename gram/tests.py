from django.test import TestCase
from .models import Comment


class CommentTestClass(TestCase):
    def setUp(self):
        self.my_comment=Comment(id=1, content="Stay strong", image_id=2, username_id=3)

    def test_save_comment(self):
        self.my_comment.save_comment()
        all_the_objects = Comment.objects.all()
        self.assertTrue(len(all_the_objects)>0)
