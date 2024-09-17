from django.shortcuts import render, redirect
from main.forms import ShoesEntryForm
from main.models import ShoesEntry
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_main(request):
    shoes_entries = ShoesEntry.objects.all()

    context = {
        'name': 'Aliya Zahira Nadra',
        'class': 'PBP B',
        'npm': '2306245863',
        'shoes_entries': shoes_entries
    }

    return render(request, "main.html", context)

def create_shoes_entry(request):
    form = ShoesEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_shoes_entry.html", context) # ganti semua jadi shoes

def show_xml(request):
    data = ShoesEntry.objects.all()

def show_xml(request):
    data = ShoesEntry.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = ShoesEntry.objects.all()

def show_json(request):
    data = ShoesEntry.objects.all()
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

