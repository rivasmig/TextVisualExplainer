import pyttsx3
import os
import random
import re
import wave

def verify_audio(file_path):
    try:
        # Open the WAV file and get its properties
        with wave.open(file_path, 'rb') as wav_file:
            frames = wav_file.getnframes()
            rate = wav_file.getframerate()
            duration = frames / float(rate)
            
            # Check if the audio length is greater than 0
            if duration > 0:
                print(f"Audio file is valid with duration: {duration} seconds.")
                return True
            else:
                raise ValueError("Audio file duration is 0.")
    except Exception as e:
        print(f"Error verifying audio file: {e}")
        # If the file is invalid or an error occurred, delete the original file
        if os.path.exists(file_path):
            os.remove(file_path)
        
        # Generate a new audio file with "Audio error" message
        engine = pyttsx3.init()
        engine.save_to_file("Audio error", file_path)
        engine.runAndWait()
        print("Replaced with an 'Audio error' message.")
        return False

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

def text_to_speech(text, outputPath="", imagenum=0):
    # Initialize the text-to-speech engine
    engine = pyttsx3.init()
    
    # Ensure the folder exists
    if not os.path.exists(outputPath):
        os.makedirs(outputPath)
    
    # Define the path for the WAV file
    rnumber = random.randint(100, 999)
    wav_file_path = os.path.join(outputPath, f"AUDIO_{imagenum}_{rnumber}.wav")
    
    # Save speech to a file
    engine.save_to_file(text, wav_file_path)
    
    # Block while processing all the currently queued commands
    engine.runAndWait()
    
    # Verify the generated audio file, and handle it if there's an error
    verify_audio(wav_file_path)
    
    return wav_file_path

def makeSpeechFromSection(txt_section, output_folder, counter = 0):
    text_to_speech(txt_section, output_folder, counter)