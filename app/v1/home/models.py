from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from base.models import BaseModel, Account

# Create your models here.
class Category(BaseModel):
    name = models.CharField(max_length=30, unique=True)
    name_slug = models.SlugField(max_length=40, unique=True)
    logo = models.ImageField(blank=False, null=True)
    desc = RichTextField()
    
    def __str__(self) :
        return f"{self.name}"
    
    
    def save(self, *args, **kwargs):
        self.name_slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)
        return self

class BlogPost(BaseModel):
    title = models.CharField(max_length=120, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, related_name="blog_post")
    title_slug = models.SlugField(max_length=120, unique=True)
    cover_img = models.ImageField(blank=False)
    post = RichTextField()

    def __str__(self) :
        return f"{self.category.name} -->> {self.title}"
    
    def save(self, *args, **kwargs):
        self.title_slug = slugify(self.title)
        super(BlogPost, self).save(*args, **kwargs)
        return self

