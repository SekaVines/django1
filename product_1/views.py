from django.shortcuts import render
from . import models, forms


class HomePage:
    def home_page(request):
        product = models.Product_in.objects.filter().order_by('-id')
        return render(request, 'home_page_in.html', {'product': products})

    def __str__(self):
        self.home_page()
