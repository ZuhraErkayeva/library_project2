from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect,get_object_or_404
from .models import Book
from .forms import BookForm
@login_required
def book_list(request):
    books = Book.objects.all()
    return render(request,'book_list.html',{'books':books})
@login_required
def book_detail(request,pk):
    book = Book.objects.get(pk=pk)
    return render(request,'book_detail.html',{'book':book})
@login_required
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list')
        else:
            return HttpResponse("Form is invalid")
    form = BookForm()
    return render(request,'add_book.html',{'form':form})
@login_required
def update_book(request,pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST,instance=book)
        if form.is_valid():
            form.save()
            return redirect('detail',pk=pk)
        else:
            return HttpResponse("Form is invalid")
    form = BookForm( instance=book)
    return render(request,'add_book.html',{'form':form, 'book': book})


@login_required
def delete_book(request,pk):
    book = get_object_or_404(Book, pk = pk)
    if request.method == 'POST':
        book.delete()
        return redirect('list')
    return render(request,'confirm.html',{'book':book})
