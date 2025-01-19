import os
import json
from PyPDF2 import PdfReader
from langchain import HuggingFacePipeline
from langchain import PromptTemplate
from transformers import pipeline
import torch

# Directory paths
input_dir = "./input_resumes"
output_dir = "./output"

def extract_text_from_pdf(file_path):
    reader = PdfReader(file_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

def setup_llm():
    # Initialize the pipeline
    model = pipeline("text-generation", model="TheBloke/Llama-2-7B-Chat-GGML")
    # Create LangChain wrapper
    llm = HuggingFacePipeline(pipeline=model)
    
    return llm

def extract_fields_with_langchain(text, llm):
    # Define prompt template
    template = """
    Extract the following information from the resume text:
    - Name
    - Contact Details (email and phone)
    - University
    - Year of Study
    - Course
    - Discipline
    - CGPA/Percentage
    - Key Skills

    Resume text:
    {text}

    Format the response as a JSON object.
    """
    
    prompt = PromptTemplate(
        input_variables=["text"],
        template=template,
    )
    
    # Get response from model
    response = llm(prompt.format(text=text))
    
    # Parse the response into a dictionary
    try:
        extracted_data = json.loads(response)
    except json.JSONDecodeError:
        extracted_data = {
            "Name": None,
            "Contact Details": None,
            "University": None,
            "Year of Study": None,
            "Course": None,
            "Discipline": None,
            "CGPA/Percentage": None,
            "Key Skills": None
        }
    
    return extracted_data

def process_pdfs_to_json(input_dir, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    # Setup LLM once
    llm = setup_llm()

    for file_name in os.listdir(input_dir):
        if file_name.endswith(".pdf"):
            file_path = os.path.join(input_dir, file_name)
            text = extract_text_from_pdf(file_path)
            extracted_data = extract_fields_with_langchain(text, llm)
            output_file_path = os.path.join(output_dir, f"{os.path.splitext(file_name)[0]}.json")

            with open(output_file_path, "w") as json_file:
                json.dump(extracted_data, json_file, indent=4)

            print(f"Data extracted and saved to {output_file_path}")

if __name__ == "__main__":
    if not os.path.exists(input_dir):
        print(f"Input directory '{input_dir}' does not exist. Please create it and add PDF files.")
    else:
        process_pdfs_to_json(input_dir, output_dir)
