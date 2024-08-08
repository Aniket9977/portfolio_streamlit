import streamlit as st


st.image("image/IMG_20240720_201333_050.jpg", width=200)  

st.title("Aniket Vishwakarma's Portfolio")

# Add a photograph



st.write("""
Hi, I'm Aniket Vishwakarma,  currently pursuing a Bachelor of Technology in Artificial Intelligence and Data Science.
Welcome to my portfolio website! Here you'll find my resume, projects, and ways to get in touch with me.
""")


st.header("Resume"  )

st.subheader("Education")
st.write("""
- **Bachelor of Technology in Artificial Intelligence and Data Science**  
  Jabalpur Engineering College (2021-2025)  
  CGPA: 7.6

- **High School**  
  Sagar Public School (2020)  
  Percentage: 90%
""")

st.subheader("Experience")
st.write("""
- **ML Mentor**  
  CodeYoung (July 2023 - March 2024, Remote)  
  - Taught Python, ML models, and Data Structures, enhancing students’ coding and problem-solving skills.  
  - Conducted one-on-one sessions via Zoom, focusing on error detection and code optimization.

- **Head Coordinator**  
  Jabalpur Engineering College (April 2024, Onsite)  
  - Led a team to organize various entrepreneurial activities and events.  
  - Fostered a culture of innovation and entrepreneurship among students.

- **Rajasthan IT Day**  
  Rajasthan Government (March 2023, Onsite)  
  - Developed a Machine Learning model to reduce fuel consumption.  
  - Gained experience in networking and pitching projects.
""")

st.subheader("Projects")
st.write("""
- **Brandbooster** (AI-Powered Review Analysis)  
  A website that provides actionable shopper insights about your product or your competition in 5 minutes.  
  - Insights of your products generated from reviews.  
  - Competition analysis using reviews.  
  - Charts and recommendations about product sales.

- **Car Renting Service** (Next.js)  
  A website where data is fetched using API and filtered by changing parameters in the URL.  
  - Facilitates users in searching for cars by name and model.  
  - Allows users to share their filtered results with others by sharing the URL.  
  - Technology Used: Next.js, TypeScript.

- **Kingcoin** (Cryptocurrency Landing Page)  
  A website designed with TailwindCSS and Flowbite styling, incorporating AOS animations.  
  - Used AOS animations and handled responsiveness using TailwindCSS.  
  - Technology Used: TailwindCSS, Flowbite, AOS.
""")

st.subheader("Technical Skills")
st.write("""
- **Languages**: C/C++, Python, SQL
- **Data Analytics**: Numpy, PowerBI, MS Excel, MySQL, Pandas, Matplotlib, Seaborn
- **Machine Learning**: Python, Scikit-learn, AWS, Azure, ML Algorithms, Statistics, Probability
""")

# Sidebar for Streamlit Project
st.sidebar.title("My Deployed Project")
st.sidebar.write("""
Check out my live Streamlit app:
""")
st.sidebar.markdown("[**Maths Marks Predictor**](https://maths-pred.streamlit.app/)", unsafe_allow_html=True)

# Add a section for contact information
st.header("Contact")
st.write("""
- **Phone**: +91-9977930826  
- **Email**: [aniketvishwakarma459@gmail.com](mailto:aniketvishwakarma459@gmail.com)  
- **LinkedIn**: [LinkedIn Profile](https://www.linkedin.com/in/your-profile)  
- **GitHub**: [GitHub Profile](https://github.com/your-profile)  
- **LeetCode**: [LeetCode Profile](https://leetcode.com/your-profile)
""")

# Add some footer text
st.write("---")
st.write("© 2024 Aniket Vishwakarma")
