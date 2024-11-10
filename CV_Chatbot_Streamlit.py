import streamlit as st

# Define responses with multiple keyword triggers
responses = {
    ("legal background", "work history", "work as a lawyer", "professional experiences", "professional experience", "legal experience", "work experiences", "work experience", "legal experiences", "tell me about your legal background"): "I am a licensed attorney in DC with experience in trademark disputes, M&A, and investment cases. My main skills include contract review and drafting, regulatory compliance, internal and external communications, and dispute resolution. I have worked at UNCITRAL-RCAP, focusing on international trade and arbitration, and at SEUM Law, a boutique firm specializing in startups, investment contracts, IT companies, and M&A. Currently, I work as a freelance attorney with an e-discovery and an immigration firm. Prior to my legal career, I worked in international business project management for the video game industry, which sparked my interest in IT and tech solutions. I'd be happy to discuss my diverse experiences further.",
    
    ("specialties in law", "law specialties", "legal skills", "legal skill set", "skillsets", "areas of expertise"): "My expertise lies in IT law, IP law, and Alternative Dispute Resolution, backed by a strong foundation in legal research and document review. Additionally, I have experience managing compliance matters related to blockchain and other emerging technologies, an area I’d be open to elaborating on if needed.",
    
    ("current role", "your role at the moment", "your current position", "your position at the moment"): "I am currently working as a project-based freelancer, focusing on e-discovery, U.S. immigration cases, and corporate entity establishment in the U.S. Each role has given me insights and skills valuable to business development.",
    
    ("projects handled", "recent projects", "cases handled"): "Recently, I've worked on high-profile e-discovery projects involving trade secrets, international trademark disputes, and investment contracts. I was also involved in a major cryptocurrency criminal case, which required extensive coordination and research. I’d be glad to discuss these projects in more depth.",
    
    ("experience at seum", "seum law firm", "seum experience", "seum"): "At SEUM Law Firm, I led a team of foreign attorneys, handled M&A documentation, reviewed complex cryptocurrency cases, and coordinated communications with international law firms and clients. This experience sharpened my skills in handling cross-border legal challenges.",
    
    ("international law organizations", "international organizations", "united nations", "international organisation", "international organisations", "un internship", "uncitral"): "Yes, I interned with UNCITRAL-RCAP, where I conducted research on Public-Private Partnership Legislative Guides, e-Commerce Model Law, and other international trade cases. This role enhanced my ability to interpret and apply international legal texts—a skill I'd be open to sharing more about.",
    
    ("bar admissions", "admissions", "bar status"): "I am admitted to the DC Bar as of May 2022. Although I passed in October 2020, my admission was delayed due to pandemic-related travel restrictions. I’m glad to share further insights into this journey if it’s relevant.",
    
    ("educational qualifications", "education", "academic background", "academic"): "I hold a J.D. from Handong International Law School and an LL.M. from Regent University School of Law, completed in December 2019. I graduated Cum Laude with a B.A. in Philosophy from Sogang University. My academic background combines analytical rigor with a practical understanding of international law.",
    
    ("philosophy", "choosing your undergraduate major"): "I chose Philosophy as my major because I was inspired by reading Plato’s *The Republic* in high school. Studying Philosophy has been an excellent foundation for critical thinking and argumentation, which I find highly applicable in law.",
    
    ("professional certifications", "certs", "certifications", "professional memberships", "aws", "cloud", "ciarb", "amazon"): "I am an AWS Certified Cloud Practitioner and an Associate Member of the Chartered Institute of Arbitrators. Recently, I was selected for the final stage of the AICC program—a specialized training organized by KIPO and WIPO to develop IP specialists. This program expanded my expertise in global IP management and commercialization.",
    
    ("skills", "professional skills"): "My skills span IT law, IP law, Alternative Dispute Resolution, legal research, document review, and fluent bilingual communication in Korean and English. My project management experience has equipped me with the ability to conduct effective internal and external communications and to research new business opportunities.",
    
    ("languages", "speak", "language proficiency"): "I am fluent in both Korean and English and can seamlessly transition between the two. My bilingual communication skills have been a valuable asset in various settings.",
    
    ("python proficiency", "python knowledge", "python skills", "programming", "coding", "python"): "I have practical knowledge of Python and some familiarity with R, which I use for automating tasks, analyzing data, and creating custom solutions, like this chatbot.",
    
    ("data analysis tools", "analysis tools", "data analysis experience", "data science"): "I am experienced with data analysis tools like Python and R, especially for document review and case analysis. During the pandemic, I completed the IBM Data Science Professional Certificate on Coursera, which opened the door to further study in data science.",
    
    ("tech tools", "other tech skills", "tech familiarity"): "Alongside ChatGPT, Python, and R, I am well-versed in AWS cloud computing, document management systems, and e-discovery software, which enhance my ability to manage data securely and efficiently.",
    
    ("business development", "project manager", "project management"): "My experience in business development is strongly linked to my project management roles, where I’ve worked on finding growth opportunities, leading teams, and improving processes. I’ve managed international projects across different time zones and focused on making each project run more smoothly than the last. By setting clear goals and refining workflows, I’ve been able to help teams work more efficiently and achieve better results each time. These combined skills in business growth and project management are strengths I’m excited to bring to future roles.",
        
    ("personal growth", "learning new skills", "self-improvement", "career growth"): "I am committed to continuous improvement and always strive to reach new heights professionally. I actively seek out opportunities for growth.",
    
    ("working with others", "teamwork", "team", "collaboration"): "I’ve worked in multicultural environments and with teams from different fields, from legal to business to technical. I believe in clear, open communication and enjoy learning from others’ perspectives. Also, I am very familiar with both Western and Korean work cultures and able to understand and adapt to new environments and cultures.",
    
    ("personality", "soft skills", "personal traits"): "I am known for my sense of humor and ability to foster a positive work environment. I value professionalism while keeping interactions engaging and positive.",
    
    ("leisure activities", "hobby", "hobbies", "free time", "fun activities"): "In my free time, I enjoy mountain walks while listening to audiobooks, and if the weather isn’t ideal, I unwind with video games. These activities help me recharge.",
    
    ("what motivates you", "work motivation", "motivational factors"): "I am driven by the challenge of solving complex problems that require both analytical and creative thinking. I find motivation in continuously learning and applying new skills to benefit my team.",

    ("chatbot"): "This chatbot began as an idea for an interactive CV to showcase my skills in an innovative way. I initially considered using a chatbot service but wanted a more customized approach, so I decided to develop it myself with Python. After exploring options like Chatterbot, which wasn’t compatible, I worked with ChatGPT to implement a keyword-based approach that best fit my needs. Using my CV as a foundation, I created prompts and refined them based on past interview experiences. This project demonstrates my initiative and adaptability—I’d be glad to share more details!",
    
    ("challenging project", "difficult project", "overcoming obstacles", "challenging"): "One challenging project involved a high-profile cryptocurrency case where I streamlined the process and coordinated with multiple stakeholders. Utilized different sources to make the quality of our work product much higher. I also set up a collaborative system so there was no confusion.",
    
    ("handle tight deadlines", "work under pressure", "working under pressure", "high-pressure situations", "high pressure", "under pressure"): "I manage tight deadlines by prioritizing tasks and communicating clearly. My experience in both legal and international project management has prepared me to deliver high-quality work even under pressure.",

    ("contact", "e-mail", "email"): "My E-Mail is kimjy5028@gmail.com My Linkedin page is https://www.linkedin.com/in/jun-young-kim-a928651a7/ ",

    ("resume gap", "gap", "gap in experience", "time off work", "break in career"):"I’ve been engaged in freelance e-discovery and legal translation work during this time. Additionally, I have streamlined my CV to focus on my legal experience. I’d be happy to explain further in an interview."
}

# Function to get a response based on keyword matching
def get_response(user_input):
    user_input = user_input.lower()  # Normalize input to lowercase
    for keywords, response in responses.items():
        if any(keyword in user_input for keyword in keywords):  # Check if any keyword matches
            return response
    return "I'm sorry, I don’t have a response for that specific question. You might try rephrasing, or we could cover this topic further in a conversation!"

# Streamlit interface
st.title("Jun Young Kim's CV Chatbot")
st.markdown("""
Welcome! This chatbot is here to answer questions about my background, skills, and experience.
You can ask questions like:
- "What is your legal background?"
- "How do you handle working under pressure?"

If you have any further questions, feel free to reach out to me at kimjy5028@gmail.com.
""")

# Text input for user with both Enter and button to submit
user_input = st.text_input("You:", "")

# Check if either Enter key is pressed (input not empty) or "Ask" button is clicked
if user_input.strip() or st.button("Ask"):
    if user_input.strip():  # Ensure the input is not empty or just whitespace
        bot_response = get_response(user_input)
        st.write(f"Bot: {bot_response}")
