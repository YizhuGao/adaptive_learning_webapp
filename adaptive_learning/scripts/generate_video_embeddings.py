# scripts/generate_video_embeddings.py

from sentence_transformers import SentenceTransformer
import numpy as np
from yourapp.models import VideoModule

model = SentenceTransformer('all-MiniLM-L6-v2')

def generate_video_embeddings():
    for video in VideoModule.objects.all():
        if not video.embedding:
            emb = model.encode(video.description)
            video.embedding = np.asarray(emb, dtype=np.float32).tobytes()
            video.save()
