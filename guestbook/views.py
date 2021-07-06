from django.shortcuts import render, redirect

from .forms import GuestbookForm
# Create your views here.
def guestbookcreate(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = GuestbookForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return redirect('list')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = GuestbookForm()

    return render(request, 'guestbook.html', {'form': form})