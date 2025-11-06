from base64 import b64encode
import streamlit as st
from streamlit_option_menu import option_menu
import requests
from streamlit_lottie import st_lottie
from PIL import Image
import base64

def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

st.set_page_config(page_title="Sudipta Giri's Portfolio", layout='wide', page_icon="🦾")

# Correct path to your profile image
profile_path = "images/profile.jpg"

# Load and encode the image once
with open(profile_path, "rb") as f:
    img_data = b64encode(f.read()).decode()

# Display greeting
st.markdown(f"""
<div class="title" style="text-align: center; margin-bottom: 20px;">
    <span style='font-size: 32px;'>Hi, I am Sudipta Giri 👋</span>
</div>
""", unsafe_allow_html=True)

st.markdown('<style>div.block-container{padding-top:4rem;}</style>', unsafe_allow_html=True)

# Display profile image centered
st.markdown(f"""
<div style="display: flex; justify-content: center; margin-bottom: 20px;">
    <img src="data:image/jpeg;base64,{img_data}" 
         alt="Sudipta Giri" 
         style="width: 250px; height: 250px; border-radius: 50%; object-fit: cover; border: 2px solid #ddd;">
</div>
""", unsafe_allow_html=True)

# Load Lottie animations
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coder = load_lottieurl("https://lottie.host/7c9818d3-cd77-49e4-ad3e-4b902a828a5d/ts3NZFkW2o.json")
lottie_contact = load_lottieurl("https://lottie.host/d01c507e-8703-4630-8f23-d363914ec43c/KDLNJvpwQh.json")

# Load project images
image1 = Image.open("images/Screenshot1.png")
image2 = Image.open("images/Screenshot2.png")
image3 = Image.open("images/Screenshot3.png")
image4 = Image.open("images/Screenshot4.png")






# Centered Tagline
st.markdown("""
<div style="text-align: center; font-size: 20px; margin-bottom: 30px;">
Turning Data into Insights & Intelligent Solutions
</div>
""", unsafe_allow_html=True)



st.markdown("""
<div style="
    padding:20px; 
    font-size:18px; 
    line-height:1.8; 
    text-align: justify; 
    color:white; 
    width: 100%;
    margin-bottom: 40px;  /* space after the text */
">
AI/ML enthusiast specializing in predictive modeling, recommendation engines, and computer vision. I love solving complex problems with data and creating intelligent applications that make an impact. When I’m not coding, you’ll find me exploring AI trends or experimenting with small ML projects for fun.
</div>
""", unsafe_allow_html=True)


with st.container():
    selected = option_menu(
        menu_title= None,
        options=['About','Projects','Contact'],
        icons = ['person','code-slash','chat-left-text-fill'],
        orientation='horizontal'
    )
    if selected == 'About':
        with st.container():
            # st.write("##")
            st.subheader("Know Me Better")
            col1, col2 = st.columns([2, 1])  # wider left column for text, smaller right for animation

            # Left Column: Text Content with Cards
            with col1:
                st.markdown("### Skills")
                st.write("""
    - **Programming:** Python, C++, SQL  
    - **ML & AI:** Scikit-Learn, TensorFlow, PyTorch  
    - **Data Visualization:** Tableau, Power BI, Matplotlib  
    - **Web Development:** Streamlit, Flask  
    - **Computer Vision & NLP:** YOLO, CNNs, Transformers  
    """)

                st.markdown("### Education")
                st.write("""
    - **IIT Kharagpur** – M.Tech, Grade: 9.02  
    - **C.K. Pithawala College of Engg. & Tech.** – B.E., Grade: 9.08  
    """)

                st.markdown("### Projects")
                st.write("""
    - Movie Recommender System  
    - Fashion Discovery Engine  
    - Deep Learning-based Computer Vision Models  
    """)

                st.markdown("### Vision")
                st.write("Leverage AI and data science to build innovative solutions with real-world impact.")

            # Right Column: Lottie Animation + Highlights
            with col2:
                st_lottie(lottie_coder, height=350)
                st.markdown("### Highlights")
                st.write("""
    - Built end-to-end ML applications  
    - Strong background in AI & data visualization  
    - Passionate about problem-solving and innovation
    """)

        st.write("---")

    
if selected == 'Projects':
    with st.container():
        st.header("🚀 My Projects")
        st.write("---")

        # Define project data
        projects = [
            {
                "title": "AssistAI Chat Application",
                "image": "images/Screenshot4.png",
                "description": "Built a real-time AI chat application using Streamlit and Ollama API. Users can chat with an AI assistant, with responses streamed live and chat history maintained.",
                "github": "https://github.com/Sudiptagiri24/AssistAI",
                "demo": "#",
                "tech": "Python, Streamlit, Requests, Ollama API"
            },
            {
                "title": "YouTube Transcript Chatbot",
                "image": "images/youtube_transcript.png",
                "description": "An AI-powered chatbot that extracts and analyzes YouTube video transcripts using LangChain and RAG. Users can ask questions and get intelligent answers from any video.",
                "github": "https://github.com/yourusername/youtube-transcript-chatbot",
                "demo": "https://your-streamlit-app-url.streamlit.app/",
                "tech": "Python, Streamlit, LangChain, Hugging Face, YouTube Transcript API"
            },
            {
                "title": "Movie Recommender System",
                "image": "images/Screenshot1.png",
                "description": "Personalized movie recommendations using collaborative and content-based filtering.",
                "github": "https://github.com/Sudiptagiri24/movie-recommender-system",
                "demo": "https://mujyft76zcztupkuoxzigv.streamlit.app/",
                "tech": "Python, Pandas, Scikit-Learn, Streamlit"
            },
            {
                "title": "Fashion Recommender System",
                "image": "images/Screenshot2.png",
                "description": "Deep learning-powered system that finds visually similar fashion items using ResNet50 embeddings.",
                "github": "https://github.com/Sudiptagiri24/Fashion-recommender-system",
                "demo": "https://mainpy-kwxlg4capjfb7kaqknlwlm.streamlit.app/",
                "tech": "TensorFlow, Streamlit, scikit-learn, Google Drive"
            },
            {
                "title": "Startup Funding Dashboard",
                "image": "images/Screenshot3.png",
                "description": "Interactive dashboard visualizing startup funding trends across India with investor insights and year-wise breakdowns.",
                "github": "https://github.com/Sudiptagiri24/startup-dashboard",
                "demo": "https://iswjcdzc4zzeabay4becrb.streamlit.app/",
                "tech": "Python, Pandas, Matplotlib, Streamlit"
            }
        ]

        # Display projects in grid
        cols = st.columns(3)
        for index, project in enumerate(projects):
            img_base64 = get_base64_image(project["image"])

            with cols[index % 3]:
                if img_base64:
                    st.markdown(f"""
                    <div style="
                        background-color: #1E1E1E;
                        padding: 20px;
                        border-radius: 15px;
                        margin-bottom: 30px;
                        box-shadow: 0 4px 10px rgba(0,0,0,0.3);
                        text-align: center;
                        transition: transform 0.3s ease;
                    ">
                        <img src="data:image/png;base64,{img_base64}" 
                                style="width:100%;height:180px;border-radius:10px;object-fit:cover;">
                            <h4 style="margin-top:15px;color:#00BFFF;">{project['title']}</h4>
                            <p style="font-size:15px;color:#ccc;">{project['description']}</p>
                            <p style="font-size:13px;color:#aaa;"><b>Tech:</b> {project['tech']}</p>
                            <a href="{project['demo']}" target="_blank" style="text-decoration:none;margin-right:10px;">
                                <button style="padding:6px 12px;border:none;border-radius:5px;background-color:#00BFFF;color:white;cursor:pointer;">Live Demo</button>
                            </a>
                            <a href="{project['github']}" target="_blank" style="text-decoration:none;">
                                <button style="padding:6px 12px;border:1px solid #00BFFF;border-radius:5px;background-color:transparent;color:#00BFFF;cursor:pointer;">GitHub</button>
                            </a>
                        </div>
                        """, unsafe_allow_html=True)
                else:
                    st.warning(f"⚠️ Image not found: {project['image']}")

    if selected == 'Contact':
        with st.container():
            st.header("Get in Touch")
            st.write("Feel free to reach out for collaborations, projects, or just to say hi! 😊")

            col1, col2 = st.columns([1, 2])  # Lottie left, contact info + form right

            # Left Column: Lottie Animation
            with col1:
                st_lottie(lottie_contact, height=500)

            # Right Column: Contact Info + Form
            with col2:
                social_icons_data = {
                    "LinkedIn": ["https://www.linkedin.com/in/sudipta-giri-992857153/","https://cdn-icons-png.flaticon.com/128/3536/3536505.png"],  # original color
                    "GitHub": ["https://github.com/Sudiptagiri24", "https://cdn-icons-png.flaticon.com/128/733/733553.png"],  # white GitHub icon
                    "Kaggle": ["https://www.kaggle.com/sudiptagiriiitkgp", "https://www.kaggle.com/static/images/site-logo.svg"],
                    "LeetCode": ["https://leetcode.com/u/sudiptagiri/","https://cdn-icons-png.flaticon.com/128/4997/4997543.png"], # white LeetCode icon
                    "Email": ["mailto:sudiptagiri4@gmail.com", "https://cdn-icons-png.flaticon.com/128/732/732200.png"]
                    # white Email icon
                }

                st.write("### Connect with me:")

                # Create columns for the icons
                cols = st.columns(len(social_icons_data))

                for i, (platform, data) in enumerate(social_icons_data.items()):
                    url, icon_url = data
                    with cols[i]:
                        st.markdown(f"""
                        <a href="{url}" target="_blank">
                            <img src="{icon_url}" width="40" style="margin:5px;">
                        </a>
                        """, unsafe_allow_html=True)

                st.write("##")
                st.subheader("Or send me a message directly:")

                # Formsubmit form for direct email
                st.markdown("""
    <form action="https://formsubmit.co/sudiptagiri4@gmail.com" method="POST" target="_blank">
      <input type="text" name="name" placeholder="Your Name" required style="width:100%;padding:8px;margin-bottom:5px;"><br>
      <input type="email" name="email" placeholder="Your Email" required style="width:100%;padding:8px;margin-bottom:5px;"><br>
      <textarea name="message" placeholder="Your Message" required style="width:100%;padding:8px;margin-bottom:5px;"></textarea><br>
      <button type="submit" style="padding:10px 20px;">Send Message</button>
    </form>
    """, unsafe_allow_html=True)



