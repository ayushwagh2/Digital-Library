from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    AddCategoryView,
    
)
from . import views


urlpatterns = [
    
    

    path('homepage', PostListView.as_view(), name='helpme-home2'),#this is to view all the post using class based view

    path('', views.home, name='blog-home'),

    path('category/add', AddCategoryView.as_view(), name='add-category'),#this is to add a category 

    path('document/<int:pk>/', PostDetailView.as_view(), name='post-detail'),#this is the detail of the post view using a class based view
     
    path('Pdfupload/',PostCreateView.as_view() , name='documentupload'),#To upload a Document

    path('document/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),#to update a document
    
    path('document/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='blog-about'),

    #TUtorial for categroy for taklya
    path('category/<str:cats>', views.Categoryview, name='category'),
    path('category-list/',views.CategoryListview, name='category-list'),
     

    #veryAcademy
    path('profile/favourite', views.favourite_list, name='favourite_list'),
    path('fav/<int:id>/', views.favourite_add, name='favourite_add'),
    
    #search

    path('search', views.search , name='search'),
    #fitler ke liye URL
    path('filter', views.new_view , name='filter-view'),


    
    #trying the Post by me section
    path('mypost/', views.userpost , name='userpost'),

    #links according to the category
    path('filterEbooks', views.E_books , name='filter-E_books'),
    path('filterFiction', views.Fiction , name='filter-Fiction'),
    path('filterNon_Fiction', views.Non_Fiction , name='filter-Non_Fiction'),
    path('filterQuestionpaper', views.Questionpaper , name='filter-Questionpaper'),
    path('filterNotes', views.Notes, name='filter-Notes'),

    #links according to the Stream
    path('filterScience', views.Science, name='filter-Science'),
    path('filterArts', views.Arts, name='filter-Arts'),
    path('filterCommerce', views.Commerce, name='filter-Commerce'),

    #-----------------Contact-----------
    path('Contact', views.user_info, name='user_info'),

]

