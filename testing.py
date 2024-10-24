from transformers import Speech2TextProcessor, Speech2TextForConditionalGeneration
import torchaudio
import torch



# Check if CUDA is available
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Running on {device}")

