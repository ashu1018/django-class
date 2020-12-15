from django.shortcuts import render
from .models import Vacancy
def index(request):
    
    vacancies = Vacancy.objects.all()
    context = {
        'vacancies': vacancies
    }
    
    return render(
        request,
        'job/index.html',
        context,
    )
