from django.contrib import admin

# Register your models here.
from .models import Review

class ReviewAdmn(admin.ModelAdmin):
    list_display = [
        'user',
        'title',
        'review_content',
        'star_score'
    ]

admin.site.register(Review)