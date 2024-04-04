import torch
from diffusers import StableDiffusionPipeline, AutoencoderKL
import random

repo = "StableDiffusion/sdxs-512-0.9"
seed = 42
weight_type = torch.float32  # or float16

# Load model.
pipe = StableDiffusionPipeline.from_pretrained(repo, torch_dtype=weight_type)

prompt = "a dog eating an apple"

# Ensure using 1 inference step and CFG set to 0.
image = pipe(
    prompt,
    num_inference_steps=1,
    guidance_scale=0,
    generator=torch.Generator(device="cpu").manual_seed(seed)
).images[0]

image.save("output.png")

def truncate_string_randomly(input_string):
    # List of common words to remove
    common_words = set([
        "the", "at", "there", "some", "my", "of", "be", "use", "her", "than", "and", "this", "an", "would",
        "first", "a", "have", "each", "make", "water", "to", "from", "which", "like", "been", "in", "or", 
        "she", "him", "call", "is", "one", "do", "into", "who", "you", "had", "how", "time", "oil", "that", 
        "by", "their", "has", "its", "it", "word", "if", "look", "now", "he", "but", "will", "two", "find", 
        "was", "not", "up", "more", "long", "for", "what", "other", "write", "down", "on", "all", "about", 
        "go", "day", "are", "were", "out", "see", "did", "as", "we", "many", "number", "get", "with", "when", 
        "then", "no", "come", "his", "your", "them", "way", "made", "they", "can", "these", "could", "may", 
        "I", "said", "so", "part"
    ])
    
    # Split the input string into tokens (words)
    tokens = input_string.split()
    
    # Filter out common words if it helps to reduce the size to less than or equal to 77 tokens
    filtered_tokens = [token for token in tokens if token.lower() not in common_words]
    
    # If filtering common words is not enough, shuffle and then truncate further
    if len(filtered_tokens) > 77:
        random.shuffle(filtered_tokens)
        filtered_tokens = filtered_tokens[:77]
    
    # Reconstruct the string from the remaining tokens
    truncated_string = ' '.join(filtered_tokens)
    
    return truncated_string

# You can test the function with any string you like by calling it as follows:
# print(truncate_string_randomly("Your input string here."))


def imageFromSection (txt_section, output_folder):
    pass

