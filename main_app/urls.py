from django.urls import path
from . import views
	
urlpatterns = [
	path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('books/', views.books_index, name='index'),
    path('books/create/', views.BookCreate.as_view(), name='books_create'),
    path('books/<int:pk>/update/', views.BookUpdate.as_view(), name='books_update'),
    path('books/<int:pk>/delete/', views.BookDelete.as_view(), name='books_delete'),
    path('books/<int:book_id>/', views.books_detail, name='detail'),
    path('books/<int:book_id>/add_reading/', views.add_reading, name='add_reading'),
    path('reading/<int:pk>/delete/', views.ReadingDelete.as_view(), name='reading_delete'),
    path('books/<int:book_id>/assoc_bookmark/<int:bookmark_id>/', views.assoc_bookmark, name='assoc_bookmark'),
    path('books/<int:book_id>/unassoc_bookmark/<int:bookmark_id>/', views.unassoc_bookmark, name='unassoc_bookmark'),
    path('bookmarks/', views.BookmarkList.as_view(), name='bookmarks_index'),
    path('bookmarks/<int:pk>/', views.BookmarkDetail.as_view(), name='bookmarks_detail'),
    path('bookmarks/create/', views.BookmarkCreate.as_view(), name='bookmarks_create'),
    path('bookmarks/<int:pk>/update/', views.BookmarkUpdate.as_view(), name='bookmarks_update'),
    path('bookmarks/<int:pk>/delete/', views.BookmarkDelete.as_view(), name='bookmarks_delete'),
    path('books/<int:book_id>/add_photo/', views.add_photo, name='add_photo'),
]
