from django.shortcuts import render
from datetime import datetime
# Create your views here.
from django.http import HttpResponse, JsonResponse
from .models import User,ActivityPeriod

def index(request):
    users = User.objects.all()
    json_dict = dict()
    json_dict["ok"] = True
    json_dict["members"] = []
    for user in users:
        activity_periods = ActivityPeriod.objects.filter(user__exact = user)
        temp_dict = dict()
        temp_dict["id"] = user.uid
        temp_dict["real_name"] = user.real_name
        temp_dict["tz"] = user.tz
        temp_dict["activity_periods"] = []
        for activity_period in activity_periods:
            temp_dict2 = dict()
            s_month = activity_period.start_time.strftime('%B')[:3]
            s_day = activity_period.start_time.day
            s_year = activity_period.start_time.year
            s_hour = activity_period.start_time.strftime('%l')
            s_min = activity_period.start_time.strftime('%M')
            s_am_pm = activity_period.start_time.strftime('%p')
            temp_dict2["start_time"] = f"{s_month} {s_day} {s_year} {s_hour}:{s_min}{s_am_pm}"

            e_month = activity_period.end_time.strftime('%B')[:3]
            e_day = activity_period.end_time.day
            e_year = activity_period.end_time.year
            e_hour = activity_period.end_time.strftime('%l')
            e_min = activity_period.end_time.strftime('%M')
            e_am_pm = activity_period.end_time.strftime('%p')
            temp_dict2["end_time"] = f"{e_month} {e_day} {e_year} {e_hour}:{e_min}{e_am_pm}"

            temp_dict["activity_periods"].append(temp_dict2)
        json_dict["members"].append(temp_dict)
    return JsonResponse(json_dict)
