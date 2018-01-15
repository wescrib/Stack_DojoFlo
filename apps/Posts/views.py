#Author: William Scribner
# 06JAN2018
#PURPOSE: make a mach stack overflow website, possibly to be used by people from the bootcamp.

from django.shortcuts import render, redirect
from .models import * 
from ..LoginAndRegistration.models import User
from django.contrib import messages

def home(request):
#all the contents that will be on the homepage
    if "user_id" not in request.session: 
        return redirect("/")

    context = {
        "subtopics" : SubTopic.objects.all(),
        "topics" : Topic.objects.all(),
        "allPosts" : Post.objects.all().order_by("-created_at") #calls all posts, and displays them in descending order from latest to oldest
    }

    return render(request, "posts/posts.html", context)

def question(request, subtopic_id):

    if "user_id" not in request.session: 
        return redirect("/")

    category = SubTopic.objects.get(id=subtopic_id)

    code_posts = Post.objects.filter(subtopic_id = subtopic_id).order_by("-created_at")

    context = {
        "category" : category,
        "Posts" : code_posts,
        "user" : User.objects.get(id=request.session['user_id']),
        "subtopics" : SubTopic.objects.all(),
        "topics" : Topic.objects.all(),
    }
    return render(request, "posts/questions.html", context)

def create_post(request):

    if "user_id" not in request.session: 
        return redirect("/")

    context = {
        "subtopics" : SubTopic.objects.all(),
        "topics" : Topic.objects.all(),
    }
    return render(request, "posts/submit.html", context)

def submit_post(request):

    if "user_id" not in request.session: 
        return redirect("/")

    if request.method == 'POST':
        if len(request.POST["title"]) < 1 or len(request.POST['content']) < 1:
            return redirect("/create_post")

        else:
            title = request.POST["title"]
            content = request.POST["content"]
            subtopic = SubTopic.objects.get(id=request.POST["subtopic"])
            subtopic_id = subtopic.id
            user = User.objects.get(id=request.session["user_id"])
            post = Post.objects.addPost(title, content, user, subtopic)
            return redirect("/question/{}".format(subtopic_id))

def info(request, post_id):

    if "user_id" not in request.session: 
        return redirect("/")

    comments = Comment.objects.filter(post_id=post_id).order_by("-created_at")
    user = User.objects.all()

    context = {
        "post" : Post.objects.get(id=post_id),
        "user" : user,
        "comments" : comments,
        "subtopics" : SubTopic.objects.all(),
        "topics" : Topic.objects.all(),

        }

    return render(request, "posts/info.html", context)

def addComment(request, post_id):

    if request.method == 'POST':
        user = User.objects.get(id=request.session['user_id'])
        content = request.POST['content']
        post = Post.objects.get(id=post_id)
        comment = Comment.objects.addComment(content,user,post)
        return redirect("/info/{}".format(post_id))
    else: 
        # for error_message in comment:
            # print dictionary["errors"]
        return redirect("/info/{}".format(post_id))

def user_profile(request, user_id):
    user = User.objects.get(id = user_id)
    posts = Post.objects.filter(user_id=user_id).order_by("-created_at")
    comments = Comment.objects.filter(user_id=user_id).order_by("-created_at")

    context = {
        "user" : user,
        "posts" : posts,
        "comments" : comments,

        "subtopics" : SubTopic.objects.all(),
        "topics" : Topic.objects.all(),
    }
    return render (request, "posts/user_profile.html", context)