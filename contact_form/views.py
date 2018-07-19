from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render

from contact_form.forms import PotentialForm


def contact_form(request):
    form = PotentialForm()
    return render(request, 'contact_form/form.html', {'form': form})


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
            return JsonResponse({'satus': 'success'})
        else:
            response = dict(form.errors)
            response['status'] = 400
            return JsonResponse(form.errors)
