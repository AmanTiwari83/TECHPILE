from django.contrib import admin
from.models import *

#Register your models here.

class categoryAdmin(admin.ModelAdmin):
    list_display = ('id','cname')
admin.site.register(category,categoryAdmin)
class signupAdmin(admin.ModelAdmin):
    list_display = ('id','enroll','name','apply','college','course','year','contact','email','date')
admin.site.register(signup,signupAdmin)

class contactusAdmin(admin.ModelAdmin):
    list_display = ('id','name','contact','email','message')
admin.site.register(contactus,contactusAdmin)

class feedAdmin(admin.ModelAdmin):
    list_display = ('id','name','picture','college','feedback')
admin.site.register(feed,feedAdmin)

class imagegalleryAdmin(admin.ModelAdmin):
    list_display = ('id','category','picture','idate')
admin.site.register(imagegallery,imagegalleryAdmin)

class videogalleryAdmin(admin.ModelAdmin):
    list_display = ('category','vlink','date')
admin.site.register(videogallery,videogalleryAdmin)

class placementsAdmin(admin.ModelAdmin):
    list_display = ('id','image','name','college','company','fyear','syear')
admin.site.register(placements,placementsAdmin)

class coursecategoryAdmin(admin.ModelAdmin):
    list_display = ('id','image','course')
admin.site.register(coursecategory,coursecategoryAdmin)
class coursesAdmin(admin.ModelAdmin):
    list_display = ('id','picture','coursecategory','link')
admin.site.register(courses,coursesAdmin)



