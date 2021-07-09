import string
import random
from datetime import datetime

from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.utils import timezone

from apps.tasks.models import Task, Comment

User = get_user_model()


class Command(BaseCommand):
    help = 'Create random 1000 tasks'

    def _log_creating_notice(self, time):
        self.stdout.write(self.style.NOTICE(f'Items added in {time}'))

    def handle(self, *args, **options):
        data = []
        comment_ids = Comment.objects.values_list('id', flat=True)
        user_ids = User.objects.values_list('id', flat=True)
        random_letters = string.ascii_letters
        start = datetime.now()
        for _ in range(1000):
            random_text = (''.join(random.choice(random_letters) for _ in range(10)))
            data.append(Task(title=random_text,
                             description=random_text,
                             status=False,
                             author_id=random.choice(user_ids),
                             created_at=timezone.now(),
                             updated_at=timezone.now(),
                             comments_id=random.choice(comment_ids)))

        Task.objects.bulk_create(data)
        end = datetime.now() - start
        self._log_creating_notice(end)
