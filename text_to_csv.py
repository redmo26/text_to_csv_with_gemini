import json
import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import csv


load_dotenv()
SYSTEM_PROMPT="""Extract these fields from the email: (company, city, items, date, budget, phone).
Reply with JSON only, no extra text.
Use exactly these field names as keys."""
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

with open("text.txt", "r", encoding="utf-8") as f:
    text= f.read()
emails = text.split("---")

def extract(email):
    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=email,
        config=types.GenerateContentConfig(
            system_instruction=SYSTEM_PROMPT,
            response_mime_type="application/json", #smh makes ai respond json shit properly
        ),
    )
    return json.loads(response.text)
rows = []
for email in emails:
    try:
        rows.append(extract(email))    
    except Exception as e:
        print("Failed on this email", e)

with open("orders.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["company", "city", "items", "date", "budget", "phone"])
    for row in rows:
        writer.writerow([row["company"], row["city"], row["items"], row["date"], row["budget"], row["phone"]])
