import string
import random
from datetime import datetime

from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.utils import timezone

from apps.tasks.models import Comment

User = get_user_model()


class Command(BaseCommand):
    help = 'Create random 1000 comments'

    def _log_creating_notice(self, time):
        self.stdout.write(self.style.NOTICE(f'Items added in {time}'))

    def handle(self, *args, **options):
        data = []
        user_ids = User.objects.values_list('id', flat=True)
        random_letters = string.ascii_letters
        start = datetime.now()
        for _ in range(1000):
            random_text = (''.join(random.choice(random_letters) for _ in range(200)))
            data.append(Comment(comments=random_text,
                                author_id=random.choice(user_ids),
                                created_at=timezone.now(),
                                updated_at=timezone.now(),
                                ))

        Comment.objects.bulk_create(data)
        end = datetime.now() - start
        self._log_creating_notice(end)
