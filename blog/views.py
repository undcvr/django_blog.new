from typing import Any, Dict
from django.shortcuts import render
from django.utils import *
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from .models import *
from .forms import *
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
import regex
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

class ShowProfilePageView(DetailView):
    model = Profile
    template_name = 'profile/profile.html'

    def get_context_data(self, *args, **kwargs):
        # users = Profile.objects.all()
        context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        context['page_user'] = page_user
        return context

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/mainpage.html', {'posts': posts, })

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.count_of_view += 1
    post.save()
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return redirect('login')
    else:
        user_form = UserRegistrationForm()
    return render(request, 'registration/signup.html', {'user_form': user_form})

class CreateProfile(CreateView):
    model = Profile
    template_name = 'profile/create_profile.html'
    
    fields = ['name', 'bio', 'profile_pic']
    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.email = self.request.user.email
        return super().form_valid(form)

    success_url = reverse_lazy('post_list')

@login_required
def like(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user in post.likes_check.all():
        post.likes_check.remove(request.user)
        post.likes -= 1
        post.count_of_view -= 1
        post.save()
    else:
        post.likes_check.add(request.user)
        post.likes += 1
        post.count_of_view -= 1
        post.save()
    return redirect('post_detail', pk=pk)

@login_required
def add_comment(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        
        content = request.POST.get('content')
        comment = Comment(post=post, author=request.user, text=content)
        comment.save()
    return redirect('post_detail', pk=pk)

def user_posts(request, username):
    user = User.objects.get(username=username)
    posts = Post.objects.filter(author=user)
    context = {
        'user': user,
        'posts': posts
    }
    return render(request, 'user_posts.html', context)


# def likes(request, pk):
#     post = Post.objects.get(pk=pk)
#     if post.likes.filter(pk=request.user.pk).exists():
#         post.likes.remove(request.user.pk)
#     else:
#         post.likes.add(request.user.pk)

#     post.save()
#     return redirect('post_detail', pk)


# def dislikes(request, pk):
#     post = Post.objects.get(pk=pk)
#     if post.dislikes.filter(pk=request.user.pk).exists():
#         post.dislikes.remove(request.user.pk)
#     else:
#         post.dislikes.add(request.user.pk)
    
#     post.save()
#     return redirect('post_detail', pk)