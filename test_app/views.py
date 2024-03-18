from django.shortcuts import render, redirect
from django.views import View 
from .models import TestModel
from .forms import TestForm
from . import tasks 


class TestView(View):
    def get(self, request):
        notes = TestModel.objects.all()
        form = TestForm
        return render(request, 'index.html', context={'notes': notes, 'form': form})

    def post(self, request):
        if request.POST.get('delete'):
            note = TestModel.objects.get(pk=request.POST.get('delete'))
            note.delete()
            return redirect('home')
        form = TestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        

class TestCeleryView(View):
    def get(self, request):
        tasks.check_celery.delay()
        return render(request, 'celery_page.html')
        