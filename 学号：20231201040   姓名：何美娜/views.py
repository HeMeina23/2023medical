from django.http import HttpResponse

def hello_world(request):
    """Hello World视图函数"""
    return HttpResponse("Hello World! - 何美娜 20231201040")