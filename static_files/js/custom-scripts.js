
var hideable_shipping_form = $('.hideable_shipping_form');
var hideable_billing_form = $('.hideable_billing_form');

var use_default_shipping = document.querySelector("#same_billing_address");
console.log(use_default_shipping);


use_default_shipping.addEventListener('change', function() {
   if (this.checked) {
    hideable_billing_form.hide();
  } else {
    hideable_billing_form.show();
  }
});
