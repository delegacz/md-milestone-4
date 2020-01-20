from django.db import models
from django.conf import settings


STAR_CHOICES = (
    ('0','0'),
    ('1','1'),
    ('2','2'),
    ('3','3'),
    ('4','4'),
    ('5','5'),
)

# Create your models here.
class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=40, blank=True, null=True)
    review_content = models.CharField(max_length=300,blank=True, null=True)
    star_score = models.CharField(choices=STAR_CHOICES, max_length=1)
    
    def __str__(self):
        return self