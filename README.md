## Text Summarization Using Hugging Face

An AI-powered text summarization application built with Python, Streamlit, and Hugging Face Transformers. It converts lengthy paragraphs and articles into concise summaries while preserving the main ideas.

## Project Overview

Reading and understanding lengthy content can be time-consuming. This project uses a pretrained Qwen3-0.6B language model to summarize text in simple English through an interactive and user-friendly web interface.

## Key Features
AI-Powered Summarization: Generates concise summaries from lengthy text.
Simple Interface: Provides an easy-to-use web application built with Streamlit.
Adjustable Input: Allows users to enter paragraphs and long articles for summarization.
Real-Time Interaction: Generates summaries with a single click.
Pre-trained Language Model: Uses Qwen3-0.6B through Hugging Face Transformers.
Summary Display: Presents the generated summary directly in the application.
Lightweight Model: Uses a relatively small language model for text generation.
## Tech Stack
Python
Streamlit
Hugging Face Transformers
PyTorch
Qwen3-0.6B
Natural Language Processing (NLP)
## Project Structure
text
Text-Summarization/
├── app.py
└── README.md

## Output

<img width="771" height="541" alt="image" src="https://github.com/user-attachments/assets/5af45bc1-de42-4d97-bb01-b68b938c1adb" />

## How It Works
Enter or paste a paragraph or article into the text area.
Click the Generate Summary button.
The Hugging Face language model processes the input text.
The model generates a concise summary of the original content.
View the generated summary in the Streamlit application.
## Installation and Execution
1. Clone the Repository
bash
git clone <your-repository-url>
cd Text-Summarization

2. Install Dependencies
bash
pip install streamlit transformers torch

3. Run the Application
bash
streamlit run app.py

## Learning Outcomes
Understanding Large Language Models (LLMs).
Learning to use Hugging Face Transformers pipelines.
Integrating a pretrained language model into a Python application.
Building an interactive web interface using Streamlit.
Exploring practical applications of Natural Language Processing.
Understanding AI-based text summarization.

## Future Improvements
Support for PDF and Word document uploads.
Adjustable summary length.
Downloadable summary files.
Support for multiple languages.
Improved handling of long documents.
Integration of additional summarization models.

## Conclusion

This project demonstrates how Large Language Models and Natural Language Processing can simplify reading by transforming lengthy text into concise, meaningful summaries. By combining Hugging Face Transformers with Streamlit, the application provides a simple and accessible introduction to building AI-powered text summarization systems.
