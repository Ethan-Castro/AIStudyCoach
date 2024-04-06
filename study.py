import openai
import streamlit as st
from openai import OpenAI

# Fetch the API key securely from Streamlit secrets
api_key = st.secrets["openai_key"]

# Initialize your OpenAI client with the API key
client = OpenAI(api_key=api_key)

def generate_business_simulation(idea):
    response = client.chat.completions.create(
        model="gpt-4-turbo-preview",
        messages=[
            # Your system, user, and assistant messages here
        ],
        temperature=1,
        max_tokens=1451,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    # Process and return the simulation output from the response
    simulation_output = response.choices[0].message['content'].strip()
    return simulation_output

# Your main function for the Streamlit app, etc.


def main():
    st.set_page_config(page_title="Business Idea Simulator", page_icon=":bulb:")
    
    st.markdown(
        """
        <style>
        .title {
            color: #FF4E50;
            font-size: 36px;
            font-weight: bold;
            text-align: center;
            margin-bottom: 20px;
        }
        .description {
            color: #333333;
            font-size: 18px;
            text-align: center;
            margin-bottom: 30px;
        }
        .input-box {
            background-color: #F0F0F0;
            padding: 10px;
            border-radius: 5px;
            margin-bottom: 20px;
        }
        .output-box {
            background-color: #E0F7FA;
            padding: 10px;
            border-radius: 5px;
            margin-bottom: 20px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    st.markdown('<div class="title">Business Idea Simulator</div>', unsafe_allow_html=True)
    st.markdown('<div class="description">Enter your business idea, and let us simulate its execution and performance!</div>', unsafe_allow_html=True)
    
    idea = st.text_input("Enter your business idea:", key="idea_input", placeholder="e.g., A subscription-based service for personalized meal planning")
    
    if st.button("Simulate Business"):
        if idea:
            simulation_output = generate_business_simulation(idea)
            st.markdown(f'<div class="output-box">{simulation_output}</div>', unsafe_allow_html=True)
        else:
            st.warning("Please enter a business idea.")

if __name__ == "__main__":
    main()
