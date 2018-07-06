from django.http import HttpResponseRedirect
from django.shortcuts import render

from contact_form.forms import PotentialForm


def new_potential(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PotentialForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            form.save()
            return HttpResponseRedirect('/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = PotentialForm()

    return render(request, 'contact_form/form.html', {'form': form})
