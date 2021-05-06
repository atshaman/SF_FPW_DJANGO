from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    def update_rating(self, ):
        self.rating = sum(
            [i['rating'] * 3 for i in Post.objects.filter(author=self, posttype='ST').values('rating')])
        self.rating += sum([i['rating'] for i in Comment.objects.filter(user=self.user).values('rating')])
        self.rating += sum(i['rating'] for i in
                           [Comment.objects.filter(post=i).values('rating') for i in Post.objects.filter(author=self)][
                               0])
        return self.rating


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    posttype = models.CharField(choices=[('ST', 'Статья'), ('NS', 'Новость')], max_length=2, default='NS')
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=20)
    text = models.TextField()
    rating = models.IntegerField(default=0)
    categories = models.ManyToManyField('Category', through='PostCategory')

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def preview(self):
        return self.text[:124] + '...'

    def __str__(self):
        return f'{self.title}: {self.preview()}'

    def get_absolute_url(self):
        return f'/news/{self.id}'


class Category(models.Model):
    name = models.CharField(max_length=64)
    posts = models.ManyToManyField(Post, through='PostCategory')


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    rating = models.IntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()
