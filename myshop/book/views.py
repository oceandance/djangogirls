from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.csrf import csrf_exempt

from book.forms import OrdersForm
from book.models import Books, Authors, BookCategory, Orders


def all_book_list(request):
    all_books = Books.objects.all().order_by('published_date')
    all_authors = Authors.objects.all()
    return render(request, 'book/main.html', {'books': all_books, 'authors' : all_authors})


def book_info(request, pk):
    book = get_object_or_404(Books, pk=pk)
    all_authors = Authors.objects.all()
    all_category = BookCategory.objects.all()
    return render(request, 'book/book_info.html', {'book': book, 'authors': all_authors, 'category': all_category})


def author_info(request, pk):
    author = get_object_or_404(Authors, pk=pk)
    all_books = Books.objects.all()
    return render(request, 'book/author_info.html', {'author': author, 'books':all_books})


@login_required
def post_new(request):
    all_books = Books.objects.all().order_by('published_date')
    all_authors = Authors.objects.all()
    return render(request, 'book/main.html', {'books': all_books, 'authors' : all_authors})


@login_required
def order_list(request):
    all_books = Books.objects.all().order_by('published_date')
    all_authors = Authors.objects.all()
    return render(request, 'book/orders.html', {'books': all_books, 'authors' : all_authors})


@csrf_exempt
def add_book(request):
    post = get_object_or_404(Orders)
    if request.method == "POST":
        form = OrdersForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            # post.published_date = timezone.now()
            post.save()
            return redirect('all_book_list')
    else:
        form = OrdersForm(instance=post)
    all_books = Books.objects.all().order_by('published_date')
    all_authors = Authors.objects.all()
    return render(request, 'book/main.html', {'books': all_books, 'authors': all_authors})

# def login(request):
#
#     username = request.POST['username']
#     password = request.POST['password']
#     user = authenticate(request, username=username, password=password)
#     login(request, user)
#     all_books = Books.objects.all().order_by('published_date')
#     all_authors = Authors.objects.all()
#     if user is not None:
#
#         return render(request, 'book/main.html', {'books': all_books, 'authors': all_authors})
#     else:
#         return render(request, 'book/main.html', {'books': all_books, 'authors': all_authors})
