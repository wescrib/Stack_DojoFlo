from __future__ import unicode_literals
from ..LoginAndRegistration.models import User
from django.db import models

class PostManager(models.Manager):
   def addPost(self, title, content, user, subtopic):
        errors = []

        if len(content) < 1:
           errors.append("There is no content in the post")
        elif len(content) < 10:
            errors.append("If your issue can be typed in less than 10 characters, Google it.")
        else:

            issue = Post.objects.create(
            title = title,
            content = content,
            user = user,
            subtopic = subtopic

        )

class CommentManager(models.Manager):
    def addComment(self, content, user, post):
        dictionary = {
            "errors" : []

        }
        print "ADDCOMMENT MANAGER"
        if len(content) < 1:
             dictionary['errors'].append("There is no content in the post")
             return dictionary
        else:
            comment = Comment.objects.create(
                content = content,
                user = user,
                post = post
            )

class LanguageManager(models.Manager):
    pass

class Topic(models.Model):
    name = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

class SubTopic(models.Model):
    name = models.CharField(max_length=20)
    topic = models.ForeignKey(Topic, related_name="parent")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

class Post(models.Model):
    title = models.TextField(max_length=100)
    content = models.TextField(max_length=2000)
    user = models.ForeignKey(User, related_name="poster")
    subtopic = models.ForeignKey(SubTopic, related_name="child")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = PostManager()

class Comment(models.Model):
    content = models.TextField(max_length=2000)
    post = models.ForeignKey(Post, related_name="comment_issue")
    user = models.ForeignKey(User, related_name="commenter")
    objects = CommentManager()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
