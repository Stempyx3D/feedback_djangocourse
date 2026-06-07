from django import forms
from .models import Review


# class ReviewForm(forms.Form):
#     user_name = forms.CharField(label='Your Name', required=True, max_length=100, error_messages={
#         "required": "Your name must not be empty",
#         "max_length": "Please enter a shorter name!"
#     })
#     review_text = forms.CharField(label="Your Feedback", widget=forms.Textarea, max_length=200)
#     rating = forms.IntegerField(label="Your Rating", min_value=1, max_value=5)

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = "__all__"
        widgets= {
            "rating": forms.NumberInput(attrs={"min":1, "max":5})
        }
        labels = {
            "user_name": "Your Name",
            "review_text": "Your Feedback",
            "rating": "Your Rating"
        }
        error_messages = {
            "user_name": {
                "required": "Type in your name, it's required",
                "max_length": "Please, write a shorter name"
            },
            "rating":{
                "min_value":"Minimum rating is 1",
                "max_value":"Maximum rating is 5"
            }
        }
    def rating_check(self):
        rating = self.cleaned_data["rating"]
        return max(1, min(5, rating))










