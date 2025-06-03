import torch
import logging
from .ncdm_model import Net
import os
from django.conf import settings

question_id_to_index = {f"Q{i + 1}": i for i in range(26)}

MODEL_PATH = os.path.join(settings.BASE_DIR, 'my_app', 'ML', 'ncdm_model.pth')
KNOWLEDGE_N = 23  # or dynamically load as needed
EXER_N = 26
STUDENT_N = 619
DEVICE = "cpu"



def load_model(model_path, KNOWLEDGE_N, EXER_N, STUDENT_N, device="cpu"):
    model = Net(knowledge_n=23, exer_n=26, student_n=619)
    model.load_state_dict(torch.load(model_path, map_location=device))
    model.eval()
    return model

# Load the model once
MODEL = load_model(MODEL_PATH, KNOWLEDGE_N, EXER_N, STUDENT_N, DEVICE)

def predict(model, user_id, question_id, knowledge_embedding, device="cpu"):
    print(f"predict function called for user: {user_id}, question: {question_id}")
    # Get the integer index from question ID (e.g., "Q14" -> 13)
    if isinstance(question_id, str) and question_id.startswith('Q'):
        item_id = question_id_to_index.get(question_id)
    else:
        item_id = int(question_id) - 1  # Convert to 0-based index

    if item_id is None or not (0 <= item_id < 26):
        raise ValueError(f"Invalid question_id: {question_id}")

    # Ensure knowledge_embedding is a 1D array or list and convert to tensor
    knowledge_tensor = torch.FloatTensor(knowledge_embedding).to(device)

    # Reshape to (1, knowledge_n)
    knowledge_tensor = knowledge_tensor.reshape(1, -1).float()

    user_tensor = torch.LongTensor([user_id]).to(device)
    item_tensor = torch.LongTensor([item_id]).to(device)

    with torch.no_grad():
        # Get student embedding
        stu_emb = model.student_emb(user_tensor)
        stat_emb = torch.sigmoid(stu_emb)  # Student proficiency vector

        # Forward pass (copied from model.forward)
        k_difficulty = torch.sigmoid(model.k_difficulty(item_tensor))
        e_difficulty = torch.sigmoid(model.e_difficulty(item_tensor))
        input_x = e_difficulty * (stat_emb - k_difficulty) * knowledge_tensor
        input_x = model.drop_1(torch.sigmoid(model.prednet_full1(input_x)))
        input_x = model.drop_2(torch.sigmoid(model.prednet_full2(input_x)))
        output = torch.sigmoid(model.prednet_full3(input_x)).view(-1)

    return output.item(), stat_emb.squeeze().cpu().numpy()