import django_filters
from django_filters import CharFilter, ChoiceFilter
from django.forms.widgets import TextInput
from .models import Item

class ProductFilter(django_filters.FilterSet):
    
    title = CharFilter(field_name="title",lookup_expr="icontains", widget=TextInput(attrs={'placeholder':'Search'}))
       
    class Meta:
        model = Item
        fields = '__all__'
        exclude = ['image','slug','desc','description','label','discount_price','price']