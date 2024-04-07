import torch
from diffusers import StableDiffusionPipeline, AutoencoderKL
import random
import logging
import string
import os
import re

# Suppress progress bars by setting logging level
logging.basicConfig(level=logging.ERROR)

def clean_section(text):
    # Remove URLs
    text = re.sub(r'http[s]?://\S+', '', text)
    
    # Replace email addresses with a generic placeholder or remove
    text = re.sub(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', '[email]', text)
    
    # Remove or replace HTML tags
    text = re.sub(r'<[^>]+>', '', text)
    
    # Optional: Remove Markdown links - [text](URL)
    text = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', text)
    
    # Remove special characters, keeping those that might be relevant to speech
    text = re.sub(r'[^a-zA-Z0-9,.!?;:\'"\s]', '', text)
    
    # Replace multiple spaces with a single space
    text = re.sub(r'\s+', ' ', text).strip()
    
    return text

def count_children_in_folder(folder_path):
    try:
        # List all entries in the folder
        entries = os.listdir(folder_path)
        # Return the count of entries
        return len(entries)
    except FileNotFoundError:
        return "The folder was not found."
    except PermissionError:
        return "Permission denied to access the folder."

def truncate_string_randomly(input_string):
    # List of common words to remove
    max_token_count = 40
    common_words = set([
        "the", "at", "there", "some", "my", "of", "be", "use", "her", "than", "and", "this", "an", "would",
        "first", "a", "have", "each", "make", "to", "from", "which", "like", "been", "in", "or", 
        "she", "him", "call", "is", "one", "do", "into", "who", "you", "had", "how", "time", "that", 
        "by", "their", "has", "its", "it", "word", "if", "look", "now", "he", "but", "will", "two", "find", 
        "was", "not", "up", "more", "long", "for", "what", "other", "write", "down", "on", "all", "about", 
        "go", "are", "were", "out", "see", "did", "as", "we", "many", "number", "get", "with", "when", 
        "then", "no", "come", "his", "your", "them", "way", "made", "they", "can", "these", "could", "may", 
        "I", "said", "so", "part", "however", "still", "been", "without", "only", "also", "further", "extensive",
        "extensively", "demonstrated", "proposed", "leverage", "measure", "guide", "novel", "significantly",
        "achieves", "outperforms", "utilization", "activation", "phenomenon", "attribute", "mechanism",
        "challenge", "challenging", "concept", "alignment", "misalignment", "issue", "problem", "strategy",
        "model", "models", "data", "performance", "benchmarks", "experiments", "reason", "cause", "due",
        "owing", "because", "thus", "therefore", "hence", "consequently", "align", "aligned", "aligning",
        "generating", "generation", "generated"
    ])

    # Split the input string into tokens (words)
    tokens = input_string.split()
    
    # Filter out common words and remove punctuation
    filtered_tokens = [token.lower().strip(string.punctuation) for token in tokens if token.lower().strip(string.punctuation) not in common_words]
    
    # If filtering common words and removing punctuation is not enough, shuffle and then truncate further
    if len(filtered_tokens) > max_token_count:
        random.shuffle(filtered_tokens)
        filtered_tokens = filtered_tokens[:max_token_count]
    
    # Reconstruct the string from the remaining tokens
    truncated_string = ' '.join(filtered_tokens)
    
    return truncated_string

# You can test the function with any string you like by calling it as follows:
# print(truncate_string_randomly("Your input string here."))

def create_image(inputprompt, outputPath = "", imagenum = 0):
    with torch.no_grad():
        repo = "StableDiffusion/sdxs-512-0.9"
        seed = 42
        weight_type = torch.float32  # or float16

        # Load model.
        pipe = StableDiffusionPipeline.from_pretrained(repo, torch_dtype=weight_type)

        prompt = inputprompt

        # Ensure using 1 inference step and CFG set to 0.
        image = pipe(
            prompt,
            num_inference_steps=1,
            guidance_scale=0,
            generator=torch.Generator(device="cpu").manual_seed(seed)
        ).images[0]
        rnumber = random.randint(100, 999)
        outputName = outputPath + "/" + "IMAGE" + "_" + str(imagenum) + "_" + str(rnumber) + ".png"
        image.save(outputName)

def makeImageFromSection(txt_section, output_folder, counter = 0, promts_to_add = "high quality, best quality, extremly detailed"):
    new_txt = clean_section(txt_section)
    truncated_text = truncate_string_randomly(new_txt)
    promptsAdded = promts_to_add + truncated_text
    create_image(promptsAdded, output_folder, counter)
