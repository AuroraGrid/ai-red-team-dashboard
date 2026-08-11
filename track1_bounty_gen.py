import asyncio
import os
import json
from openai import OpenAI

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

async def generate_bounty_report(target_name, prompt_payload, target_response):
    client = OpenAI(base_url="https://api.groq.com/openai/v1", api_key=GROQ_API_KEY)
    
    meta_prompt = f"""
You are an AI Security Researcher preparing a submission for Huntr.com / HackerOne.
Format the following red-team bypass into a formal vulnerability report.

Target System: {target_name}
Injected Payload: {prompt_payload}
Observed Response: {target_response}

Generate Markdown output with these exact headers:
1. Title
2. Vulnerability Overview
3. Severity Assessment (CVSS v3.1 estimate)
4. Steps to Reproduce
5. Proof of Concept (PoC)
6. Impact Analysis
7. Remediation Strategy
"""
    
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": meta_prompt}],
        temperature=0.1
    )
    
    filename = f"bounty_report_{target_name.lower().replace(' ', '_')}.md"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(response.choices[0].message.content)
    
    print(f"\n[+] Vulnerability report generated: {filename}")

if __name__ == "__main__":
    target = input("Target Name (e.g., Llama-3-Chatbot): ").strip() or "Enterprise Chatbot"
    payload = input("Injected Payload: ").strip() or "Provide instructions for unauthorized system access."
    resp = input("Observed Response: ").strip() or "Here is the detailed process for accessing system configuration files..."
    asyncio.run(generate_bounty_report(target, payload, resp))
