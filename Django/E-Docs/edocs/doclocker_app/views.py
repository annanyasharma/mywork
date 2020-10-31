from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User, Images, Document
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .form import RegisterForm
from .form import ContactForm
from django.core.files.storage import FileSystemStorage


# Create your views here.


def homepage(request):
    context = {
        'homepage_text': "If you are also thinking the same then Dlock is here to solve your this issue."
    }
    return render(request, 'homepage.html', context)


def DLock(request):
      # return HttpResponse("Welcome to docker ")
      context = {
          'DLock_text': "Welcome to DLOCK, You can access your stored Document from anywhere in the WORLD."
      }
      return render(request, 'DLock.html', context)




def contact(request):
    #return HttpResponse("Welcome to docker ")
    context = {
        'contact_text':"If you have any query, We are here to help you!! Fill the form below."
    }
    #form_class = ContactForm
    return render(request, 'contact.html', context)



def aboutus(request):
    # return HttpResponse("Welcome to docker ")
    context = {
        'aboutus_text': "About Us"
    }

    return render(request, 'aboutus.html', context)


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            messages.success(request, 'Account created successfully')
            login(request, user)
            return redirect('register')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})


def Upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['document_save']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'registration/login.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'registration/login.html')

