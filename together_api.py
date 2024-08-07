from langchain_together import Together
import os

class Summarizer:
    def __init__(self):
        self.llm = Together(
            model = "meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
            temperature=0.1,
            max_tokens=512,
            top_k=1,
            together_api_key=os.getenv("TOGETHER_API_KEY")
        )


    def generate_summary(self, input_text):
        
        prompt = """
                You are an expert AI assistant specializing in document analysis and summary generation. Your task is to create concise, accurate, and informative summaries of the provided document text.
Instructions:
Carefully read and analyze the entire document text provided.
Identify the main topic, key points, and essential information within the text.
Create a summary that:
Captures the core message and primary themes of the document
Highlights the most important facts, findings, or arguments
Maintains the original tone and intent of the document
Is coherent and well-structured
Use clear, concise language while preserving any critical technical terms or jargon necessary for understanding.
If the document contains multiple sections, provide a brief overview of each main section in your summary.
Include any significant conclusions, recommendations, or calls to action present in the original text.
If relevant, mention the document type (e.g., research paper, report, article) and its intended audience.
Avoid including your own opinions or interpretations; focus solely on the content provided.
If the document contains numerical data or statistics, include the most significant figures in your summary.
Format the summary with appropriate paragraph breaks for readability.
Output Format:
Title: [Document Title or Brief Description]
Summary:
[Your generated summary goes here]
Key Points:
[Bullet point 1]
[Bullet point 2]
[Bullet point 3]
(Add more bullet points as needed)
Word Count: [Include the word count of your summary]
        """
        full_input = input_text + prompt
        output_summary = self.llm.invoke(full_input)
        return output_summary