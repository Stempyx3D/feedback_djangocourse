from urllib.parse import urlencode

from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, TemplateView


from .forms import ReviewForm
from .models import Review

class ReviewView(View):
    def get(self, request):
        form = ReviewForm()
        return render(request, 'reviews/review.html', {"form": form})

    def post(self, request):
        form = ReviewForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect(f"{reverse('thank_you')}?{urlencode({'user_name': form.cleaned_data['user_name']})}")
        return render(request, 'reviews/review.html', {"form": form})

class ThankYouView(View):
    def get(self, request):
        user_name = request.GET.get('user_name')
        return render(request, 'reviews/thank_you.html', {"user_name": user_name})
    
class AllReviewsView(View):
    def get(self, request):
        reviews = Review.objects.all()
        return render(request, 'reviews/all_reviews.html', {"reviews": reviews})
    
class ReviewListView(ListView):
    template_name = 'reviews/review_list.html'
    model = Review
    context_object_name = 'reviews'

    def get_queryset(self):
        base_query = super().get_queryset()
        data = base_query.filter(rating__gt=3)
        return {'data': data, 'base_query': base_query}

class SingleReviewView(TemplateView):
    template_name = 'reviews/single_review.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        review_id = kwargs['id']
        context['review'] = Review.objects.get(pk=review_id)
        return context

# def review(request):
#     if request.method == 'POST':
#         form = ReviewForm(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data)
#             form.save()
#             return redirect(f"{reverse('thank_you')}?{urlencode({'user_name': review.user_name})}")
#     else:
#         form = ReviewForm()
#     return render(request, 'reviews/review.html', {"form": form})


# def thank_you(request):
#     get_request = request.GET
#     user_name = get_request.get('user_name')
#     return render(request, 'reviews/thank_you.html', {"user_name": user_name})
