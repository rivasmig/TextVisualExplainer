import re
import random

def separate_into_parts(text, split_type=0, max_difference=1000, minimum_parts=3):
    # Define the splitting strategy based on split_type
    if split_type == 0:
        parts = text.split('\n\n')  # Split by double newline (paragraphs)
    elif split_type == 1:
        parts = text.split('\n')  # Split by any newline
    elif split_type == 2:
        # Split by sentence-ending punctuation
        parts = re.split(r'(?<=[.!?]) +', text)
    elif split_type == 3:
        # Split by colons and semi-colons
        parts = re.split(r'(?<=[;:]) +', text)
    else:
        raise ValueError("Invalid split_type provided. Must be between 0 and 3.")
    
    # Remove empty parts and strip whitespace
    parts = [part.strip() for part in parts if part.strip() != '']
    
    # Correctly compare lengths of parts to ensure they are within the max_difference
    if len(parts) < minimum_parts or (len(max(parts, key=len)) - len(min(parts, key=len)) > max_difference):
        # The error was here; it's now corrected to compare the lengths of strings
        longest_part_index = parts.index(max(parts, key=len))
        if split_type < 3:
            further_split_parts = separate_into_parts(parts[longest_part_index], split_type + 1, max_difference, minimum_parts)
            parts.pop(longest_part_index)  # Remove the original longest part
            parts.extend(further_split_parts)  # Add the further split parts
        else:
            # If at max split_type, split the longest part by half
            half_index = len(parts[longest_part_index]) // 2
            parts[longest_part_index:longest_part_index+1] = [parts[longest_part_index][:half_index], parts[longest_part_index][half_index:]]

    # Re-check if adjustments have caused the parts to meet the criteria
    if len(parts) < minimum_parts or (len(max(parts, key=len)) - len(min(parts, key=len)) > max_difference):
        # If not, attempt a different strategy by splitting all parts evenly if possible
        all_text = " ".join(parts)
        avg_length = len(all_text) // minimum_parts
        parts = [all_text[i:i+avg_length] for i in range(0, len(all_text), avg_length)]

    return parts

def estimate_reading_time(parts):
    words_per_minute = 165
    seconds_per_word = 60 / words_per_minute
    
    total_time_seconds = 0
    
    # Calculate time for words
    for part in parts:
        word_count = len(re.findall(r'\w+', part))
        total_time_seconds += word_count * seconds_per_word
        
    # Calculate time for breaks between parts
    total_time_seconds += sum(random.uniform(0.2, 1) for _ in parts)
    
    # Calculate time for punctuation in the entire body of text
    punctuation_count = len(re.findall(r'[.!?;:]', ' '.join(parts)))
    total_time_seconds += sum(random.uniform(0.1, 0.3) for _ in range(punctuation_count))
    
    return total_time_seconds

def estimate_image_count(parts):
    return len(parts)

def estimate_filesize(speaking_seconds: float, number_of_pictures: float) -> float:
    """
    Estimate the total file size of audio and pictures for a slideshow.
    
    Parameters:
    - speaking_seconds: The total seconds of speaking as a float.
    - number_of_pictures: The total number of pictures in the slideshow as a float.
    
    Returns:
    - The total estimated file size in megabytes (MB) as a float.
    """
    # Average file sizes
    average_audio_filesize_per_minute_MB = 0.5  # in MB
    average_picture_filesize_MB = 30 / 1024  # converting KB to MB
    
    # Calculating total file sizes
    total_audio_filesize_MB = (speaking_seconds / 60) * average_audio_filesize_per_minute_MB
    total_picture_filesize_MB = number_of_pictures * average_picture_filesize_MB
    
    # Total estimated file size
    total_filesize_MB = total_audio_filesize_MB + total_picture_filesize_MB
    
    return total_filesize_MB
