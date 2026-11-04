from groq import Groq

client = Groq(api_key="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")

resume = """# AFTAB MOHAMMED
Guntur, Andhra Pradesh, India  
Phone: +91 XXXXX XXXXX | Email: yourmail@gmail.com  
LinkedIn: linkedin.com/in/yourprofile | GitHub: github.com/yourprofile

## CAREER OBJECTIVE
Motivated Computer Science Engineering student with knowledge of Java, Python, HTML, CSS, and JavaScript. Interested in software development and problem-solving. Looking for an internship opportunity to improve technical skills and gain practical experience.

## EDUCATION
**B.Tech – Computer Science and Engineering**  
Your College Name  
2024 – 2028  
CGPA: X.XX

## TECHNICAL SKILLS
- Programming Languages: Java, Python
- Frontend: HTML, CSS, JavaScript, React
- Backend: Node.js, Express.js
- Database: MySQL, MongoDB
- Tools: Git, GitHub, VS Code

## PROJECTS

**1. CampusBite – College Food Pre-ordering System**
- Developed a platform for students to pre-order food from the college cafeteria.
- Helps reduce waiting time during lunch breaks.
- Technologies: HTML, CSS, JavaScript, React, Node.js.

**2. Hospital Appointment Booking System**
- Designed a system for patients to book doctor appointments online.
- Helps doctors manage appointments and daily schedules.
- Technologies: Java, MySQL, HTML, CSS.

## CERTIFICATIONS
- Java Programming – [Platform]
- Python Programming – [Platform]
- Web Development – [Platform]

## ACHIEVEMENTS
- Participated in coding challenges.
- Practiced Data Structures and Algorithms.
- Completed academic projects.

## SOFT SKILLS
- Problem-solving
- Teamwork
- Communication
- Time management

## DECLARATION
I hereby declare that the information provided above is true to the best of my knowledge."""

response = client.chat.completions.create(
    model="qwen/qwen3.8-27b",
    messages=[
        {
            "role": "system",
            "content": "You are a brutally honest recruiter who roasts resumes. "
                       "Structure: THE ROAST, THE HARD TRUTH, THE FIX."
        },
        {
            "role": "user",
            "content": f"Roast this resume:\n{resume}"
        }
    ],
    temperature=0.85,
    max_tokens=700
)

print(response.choices[0].message.content)