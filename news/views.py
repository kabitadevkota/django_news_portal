from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from news.forms import NewsForm
from news.models import News
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

# Create your views here.
def home(request):
    print(request)
    template_name="index.html"
    context={'content':'this is my home page'}
    return render(request, template_name,context)

#@login_required(login_url='/account/login')
class NewsCreateView(LoginRequiredMixin,CreateView):
    login_url='/account/login/'
    template_name = "news/create.html"
    form_class = NewsForm
    queryset = News.objects.all()
    success_url ="/"

    def form_valid(self,form):
        print("form valid")
        news = form.save(commit=False)
        news.author = self.request.user
        news.save()
        return super(NewsCreateView,self).form_valid(form)

    def form_invalid(self,form):
        print(form.errors)
        pass

class NewsList(ListView):
    model = News
    context_object_name = 'list_news'
    template_name='index.html'

class NewsDetail(DetailView):
    model = News
    template_name='news/details_post.html'
    context_object_name = 'news'


#class NewsDeleteView(DeleteView):
#    model = News
 #   template_name='news/delete_news.html'
 #   success_url= reverse_lazy('index')
   

class NewsDeleteView(DeleteView):
    model = News
    success_url= reverse_lazy('index')

    def get(self, *args ,**kwargs):
        return self.post(self, *args, **kwargs)