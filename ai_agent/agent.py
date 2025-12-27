import google.generativeai as genai
from time_tool import get_time
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-pro")

def run_agent():
    print("Time Agent Started (type exit to stop)")
    while True:
        user_input = input("Ask: ")

        if user_input.lower() == "exit":
            break

        if "time" in user_input.lower():
            city = user_input.split("in")[-1].strip()
            time = get_time(city)
            print(f"Current time in {city}: {time}")
        else:
            response = model.generate_content(user_input)
            print(response.text)

run_agent()
