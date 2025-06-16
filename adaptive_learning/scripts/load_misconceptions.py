import json
import os
import sys
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "adaptive_learning.settings")
django.setup()

from django.conf import settings
from my_app.models import Misconception  # Replace with your actual app name

def load_misconceptions_from_json():
    json_path = os.path.join(settings.BASE_DIR, 'scripts', 'misconceptions.json')
    with open(json_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        for item in data:
            Misconception.objects.update_or_create(
                misconception_id=item['misconception_id'],
                defaults={'name': item['name']}
            )
    print("✅ Misconceptions loaded successfully.")

# Optional: Run when the script is executed directly
if __name__ == "__main__":
    load_misconceptions_from_json()
