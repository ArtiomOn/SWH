import string
import random
from datetime import datetime

from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.utils import timezone

from apps.tasks.models import Subject, Task

User = get_user_model()


class Command(BaseCommand):
    help = 'Create random 100 subjects'

    def _log_creating_notice(self, time):
        self.stdout.write(self.style.NOTICE(f'Items added in {time}'))

    def handle(self, *args, **options):
        data = []
        task_ids = Task.objects.values_list('id', flat=True)
        random_letters = string.ascii_letters
        start = datetime.now()
        for _ in range(100):
            random_title = (''.join(random.choice(random_letters) for _ in range(6)))
            data.append(Subject(title=random_title,
                                created_at=timezone.now(),
                                updated_at=timezone.now(),
                                tasks_id=random.choice(task_ids)))

        Subject.objects.bulk_create(data)
        end = datetime.now() - start
        self._log_creating_notice(end)
