from django.shortcuts import render

from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render
from django.http import FileResponse
from .models import CVData, CVExperience, CVSkills

import pdfkit

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def get_data():
    try:
        my_data = CVData.objects.get(name="Prijilevschi")
        my_skills = CVSkills.objects.all()
        my_experience = CVExperience.objects.all()
    except:
        return HttpResponse("Name not found.")

    info = {
        'name' : my_data.name,
        'surrname' : my_data.surrname,
        'email' : my_data.email,
        'profession' : my_data.profession,
        'phone_number' : my_data.phone_number,
        'skills' : my_skills,
        'experiences' : my_experience,
    }
    return info

def main_page(request):
    return render(request, 'index.html', get_data())

def down_pdf(request):
    pdfkit.from_url('http://localhost:8000/polls/sample', 'pdf.pdf')
    pdf = open('pdf.pdf', 'rb')
    response = FileResponse(pdf)
    return response

def static_main(request):
    return render(request, 'sample.html', get_data())
