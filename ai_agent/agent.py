import os
from dotenv import load_dotenv
import google.generativeai as genai
from time_tool import get_time

# Load API key from .env file
load_dotenv()

# Configure Gemini
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-pro")

print("Time Agent Started (type exit to stop)")

while True:
    user_input = input("Ask: ")

    if user_input.lower() == "exit":
        print("Agent stopped.")
        break

    # If question is about time
    if "time" in user_input.lower():
        city = (
            user_input.lower()
            .replace("what time in", "")
            .replace("what is the time in", "")
            .replace("time in", "")
            .strip()
        )

        result = get_time(city)
        print(result)

    # Otherwise use Gemini normally
    else:
        response = model.generate_content(user_input)
        print(response.text)

