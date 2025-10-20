from django.shortcuts import render

def addition_view(request):
    """加法练习应用的主视图"""
    return render(request, 'addition/index.html')