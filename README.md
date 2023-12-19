# Image Analysis with Google Generative AI

This Python script uses Google's Generative AI to analyze an image and explain the different components seen in it. The image is loaded using the PIL library and the analysis is done using the 'gemini-pro-vision' model from Google's Generative AI models.

## Requirements

- Python 3.6 or higher
- google-generativeai Python package
- PIL Python package
- dotenv Python package

## Setup

1. Clone this repository to your local machine.
2. Set up a virtual environment and activate it with `python3 -m venv venv && source venv/bin/activate`. 
3. Install the required Python packages by running `pip install -r requirements.txt` in your terminal.
4. Create a `.env` file in the root directory of the project, and add your Google Generative AI API key as `GEMINI_API_KEY`.

## Usage

1. Optionally, replace the 'ArduinoStarterKit.webp' with the image you want to analyze and update the prompt at main.py:14.
2. Run the script using `python main.py` in your terminal.
3. The script will print the analysis of the image to the console.
