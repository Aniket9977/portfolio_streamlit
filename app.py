import streamlit as st

# Create a two-column layout
col1, col2 = st.columns([1, 2])

# Add photo in the first column
with col1:
    st.image("image/IMG_20240720_201333_050.jpg", width=200)  

    # Add a download button for the resume below the photo
    try:
        with open("image/Resume (1).pdf", "rb") as file:
            st.download_button(
                label="Download Resume",
                data=file,
                file_name="Resume (1).pdf",
                mime="application/pdf",
            )
    except FileNotFoundError:
        st.error("Resume file not found. Please check the file path.")

# Add title and introduction in the second column
with col2:
    st.title("Aniket Vishwakarma's Portfolio")
    st.write("""
    Hi, I'm Aniket Vishwakarma, currently pursuing a Bachelor of Technology in Artificial Intelligence and Data Science.
    Welcome to my portfolio website! Here you'll find my resume, projects, and ways to get in touch with me.
    """)

# (Rest of your code...)

# Education section
st.subheader("Education")
st.write("""
- **Bachelor of Technology in Artificial Intelligence and Data Science**  
  Jabalpur Engineering College (2021-2025)  
  CGPA: 7.6

- **High School**  
  Sagar Public School (2020)  
  Percentage: 90%
""")

# Experience section
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

# Projects section
st.subheader("Projects")
st.write("""
- **ATS Resume Expert (AI-Powered ATS Resume Evaluation Tool)**  
  Developed an application to evaluate resumes against job descriptions and optimize them for ATS.
  - Utilized gemini-1.5-flash to generate detailed feedback on resume alignment with job descriptions.
  - Developed custom prompts to assess weaknesses and provide a percentage match to the job description.
  - Immediate feedback, keyword optimization, format compatibility, and alignment to specific job descriptions.
  - **Technology Used**: Pandas, Pickle, Scikit-Learn.

- **Remote Proctoring System with Real-Time Facial Landmark Detection (OpenCV)**  
  The system tracks eye and mouth movements to identify potential cheating behaviors.
  - Developed an application to leverage facial landmarks to monitor eye and mouth activities using OpenCV and Dlib.
  - Utilized metrics to detect suspicious activities, enhancing the accuracy of remote proctoring systems.
  - **Technology Used**: Python, OpenCV, Dlib, Machine Learning.

- **Maths Marks Predictor (Real-Time Predictions)**  
  An application to predict marks using machine learning algorithms.
  - Developed machine learning prediction, preprocessing, inference, and accurate predictions based on input data.
  - Managed the end-to-end machine learning workflow.
  - **Technology Used**: Pandas, Scikit-learn, Python.
""")

# Technical Skills section
st.subheader("Technical Skills")
st.write("""
- **Languages**: Python, SQL
- **Data Analytics**: Numpy, PowerBI, MS Excel, MySQL, Pandas, Matplotlib, Seaborn
- **Machine Learning**: Python, Scikit-learn, AWS, Azure, ML Algorithms, Statistics, Probability
""")

# Sidebar for Streamlit Project
st.sidebar.title("My Deployed Projects")
st.sidebar.write("Check out my live apps:")

st.sidebar.markdown(
    """
    <a href="https://proct-remote.streamlit.app/" target="_blank" 
       style="text-decoration: none;">
        <div style="border: 1px solid #bbb; padding: 12px; border-radius: 10px; 
                    background: linear-gradient(135deg, #e0f7fa, #e1f5fe); 
                    box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2); 
                    margin-bottom: 20px; transition: transform 0.3s ease-in-out; 
                    color: #004d40; font-weight: bold; font-size: 15px;">
            Remote Proctoring System
        </div>
    </a>
    """, unsafe_allow_html=True
)

st.sidebar.markdown(
    """
    <a href="https://free-ats.streamlit.app/" target="_blank" 
       style="text-decoration: none;">
        <div style="border: 1px solid #bbb; padding: 12px; border-radius: 10px; 
                    background: linear-gradient(135deg, #f1f8e9, #dcedc8); 
                    box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2); 
                    margin-bottom: 20px; transition: transform 0.3s ease-in-out; 
                    color: #33691e; font-weight: bold; font-size: 15px;">
            ATS  Predictor
        </div>
    </a>
    """, unsafe_allow_html=True
)


st.sidebar.markdown(
    """
    <a href="https://maths-pred.streamlit.app/" target="_blank" 
       style="text-decoration: none;">
        <div style="border: 1px solid #bbb; padding: 12px; border-radius: 10px; 
                    background: linear-gradient(135deg, #e0f7fa, #e1f5fe); 
                    box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2); 
                    margin-bottom: 20px; transition: transform 0.3s ease-in-out; 
                    color: #004d40; font-weight: bold; font-size: 15px;">
            Maths Marks Predictor
        </div>
    </a>
    """, unsafe_allow_html=True
)

# Contact section
st.header("Contact")
st.write("""
- **Phone**: +91-9977930826  
- **Email**: [aniketvishwakarma459@gmail.com](mailto:aniketvishwakarma459@gmail.com)  
- **LinkedIn**: [LinkedIn Profile](https://www.linkedin.com/in/aniket-vishwakarma-7a222a147/)  
- **GitHub**: [GitHub Profile](https://github.com/Aniket9977)  
- **LeetCode**: [LeetCode Profile](https://leetcode.com/u/Aniket9977/)
""")

# Footer
st.write("---")
st.write("© 2024 Aniket Vishwakarma")
