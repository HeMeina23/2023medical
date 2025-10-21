from django.http import Http404, HttpResponse 
from django.shortcuts import render 

# Create your views here. 
def index(request): 
    return render(request, "singlepage/index.html") 

# The texts are much longer in reality, but have 
# been shortened here to save space 
texts = [
    "<h1>The Importance of Reading</h1><p>Reading is one of the most fundamental skills a person can develop. It opens doors to knowledge, imagination, and understanding. Through reading, we can explore different cultures, learn new perspectives, and expand our vocabulary. Regular reading improves cognitive function and enhances critical thinking abilities.</p>",
    
    "<h1>Benefits of Exercise</h1><p>Regular physical activity is essential for maintaining good health. Exercise helps control weight, reduces the risk of chronic diseases, and improves mental health. It boosts energy levels, promotes better sleep, and strengthens the immune system. Even moderate exercise can make a significant difference in overall well-being.</p>",
    
    "<h1>Technology in Modern Life</h1><p>Technology has transformed how we live, work, and communicate. From smartphones to artificial intelligence, technological advancements continue to shape our world. While technology offers numerous benefits, it's important to maintain a balance and use it responsibly to avoid negative impacts on mental health and social relationships.</p>"
] 

def section(request, num): 
    if 1 <= num <= 3: 
        return HttpResponse(texts[num - 1]) 
    else: 
        raise Http404("No such section")