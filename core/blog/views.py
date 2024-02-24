from django.shortcuts import render

def indexview(request):
    name = 'ali'
    context = {
        'name' : name
    }
    return render(request, 'index.html', context)