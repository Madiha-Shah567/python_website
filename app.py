# import streamlit as st

# st.set_page_config(page_title="🚀 My Python Website", layout="wide")

# st.markdown(
#     """
#     <style>
#         .stApp {
#             background: linear-gradient(45deg, #FF69B4, #4682B4, #BA55D3);
#             background-size: cover;
#             color: white;
#             font-family: Arial, sans-serif;
#         }
#         h1, h2, h3, h4, h5, h6 {
#             color: #FFFFFF !important;
#             text-align: center;
#             font-weight: bold;
#         }
#         .stSidebar {
#             background: linear-gradient(to bottom, #4682B4, #FF69B4, #BA55D3);
#             color: white;
#             padding: 10px;
#             border-radius: 10px;
#         }
#         .footer {
#             text-align: center;
#             font-weight: bold;
#             font-size: 20px;
#             color: white;
#             padding: 10px;
#             background: rgba(0, 0, 0, 0.3);
#             border-radius: 10px;
#         }
#         .stButton>button {
#             background-color: #ff007f;
#             color: white;
#             border-radius: 20px;
#             padding: 10px 20px;
#             font-size: 16px;
#             border: none;
#         }
#         .stTextInput>div>div>input {
#             border-radius: 10px;
#             padding: 10px;
#         }
#     </style>
#     """,
#     unsafe_allow_html=True
# )

# st.sidebar.header("🚀 Navigation")
# page = st.sidebar.radio("🔍 Go to", ["🏠 Home", "💼 Services", "📧 Contact", "ℹ️ About"])

# if page == "🏠 Home":
#     st.title("🌟 Welcome to My Python Website")
#     st.image("https://source.unsplash.com/800x400/?technology,web", use_container_width=True)
#     st.write(
#         """
#         ## 🚀 Explore the Power of Python & Streamlit!
#         - 🖥️ Create web applications effortlessly
#         - 🎨 Interactive UI with minimal code
#         - ⚡ Fast and responsive performance
#         """
#     )
#     st.image("https://source.unsplash.com/800x400/?coding,python", use_container_width=True)

# elif page == "💼 Services":
#     st.header("💡 Our Services")
#     st.write(
#         """
#         We offer the following services:
#         - 🌐 Web Development
#         - 📊 Data Visualization
#         - 🤖 AI & Machine Learning Solutions
#         - 📱 Mobile App Prototyping
#         """
#     )
#     st.image("https://source.unsplash.com/800x400/?ai,technology", use_container_width=True)

# elif page == "📧 Contact":
#     st.header("📞 Contact Us")
#     name = st.text_input("✍️ Your Name")
#     email = st.text_input("📧 Your Email")
#     message = st.text_area("💬 Your Message")
#     if st.button("📨 Send Message", use_container_width=True):
#         st.success("✅ Thank you! We will get back to you soon.")
#     st.image("https://source.unsplash.com/800x400/?customer-service", use_container_width=True)

# elif page == "ℹ️ About":
#     st.header("📜 About This Website")
#     st.write(
#         """
#         - 🐍 Developed with: Python & Streamlit
#         - 🎯 Purpose: To demonstrate how to build a simple web application
#         - ⚙️ Features: Navigation, Forms, and Interactive Content
#         """
#     )
#     st.image("https://source.unsplash.com/800x400/?developer,coding", use_container_width=True)

# st.markdown("---")
# st.markdown("🔋 Powered by Streamlit & Python")
# st.markdown(
#     """
#     <div class='footer'>
#         🎨 Designed by Syeda Madiha
#     </div>
#     """,
#     unsafe_allow_html=True
# )


import streamlit as st

st.set_page_config(page_title="🚀 My Python Website", layout="wide")

st.markdown(
    """
    <style>
        .stApp {
            background: linear-gradient(45deg, #FF69B4, #4682B4, #BA55D3);
            background-size: cover;
            color: white;
            font-family: Arial, sans-serif;
        }
        h1, h2, h3, h4, h5, h6 {
            color: #FFFFFF !important;
            text-align: center;
            font-weight: bold;
        }
        .stSidebar {
            background: linear-gradient(to bottom, #4682B4, #FF69B4, #BA55D3);
            color: white;
            padding: 10px;
            border-radius: 10px;
        }
        .footer {
            text-align: center;
            font-weight: bold;
            font-size: 20px;
            color: white;
            padding: 10px;
            background: rgba(0, 0, 0, 0.3);
            border-radius: 10px;
        }
        .stButton>button {
            background-color: #ff007f;
            color: white;
            border-radius: 20px;
            padding: 10px 20px;
            font-size: 16px;
            border: none;
        }
        .stTextInput>div>div>input {
            border-radius: 10px;
            padding: 10px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.sidebar.header("🚀 Navigation")
page = st.sidebar.radio("🔍 Go to", ["🏠 Home", "💼 Services", "📧 Contact", "ℹ️ About"])

if page == "🏠 Home":
    st.title("🌟 Welcome to My Python Website")
    st.write(
        """
        ## 🚀 Explore the Power of Python & Streamlit!
        - 🖥️ Create web applications effortlessly
        - 🎨 Interactive UI with minimal code
        - ⚡ Fast and responsive performance
        """
    )

elif page == "💼 Services":
    st.header("💡 Our Services")
    st.write(
        """
        We offer the following services:
        - 🌐 Web Development
        - 📊 Data Visualization
        - 🤖 AI & Machine Learning Solutions
        - 📱 Mobile App Prototyping
        """
    )

elif page == "📧 Contact":
    st.header("📞 Contact Us")
    name = st.text_input("✍️ Your Name")
    email = st.text_input("📧 Your Email")
    message = st.text_area("💬 Your Message")
    if st.button("📨 Send Message", use_container_width=True):
        st.success("✅ Thank you! We will get back to you soon.")

elif page == "ℹ️ About":
    st.header("📜 About This Website")
    st.write(
        """
        - 🐍 Developed with: Python & Streamlit
        - 🎯 Purpose: To demonstrate how to build a simple web application
        - ⚙️ Features: Navigation, Forms, and Interactive Content
        """
    )

st.markdown("---")
st.markdown("🔋 Powered by Streamlit & Python")
st.markdown(
    """
    <div class='footer'>
        🎨 Designed by Syeda Madiha
    </div>
    """,
    unsafe_allow_html=True
)
