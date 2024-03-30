# WhisperTranscriber

WhisperTranscribe is a service for local audio transcription based on OpenAI's Whisper model. It allows users to upload audio files and return transcripts through a REST API interface. It is designed for scenarios that need to process their own data sets, ensuring data privacy and security.

## Features

- **Local Deployment**: Ensures that all audio processing work is done in the user's private environment.
- **REST API interface**: Provides a simple and easy-to-use API to facilitate users to upload files and receive transcription results.
- **Custom dataset support**: Allows users to use personal or professional datasets for transcription, improving transcription quality and adaptability.

## Quick start

This section will guide you how to deploy and run LocalWhisperTranscriber locally.

### Prerequisites

Before you begin, make sure you have the following software installed on your system:

- Python 3.10 or higher


### Installation steps

1. **Clone repository**

    Open a terminal and run the following command to clone the project locally:

    ```bash
    git clone https://github.com/yourusername/LocalWhisperTranscribe.git
    cd LocalWhisperTranscriber
