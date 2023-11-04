from django.shortcuts import render
from datetime import datetime

# Create your views here.
def index(request):
    today = datetime.today().date()
    context = {"date": today}
    return render(request, 'foods/index.html', context=context)

def food_detail(request, food):
    context = {"name": food}
    return render(request, 'foods/detail.html', context=context)