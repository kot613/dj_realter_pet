from django.db import models


class Comment(models.Model):
    """
        Comment model for db
    """
    name = models.CharField(max_length=50)
    comment = models.TextField()
    image = models.ImageField(upload_to='users_comment')

    def __str__(self):
        return self.name
