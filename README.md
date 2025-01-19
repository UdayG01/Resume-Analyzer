[![Build Status](https://img.shields.io/badge/build-passing-brightgreen)](https://github.com/yourusername/ResumeAnalyzer/actions)
[![License](https://img.shields.io/badge/license-MIT-blue)](LICENSE)
[![Version](https://img.shields.io/badge/version-1.0.0-blue)](https://github.com/yourusername/ResumeAnalyzer/releases)

# Resume Analyzer

<p align="center">
   <img src="https://github.com/user-attachments/assets/f362b9a9-d322-4a91-8bb6-58fb44c2e210" alt="Project Logo" width="400px">
</p>

Analyze and score resumes using AI models to extract relevant information and evaluate candidates based on specific criteria.

---


## ⚡ Table of Contents
- [🌟 Project Overview](#-project-overview)
- [📥 Installation Instructions](#-installation-instructions)
- [🛠️ Usage Guide](#️-usage-guide)
- [✨ Features](#-features)
- [📐 Workflow](#-workflow)
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


## 📐 Workflow

```plaintext
+-------------------+       +-------------------+       +-------------------+
|                   |       |                   |       |                   |
|   Input Resumes   +------->  Data Extraction  +------->  JSON Data Files  |
|                   |       |                   |       |                   |
+-------------------+       +--------+----------+       +-------------------+
                                    |
                                    |
                                    v
                          +---------+----------+
                          |                    |
                          |  Resume Processing |
                          |                    |
                          +---------+----------+
                                    |
                                    |
                                    v
                          +---------+----------+
                          |                    |
                          |    Scoring         |
                          |                    |
                          +---------+----------+
                                    |
                                    |
                                    v
                          +---------+----------+
                          |                    |
                          |  Excel Report      |
                          |                    |
                          +--------------------+
```



1. **Input Resumes**: Place PDF resumes in the `input_resumes` directory.
2. **Data Extraction**: Run the data extraction script to extract key information from the resumes and save it as JSON files.
3. **Resume Processing**: Process the JSON data files to prepare them for scoring.
4. **Scoring**: Score the resumes based on the extracted data using AI models.
5. **Excel Report**: Generate a detailed Excel report with the extracted data and scores.


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

- **Email**: udaygupta.ph@gmail.com
- **GitHub Issues**: Open an issue
