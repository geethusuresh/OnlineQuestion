from django.db import models
from django.contrib.auth.models import User

from taggit.managers import TaggableManager
from taggit.models import TaggedItemBase

class DatetimeStamp(models.Model):

    created_date = models.DateTimeField('Created Date', auto_now_add=True, null=True, blank=True)
    modified_date = models.DateTimeField('Modified Date', auto_now=True, null=True, blank=True)

class TaggedQuestions(TaggedItemBase):
    content_object = models.ForeignKey('Question', blank=True)


class Answer(DatetimeStamp):

    answer = models.TextField(blank=True)
    added_by = models.ForeignKey(User, null=True, blank=True)

class Question(DatetimeStamp):

    question = models.TextField(blank=True)
    answer = models.ForeignKey(Answer, blank=True)
    tags = TaggableManager(through=TaggedQuestions)

