# Import necessary modules for text processing, AI processing, and progress tracking
import TextProcessors.TextAnalysis as ta
import TextProcessors.TextPartsHandling as ts
import AiProcessors.TextToImages as txtImg
import AiProcessors.TextToSpeeches as txtSpch
import AiProcessors.AssetsToVideo as assV
import tqdm
import os

# Define file paths for the source PDF and the output folder
path_to_main_text = "sample_files\FishStory.pdf"  # Path to the source PDF document
path_to_usable_folder = "sample_files"  # Output folder for processed media and final video

# Analyze the text from the PDF to obtain summary, topics, and tone
# This section performs an initial analysis of the text, breaking down its content to understand its overarching themes, sentiment, and structure
full_text = ta.convert_file_to_text(path_to_main_text)  # Convert the PDF file to a text string
text_summary = ta.get_text_summary(full_text)  # Summarize the text to understand its main points
text_topic_list = ta.get_text_surrounding_topics(full_text)  # Identify the main topics covered in the text
text_tone = ta.get_text_tone(full_text)  # Analyze the tone of the text

# Estimate the resources required for video creation
# Based on the text analysis, estimate the length of the final video, the number of images needed, and the overall file size
seperated_text = ts.separate_into_parts(full_text)  # Split the text into manageable parts for processing
estimated_time_of_final = ts.estimate_reading_time(seperated_text)  # Estimate the total video duration
estimated_images_count = ts.estimate_image_count(seperated_text)  # Estimate the number of images required for the video
estimated_filesize = ts.estimate_filesize(estimated_time_of_final, estimated_images_count)  # Estimate the final video file size

# Display estimated video duration and file size for user review
print(round(estimated_time_of_final / 60), "minutes")  # Print the estimated duration in minutes
print(round(estimated_filesize), "MB")  # Print the estimated file size in megabytes
# Placeholder for user input adjustments (currently not implemented)

# Generate images and audio for each section of text
# Iterates through each text part, generating corresponding images and speech audio files, tracking progress with tqdm
counter_num = 0
for txt in tqdm.tqdm(seperated_text, desc="Generating assets", unit="section"):
    txtImg.makeImageFromSection(txt, path_to_usable_folder, counter_num)  # Create an image for the text section
    txtSpch.makeSpeechFromSection(txt, path_to_usable_folder, counter_num)  # Generate speech audio for the text section
    counter_num += 1

# Compile the generated media into a final video
# Takes the images and audio files generated in the previous step and combines them into the final video output
assV.create_video_from_images_and_audios(path_to_usable_folder, path_to_usable_folder, os.path.join(path_to_usable_folder,"finalVideo.mp4"))

# Main program indicator
if __name__ == "__main__":
    print("This script is being run as the main program.")
else:
    print("This script is being imported as a module.")
