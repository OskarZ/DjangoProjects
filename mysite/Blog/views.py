from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.utils import timezone
from .forms import PostForm
from .forms import MailForm
from .models import Mail
from .forms import AutoForm

def index(request):

    art = Post.objects.order_by('-created_date')
    return render(request, 'Blog/Bltemp.html',{
        'art':art
    })

def index1(request):
    art = Post.objects.filter(category='Andere').order_by('-created_date')
    return render(request, 'Blog/Antemp.html',{
        'art':art
    })

def index2(request):
    art = Post.objects.filter(category='Reisen').order_by('-created_date')
    return render(request, 'Blog/Reitemp.html',{
        'art': art
    })

def index3(request):
    art = Post.objects.filter(category='Arbeit').order_by('-created_date')
    return render(request, 'Blog/Artemp.html',{
        'art': art
    })

def index4(request):
    art = Post.objects.filter(category='Freizeit').order_by('-created_date')
    return render(request, 'Blog/Frtemp.html',{
        'art': art
    })

def index5(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.published_date = timezone.now()
            post.save()
            return render(request, 'Blog/erfolg.html',{})
    else:
        form = PostForm()
    return render(request, 'blog/newtemp.html',{
        'form':form
    })


def index6(request):
    if request.method == "POST":
        form = MailForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return render(request, 'Blog/Nachricht/erfolg.html',{})
    else:
        form = MailForm()
    return render(request, 'Blog/Nachricht/newtemp.html',{
        'form':form
    })

def index7(request):

    if request.method == "POST":
        form = AutoForm(request.POST)
        if form.is_valid():
            p1 = form.cleaned_data['schl1']
            p2 = form.cleaned_data['schl2']
            var = Mail.objects.filter(mail=p1, Schlüssel=p2)
            return render(request, 'Blog/Nachricht/Anzeigetemp.html', {
                'var':var
            })
    else:
        form = AutoForm()
    return render(request, 'Blog/Nachricht/Autotemp.html', {
        'form':form
    })

def index8(request):
    return render(request, 'Blog/Nachricht/Start.html', {})
