import streamlit as st
import google.generativeai as genai
from openai import OpenAI
from apikey import google_gemini_api_key, open_api_key

client = OpenAI(api_key=open_api_key)

genai.configure(api_key=google_gemini_api_key)

def generate(blog_title, keywords, num_words):

    model = genai.GenerativeModel("gemini-2.5-pro")

    prompt = f"""
    Generate a comprehensive, engaging blog post relevant to the given title "{blog_title}"
    and keywords "{keywords}". Make sure to incorporate these keywords in the blog post.
    The blog should be approximately {num_words} words in length, suitable for an online audience.
    Ensure the content is original, informative, and maintains a consistent tone throughout.
    """

    response = model.generate_content(prompt)

    return response.text if response and response.text else "No content generated."

st.set_page_config(layout="wide", page_title="AI Blogger")

# Title and header
st.title("AI Blogger Companion")
st.subheader("Generate Blog Posts with AI")

# Sidebar inputs
with st.sidebar:
    st.title("Blog Settings")
    st.subheader("Enter the details for your blog post")

    blog_title = st.text_input("Blog Title", placeholder="Enter the title of your blog")
    
    keywords = st.text_area("Keywords (comma separated)", placeholder="Enter keywords related to your blog")
    
    num_words = st.slider("Number of Words", min_value=250, max_value=1000, step=100)
    
    # num_images = st.number_input("Number of Images", min_value=0, max_value=5, step=1)
    
    submit_button = st.button("Generate Blog")

if submit_button:
    if not blog_title.strip() or not keywords.strip():
        st.error("Please enter both a blog title and keywords before generating.")
    else:
        with st.spinner("Generating your blog... Please wait."):
            blog_content = generate(blog_title, keywords, num_words)

        # Display the generated blog
        st.markdown("## ✨ Generated Blog Post")
        st.markdown(blog_content)

        # Optional: Display placeholder for images
        # if num_images > 0:
        #     image_prompt = f"An artistic illustration for the blog titled '{blog_title}', focusing on {keywords}"
        #     response = client.images.generate(
        #         model="gpt-image-1",
        #         prompt=image_prompt,      
        #         size="1024x1024"
        #     )
        #     image_url = response.data[0].url

        #     st.image(image_url, caption="Generated Image", use_column_width=True)

        #     st.title("Your Blog Post:")
            