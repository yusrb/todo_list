from django.urls import path
from .views import(
  BaseListView,
  BaseCreateView,
  BaseUpdateView,
  BaseDeleteView,
  BaseDetailView,
)

urlpatterns = [
    path('' , BaseListView.as_view() , name="index"),
    path('create/' , BaseCreateView.as_view() , name="create"),
    path('update/<int:pk>' , BaseUpdateView.as_view() , name="update"),
    path('delete/<int:pk>' , BaseDeleteView.as_view() , name="delete"),
    path('detail/<int:pk>' , BaseDetailView.as_view() , name="detail"),
]
