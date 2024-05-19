from django.db import models
from django.contrib.auth import get_user_model
from django.utils.timezone import now
from django.core.validators import MaxValueValidator
User = get_user_model()

class Blog(models.Model):
    BLOG_TYPE_CHOICES = [
        ('tips', 'Caregiving Tips and Best Practices'),
        ('health', 'Health and Wellness Articles'),
        ('stories', 'User Stories and Experiences'),
    ]
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.TextField()
    content = models.TextField()
    image = models.ImageField(upload_to='media/blogs', default=None)
    post_type = models.CharField(
        max_length=10,
        choices=BLOG_TYPE_CHOICES,
        default='tips',
    )
    created_at = models.DateTimeField(default=now)

    def __str__(self):
        return self.title


class Review(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(default=0, validators=[MaxValueValidator(5)])

    def __str__(self):
        return f"{self.blog.title} - {self.user.name} - {self.rating}"