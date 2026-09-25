from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView
from .models import Product

class ProductListView(ListView):
    model = Product
    template_name = 'myapp/product_list.html' 

    def get_queryset(self): #get_queryset() определяет, какие объекты будут получены из базы данных
        return Product.objects.filter(price__gt = 100)


from django.views.generic import ListView, DetailView
class ProductDetailView(DetailView):
    model = Product
    template_name = 'myapp/product_detail.html'

    def get_object(self):
        return Product.objects.get(pk= self.kwargs['pk']) # если url /products/5/ то self.kwargs['pk'] получит 5

    def get_context_data(self, **kwargs):
        # 1 Получаем базовый словарь контекста от родительского класса (Django сам туда уже положил наш 'product')
        context = super().get_context_data(**kwargs)
        # 2 Добавляем в этот словарь свою собственную переменную 'message'
        context['message'] = 'This is a product detail page'
        # 3 Возвращаем обновленный словарь
        return context


from django.views.generic import ListView, DetailView, CreateView
class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'myapp/product_form.html'

    def form_valid(self, form):
        print('Form is valid')
        return super().form_valid(form) # POST - form - is_valid() - YES - form_valid()

    def form_invalid(self, form):
        print('Form has errors')
        print(form.errors)
        return super().form_invalid(form)

    def get_form(self, form_class = None):
        form = super().get_form(form_class)
        form.fields['name'].required = False
        return form