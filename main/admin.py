from django.contrib import admin

# Register your models here.
from main.models import User_profile, Challenge, gherbi, Comment


@admin.register(User_profile)
class User_profile_admin(admin.ModelAdmin):
    list_filter = ('name', 'XP',)
    list_display = ('XP', 'name',)
    search_fields = ('XP', 'name',)

@admin.register(Challenge)
class Challenge_admin(admin.ModelAdmin):
    list_filter = ('id', 'creator', 'name', 'description', 'category')
    list_display = ('id', 'creator', 'name', 'description', 'category')
    search_fields = ('id', 'creator', 'name', 'description', 'category')

@admin.register(gherbi)
class gherbi_admin(admin.ModelAdmin):
    list_display = ('challenge',)
    list_filter = ('performer', 'vote', 'challenge')
    search_fields = ('performer', 'vote', 'challenge')

@admin.register(Comment)
class comment_admin(admin.ModelAdmin):
    list_display = ('comment', 'writer', 'date', 'challenge', 'user')
    list_filter = ('comment', 'writer', 'date', 'challenge', 'user')
    search_fields = ('comment', 'writer', 'date', 'challenge', 'user')
