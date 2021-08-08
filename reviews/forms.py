from django import forms
from . import models

class CreateReviewForm(forms.ModelForm):
  
  text = forms.CharField(widget=forms.Textarea(attrs={'class': "w-full"}))
  rating = forms.IntegerField(min_value=1, max_value=5)
  
  class Meta:
    model = models.Review
    fields = ("text","rating")

  
  def save(self):
    review = super().save(commit=False)
    return review




  