import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'django_tutorials.settings'

import django
django.setup()

from polls.models import Question, Choice
import csv

from django.utils import timezone
import pytz

print('loading data into question/choice model')
with open('data/questions.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        q = Question.objects.get_or_create(question_text=row[0], pub_date=timezone.now())
        
        # load all the choices
        for choice in row[1:]:
            c = Choice.objects.get_or_create(question=q[0], choice_text=choice, votes=0)