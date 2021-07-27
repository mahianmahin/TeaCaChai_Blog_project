from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from datetime import datetime
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail


class SiteUtilities(models.Model):
    about_us_avatar = models.ImageField(upload_to = 'site_utilities')
    about_us_description = RichTextField()
    help_text = RichTextField()
    home_first_section_heading = RichTextField()
    home_second_section_heading = RichTextField()
    types_heading = RichTextField()

class Subscribers(models.Model):
    subs_mail = models.EmailField(max_length=300)
    subs_first_name = models.CharField(max_length=300)

class Blog(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    blog = RichTextField()
    thumbnail_img = models.ImageField(upload_to = 'blog_thumbnails')
    published_date = models.DateTimeField(default=datetime.now(), blank=True)

    def __str__(self):
        return self.title

@receiver(post_save, sender=Blog)
def at_ending_save(sender, instance, created, **kwargs):
    if created:
        subscribers_list = []
        subs = Subscribers.objects.all()

        for subscribers in subs:
            subscribers_list.append(subscribers.subs_mail)

        send_mail(
            "New Post Uploaded",
            "A new post has just been uploaded. Check right now!",
            'drinkteaville@gmail.com',
            subscribers_list,
            fail_silently=False
        )

class AboutMe(models.Model):
    about_me_avatar = models.ImageField(upload_to = 'about_me_picture')
    about_me_description = RichTextField()

class ImageSlider(models.Model):
    slider_img = models.ImageField(upload_to = 'slider_images')
    active = models.BooleanField(default=False)

class TypesOfTea(models.Model):
    tea_picture = models.ImageField(upload_to='tea_types')
    type_name = models.CharField(max_length = 100, null=True)
    tea_description = RichTextField()
    first_section = models.BooleanField(default = False)
    second_section = models.BooleanField(default = False)

