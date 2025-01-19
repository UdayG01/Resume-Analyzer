from langchain_mistralai.chat_models import ChatMistralAI
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_community.document_loaders import PyPDFLoader
from typing import List

import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("MISTRAL_API_KEY")

# loading the resume
def load_resume(file_path):
    loader = PyPDFLoader(file_path)
    pages = loader.load_and_split()
    return pages

# extract text from pdf
def extract_text_from_pdf(pages):
    text = " ".join(list(map(lambda page: page.page_content, pages)))
    return text

class CVDataExtraction(BaseModel):
    username: str = Field(description="candidate username")
    email: str = Field(description="candidate email")
    profile: str = Field(description="candidate profile description")
    education: List[str] = Field(description="candidate education details")
    cgpa: float = Field(description="candidate cgpa in education")
    skills: List[str] = Field(description="soft and technical skills")
    summary: str = Field(description="candidate summary")

def load_model():
    model = ChatMistralAI(api_key=api_key, model='mistral-large-latest')
    return model

def generate_response(model, file_path):
    structured_llm = model.with_structured_output(CVDataExtraction)
    resume_pages = load_resume(file_path)
    texts = extract_text_from_pdf(resume_pages)
    response = structured_llm.invoke(texts)
    return response

# Testing the module
# mistral = load_model()
# file_path = "input_resumes/ML-resume-sample1.pdf"
# response = generate_response(mistral, file_path)
# for key, value in response.__dict__.items():
#     print(f"{key}: {value}")