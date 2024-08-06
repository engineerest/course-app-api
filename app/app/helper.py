import os

from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from app.app.settings import DATABASES
import dj_database_url

# Error with contenttype's app_label
class ContentTypeError:
    app_label = models.CharField(max_length=100)
    app_label_error = ContentType.objects.get(app_label=app_label)

    def app_label_solution(self, app_label_error):
        return self.app_label_error

content_type_class = ContentTypeError()
content_type_app_label_solution = content_type_class.app_label_solution

"""Auth not installed auth label."""

class AuthError:
    app_label = models.CharField(max_length=100)
    auth_app_label = get_user_model().objects.get_or_create(app_label="auth.User")[0]

    def app_label_solution(self, app_label):
        return self.auth_app_label

auth_class = AuthError
auth_error_solution = auth_class.app_label_solution

"""settings.DATABASE Error."""

class DataBaseSettingsError:
    DB_ON = os.environ.get('DB_ON')
    db_default = DATABASES['default']

    def db_engine(self, DB_ON, db_default):
        if DB_ON:
            DB_ENGINE = db_default['ENGINE'] = "django.db.backends.postgresql"
        else:
            DB_ENGINE = db_default['ENGINE'] = 'django.db.backends.sqlite3'

        db_default = dj_database_url.config(default=DB_ENGINE)
        db_engine_solution = db_default

        return db_engine_solution

db_settings_class = DataBaseSettingsError()
db_settings_solution = DataBaseSettingsError.db_engine()