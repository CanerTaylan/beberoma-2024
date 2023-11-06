from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.utils.text import slugify

# Create your views here.

def user_login(request):
    # if request.method == 'POST':
    #     username = request.POST.get('username')
    #     password = request.POST.get('password')
    #     user = authenticate(request, username=username, password=password)
    #     if user is not None:
    #         login(request, user)
    #         return redirect('home')
    #     else:
    #         messages.error(request, 'Invalid username or password')
    context={"title":"Kullanıcı Girişi",}
    return render(request, 'user/login.html', context)


