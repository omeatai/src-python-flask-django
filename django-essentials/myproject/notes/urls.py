from django.urls import path
from . import views

urlpatterns = [
    # path('notes', views.list),
    path('notes', views.NotesListView.as_view(), name='notes-list'),
    # path('notes/<int:pk>', views.detail),
    path('notes/<int:pk>', views.NotesDetailView.as_view(),
         name='notes-detail-list'),
    path('notes/create', views.NotesCreateView.as_view(), name='notes-create'),
]
