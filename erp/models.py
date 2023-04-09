# tweet/models.py
from django.db import models
from user.models import UserModel


# Create your models here.
class TweetModel(models.Model):
    class Meta:
        db_table = "tweet"

    author = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    content = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Product(models.Model):
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    amount = models.IntegerField()
    price = models.CharField(max_length=20)
    sizes = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'X-Large'),
        ('F', 'Free'),
    )
    size = models.CharField(choices=sizes, max_length=20)

    def __str__(self):
        return self.code

    def save(self, *args, **kwargs):
        pass  # 생성될 때 stock quantity를 0으로 초기화 로직




