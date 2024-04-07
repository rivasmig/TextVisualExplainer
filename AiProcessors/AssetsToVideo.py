# AssetsToVideo.py
import os
import re
from moviepy.editor import ImageClip, concatenate_videoclips, AudioFileClip

def create_video_from_images_and_audios(image_folder, audio_folder, output_path):
    """
    Creates an MP4 video from images and corresponding audio files, matching them by the image and audio numbers.

    :param image_folder: The folder containing the images.
    :param audio_folder: The folder containing the audio files.
    :param output_path: The path to save the final video.
    """
    clips = []
    # Get a list of image files
    image_files = sorted([f for f in os.listdir(image_folder) if f.lower().endswith('.png')])
    for image_file in image_files:
        # Extract the sequence number from the image file name
        match = re.search(r'IMAGE_(\d+)_\d+.png', image_file)
        if not match:
            continue  # Skip files that don't match the pattern
        sequence_num = match.group(1)
        
        # Find the corresponding audio file
        audio_file_pattern = re.compile(r'AUDIO_' + re.escape(sequence_num) + r'_\d+.wav')
        audio_files = [f for f in os.listdir(audio_folder) if audio_file_pattern.match(f)]
        
        if not audio_files:
            continue  # Skip if no corresponding audio file is found
        
        audio_file = audio_files[0]  # Assuming there's only one matching audio file
        
        # Create the ImageClip and set its duration to the duration of the audio
        image_path = os.path.join(image_folder, image_file)
        audio_path = os.path.join(audio_folder, audio_file)
        audio_clip = AudioFileClip(audio_path)
        img_clip = ImageClip(image_path).set_duration(audio_clip.duration).set_audio(audio_clip)
        
        clips.append(img_clip)
    
    if clips:
        # Concatenate all ImageClips into one video
        final_clip = concatenate_videoclips(clips, method="compose")
        # Write the result to a file
        final_clip.write_videofile(output_path, fps=24, codec='libx264')
        # print(f"Video created successfully at {output_path}")
    else:
        pass
        # print("No matching image-audio pairs were found.")

if __name__ == "__main__":
    # Example usage
    image_folder = "path/to/images"
    audio_folder = "path/to/audios"
    output_video_path = "path/to/output/final_video.mp4"
    create_video_from_images_and_audios(image_folder, audio_folder, output_video_path)
