from django.shortcuts import render, HttpResponse, redirect

import json
from .models import Movie, Genre
from django.conf import settings
from .forms import MovieRegistration
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User

def index(request):
    return render(request, 'base.html')


def search_movie(request):
    if request.method == 'GET':
        print('currently getting query')
        query = request.GET.get('query',None)
        if not query:
            print('you did not eneter any query')
            return redirect('index')
        print('yessss')

        allPostsname= Movie.objects.filter(name__icontains=query)
        allPostspopularity= Movie.objects.filter(popularity__icontains=query)
        allPostsdirector =Movie.objects.filter(director__icontains=query)
        allPostsgenre =Movie.objects.filter(genre__name__icontains=query)
        allPosts=  allPostsname.union(allPostsdirector, allPostspopularity,allPostsgenre)
        params = {'allPosts': allPosts, 'query': query}

        return render(request,'search.html',params)
    return redirect('index')

def allmovies(request):

    allPosts = Movie.objects.all()
    params = {'allPosts': allPosts}

    return render(request,'allmovies.html',params)



def registerMovie(request):
    if request.method == 'POST':
        name = request.POST['name']
        popularity = request.POST['popularity']
        director = request.POST['director']
        imdb_score = request.POST['imdb_score']
        genre_list = request.POST['genre'].split()
        print(name,popularity,director,imdb_score,genre_list)
        movie, created = Movie.objects.get_or_create(name=name, popularity=popularity, director=director, imdb_score=imdb_score)
        for name in genre_list:
            name = name.strip()
            genre, created = Genre.objects.get_or_create(name=name)
            movie.genre.add(genre)
        movie.save()
        return redirect('allmovies')

    return render(request, 'Moviereg.html')



def handlelogin(request):
    if request.method == 'POST':
        # Get the post parameter
        loginusername = request.POST['loginusername']
        loginpass = request.POST['loginpass']
        user = authenticate(username=loginusername,password = loginpass)
        if user is not None:
            print('yess')
            login(request, user)
            return redirect('index')
        else:
            print('incorrect')
            return redirect('index')

    return HttpResponse('404')

def handlelogout(request):
    print('logged out')
    logout(request)
    return redirect('index')


def delete_data(request, id):
    if request.method == 'POST':
        delete = Movie.objects.get(id=id)
        delete.delete()
        return redirect('allmovies')

def update_data(request, id):
    if request.method == 'POST':
        edit = Movie.objects.get(pk=id)
        fm = MovieRegistration(request.POST, instance=edit)
        if fm.is_valid():
            fm.save()
        return redirect('allmovies')
    else:
        edit = Movie.objects.get(pk=id)
        fm = MovieRegistration(instance=edit)
        return render(request, 'update.html', {'form': fm})
    return render(request, 'update.html', {'form': fm})