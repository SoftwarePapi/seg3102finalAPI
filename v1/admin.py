from django.contrib import admin
from .models import Users, Teams, Team_Members, Comments, Courses, Section_students, Threads, Sections

#Register models here
admin.site.register(Users)
admin.site.register(Teams)
admin.site.register(Team_Members)
admin.site.register(Comments)
admin.site.register(Courses)
admin.site.register(Section_students)
admin.site.register(Threads)
admin.site.register(Sections)
