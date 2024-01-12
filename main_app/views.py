import uuid
import boto3
import os
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Book, Reading, Bookmark, Photo
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
  id_list = book.bookmarks.all().values_list('id')
  # Query for the toys that the cat doesn't have
  # by using the exclude() method vs. the filter() method
  bookmarks_book_doesnt_have = Bookmark.objects.exclude(id__in=id_list)
  reading_form = ReadingForm()
  return render(request, 'books/detail.html', { 
    'book': book, 'reading_form': reading_form, 'bookmarks': bookmarks_book_doesnt_have })

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

class ReadingDelete(DeleteView):
    model = Reading
    success_url = '/books/'

class BookmarkList(ListView):
  model = Bookmark

class BookmarkDetail(DetailView):
  model = Bookmark

class BookmarkCreate(CreateView):
  model = Bookmark
  fields = '__all__'

class BookmarkUpdate(UpdateView):
  model = Bookmark
  fields = ['name', 'color']

class BookmarkDelete(DeleteView):
  model = Bookmark
  success_url = '/bookmarks'

def assoc_bookmark(request, book_id, bookmark_id):
  Book.objects.get(id=book_id).bookmarks.add(bookmark_id)
  return redirect('detail', book_id=book_id)

def unassoc_bookmark(request, book_id, bookmark_id):
  Book.objects.get(id=book_id).bookmarks.remove(bookmark_id)
  return redirect('detail', book_id=book_id)


def some_function(request):
    secret_key = os.environ['SECRET_KEY']

def add_photo(request, book_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        try:
            bucket = os.environ['S3_BUCKET']
            s3.upload_fileobj(photo_file, bucket, key)
            url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
            Photo.objects.create(url=url, book_id=book_id)
        except Exception as e:
            print('An error occurred uploading file to S3')
            print(e)
    return redirect('detail', book_id=book_id)