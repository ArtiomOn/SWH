from django.contrib import admin
from django.contrib.admin import ModelAdmin

from apps.tasks.models import Task, Comment, Subject


@admin.register(Subject)
class SubjectAdmin(ModelAdmin):
    list_display = ['title', 'created_at', 'updated_at', 'tasks']


@admin.register(Task)
class TaskAdmin(ModelAdmin):
    list_display = ['title', 'description', 'status', 'author', 'created_at', 'updated_at', 'comments']


@admin.register(Comment)
class CommentAdmin(ModelAdmin):
    list_display = ['comments', 'author', 'created_at', 'updated_at']
