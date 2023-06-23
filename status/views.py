from django.shortcuts import render
from . import gitfetch

def home(request):
    if request.method =='POST':
        username = request.POST['name']
        reponame = request.POST['repo_name']
        user_data = gitfetch.alluserrepo(username)
        print(user_data[0])
        if user_data is not None:
            return render(request,'index.html',{'user_data':user_data},)
        else:
            return render(request,'index.html',{'error':'User not found'})
    return render(request,'index.html')

