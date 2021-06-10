from django.db import models


class BlogCategory(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя объекта')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class ContentPost(models.Model):
    blog_category = models.ForeignKey(BlogCategory, verbose_name='Шифр обьекта', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name='Имя ответственного инженера ПТО')
    slug = models.SlugField(unique=True)
    content = models.TextField()
    image = models.ImageField(upload_to='blog_post/', blank=True, null=True)
    pub_date = models.DateTimeField(auto_now=True)
    in_archive = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} из шифра \"{self.blog_category.name}\""

