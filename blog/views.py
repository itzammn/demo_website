from django.shortcuts import render

# Create your views here.
def home(request):
    author = 'wallium ladrian'
    age = 49
    address = 'the citadel'
    ctx = {'athr' :author, 'age' :age, 'addr' :address}
    return render(request, 'home.html',context=ctx)
def categories(request):
    cats = ['python','django','web development','programming']
    return render(request, 'categories.html',
                  context={'categories':cats})
def articles(request):
    data = [
        {'title':'first article',
         :'author':'waxlium ladrian',
         'data':'2020-01-01'},
         {'title':'the basin of life',
          'author':'steris',
          'date':'the second article',
          'author':'waxllium ladrian',
          'data':'2020-01-03'},
    ]
    return render(request,'articles.html',
                  context={'articles':data})
