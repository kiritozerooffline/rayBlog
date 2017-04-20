from django.shortcuts import render

# Create your views here.

def index(request):
	blogs = Blog.object.all()

	return render(request, 'index.html',{"blogs": Blogs})