from django.shortcuts import render

# Create your views here.
def privacy_policy_view(request, *args, **kwargs):
    return render(request, "privacy-policy.html")

def terms_and_conditions_view(request, *args, **kwargs):
    return render(request, "terms-and-conditions.html")

def refund_policy_view(request, *args, **kwargs):
    return render(request, "refund-policy.html")