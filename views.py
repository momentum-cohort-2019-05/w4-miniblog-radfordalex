from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
# Create your views here.

from blog.models import BlogPost, Blogger, Comment

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_blogs = BlogPost.objects.all().count()
    num_comments = Comment.objects.all().count()
    
    # The 'all()' is implied by default.    
    num_bloggers = Blogger.objects.count()
    
    context = {
        'num_blogs': num_blogs,
        'num_comments': num_comments,
        'num_bloggers': num_bloggers,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)



class BlogPostListView(generic.ListView):
    model = BlogPost
    paginate_by = 5

class BlogPostDetailView(generic.DetailView):
    model = BlogPost

class BloggerListView(generic.ListView):
    model = Blogger
    
class BloggerDetailView(generic.DetailView):
    model = Blogger

def add_comment_to_post(request, pk):
    from blog.forms import CommentForm
    from django.views.generic.edit import CreateView
    comment = get_object_or_404(BlogPost, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            # comment.user = request.user
            comment.post = Comment
            form.save(Comment)
            return redirect('blog-detail', pk=pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html', {'form': form})