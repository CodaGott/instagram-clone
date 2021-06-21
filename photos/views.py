from django.shortcuts import render

# Create your views here.
from photos.models import PostForm, Photo


def home_page(request):
    if request.method == 'POST':
        print(request.POST)
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = PostForm()

    photos = Photo.objects.order_by('-date_created')
    context = {
        'photos': photos,
        'form': form,
    }
    return render(request, 'home.html', context)
