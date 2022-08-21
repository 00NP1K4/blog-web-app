from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
# from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django_resized import ResizedImageField

# Create your models here.
STATUS = (
    ("Draft", "Draft"),
    ("Publish", "Publish")
)


class Category(models.Model):
    category = models.CharField(max_length=250)

    def __str__(self):
        return self.category


class Post(models.Model):
    title = models.CharField(max_length=1000, unique=True)
    slug = models.SlugField(max_length=2000, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now=True)
    content = RichTextUploadingField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=STATUS, max_length=250)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="cate", blank=True, null=Trueqa   )
    preview = models.ImageField(upload_to='uploads/preview/')
    editor_pick = models.BooleanField(default=False)
    post_image = ResizedImageField(size=[100, 80], upload_to='uploads/preview_sm/', blank=True, null=True)
    featured = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_on']

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class SiteAdmin(models.Model):
    phone_number = models.CharField(max_length=15)
    email = models.CharField(max_length=250)
    facebook_link = models.CharField(max_length=500)
    twitter_link = models.CharField(max_length=500)
    instagram_link = models.CharField(max_length=500)
    address = models.CharField(max_length=500)
    banner = ResizedImageField(size=[1140, 650], upload_to='uploads/banner/')
    about_us = RichTextUploadingField(blank=True, null=True)

    def __str__(self):
        return "Admin"

# class Comment(models.Model):
#     pass
