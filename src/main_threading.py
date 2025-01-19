import os
import pandas as pd
from concurrent.futures import ThreadPoolExecutor, as_completed
from extract_data_v2 import load_model, generate_response
from scoring import score_resume, print_scoring_results, str_response

def process_single_resume(file_name, file_path, model):
    """Process a single resume and return its results"""
    try:
        print(f"\nProcessing: {file_name}")
        cv_data = generate_response(model, file_path)
        resume_string = str_response(cv_data)
        score_result = score_resume(resume_string)
        
        if score_result:
            result_row = {
                'File_Name': file_name,
                'Candidate_Name': cv_data.username,
                'Email': cv_data.email,
                'CGPA': cv_data.cgpa,
                'Skills': ', '.join(cv_data.skills),
                'GenAI_Score': score_result['gen_ai_score'],
                'GenAI_Justification': score_result['gen_ai_justification'],
                'GenAI_Keywords': ', '.join(score_result['gen_ai_keywords']),
                'AIML_Score': score_result['ai_ml_score'],
                'AIML_Justification': score_result['ai_ml_justification'],
                'AIML_Keywords': ', '.join(score_result['ai_ml_keywords'])
            }
            print_scoring_results(score_result)
            return result_row
    except Exception as e:
        print(f"Error processing {file_name}: {str(e)}")
        return None

def process_all_resumes(input_dir="input_resumes", output_file="output/output_xl/resume_scores_threaded.xlsx", batch_size=2):
    """Process resumes in batches using parallel execution"""
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    model = load_model()
    results = []
    
    # Get all PDF files
    pdf_files = [(f, os.path.join(input_dir, f)) 
                 for f in os.listdir(input_dir) 
                 if f.endswith(".pdf")]
    
    # Process in batches
    for i in range(0, len(pdf_files), batch_size):
        batch = pdf_files[i:i + batch_size]
        print(f"\nProcessing batch {i//batch_size + 1}")
        
        with ThreadPoolExecutor(max_workers=batch_size) as executor:
            future_to_file = {
                executor.submit(process_single_resume, file_name, file_path, model): file_name
                for file_name, file_path in batch
            }
            
            for future in as_completed(future_to_file):
                result = future.result()
                if result:
                    results.append(result)
    
    if results:
        df = pd.DataFrame(results)
        df.to_excel(output_file, index=False, engine='openpyxl')
        print(f"\nResults exported to {output_file}")
        return df
    
    print("No results to process. DataFrame could not be created.")
    return None

def generate_summary_report(df):
    """Generate a detailed summary report"""
    if df is None or df.empty:
        return
    
    print("\n=== Detailed Analysis Report ===")
    print(f"\nTotal Resumes Processed: {len(df)}")
    
    print("\nScore Distribution:")
    print("GenAI Scores:")
    print(df['GenAI_Score'].value_counts().sort_index())
    print("\nAI/ML Scores:")
    print(df['AIML_Score'].value_counts().sort_index())
    
    print("\nAverage Scores:")
    print(f"GenAI Average: {df['GenAI_Score'].mean():.2f}/3")
    print(f"AI/ML Average: {df['AIML_Score'].mean():.2f}/3")
    
    # Most common skills
    all_skills = [skill.strip() for skills in df['Skills'].str.split(',') for skill in skills]
    skill_counts = pd.Series(all_skills).value_counts()
    print("\nTop 10 Most Common Skills:")
    print(skill_counts.head(10))

if __name__ == "__main__":
    results_df = process_all_resumes(batch_size=5)
    if results_df is not None:
        generate_summary_report(results_df)
