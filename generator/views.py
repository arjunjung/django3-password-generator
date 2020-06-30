from django.shortcuts import render
from django.http import HttpResponse
import random
import string
# Create your views here.

def home(request):
    return render(request,'generator/home.html',{'name': 'Arjun Bhat'})

def password(request):
    a_z = string.ascii_lowercase
    A_Z = string.ascii_uppercase
    special_chars = "!#$&’()*+# ,-./:;<=>?@[\\]^_`{|}~"

    length = int(request.GET.get('length',14))
    uppercase_checker = request.GET.get('uppercase')
    special_chars_checker = request.GET.get('specialchars')
    final_password = ''

    if uppercase_checker:
        a_z += A_Z
    if special_chars_checker:
        a_z += special_chars

    for x in range(length):
        final_password += random.choice(a_z)

    return render(request,'generator/password.html',{'passkey':final_password, 'uppercase':uppercase_checker})

def test(request):
    return HttpResponse("Heelo")

def about_us(request):
    return render(request,'generator/about.html')