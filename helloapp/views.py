from django.shortcuts import render
from .serializer import BookSerializer,AuthorSerializer
from .models import Book,Author
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Avg,Case,When,F,Value,CharField,Max,Min

# Create your views here.
#model book
class BooklistView(APIView):
    def get(self,request):
        obj=Book.objects.all()
        serializer=BookSerializer(obj,many=True)
        return Response(serializer.data)

        

    def post(self,request):
        data=request.data
        serializer=BookSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class BookFilter(APIView):
    def get(self,request,title):
        books=Book.objects.filter(title=title)
        serializer=BookSerializer(books,many=True)
        return Response(serializer.data)

        
class Bookannotate(APIView):
    def get(self,request):
        books=Book.objects.annotate(
            disc_price=Case(
                When(price__gt=5000, then=F('title')),
                default=Value('price below 5000'),
                output_field=CharField()
             
            )
        
        )
        data=[{'title':book.title,'disc_price':book.disc_price}
        for book in books]
        return Response({'books':data})
 
    
class Bookvaluesview(APIView):
    def get(self, request):
        books = Book.objects.values('id', 'title', 'price', 'author__firstname', 'author__lastname')
        return Response(books)
    

class BookValuesListView(APIView):
    def get(self, request):
        books = Book.objects.values_list('title', 'price', 'author__firstname', 'author__lastname')
        return Response(books)


class Bookexcludeview(APIView):
    def get(self,request):
        books=Book.objects.exclude(price__gt=5000)
        serializer=BookSerializer(books,many=True)
        return Response(serializer.data)


class Bookaggregateview(APIView):
    def get(self,request):
        stats=Book.objects.aggregate(
            avgprice=Avg('price'),
            maxp=Max('price'),
            minp=Min('price'),
        )
        print(stats)
        return Response(stats)


# class Multiqueryview(APIView):
#     def get(self,request):


#model author related classes and functions
class AuthorlistView(APIView):
    def get(self,request):
        obj=Author.objects.all()
        serializer=AuthorSerializer(obj,many=True)
        return Response(serializer.data)
    
        

    def post(self,request):
        data=request.data
        serializer=AuthorSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)