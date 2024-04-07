# TextVisualExplainer

## Introduction
TextVisualExplainer is a Python-based tool that automates the conversion of text documents into visually engaging AI-generated videos. The project currently supports PDF, TXT, and DOCX documents, translating them into a series of images and audio files that are then compiled into a video presentation. It leverages several external Python modules, such as `pyttsx3` for text-to-speech, `moviepy` for video editing, and a fast Stable Diffusion model for generating images from text.

## Current State of the Project
Implemented features include:
- Conversion of text documents to plain text.
- Basic text analysis for extracting tone and topics (placeholders for future development).
- Text-to-speech generation for creating audio files from text.
- Image generation from text using the SDXS-512-0.9 model.
- Compilation of audio and images into a video format.
  
External Python modules used:
- `pyttsx3`
- `moviepy`
- `fitz` (PyMuPDF)
- `python-docx`
- `torch`
- `diffusers`
- `tqdm`

## How to Utilize and Run the Code
1. Clone the repository to your local machine.
2. Install the required Python modules listed in `requirements.txt`.
3. Use the following command to download the fast Stable Diffusion model:
git clone https://huggingface.co/IDKiro/sdxs-512-0.9
4. Set up your virtual environment and activate it.
5. Place your document files in the `sample_files` directory.
6. Run `application.py` to start the process. This script will guide you through the entire pipeline, from text extraction to video compilation.
7. Follow the prompts and provide necessary input when requested.

Ensure that you have the necessary system dependencies installed for the `fitz` and `python-docx` libraries to function correctly.

## Future Goals
- **Common Utilities Module**: Development of a utility module for file naming, searching, and metadata management.
- **Modular Functionality**: Refactoring code into more discrete and reusable modules for improved maintainability and performance.
- **Consistent Error Handling**: Implementing comprehensive error handling and logging strategies.
- **Unit Tests**: Establishing a suite of unit tests for robustness and reliability.
- **File Management**: Creating scripts to handle file naming and tracking systematically.
- **Abstraction Layers**: Further abstraction of third-party library usage to reduce code dependencies.
- **Logging**: Integrating detailed logging for monitoring and debugging.
- **CI/CD Pipelines**: Setting up CI/CD for automated testing and deployment.
- **Google Colab Functionality**: Adapting the tool for use in Google Colab environments.
- **Gradio Interface**: Introducing a Gradio interface for a more user-friendly experience.
- **Improved Text-to-Voice**: Enhancing text-to-speech quality with more natural and dynamic voice synthesis.
- **Refined Image Prompts**: Developing better image prompts for high-quality image generation.
- **Use of LLMS**: Employing language model summaries to improve scene description for image generation.
- **Audio Enhancements**: Incorporating sound effects where appropriate for a more immersive video experience.
- **Advanced Video Creation**: Creating more complex and multi-layered videos through advanced scripting and video editing techniques.

Stay tuned for updates and new features as we continue to develop and improve TextVisualExplainer. Your contributions and feedback are welcome!
