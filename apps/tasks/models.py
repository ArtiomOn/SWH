from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Subject(models.Model):
    title = models.CharField(max_length=25)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tasks = models.ForeignKey('Task', on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.title}, {self.created_at}, {self.updated_at}, {self.tasks}'

    class Meta:
        verbose_name = 'Subject'
        verbose_name_plural = 'Subjects'


class Task(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    status = models.BooleanField(default=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    comments = models.ForeignKey('Comment', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}, {self.description}, {self.status}, {self.author}, ' \
               f'{self.created_at}, {self.updated_at}, {self.comments} '

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'


class Comment(models.Model):
    comments = models.TextField(max_length=500)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.comments}, {self.author}, {self.created_at}, {self.updated_at}'

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
