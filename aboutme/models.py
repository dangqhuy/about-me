from model_utils import TimeStampedModel, SoftDeletableModel
from django.db import models
from ckeditor.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


class Post(TimeStampedModel, SoftDeletableModel, models.Model):
    title = models.CharField(_('Title'), max_length=250)
    content = RichTextUploadingField(_('Content'))
    author = models.ForeignKey(User, on_delete=models.CASCADE)
