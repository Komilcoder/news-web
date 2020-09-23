from django.shortcuts import render,redirect
from .models import News
from .forms import NewsForm

def Home(request):
    news = News.objects.all()
    context = {'news':news}
    return render(request,'news_job/home.html', context)


def newcreate(request):
    form = NewsForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')


    context ={'form':form}
    return render(request,'news_job/createform.html',context)        


def newsupdate(request, pk):
    news = News.objects.get(id=pk)
    form = NewsForm(instance=news)
    if request.method == 'POST':
        form = NewsForm(request.POST,instance=news)
        if form.is_valid():
            form.save()
            return redirect('home')


    context = {'form':form}
    return render(request, 'news_job/createform.html', context)


def newsdelete(request, pk):

    news=News.objects.get(id=pk)
    if request.method == 'POST':
        news.delete()
        return redirect('home')
    context = {'news':news}
    return render(request, 'news_job/deleteform.html', context)    