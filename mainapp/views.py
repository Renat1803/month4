from django.shortcuts import render, redirect
from mainapp.models import Director, Movie, Review
import datetime
from mainapp.forms import DirectorForm, MovieForm, RegisterForm, LoginForm

now = datetime.datetime.now().replace(microsecond=0)

def index(request):
    dict_ = {
        'key': 'Information about website, you can follow the link',
        'color': '#d534eb'
    }
    return render(request, 'index.html', context=dict_)

def index1(request):
    dict_ = {
        'description': 'Continuation of information, in this website you can add, change information in database',
        'color': 'green'
    }
    return render(request, 'index.html', context=dict_)

def index2(request):
    dict_ = {
        'data' f"{now}"
    }
    return render(request, 'index.html', context=dict_)


def director_list_view(request):
    directors = Director.objects.all()
    context = {
        'director_list': directors
    }
    return render(request, 'directors.html', context=context)


def director_detail_view(request, id):
    director = Director.objects.get(id=id)
    return render(request, 'detail.html', context={'director_detail': director})


def movie_list_view(request):
    context = {
        'movie_list': Movie.objects.all(),
        'director_list': Director.objects.all()
    }
    return render(request, 'movies.html', context=context)


def movie_detail_view(request, id):
    movie = Movie.objects.get(id=id)
    return render(request, 'detail.html', context={'movie_detail': movie,
                                                   'director_list': Director.objects.all(),
                                                   'reviews': Review.objects.filter(movie=movie)})


def review_list_view(request):
    context = {
        'review_list': Review.objects.all(),
        'movie_list': Movie.objects.all()
    }
    return render(request, 'reviews.html', context=context)


def review_detail_view(request, id):
    review = Review.objects.get(id=id)
    return render(request, 'detail.html', context={'review_detail': review})


def director_movie_filter_view(request, directors_id):
    context = {
        'movie_list': Movie.objects.filter(director_id=directors_id),
        'director_list': Director.objects.all()
    }
    return render(request, 'movies.html', context=context)


def movie_review_filter_view(request, id):
    context = {
        'review_list': Review.objects.filter(id=id),
        'movie_list': Movie.objects.all()
    }
    return render(request, 'reviews.html', context=context)

def add_director_view(request):
    form = DirectorForm
    return render(request, 'add_director.html', context={
        'form': form
    })

def add_movie_view(request):
    form = MovieForm
    return render(request, 'add_director.html', context={
        'form': form
    })

def register_view(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/register/')
    return render(request, 'register.html', context={
        'form': form
    })

def login_view(request):
    form = LoginForm()
    return render(request, 'login.html', context={
        'form':form
    })
