import django_filters
from .models import Document2

class Document2Filter(django_filters.FilterSet):

    class Meta:
        model = Document2
        fields = {'stream' : ['exact'], 'year' :  ['exact'], 'course':  ['exact'], 'category':  ['exact']}


class Document2Filter1(django_filters.FilterSet):

    class Meta:
        model = Document2
        fields = {'stream' : ['exact'], 'year' :  ['exact'], 'course':  ['exact'],}

class Document2Filter2(django_filters.FilterSet):

    class Meta:
        model = Document2
        fields = {'stream' : ['exact'], 'year' :  ['exact'], 'course':  ['exact'],}

        
class Document2Filter3(django_filters.FilterSet):

    class Meta:
        model = Document2
        fields = {'stream' : ['exact'], 'year' :  ['exact'], 'course':  ['exact'],}
        

class Document2Filter4(django_filters.FilterSet):

    class Meta:
        model = Document2
        fields = {'category':  ['exact'], 'year' :  ['exact'], 'course':  ['exact'],}

