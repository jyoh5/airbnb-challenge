from django.contrib import messages
from django.shortcuts import redirect, reverse
from movies.models import Movie
from books.models import Book
from reviews import forms
from reviews.models import Review

# Create your views here.
def create_review(request, pk):
  if request.user.is_authenticated:
    if request.method == "POST":
      form = forms.CreateReviewForm(request.POST)
      param_type = request.GET.get("type")

      if param_type == "movie":
        movie = Movie.objects.get(pk=pk)
        if movie is None:
          return redirect(reverse("core:home"))
        if form.is_valid():
          review = form.save()
          review.movie = movie
          review.created_by = request.user
          review.save()
          messages.success(request, "Movie reviewed")
          return redirect(reverse("movies:movie", kwargs={"pk": movie.pk}))
        else:
          return redirect(reverse("movies:movie", kwargs={"pk": movie.pk}))
      elif param_type == "book":
        book = Book.objects.get(pk=pk)
        if book is None:
          return redirect(reverse("core:home"))
        if form.is_valid():
          review = form.save()
          review.book = book
          review.created_by = request.user
          review.save()
          messages.success(request, "Book reviewed")
          return redirect(reverse("books:book", kwargs={"pk": book.pk}))
        else:
          return redirect(reverse("books:book", kwargs={"pk": book.pk}))
  else:
    return redirect(reverse("users:login"))
    
def delete_review(request, pk):
  if request.user.is_authenticated:
    if request.method == "GET":
      review = Review.objects.get(pk=pk)
      if review.created_by == request.user:
        review.delete()
  param_type = request.GET.get("type")
  param_pk = request.GET.get("pk")
  if param_type == "movie":
    return redirect(reverse("movies:movie", kwargs={"pk": param_pk}))
  elif param_type == "book":
    return redirect(reverse("books:book", kwargs={"pk": param_pk}))
    