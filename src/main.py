import os
import pandas as pd
from extract_data_v2 import load_model, generate_response
from scoring import score_resume, print_scoring_results, str_response

def process_all_resumes(input_dir="input_resumes", output_file="output/output_xl/resume_scores.xlsx"):
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    
    # loading Mistral llm
    model = load_model()
    
    # list to store results from mistral, or any other llm
    results = []
    
    # Processing the pdfs in input_resumes directory
    for file_name in os.listdir(input_dir):
        if file_name.endswith(".pdf"):
            try:
                file_path = os.path.join(input_dir, file_name)
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
                    results.append(result_row)
                    
                    print_scoring_results(score_result)
                    
            except Exception as e:
                print(f"Error processing {file_name}: {str(e)}")
                continue
    
    if results:
        df = pd.DataFrame(results)
        
        df.to_excel(output_file, index=False, engine='openpyxl')
        print(f"\nResults exported to {output_file}")
        
        return df
    else:
        print("No results to process. DataFrame could not be created.")
        return None

if __name__ == "__main__":
    results_df = process_all_resumes()

    if results_df is not None and not results_df.empty:
        print("\nSummary of Processed Resumes:")
        print(f"Total resumes processed: {len(results_df)}")
        print("\nAverage Scores:")
        print(f"GenAI Average: {results_df['GenAI_Score'].mean():.2f}/3")
        print(f"AI/ML Average: {results_df['AIML_Score'].mean():.2f}/3")
