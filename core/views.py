from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render
from .models import Post
from django.shortcuts import redirect
from .models import Profile
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect
from .models import Post

def create_post(request):
    if request.method == "POST":
        image = request.FILES.get("image")
        video = request.FILES.get("video")
        caption = request.POST.get("caption")

        Post.objects.create(
            user=request.user,
            image=image,
            video=video,
            caption=caption
        )
        return redirect("home")

    return render(request, "create_post.html")

@login_required
def follow_toggle(request, username):
    profile = get_object_or_404(Profile, user__username=username)

    if request.user in profile.followers.all():
        profile.followers.remove(request.user)
    else:
        profile.followers.add(request.user)

    return HttpResponseRedirect(reverse('profile', args=[username]))
def profile_view(request, username):
    user_profile = get_object_or_404(Profile, user__username=username)
    posts = user_profile.user.post_set.all()

    return render(request, "profile.html", {
        "profile": user_profile,
        "posts": posts
    })
@login_required
def like_post(request, id):
    post = Post.objects.get(id=id)

    if request.user in post.likes.all():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True

    return JsonResponse({
        'likes_count': post.likes.count(),
        'liked': liked
    })
from .models import Comment
@login_required
def add_comment(request, id):
    post = Post.objects.get(id=id)
    text = request.POST.get('text')

    comment = Comment.objects.create(
        post=post,
        user=request.user,
        text=text
    )

    return JsonResponse({
        "username": comment.user.username,
        "text": comment.text
    })


@login_required
def home(request):
    if request.method == "POST":
        image = request.FILES.get('image')
        caption = request.POST.get('caption')

        if image and caption:
            Post.objects.create(
                user=request.user,
                image=image,
                caption=caption
            )

        return redirect('home')
    

    posts = Post.objects.all().order_by('-id')
    return render(request, 'home.html', {'posts': posts})

