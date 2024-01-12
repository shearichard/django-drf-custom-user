import uuid
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])


class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)
    highlighted = models.TextField()

    class Meta:
        ordering = ['created']

class Foo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100, blank=True, default='')

class BarOwner(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100, blank=True, default='')

class Bar(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    django_user = models.OneToOneField(
        User,
        null=False,
        on_delete=models.PROTECT)
    title = models.CharField(max_length=100, blank=True, default='')
    barowner = models.ForeignKey(  BarOwner, on_delete=models.CASCADE)


    class Meta:
        verbose_name = "Bar"
        verbose_name_plural = "Bars"

    def __str__(self):
        return str(self.id)
    #
@receiver(post_save, sender=User)
def create_user_bar(sender, instance, created, **kwargs):
    if created:
        Bar.objects.create(django_user=instance)
#
@receiver(post_save, sender=User)
def save_user_bar(sender, instance, **kwargs):
    instance.bar.save()

