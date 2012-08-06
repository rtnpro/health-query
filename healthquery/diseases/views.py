from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from healthquery.diseases.forms import DiseaseForm
from healthquery.diseases.models import *
from tagging.models import TaggedItem
from django.views.decorators.csrf import csrf_exempt


def _create_update_disease(request, disease_id=None):
    if disease_id is not None:
        disease = Disease.objects.get(id=disease_id)
    else:
        disease = None
    if request.method == "POST":
        disease_form = DiseaseForm(request.POST, instance=disease)
        if disease_form.is_valid():
            disease = disease_form.save()
            return HttpResponseRedirect(reverse('disease_detail',
                args=[disease.id]))
    form = DiseaseForm()
    return render_to_response('diseases/disease_form.html',
            {'form': form},
            context_instance=RequestContext(request))


def disease_add(request):
    return _create_update_disease(request)


def disease_detail(request, disease_id):
    disease = get_object_or_404(Disease, id=disease_id)
    return render_to_response('diseases/disease_detail.html',
            {'disease': disease},
            context_instance=RequestContext(request))
