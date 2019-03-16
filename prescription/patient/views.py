from django.shortcuts import render
from .models import Person
import io
from io import BytesIO
from django.http import FileResponse
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from django.views.generic.detail import DetailView
from easy_pdf.views import PDFTemplateResponseMixin
from .tasks import add_person



def index(request):
    if request.method == 'POST':
        add_person.apply_async([
            request.POST.get('first_name'),
            request.POST.get('last_name'),
            request.POST.get('age'),
            request.POST.get('prescription'),
            request.POST.get('exp_date'),
        ])
        return render(request, 'patient/index.html')

    else:
        return render(request, 'patient/index.html')

def pdf_list(request):
        return render(request, 'patient/pdf_list.html', {'pdfs': Person.objects.all()})


class PDFUserDetailView(PDFTemplateResponseMixin, DetailView):
    model = Person
    template_name = 'patient/person.html'
