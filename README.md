# Cantonese Speech Recognition with Whisper

## Project Overview

This project leverages the Whisper model for speech recognition, focusing on the Cantonese language. It is designed to transcribe Cantonese audio files into text, enhancing the accessibility and usability of speech recognition technologies for Cantonese speakers. Due to privacy concerns, our specific dataset is not included in this repository. Users are encouraged to use their own datasets by placing audio files in the designated data folder.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. Follow these simple steps to start transcribing Cantonese audio files.

### Prerequisites

Before installing the project, make sure you have Python and pip installed on your system. This project uses Flask to run the local API server, and it requires other dependencies listed in the `requirements.txt` file.

### Installation

- **Clone the Project**

   Start by cloning the repository to your local machine:

   ```bash
   git clone git@github.com:david188888/WhisperTranscriber.git
   cd WhisperTranscriber
   ```
- **Install Dependencies**

   Install the required dependencies using pip:

   ```bash
   pip install -r requirements.txt
   ```

- **Prepare the Data**

   Place your Cantonese audio files in the `data` folder. The audio files should be in `.wav` or `.mp3` format.

- **Import the Whisper-Middle model**
    ```
    The model.safetensors file containing the model's parameters and data is not included due to its size. Follow the steps in proposs_model.md to import the model from Hugging Face Hub.
    ```

- **Run the Transcriber Service**

- **Running the API Server**

    #### Start the Flask server to transcribe Cantonese audio files:

    ```bash
    uvicorn request:app --reload --host 127.0.0.1 --port 8010
    ```
    1. #### Send a POST request to the API server with the audio file to transcribe:

        ```bash
        curl -X POST -F "file=@data/your_audio_file.wav" http://127.0.0.1:8010/transcribe/
        ```
    2.  #### Using the Python Script:
        ```bash
        python upload_audio_files.py
        ```
### **Acknowledgements**

   - OpenAI for providing the Whisper model.
   - Hugging Face for hosting the Whisper model on their model hub.



   
