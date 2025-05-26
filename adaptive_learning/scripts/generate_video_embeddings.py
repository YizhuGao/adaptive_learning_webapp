import os
import sys
import django
from sentence_transformers import SentenceTransformer
import numpy as np

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "adaptive_learning.settings")
django.setup()

from my_app.models import VideoModule  # Changed to absolute import

model = SentenceTransformer('all-MiniLM-L6-v2')

def generate_video_embeddings():
    for video in VideoModule.objects.all():
        if not video.embedding:
            try:
                emb = model.encode(video.description)
                video.embedding = np.asarray(emb, dtype=np.float32).tobytes()
                video.save()
                print(f"Processed video: {video.video_module_id}")
            except Exception as e:
                print(f"Error processing video {video.video_module_id}: {e}")

if __name__ == "__main__":
    generate_video_embeddings()