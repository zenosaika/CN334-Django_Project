from django.shortcuts import render
from django.http import HttpResponse

def ecommerce_index_view(request):
    '''This function render index page of ecommerce views'''
    return HttpResponse('Welcome to 6510742502 Phuree Phenhiran views!')
    
def item_view(request, item_id):
    context_data = {
        "item_id": item_id
    }
    return render(request, 'index.html',context = context_data)