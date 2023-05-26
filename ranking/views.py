from django.shortcuts import render

# Create your views here.
def rankingHome(request):
    return render(request, "rankingIndex.html")