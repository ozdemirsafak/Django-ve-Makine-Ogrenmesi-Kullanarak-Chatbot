from django.apps import AppConfig
from pathlib import Path
from fast_bert.prediction import BertClassificationPredictor

class TodoConfig(AppConfig):
    default_auto_field  = 'django.db.models.BigAutoField'
    name = 'todo'