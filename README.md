# Resume Analyzer

![Project Logo](https://via.placeholder.com/150 "Project Logo")

[![Build Status](https://img.shields.io/badge/build-passing-brightgreen)](https://github.com/yourusername/ResumeAnalyzer/actions)
[![License](https://img.shields.io/badge/license-MIT-blue)](LICENSE)
[![Version](https://img.shields.io/badge/version-1.0.0-blue)](https://github.com/yourusername/ResumeAnalyzer/releases)
[![Downloads](https://img.shields.io/badge/downloads-1k%2B-brightgreen)](https://github.com/yourusername/ResumeAnalyzer)

Analyze and score resumes using AI models to extract relevant information and evaluate candidates based on specific criteria.

---

![Resume Analyzer Workflow](https://via.placeholder.com/800x400 "Workflow Visualization")

## ⚡ Table of Contents
- [🌟 Project Overview](#-project-overview)
- [📥 Installation Instructions](#-installation-instructions)
- [🛠️ Usage Guide](#️-usage-guide)
- [✨ Features](#-features)
- [📐 Architecture](#-architecture)
- [🛑 Technologies and Dependencies](#-technologies-and-dependencies)
- [🔧 Setup for Development](#-setup-for-development)
- [🚀 Roadmap](#-roadmap)
- [🙏 Acknowledgments](#-acknowledgments)
- [📧 Contact Information](#-contact-information)

## 🌟 Project Overview

Resume Analyzer is a tool designed to process PDF resumes, extract relevant information, and score them based on specific criteria using AI models. It helps in evaluating candidates efficiently by automating the resume screening process.

## 📥 Installation Instructions

### Prerequisites
- Python 3.8 or higher
- Git

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/ResumeAnalyzer.git
   cd ResumeAnalyzer
   ```

2. Set up a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   Create a `.env` file in the root directory and add your Mistral API key:
   ```
   MISTRAL_API_KEY=your_api_key_here
   ```

## 🛠️ Usage Guide

### Extract Data from Resumes
1. Place PDF resumes in the `input_resumes` directory.
2. Run the data extraction script:
   ```bash
   python src/extract_data_v2.py
   ```
3. Run the scoring script:
    ```bash
    python src/scoring.py
    ```

### Process and Score Resumes
1. Run the main processing script:
   ```bash
   python src/main.py
   ```
   This will process all resumes in the `input_resumes` directory, extract data, score them, and save the results to an Excel file in the `output_xl` directory.

### Parallel Processing
1. Run the threading script for faster processing:
   ```bash
   python src/main_threading.py
   ```

## ✨ Features

- **Automated Data Extraction**: Extracts key information from PDF resumes.
- **AI Scoring**: Scores resumes based on Generative AI and AI/ML experience.
- **Parallel Processing**: Processes multiple resumes simultaneously for faster execution.
- **Detailed Reports**: Generates detailed Excel reports with extracted data and scores.

## 📐 Architecture

The project is structured as follows:

**Root Directory:**
- `.env`: Environment variables file.
- `requirements.txt`: Python dependencies.
- `input_resumes`: Directory for input PDF resumes.
- `output`: Directory for extracted JSON data and Excel files.
- `src`: Source code directory.

### Workflow
1. **Data Extraction**: Extracts text from PDF resumes and uses AI models to extract specific fields.
2. **Resume Processing**: Processes all resumes, scores them, and saves the results to an Excel file.
3. **Scoring**: Uses AI models to score resumes based on extracted data.


## 🛑 Technologies and Dependencies

- **LangChain**: For language model integration.
- **HuggingFacePipeline**: For text generation.
- **MistralAI**: For advanced data extraction.
- **PyPDF2**: For reading PDF files.
- **Pandas**: For data manipulation and Excel file generation.
- **Transformers**: For AI model integration.

## 🔧 Setup for Development

Clone the repository and set up the environment as described in the installation instructions.

## 🚀 Roadmap

- **Improve Data Extraction**: Enhance the extraction logic to handle more resume formats.
- **Model Tuning**: Fine-tune the scoring model for better accuracy.
- **Add More Features**: Include additional scoring criteria and support for more file formats.

## 🙏 Acknowledgments

- **LangChain**: For providing the language model integration.
- **HuggingFace**: For the text generation pipeline.
- **MistralAI**: For advanced data extraction capabilities.
- **PyPDF2**: For PDF reading functionality.

## 📧 Contact Information

For queries or feedback, please contact:

- **Email**: your.email@example.com
- **GitHub Issues**: Open an issue
