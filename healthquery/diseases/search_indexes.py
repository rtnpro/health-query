import datetime
from haystack.indexes import *
from healthquery.diseases.models import Disease

class DiseaseIndex(SearchIndex, Indexable):
    text = CharField(document=True, use_template=True)
    name = CharField(model_attr='name')
    tagsobj = MultiValueField()

    def get_model(self):
        return Disease

    def index_queryset(self):
        return self.get_model().objects.all()

    def prepare(self, obj):
        self.prepared_data = super(DiseaseIndex, self).prepare(obj)
        print self.prepared_data
        return self.prepared_data

    def prepare_tagsobj(self, obj):
        return [tag.name for tag in obj.tagsobj.all()]
