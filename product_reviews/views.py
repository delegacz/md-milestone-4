from django.shortcuts import render
from .models import Review

# Create your views here.
def product_review(View):
    model = Review
    template_name = "product-review.html"
