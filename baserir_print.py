import os
from pathlib import Path

# Set up the Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'langchain_website.settings')

import django
django.setup()

from django.conf import settings

print("BASE_DIR:", settings.BASE_DIR)