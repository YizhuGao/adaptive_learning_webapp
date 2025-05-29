import json
import faiss
from sentence_transformers import SentenceTransformer

_model = None
_faiss_index = None
_video_data = None

def get_chatbot_resources():
    global _model, _faiss_index, _video_data
    if _model is None:
        _model = SentenceTransformer("all-MiniLM-L6-v2")
        _faiss_index = faiss.read_index("video_index.faiss")
        with open("video_metadata.json", "r") as f:
            _video_data = json.load(f)
    return _model, _faiss_index, _video_data

