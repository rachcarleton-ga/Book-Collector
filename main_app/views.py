from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Book
from .forms import ReadingForm


# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def books_index(request):
      books = Book.objects.all()
      return render(request, 'books/index.html', {
    'books': books
  })

def books_detail(request, book_id):
  book = Book.objects.get(id=book_id)
  reading_form = ReadingForm()
  return render(request, 'books/detail.html', { 
    'book': book, 'reading_form': reading_form })

def add_reading(request, book_id):
  form = ReadingForm(request.POST)
  if form.is_valid():
    new_reading = form.save(commit=False)
    new_reading.book_id = book_id
    new_reading.save()
  return redirect('detail', book_id=book_id)

class BookCreate(CreateView):
    model = Book
    fields = '__all__'


class BookUpdate(UpdateView):
    model = Book
    fields = ['author', 'description', 'publishedyear']

class BookDelete(DeleteView):
    model = Book
    success_url = '/books'