
import google.generativeai as genai
import os 
from dotenv import load_dotenv 

load_dotenv()


api_key = os.getenv('GOOGLE_API_KEY')
# print(f"Value of GOOGLE_API_KEY from environment: {api_key}")
if not api_key:
    raise ValueError("Google api key not set")

genai.configure(api_key=api_key)

print("Gemini API configured!")

model = genai.GenerativeModel('gemini-1.5-flash')

user_prompt = "what is generative ai "
response = model.generate_content(user_prompt)
print("\n-- Gemini's Response: ")
print(response.text)