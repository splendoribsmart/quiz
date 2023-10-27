from django.contrib import admin
from .models import Subject, Level, Quiz, Question, Choice, Answer, Point, CountdownTimer

admin.site.register(Subject)
admin.site.register(Level)
admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Answer)
admin.site.register(Point)
admin.site.register(CountdownTimer)
