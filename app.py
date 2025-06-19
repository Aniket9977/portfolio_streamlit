import streamlit as st

# Create a two-column layout
col1, col2 = st.columns([1, 2])

# Add photo in the first column
with col1:
    st.image("image/IMG_20240720_201333_050.jpg", width=200)  

    # Add a download button for the resume below the photo
    try:
        with open("image/AniketVishwakarmaEcp.pdf", "rb") as file:
            st.download_button(
                label="Download Resume",
                data=file,
                file_name="AniketVishwakarmaEcp.pdf",
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

# Education section
st.subheader("Education")
st.write("""
- **Bachelor of Technology in Artificial Intelligence and Data Science**  
  Jabalpur Engineering College (2021-2025)  
  CGPA: 7.81
""")

# Experience section
st.subheader("Experience")
st.write("""
- **AI Engineer (Intern)**  
  INeuron.ai (February 2024 - March 2025)  
  - Orchestrated end-to-end GenAI workflows using Apache Airflow, enabling automated data ingestion, model inference and result delivery
  - Fine-tuned a transformer-based language model on domain-specific educational datasets, resulting in a 25% improvement in response coherence and factual accuracy.

- **Head Coordinator (E-CELL)**  
  Jabalpur Engineering College (April 2024 - April 2025)  
  - Managed a team of 15 to organize 5+ events, increasing student engagement in entrepreneurial activities.  
  - Developed initiatives that boosted student participation in innovation challenges.

- **Rajasthan IT Day (Hackathon)**  
  Rajasthan Government (March 2023)  
  - Designed a model to optimize fuel consumption, achieving a potential savings of up to 10% in preliminary testing.  
  - Learned networking and pitching projects.
""")

# Projects section
st.subheader("Projects")
st.write("""
- **AI-Powered SQL Query Generation (Gemini and SQL)**  
  Developed an application utilizing Google’s Gemini model to convert natural language queries into SQL.  
  - Convert user questions into accurate SQL queries, optimizing database interactions and data accessibility.
  - Allows users to input queries, upload Excel files, and preview data before ingestion.
  - **Technology Used**: GenAI, SQLite3, Pandas

- **Remote Proctoring System with Real-Time Facial Landmark Detection (OpenCV)**  
  Engineered a proctoring system for tracking facial landmarks to enhance cheating detection accuracy.  
  - Developed an application to leverage facial landmarks to monitor eye and mouth activities.  
  - Utilized metrics to detect suspicious activities, enhancing the accuracy of remote proctoring systems.  
  - **Technology Used**: Python, OpenCV, Dlib, Machine Learning

- **RAG Document with Groq and Lama**  
  Document Q&A powered by RAG with Groq and Lama for precise retrieval-based responses.  
  - Built modular backend services for QA, theme identification, and document routing with FastAPI.
  - Enabled real-time Q&A and thematic insights over uploaded documents via LangChain and OpenAI APIs.
  -Containerized the application with Docker and managed environment configurations using .env files.
  - **Technology Used**: LangChain,OpenAI API,FAISS,Python
""")

# Technical Skills section
st.subheader("Technical Skills and Interests")
st.write("""
- **Languages**: Python, SQL  
- **Data Analytics and Visualization**: NumPy, Pandas, EDA, PowerBI, MS Excel, SQL, Matplotlib, Seaborn  
- **Deep Learning**: NLP, LSTM, CNNs, RNNs, TensorFlow, Keras, Neural Networks, Hugging Face, Transformers, BERT, GPT, PyTorch, OpenCV  
- **Gen-AI**: LLMs, GANs, LangChain, Llama Index, Gemini Pro, LangGraph, RAG  
- **MLOps**: Model Deployment, Monitoring, Automation, AWS SageMaker, AWS S3, AWS EC2, AWS Lambda, CI/CD for ML, Docker, Azure, GCP, GitHub, MLflow
""")

# Achievements section
st.subheader("Achievements")
st.write("""
- **GATE 2024 Qualified**  
- **Certified ML Mentor**  
- **LeetCode**: Solved 250+ questions  
- **Hackathon Semi-Finalist**
""")

# Sidebar for Streamlit Projects
st.sidebar.title("My Deployed Projects")
st.sidebar.write("Check out my live apps:")
st.sidebar.markdown(
    """
    <a href="https://llm-with-sql.streamlit.app/" target="_blank" 
       style="text-decoration: none;">
        <div style="border: 1px solid #bbb; padding: 12px; border-radius: 10px; 
                    background: linear-gradient(135deg, #e0f7fa, #e1f5fe); 
                    box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2); 
                    margin-bottom: 20px; transition: transform 0.3s ease-in-out; 
                    color: #004d40; font-weight: bold; font-size: 15px;">
            SQL Query Generation
        </div>
    </a>
    """, unsafe_allow_html=True
)
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
    <a href="https://rag-with-openai.streamlit.app/" target="_blank" 
       style="text-decoration: none;">
        <div style="border: 1px solid #bbb; padding: 12px; border-radius: 10px; 
                    background: linear-gradient(135deg, #e0f7fa, #e1f5fe); 
                    box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2); 
                    margin-bottom: 20px; transition: transform 0.3s ease-in-out; 
                    color: #004d40; font-weight: bold; font-size: 15px;">
            Document Research System
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
st.write("© 2024 Aniket Vishwakarma ")
