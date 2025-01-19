from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
# LLMChain is deprecated
# from langchain.chains import LLMChain
from extract_data_v2 import generate_response, load_model, CVDataExtraction


def set_llm_chain():
    # Load the model
    model = load_model()

    # Define the scoring prompt template
    scoring_template = """
    You are an expert AI recruiter analyzing resumes. Based on the following resume data, please provide a detailed scoring analysis.

    Resume Content:
    {resume_text}

    Please analyze and score the following criteria on a scale of 1-3:

    1. Generative AI Experience:
    - Score 1: Basic familiarity/exposure
    - Score 2: Hands-on practical application
    - Score 3: Advanced (e.g., Agentic RAG, Evaluations)

    2. AI/ML Experience:
    - Score 1: Basic understanding/coursework
    - Score 2: Project implementation/practical experience
    - Score 3: Advanced projects/professional experience

    For each category, provide:
    - Numerical score (1-3)
    - Brief justification for the score
    - Key identified keywords/projects that influenced the score

    Output Format:
    {{"gen_ai_score": <score>, "gen_ai_justification": "<text>", "gen_ai_keywords": [<keywords>],
    "ai_ml_score": <score>, "ai_ml_justification": "<text>", "ai_ml_keywords": [<keywords>]}}
    """

    # Create the prompt template
    prompt = PromptTemplate(
        input_variables=["resume_text"],
        template=scoring_template
    )

    # Create the chain
    scoring_chain = prompt | model | JsonOutputParser()
    
    return scoring_chain

# Function to score a resume
def score_resume(resume_text):
    scoring_chain = set_llm_chain()
    try:
        result = scoring_chain.invoke({"resume_text": resume_text})
        return result
    except Exception as e:
        print(f"Error scoring resume: {str(e)}")
        return None

def print_scoring_results(score_data):
    """
    Print scoring results in a formatted, readable manner
    """
    print("\n=== Resume Scoring Results ===")
    print("\n1. Generative AI Experience:")
    print(f"   Score: {score_data['gen_ai_score']}/3")
    print(f"   Justification: {score_data['gen_ai_justification']}")
    print("   Keywords:", ", ".join(score_data['gen_ai_keywords']))
    
    print("\n2. AI/ML Experience:")
    print(f"   Score: {score_data['ai_ml_score']}/3")
    print(f"   Justification: {score_data['ai_ml_justification']}")
    print("   Keywords:", ", ".join(score_data['ai_ml_keywords']))
    print("\n===========================")

def str_response(response):
    string_response = f"{response}"    
    print("Raw Resume Text:")
    return string_response



# Test the scoring with the response
# model = load_model()
# file_path = "input_resumes/ML-resume-sample1.pdf"
# response = generate_response(model, file_path)
# string_response = str_response(response)
# if isinstance(string_response, str):
#     score_result = score_resume(string_response)
#     if score_result:
#         print_scoring_results(score_result)
# else:
#     print("Error: Response is not in the expected format")
