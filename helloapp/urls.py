
from django.urls import path
from .views import BooklistView,BookFilter,Bookannotate,BookValuesListView,Bookvaluesview,AuthorlistView,Bookexcludeview,Bookaggregateview
urlpatterns = [
    path('book/',BooklistView.as_view(),name='book'),
    path('book/filter/<str:title>',BookFilter.as_view(),name='bookfilter'),
    path('book/annotate/',Bookannotate.as_view(),name='bookannotate'),
    path('book/values/',BookValuesListView.as_view(),name='bookvalues'),
    path('book/valueslist/',Bookvaluesview.as_view(),name='bookvalueslist'),
    path('author/',AuthorlistView.as_view(),name='AuthorlistView'),
    path('book/exclude/',Bookexcludeview.as_view(),name='Bookexcludeview'),
    path('book/aggregate/', Bookaggregateview.as_view(),name='Bookaggregateview')



    
]