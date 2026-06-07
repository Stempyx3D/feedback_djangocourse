from . import views
from django.urls import path

urlpatterns = [
    path('', views.ReviewView.as_view(), name='review'),
    path('thank-you/', views.ThankYouView.as_view(), name='thank_you'),
    path('all-reviews', views.AllReviewsView.as_view(), name='all_reviews'),
    path('reviews', views.ReviewListView.as_view(), name='review_list'),
    path('reviews/<int:id>', views.SingleReviewView.as_view(), name='single_review')

]