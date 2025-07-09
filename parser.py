import re

def extract_details(text):
    name = text.split('\n')[0]
    email = re.findall(r'\S+@\S+', text)
    phone = re.findall(r'\d{10}', text)
    skills = ["Python", "Java", "SQL", "Excel", "C++"]
    found_skills = [skill for skill in skills if skill.lower() in text.lower()]

    print("Name:", name)
    print("Email:", email)
    print("Phone:", phone)
    print("Skills:", found_skills)

with open("sample_resume.txt", "r", encoding='utf-8') as file:
    resume_text = file.read()

extract_details(resume_text)
