from django.conf import settings
from django.shortcuts import render
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect
from django.views.generic import View
from .forms import RefundForm
from .models import Refund
from ecommerce.models import Order

# Create your views here.
class RequestRefundView(View):
    def get(self, *args, **kwargs):
        form = RefundForm()
        context = {
            'form': form
        }
        return render(self.request, "request_refund.html", context)

    def post(self, *args, **kwargs):
        form = RefundForm(self.request.POST)
        if form.is_valid():
            ref_code = form.cleaned_data.get('ref_code')
            message = form.cleaned_data.get('message')
            email = form.cleaned_data.get('email')
            # edit the order
            try:
                order = Order.objects.get(ref_code=ref_code)
                order.refund_requested = True
                order.save()

                # store the refund
                refund = Refund()
                refund.order = order
                refund.reason = message
                refund.email = email
                refund.save()

                messages.info(self.request, "Your request was received.")
                return redirect("ecommerce:request-refund")

            except ObjectDoesNotExist:
                messages.info(self.request, "This order does not exist.")
                return redirect("ecommerce:request-refund")
