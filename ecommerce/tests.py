from django.test import TestCase, Client
from django.urls import reverse
from .models import Item, OrderItem, Order, Address, Payment, UserProfile
from django.contrib.auth.models import User
from .forms import CheckoutForm, PaymentForm
from coupons.forms import CouponForm
from refunds.forms import RefundForm
from coupons.forms import CouponForm
from django_countries import fields, countries, data
from django_countries.fields import CountryField
from django_countries.tests import forms, custom_countries
from django_countries.tests.models import Person, AllowNull, MultiCountry, WithProp
# Create your tests here.

class ItemTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.title = "Test Sneakers"
        cls.price = "100"
        cls.slug = "test-sneakers"
    
    def test_string_representation(self):
        self.assertEqual(str(self.title), "Test Sneakers")
    
    def test_get_absolute_url(self):
        expected = "/product/test-sneakers/"
        actual = Item.get_absolute_url(self)
        self.assertEqual(actual, expected) 

    def test_add_to_cart_url(self):
        expected = "/add-to-cart/test-sneakers/"
        actual = Item.get_add_to_cart_url(self)
        self.assertEqual(actual, expected)
    
    def test_get_remove_from_cart_url(self):
        expected = "/remove-from-cart/test-sneakers/"
        actual = Item.get_remove_from_cart_url(self)
        self.assertEqual(actual, expected)

class OrderItemTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.title = "Test Sneakers"
        cls.price = 20
        cls.discount_price = 10
        cls.quantity = 4
        cls.item = Item(title=cls.title, 
                        price=cls.price, 
                        discount_price=cls.discount_price
                        )
    
    def test_string_representation(self):
        expected = "4 of Test Sneakers"
        actual = OrderItem(item=Item(title=self.title), quantity=self.quantity)
        self.assertEqual(str(actual), expected)

    def test_get_total_item_price(self):
        expected = 80
        actual = OrderItem.get_total_item_price(self)
        self.assertEqual(actual, expected)

    def test_get_total_discount_item_price(self):
        expected = 40
        actual = OrderItem.get_total_discount_item_price(self)
        self.assertEqual(actual, expected)
    
    def test_get_amount_saved(self):
        expected = 40
        actual = OrderItem.get_total_item_price(self) - OrderItem.get_total_discount_item_price(self)
        self.assertEqual(actual, expected)
    
class OrderTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = User(username="TestUser")
    
    def test_string_representation(self):
        expected = "TestUser"
        actual = Order(user=self.user)
        self.assertEqual(str(actual), expected)
    
class AddressTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = User(username="TestUser")

    def test_string_representation(self):
        expected = "TestUser"
        actual = Address(user=self.user)
        self.assertEqual(str(actual), expected)

class TestPayment(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = User(username="TestUser")

    def test_string_representation(self):
        expected = "TestUser"
        actual = Payment(user=self.user)
        self.assertEqual(str(actual), expected)

class TestHomeView(TestCase):
    @classmethod
    def setUpTestData(cls):
        number_of_items = 15
        for item in range(number_of_items):
            Item.objects.create(
                title=f'N {item}',
                price=10,
                category='S',
                label='P',
                slug=f's {item}',
                description='Aaa',
                image="media/logo.png"
            )
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_pagination_works(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)

class TestItemDetailView(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.client = Client()
        cls.product = Item(title="NikeTest",
                       price=100,
                       slug="niketest")
        cls.product = Item.objects.create(title="NikeTest",
                       price=100,
                       slug="niketest",
                       description="",
                       image="media/logo.png")
    def test_template(self):
        
        response = self.client.get('/product/niketest/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'product.html')

class TestOrderSummaryView(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create(username="TestUser",
                                       password="TestPass!",
                                       #password2="TestPass!",
                                       email="test@example.com")
        cls.product = Item.objects.create(title="NikeTest",
                           price=100,
                           slug="niketest") 
        cls.order = OrderItem.objects.create(user=cls.user,
                                             item = cls.product,
                                             quantity=2
                                             )
        
        cls.context = {
            'object': cls.order
        }
        client = Client()
    def test_user_not_logged_in(self):
        url = '/order-summary/'
        response = self.client.get('/order-summary/')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, "/accounts/login/?next=/order-summary/")
    
class FormTest(TestCase):

    def test_payment_form(self):
        form_data = {'stripeToken':'ysdsda',
                     'save':False,
                     'use_default':False}
        form = PaymentForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_refund_form(self):
        form_data = {
            'ref_code':'7ssadasdjlads',
            'message':'Test Message',
            'email':'test@example.com'
        }
        form = RefundForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_coupon_form(self):
        form_data = {
            'code':'2zzx'
        }
        form = CouponForm(data=form_data)
        self.assertTrue(form.is_valid())