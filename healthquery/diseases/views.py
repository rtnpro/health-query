from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from healthquery.diseases.forms import DiseaseForm
from healthquery.diseases.models import *
from tagging.models import TaggedItem
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required


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
    else:
        disease_form = DiseaseForm()
    return render_to_response('diseases/disease_form.html',
            {'form': disease_form},
            context_instance=RequestContext(request))


@login_required
def disease_add(request):
    return _create_update_disease(request)


def disease_detail(request, disease_id):
    disease = get_object_or_404(Disease, id=disease_id)
    return render_to_response('diseases/disease_detail.html',
            {'disease': disease},
            context_instance=RequestContext(request))


def ajax_get_remedy_details(request, remedy_id):
    remedy = get_object_or_404(Remedy, id=remedy_id)
    return render_to_response("diseases/ajax_remedy_details.html",
        {'remedy': remedy}, context_instance=RequestContext(request))


def ajax_get_medicine_details(request, medicine_id):
    medicine = get_object_or_404(Medicine, id=medicine_id)
    return render_to_response("diseases/ajax_medicine_details.html",
        {'medicine': medicine}, context_instance=RequestContext(request))