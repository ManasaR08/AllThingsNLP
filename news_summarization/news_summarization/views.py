from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage
from summarizer import Summarizer,TransformerSummarizer
import textract


def home(request):
    return render(request, 'index.html')

def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        bert_model = Summarizer()
        raw_text = textract.process("media\\" +  name).decode("utf-8")
        summary = ''.join(bert_model(raw_text, min_length = 60))
        return render(request, "upload.html", {"something": True, "summary": summary})
        context['url'] = fs.url(name)
    else:
        return render(request, 'upload.html', context)