# imports and stuff
import TextProcessors.TextAnalysis as ta
import TextProcessors.TextPartsHandling as ts
import AiProcessors.TextToImages as txtImg
import AiProcessors.TextToSpeeches as txtSpch

# user input
#   user uploads txt file
#   also folder location for final video and other elements

path_to_main_text = "sample_files\Irving_Winkle.pdf"
path_to_usable_folder = "sample_files"

# process text and confirmations
#   analyze the text as a whole to get a summary, other corresponding topics, and overall tone of the text
#   estimate the amount of time the final video will be, amount of images and general file sizes
#   user can edit these to give more or less stuff
#   also give user number of sections, and other information on what was detected

# analysis
full_text = ta.convert_file_to_text(path_to_main_text)
text_summary = ta.get_text_summary(full_text)
text_topic_list = ta.get_text_surrounding_topics(full_text)
text_tone = ta.get_text_tone(full_text)

# estimations
seperated_text = ts.separate_into_parts(full_text)
estimated_time = ts.estimate_reading_time(seperated_text)
estimated_images = ts.estimate_image_count(seperated_text)
estimated_filesize = ts.estimate_filesize(estimated_time, estimated_images)

# user updates
print(round(estimated_time / 60))
print(round(estimated_filesize))
# insert some taking in input here, but rn no

# loop
#   after everything is defined, go through each section and then the loop begins
#   a section is selected and then is converted in multiple ways for the multiple ais contributing to the final
#   the ai of each will output into a folder

for txt in seperated_text:
    txtImg.imageFromSection(txt, path_to_usable_folder)
    txtSpch.speechFromSection(txt, path_to_usable_folder)

# final build
#   loop through the elements in the folder and put together in a video output


if __name__ == "__main__":
    print("This script is being run as the main program.")
else:
    print("This script is being imported as a module.")
