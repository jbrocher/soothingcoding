from django.http import HttpResponseRedirect, JsonResponse, HttpResponseNotFound
from django.shortcuts import render

from contact_form.forms import PotentialForm
import logging

logger = logging.getLogger('django')

def contact_form(request):
    form = PotentialForm()
    return render(request, 'contact_form/form.html', {'form': form})


def new_potential(request):
    # if this is a POST request we need to process the form data
    try:
        if request.method == 'POST':
            # create a form instance and populate it with data from the request:
            form = PotentialForm(request.POST)
            # check whether it's valid:
            if form.is_valid():
                logger.info('Valid potential form submitted')
                # process the data in form.cleaned_data as required
                # ...
                # redirect to a new URL:
                form.save()
                logger.info('New potential registered')
                return JsonResponse({'satus': 'success'})
            else:
                logger.warning('Invalid potential form submitted')
                response = dict(form.errors)
                response['status'] = 400
                return JsonResponse(form.errors)
        else:
            return HttpResponseNotFound('<h1> Page not foudn </h1>')

    except Exception as e:
        logger.exception("Unexpected exception" + e)
    raise
