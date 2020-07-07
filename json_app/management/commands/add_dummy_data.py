from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import datetime
import pytz
from json_app.models import User, ActivityPeriod
from json_app.rand_date import random_date
import string
import random 

class Command(BaseCommand):
    help = 'Displays current time'

    def handle(self, *args, **kwargs):
        user = User.objects.create(uid= ''.join(random.choice(string.ascii_uppercase) for _ in range(10)), real_name = "Adam Eve", tz = "America/Los_Angeles")
        user.save()
        n = random.randint(1,4)
        for i in range(n):
            start_time = random_date(datetime(2018, 1, 1), datetime.now())
            end_time = random_date(start_time, datetime.now())
            ap = ActivityPeriod.objects.create(user = user,start_time = pytz.utc.localize(start_time), end_time = pytz.utc.localize(end_time))
            ap.save()
        self.stdout.write("Added") 