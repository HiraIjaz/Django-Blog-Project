from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

User = get_user_model()


class Post(models.Model):
    """
    Represents a blog post.

    Attributes:
        title (str): The title of the blog post (max length: 100 characters).
        content (str): The content of the blog post.
        date_posted (datetime): The date and time when the post was initially created.
        last_edited (datetime): The date and time when the post was last edited.
        author (User): The author of the post (foreign key to the User model).
    """

    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    last_edited = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE)

    objects = models.Manager()

    def __str__(self):
        """
        Return a string representation of the post.
        """
        return self.title


class Comment(models.Model):
    """
    Represents a comment on a blog post.

    Attributes:
        post (Post): The blog post this comment belongs to (foreign key to the Post model).
        writer (User): The user who wrote the comment (foreign key to the User model).
        text (str): The content of the comment.
        date_added (datetime): The date and time when the comment was added.
    """

    post = models.ForeignKey(
        Post,
        related_name='comments',
        on_delete=models.CASCADE)

    writer = models.ForeignKey(User,
                               on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
