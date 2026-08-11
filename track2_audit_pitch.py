import os
from openai import OpenAI

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

def generate_audit_package(company_name, founder_name, vulnerability_found):
    client = OpenAI(base_url="https://api.groq.com/openai/v1", api_key=GROQ_API_KEY)
    
    prompt = f"""
Generate a high-converting Cold Outreach Package for an AI Security Consultant pitching to {founder_name}, founder of {company_name}.
Vulnerability Identified: {vulnerability_found}

Output two distinct sections:
SECTION 1: 1-Page Executive Security Assessment (Markdown report format)
SECTION 2: LinkedIn DM / Cold Email Pitch Template (Direct, professional, zero filler, pointing to the audit report).
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )
    
    filename = f"audit_pitch_{company_name.lower().replace(' ', '_')}.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(response.choices[0].message.content)
        
    print(f"\n[+] Audit pitch package saved to: {filename}")

if __name__ == "__main__":
    company = input("Company Name: ").strip() or "Acme AI"
    founder = input("Founder Name: ").strip() or "John Doe"
    vuln = input("Vulnerability Description: ").strip() or "System prompt extraction via roleplay jailbreak"
    generate_audit_package(company, founder, vuln)
