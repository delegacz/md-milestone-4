from django.shortcuts import render
from django.conf import settings
from django.contrib import messages
from django.views.generic import View
from django.shortcuts import redirect
from django.core.exceptions import ObjectDoesNotExist
from ecommerce.models import Order, OrderItem
from .models import Coupon
from .forms import CouponForm

# Create your views here.
def get_coupon(request, code):
    try:
        coupon = Coupon.objects.get(code=code)
        return coupon
    except ObjectDoesNotExist:
        messages.info(request, "This coupon does not exist")
        return redirect("ecommerce:checkout")


class AddCouponView(View):
    def post(self, *args, **kwargs):
        form = CouponForm(self.request.POST or None)
        if form.is_valid():
            try:
                code = form.cleaned_data.get('code')
                order = Order.objects.get(
                    user=self.request.user, ordered=False)
                order.coupon = get_coupon(self.request, code)
                order.save()
                messages.success(self.request, "Successfully added coupon")
                return redirect("ecommerce:checkout")
            except ObjectDoesNotExist:
                messages.info(self.request, "You do not have an active order")
                return redirect("ecommerce:checkout")
