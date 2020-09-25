from celery import shared_task
from celery.schedules import crontab
from celery.task import periodic_task

from .models import Like


@periodic_task(run_every=crontab(hour="0"))
def delete_all_likes():
    Like.objects.all().delete()
