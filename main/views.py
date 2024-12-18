from django.shortcuts import render, redirect, reverse
from main.forms import ShoesEntryForm
from main.models import ShoesEntry
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.html import strip_tags
from django.http import HttpResponse
from django.core import serializers
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


# Create your views here.
@login_required(login_url='/login')
def show_main(request):
    context = {
        'name': request.user.username,
        'class': 'PBP B',
        'npm': '2306245863',
        'last_login': request.COOKIES['last_login'],
    }

    return render(request, "main.html", context)

def create_shoes_entry(request):
    form = ShoesEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        shoes_entry = form.save(commit=False)
        shoes_entry.user = request.user
        shoes_entry.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_shoes_entry.html", context)

def show_xml(request):
    data = ShoesEntry.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

# @login_required
def show_json(request):
    data = ShoesEntry.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = ShoesEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_xml_by_id(request, id):
    data = ShoesEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = ShoesEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
        user = form.get_user()
        login(request, user)
        response = HttpResponseRedirect(reverse("main:show_main"))
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response
      else:
        messages.error(request, "Invalid username or password. Please try again.")

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def edit_shoes(request, id):
    # Get shoes entry berdasarkan id
    shoes = ShoesEntry.objects.get(pk = id)

    # Set shoes entry sebagai instance dari form
    form = ShoesEntryForm(request.POST or None, instance=shoes)

    if form.is_valid() and request.method == "POST":
        # Simpan form dan kembali ke halaman awal
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_shoes.html", context)

def delete_shoes(request, id):
    # Get shoes berdasarkan id
    shoes = ShoesEntry.objects.get(pk = id)
    # Hapus shoes
    shoes.delete()
    # Kembali ke halaman awal
    return HttpResponseRedirect(reverse('main:show_main'))

@csrf_exempt
@require_POST
def add_shoes_entry_ajax(request):
    name = strip_tags(request.POST.get("name"))
    price = request.POST.get("price")
    description = strip_tags(request.POST.get("description"))
    color = strip_tags(request.POST.get("color"))
    condition = strip_tags(request.POST.get("condition"))
    release_year = request.POST.get("release_year")
    user = request.user

    new_shoes = ShoesEntry(
        name=name,
        price=price,
        description=description,
        color=color,
        condition=condition,
        release_year=release_year,
        user=user
    )
    new_shoes.save()

    return HttpResponse(b"CREATED", status=201)

@csrf_exempt
def create_shoes_flutter(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            new_shoes = ShoesEntry.objects.create(
                user=request.user,
                name=data["name"],           
                price=int(data["price"]),   
                description=data["description"],
                color=data["color"],
                condition=data["condition"],
                release_year=int(data["release_year"]) 
            )
            new_shoes.save()
            return JsonResponse({"status": "success"}, status=200)
        except Exception as e:
            return JsonResponse({
                "status": "error",
                "message": str(e)
            }, status=400)
    else:
        return JsonResponse({"status": "error", "message": "Invalid method"}, status=401)