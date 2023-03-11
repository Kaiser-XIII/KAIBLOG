from django.shortcuts import render
from django.http.response import HttpResponse

data = {
    "blogs":[
        {
            "id":1,
            "title":"Who am I?",
            "image":"whoami.png",
            "is_active":True,
            "is_home":True,
            "description":"Who is Kaiser?"
        },
        {
            "id":2,
            "title":"Resume?",
            "image":"resume.jpg",
            "is_active":True,
            "is_home":True,
            "description":"My resume"
        },
        {
            "id":3,
            "title":"Projects",
            "image":"projects.jpg",
            "is_active":True,
            "is_home":True,
            "description":"My projects"
        },
        {
            "id":4,
            "title":"Hobbies",
            "image":"hobbies.jpg",
            "is_active":True,
            "is_home":False,
            "description":"My hobbies"
        },
        {
            "id":4,
            "title":"Mixed",
            "image":"whoami.png",
            "is_active":True,
            "is_home":False,
            "description":"Mixed catagory"
        }
    ]
}


# Create your views here.

def index(request):
    context = {
        "blogs":data["blogs"]
    }
    return render(request, "blog/index.html",context)

def blogs(request):
    context = {
        "blogs":data["blogs"]
    }
    return render(request , "blog/blogs.html",context)

def blog_details(request, id):
    # blogs = data["blogs"]
    # selectedBlog = None
    # for blog in blogs:
    #     if blog["id"] == id:
    #         selectedBlog = blog
    blogs = data["blogs"]
    selectedBlog = [blog for blog in blogs if blog["id"] == id][0]


    return render(request, "blog/blog-details.html",{
        "blog" : selectedBlog
    })

