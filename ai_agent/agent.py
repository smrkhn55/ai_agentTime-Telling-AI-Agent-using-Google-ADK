import os
from dotenv import load_dotenv
import google.generativeai as genai
from time_tool import get_time

# Load API key
load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-pro")

print("Time Agent Started (type exit to stop)")

while True:
    user_input = input("Ask: ").strip()

    # 🔹 Ignore empty input (FIX)
    if not user_input:
        print("Please ask a question.")
        continue

    if user_input.lower() == "exit":
        print("Agent stopped.")
        break

    # 🔹 Time-related questions
    if "time" in user_input.lower():
        city = (
            user_input.lower()
            .replace("what time in", "")
            .replace("what is the time in", "")
            .replace("time in", "")
            .strip()
        )

        print(get_time(city))

    # 🔹 Other questions → Gemini
    else:
        response = model.generate_content(user_input)
        print(response.text)
