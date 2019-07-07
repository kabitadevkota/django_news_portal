from django.shortcuts import render

# Create your views here.
def home(request):
    print(request)
    template_name="index.html"
    context={'content':'this is my home page'}
    return render(request, template_name,context)
