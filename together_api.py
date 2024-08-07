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
                Summarize the following text:
        """
        full_input = input_text + prompt
        output_summary = self.llm.invoke(full_input)
        return output_summary