from urllib.parse import urlencode

from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse

from .forms import ReviewForm
from .models import Review

def review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)

        if form.is_valid():
            review = Review(user_name=form.cleaned_data['user_name'],
                            review_text=form.cleaned_data['review_text'],
                            rating=form.cleaned_data['rating'])
            review.save()
            print(form.cleaned_data)
            return redirect(f"{reverse('thank_you')}?{urlencode({'user_name': review.user_name})}")
    else:
        form = ReviewForm()
    return render(request, 'reviews/review.html', {"form": form})

def thank_you(request):
    get_request = request.GET
    user_name = get_request.get('user_name')
    return render(request, 'reviews/thank_you.html', {"user_name": user_name})
