from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings

from .forms import ResumeForm

from easy_pdf.views import PDFTemplateView
import easy_pdf

# Create your views here.

class HelloPDFView(PDFTemplateView):
    template_name = 'pdf_generator/hello.html'

    base_url = 'file://' + str(settings.STATIC_ROOT)
    download_filename = 'hello.pdf'

    def get_context_data(self, **kwargs):
        return super(HelloPDFView, self).get_context_data(
            pagesize='letter',
            title='Hi there!',
            **kwargs
            )

def index(request):
    form = ResumeForm()
    if request.method == 'POST':
        form = ResumeForm(data=request.POST)
        if form.is_valid():
            context = {
            'name': request.POST.get('name'),
            }
            template = 'pdf_generator/hello.html'
            return easy_pdf.rendering.render_to_pdf_response(request,template,context,using=None,download_filename='Hello.pdf',content_type='application/pdf',response_class=HttpResponse)
    context = {
    'form': form,
    }
    return render(request, 'pdf_generator/index.html', context)