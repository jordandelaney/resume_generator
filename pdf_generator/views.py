from django.shortcuts import render
from django.http import FileResponse

import io
from reportlab.pdfgen import canvas


# Create your views here.
def index(request):
    context = {

    }
    return render(request, 'pdf_generator/index.html', context=context)

def generate_pdf(request):
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer)
    p.drawString(100,100,"Hello world.")
    p.showPage()
    p.save()
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename="hello.pdf")