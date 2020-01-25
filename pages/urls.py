from django.urls import path
from .views import privacy_policy_view, terms_and_conditions_view, refund_policy_view

urlpatterns = [
    path('privacy-policy/', privacy_policy_view, name="privacy-policy"),
    path('terms-and-conditions/', terms_and_conditions_view, name="terms-and-conditions"),
    path('refund-policy/', refund_policy_view, name="refund-policy")
]