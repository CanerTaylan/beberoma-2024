from appProduct.models import *
from appPage.models import *

def nav_context(request):
    context = dict()
    context['categories'] = Category.objects.filter(status = True).order_by('row_number')
    context['subcategories'] = SubCategory.objects.filter(status = True).order_by('row_number')
    context['pages'] = Page.objects.filter(status="PSH").order_by('title')
    return context

