
import google.generativeai as genai

GOOGLE_API_KEY = "<API-KEY>"

genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro')

def get_completion(query):
    response = model.generate_content(query)
    print(response.text, type(response.text))
    return response.text