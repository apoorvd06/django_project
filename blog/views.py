from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

posts=[
    {
        'author':'CoreyMS',
        'title':'blog Post1 ',
        'content':'first post content',
        'date_posted': 'June 29, 2026'
    },
    {
        'author':'apporv',
        'title':'blog Post  2 ',
        'content':'2nd post content',
        'date_posted': 'June 30, 2026'
    }

]
# Create your views here.
def home(request):
    context={
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html',context)
def about(request):
    return render(request,'blog/about.html',{'title': "About"})