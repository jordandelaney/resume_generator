from django.shortcuts import render, redirect
from django.http import FileResponse

from .forms import ResumeForm

import io
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.rl_config import defaultPageSize
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter


# Create your views here.

def generate_pdf(name):
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer, pagesize="letter")
    p.drawString(500,500,f"{name}")
    p.showPage()
    p.save()
    buffer.seek(0)
    return FileResponse(buffer, filename="hello.pdf")

def index(request):
    form = ResumeForm()
    if request.method == 'POST':
        form = ResumeForm(data=request.POST)
        if form.is_valid():
            return generate_pdf(name=request.POST.get('name'))
    context = {
    'form': form,
    }
    return render(request, 'pdf_generator/index.html', context)