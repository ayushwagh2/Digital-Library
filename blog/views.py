from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Document2, Category2, Stream
from django.views.decorators.csrf import csrf_exempt

from django.contrib.auth.decorators import login_required
from django.contrib import messages
#from .forms import Pdfuploadform
from .filters import Document2Filter,Document2Filter1, Document2Filter4
 
def home(request):
     
     
   
    return render(request, 'blog/nicepage.html',  ) 
  

def Science(request):
    first_category = Stream.objects.get(name='Science')
    document2 = Document2.objects.filter(stream=first_category)
    document2_filter = Document2Filter4(request.GET, queryset=document2)

    filtered_documents = document2_filter.qs.filter(stream=first_category)

    context = {}
    if filtered_documents.exists():
        # add the filtered queryset to the context dictionary
        context['document2_filter'] = document2_filter
    else:
        # print a statement when no objects of the filtered category exist
        print("No documents found for category 'Science'")
        # add an empty queryset to the context dictionary
        context['document2_filter'] = Document2.objects.none()

    return render(request, "blog/Science.html", context)


def Commerce(request):
    first_category = Stream.objects.get(name='Commerce')
    document2 = Document2.objects.filter(stream=first_category)
    document2_filter = Document2Filter4(request.GET, queryset=document2)

    filtered_documents = document2_filter.qs.filter(stream=first_category)

    context = {}
    if filtered_documents.exists():
        # add the filtered queryset to the context dictionary
        context['document2_filter'] = document2_filter
    else:
        # print a statement when no objects of the filtered category exist
        print("No documents found for category 'Science'")
        # add an empty queryset to the context dictionary
        context['document2_filter'] = Document2.objects.none()

    return render(request, "blog/Commerce.html", context)


def Arts(request):
    first_category = Stream.objects.get(name='Arts')
    document2 = Document2.objects.filter(stream=first_category)
    document2_filter = Document2Filter4(request.GET, queryset=document2)

    filtered_documents = document2_filter.qs.filter(stream=first_category)

    context = {}
    if filtered_documents.exists():
        # add the filtered queryset to the context dictionary
        context['document2_filter'] = document2_filter
    else:
        # print a statement when no objects of the filtered category exist
        print("No documents found for category Arts")
        # add an empty queryset to the context dictionary
        context['document2_filter'] = Document2.objects.none()

    return render(request, "blog/Arts.html", context)

def Non_Fiction(request):
    first_category = Category2.objects.get(name='Non_Fiction')
    document2 = Document2.objects.filter(category=first_category)
    document2_filter = Document2Filter4(request.GET, queryset=document2)

    filtered_documents = document2_filter.qs.filter(category=first_category)

    context = {}
    if filtered_documents.exists():
        # add the filtered queryset to the context dictionary
        context['document2_filter'] = document2_filter
    else:
        # print a statement when no objects of the filtered category exist
        print("No documents found for category 'Science'")
        # add an empty queryset to the context dictionary
        context['document2_filter'] = Document2.objects.none()

    return render(request, "blog/Non_fiction.html", context)

def Questionpaper(request):
    first_category = Category2.objects.get(name='Questionpapers')
    document2 = Document2.objects.filter(category=first_category)
    document2_filter = Document2Filter4(request.GET, queryset=document2)

    filtered_documents = document2_filter.qs.filter(category=first_category)

    context = {}
    if filtered_documents.exists():
        # add the filtered queryset to the context dictionary
        context['document2_filter'] = document2_filter
    else:
        # print a statement when no objects of the filtered category exist
        print("No documents found for category 'Science'")
        # add an empty queryset to the context dictionary
        context['document2_filter'] = Document2.objects.none()

    return render(request, "blog/Questionpaper.html", context)

def Notes(request):
    first_category = Category2.objects.get(name='Notes')
    document2 = Document2.objects.filter(category=first_category)
    document2_filter = Document2Filter4(request.GET, queryset=document2)

    filtered_documents = document2_filter.qs.filter(category=first_category)

    context = {}
    if filtered_documents.exists():
        # add the filtered queryset to the context dictionary
        context['document2_filter'] = document2_filter
    else:
        # print a statement when no objects of the filtered category exist
        print("No documents found for category 'Science'")
        # add an empty queryset to the context dictionary
        context['document2_filter'] = Document2.objects.none()

    return render(request, "blog/Notes.html", context)
def Fiction(request):
    first_category = Category2.objects.get(name='Fiction')
    document2 = Document2.objects.filter(category=first_category)
    document2_filter = Document2Filter4(request.GET, queryset=document2)

    filtered_documents = document2_filter.qs.filter(category=first_category)

    context = {}
    if filtered_documents.exists():
        # add the filtered queryset to the context dictionary
        context['document2_filter'] = document2_filter
    else:
        # print a statement when no objects of the filtered category exist
        print("No documents found for category 'Science'")
        # add an empty queryset to the context dictionary
        context['document2_filter'] = Document2.objects.none()

    return render(request, "blog/Fiction.html", context)
 
def E_books(request):
    first_category = Category2.objects.get(name='E_books')
    document2 = Document2.objects.filter(category=first_category)
    document2_filter = Document2Filter4(request.GET, queryset=document2)

    filtered_documents = document2_filter.qs.filter(category=first_category)

    context = {}
    if filtered_documents.exists():
        # add the filtered queryset to the context dictionary
        context['document2_filter'] = document2_filter
    else:
        # print a statement when no objects of the filtered category exist
        print("No documents found for category 'Science'")
        # add an empty queryset to the context dictionary
        context['document2_filter'] = Document2.objects.none()

    return render(request, "blog/E_books.html", context)
  
def new_view(request):
    document2 = Document2.objects.all()
    document2_filter = Document2Filter(request.GET, queryset=document2)
    context = {
        'document2_filter': document2_filter
    }
    return render(request, "blog/filter.html", context)
 
class PostListView(ListView):
    model = Document2
    template_name = 'blog/home.html '  # <app>/<model>_<viewtype>.html
    context_object_name = 'documents'
    ordering = ['-date_posted']

    # this is takle ka tutorial and he is using a class inside this calss based 
    def get_context_data(self, *args, **kwargs):
        cat_menu = Category2.objects.all()
        context = super(PostListView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context
 

from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy   
from .forms import YourModelForm

class PostCreateView(CreateView):
    model = Document2
    form_class = YourModelForm
    template_name = 'blog/pdfupload.html'
    
    success_url = reverse_lazy('blog-home') 


class PostDetailView(DetailView):
    model = Document2
    template_name = 'blog/document2_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Get the category of the document
        category = context['object'].category

        # Retrieve other documents with the same category
        recommended_documents = Document2.objects.filter(category=category)

        # Exclude the current document from the recommended documents
        recommended_documents = recommended_documents.exclude(id=context['object'].id)

        context['recommended_documents'] = recommended_documents
        return context

#this right here (PostUpdateView) is working idk how but it is and it is using html template called document_form.html i guess
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Document2
    fields = ['description', 'pdf', 'category', 'stream', 'year', 'course' ]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Document2
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
 
def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
 
 

#this is adding a category form that takle ka tutorial
from .models import Category2
class AddCategoryView(CreateView):
    model = Category2
    template_name = 'blog/add_category.html'
    fields = '__all__'


def Categoryview(request, cats):
    # category_Posts = Document2.objects.filter(category_id=cats)
    category_posts = Document2.objects.filter(category=cats)
    return render(request, 'blog/categories.html', {'cats':cats})

def CategoryListview(request):
    cat_menu_List = Category2.objects.all()
    return render(request, 'blog/category_List.html', {'cat_menu_List': cat_menu_List})

from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
#------------------------------------------this is using veryAcademy youtube tutorial-----------------------------------------------------------------------------------------------------------
@login_required
def favourite_add(request, id):
    document = get_object_or_404(Document2, id=id)
    if document.favourites.filter(id=request.user.id).exists():
        document.favourites.remove(request.user)
    else:
        document.favourites.add(request.user)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

 

@login_required
def favourite_list(request):
    new = Document2.objects.all().filter(favourites=request.user)
    return render(request,
        'users/favourites.html',
        {'new' : new})

def search(request):
    model = Document2
    query = request.GET['query']
    documents = Document2.objects.filter(description__icontains=query)


    params = { 'documents' : documents }
    
    return render(request, 'blog/search.html', params  )




 #this is trying to get all Post done by one user
def userpost(request):
    user = request.user
    user_posts = Document2.objects.filter(author=request.user).order_by('-date_posted')
    template = 'blog/userpost.html'
    return render(request, template, {'user_posts':user_posts,'user': user})


# ------------------------------------------------------RECOMMENDATON VIEWW---------------------------------------------------------------------------------------







#------------------------------------------FOR contact FOrm--------------
from django.shortcuts import render
from .forms import UserInfoForm
from .models import UserInfo

def user_info(request):
    form = UserInfoForm()
    if request.method == 'POST':
        form = UserInfoForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            # Create a new instance of the UserInfo model and save it to the database
            user_info = UserInfo(name=name, email=email, phone_number=phone_number)
            user_info.save()
            # Render a success page
            return render(request, 'blog/nicepage.html')
    return render(request, 'blog/user_info.html', {'form': form})
