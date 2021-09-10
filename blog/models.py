from django.db import models
from django.utils.html import format_html
from ckeditor.fields import RichTextField
from django.utils import timezone
from django.utils.safestring import mark_safe

# Create your models here.

# Category Model


class Category(models.Model):
    cat_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    url = models.CharField(max_length=100)
    image = models.ImageField(upload_to='category/')
    add_date = models.DateTimeField(auto_now_add=True, null=True)

    def image_tag(self):
        if self.image:
            return mark_safe('<img src="%s" style="width: 70px; object-fit: cover; height: 50px;" />' % self.image.url)
        else:
            return 'No Image Found'
    image_tag.short_description = 'Image'

    def __str__(self):
        return self.title

# Post Model


class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    content = RichTextField()
    url = models.CharField(max_length=100)
    created_date = models.DateTimeField(default=timezone.now)
    cat = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post/')

    def image_tag(self):
        if self.image:
            return mark_safe('<img src="%s" style="width: 70px; object-fit: cover; height: 50px;" />' % self.image.url)
        else:
            return 'No Image Found'
    image_tag.short_description = 'Image'

    def __str__(self):
        return self.title
