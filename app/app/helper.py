
from django.db import models
from django.contrib.contenttypes.models import ContentType

# Error with contenttype's app_label
class ContentTypeError(object):
    app_label = models.CharField(max_length=100)
    app_label_error = ContentType.objects.get(app_label=app_label)

    def app_label_solution(self, app_label_error):
        return self.app_label_error

content_type_class = ContentTypeError()
content_type_app_label_solution = content_type_class.app_label_solution