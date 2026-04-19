from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages
from .models import Post


def index(request):

    if request.method == 'POST' and request.user.is_authenticated:
        content = request.POST.get('content')
        if content:

            Post.objects.create(content=content, author=request.user)
            return redirect('index')


    posts = Post.objects.all().order_by('-date')
    return render(request, 'index.html', {'posts': posts})


def register(request):
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Цей нік вже зайнятий')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Цей Email вже використовується')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)

                messages.success(request, 'Акаунт створено! Тепер увійди.')
                return redirect('login')
        else:
            messages.error(request, 'Паролі не збігаються')
            return redirect('register')

    return render(request, 'register.html')


def login(request):
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Невірний нік або пароль')
            return redirect('login')

    return render(request, 'login.html')


def logout_user(request):
    auth_logout(request)
    return redirect('index')



def profile_view(request, username):
    profile_user = get_object_or_404(User, username=username)
    is_me = False
    if request.user.is_authenticated and request.user == profile_user:
        is_me = True
    posts = Post.objects.filter(author=profile_user).order_by('-date')

    return render(request, 'profile.html', {
        'profile_user': profile_user,
        'posts': posts,
        'is_me': is_me
    })

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer

class MyFirstAPI(APIView):
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)

        return Response(serializer.data)

