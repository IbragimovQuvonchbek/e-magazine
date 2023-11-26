from django.db import models
from django.urls import reverse


class Post(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    price = models.PositiveIntegerField()
    photo = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('full_post', args=[str(self.pk)])
