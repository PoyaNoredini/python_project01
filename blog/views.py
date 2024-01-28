from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post, Account
from django.views.generic import ListView
from .form import AccountForm


# Create your views here.


def index(request):
    Post.objects.all()
    return HttpResponse("welcome to the my blog ")


def PostList(request):
    posts = Post.objects.filter(status='published')

    paginator = Paginator(posts, 2)  # For pagination, it is used to place several posts on each page of the site
    page = request.GET.get('page')

    try:
        posts = paginator.page(page)  # It takes the posts of each page and shows them in the output

    except PageNotAnInteger:  # To control the errors
        posts = paginator.page(1)
        # anything that is not found, transfer directly to the first page
    except EmptyPage:
        posts = paginator.page(Paginator.num_pages)
        # If a page was empty, it will return to the last page of the post

    return render(request, 'blog/post/list.html', {'posts': posts, 'page': page})


# This view class does all the work of the above function and the use of view classes
# helps a lot in styling the program

class PostListView(ListView):
    queryset = Post.objects.filter(status='published')
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'


def PostDetails(request, post, pk):
    post = get_object_or_404(Post, id=pk, slug=post)

    return render(request, 'blog/post/details.html', {'post': post})


def UserAccount(request):
    user = request.user  # It specifies which user we logged in with
    try:
        account = Account.objects.get(user=user)  # If account was not loaded, we will fix it with this try
    except:
        account = Account.objects.create(user=user)
    if request.method == 'POST':
        # In the "if" section, we check what the user's request
        # is and whether the information he entered is correct or not

        form = AccountForm(data=request.POST)
        if form.is_valid():

            user.first_name = form.cleaned_data['name']
            user.last_name = form.cleaned_data['last_name']
            account.gender = form.cleaned_data['gender']
            account.address = form.cleaned_data['address']
            user.save()
            account.save()
            return redirect('blog:index')
        else:
            
            return render(request, 'blog/forms/account_form.html', {'form': form, 'account': account})
    form = AccountForm()
    return render(request, 'blog/forms/account_form.html', {'form': form})
