import os
import json
from openai import OpenAI

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

def run_metaculus_parser(question):
    client = OpenAI(base_url="https://api.groq.com/openai/v1", api_key=GROQ_API_KEY)
    
    system_instruction = """
You are a Superforecaster producing calibrated estimates for Metaculus / Prediction Markets.
For the question provided, output:
1. Exact Point Prediction (%)
2. 80% Confidence Interval (Lower % - Upper %)
3. Reference Class & Base Rate Analysis
4. Key Catalysts / Drivers
5. Reversal Triggers (What changes this prediction?)

Keep the rationale formatted for copy-paste directly into Metaculus submission boxes.
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": system_instruction},
            {"role": "user", "content": question}
        ],
        temperature=0.1
    )
    
    print("\n" + "="*60)
    print("METACULUS SUBMISSION READY FORMAT")
    print("="*60)
    print(response.choices[0].message.content)
    print("="*60 + "\n")

if __name__ == "__main__":
    q = input("Metaculus Question: ").strip() or "Will an AI pass a standardized US bar exam with a score in the 99th percentile before 2027?"
    run_metaculus_parser(q)
