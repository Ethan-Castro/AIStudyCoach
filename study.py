import openai
import streamlit as st

# Assuming you have a custom OpenAI client setup as per your project's structure
from openai import OpenAI

# Fetch the API key securely from Streamlit secrets
api_key = st.secrets["openai_key"]

# Initialize your OpenAI client with the API key
client = OpenAI(api_key=api_key)

def generate_business_simulation(idea):
    messages = [
        {
             "role": "system",
             "content": "The point of the program is that someone gives in their business or product Idea, and you will give, what each person does, and have each person do the task, then make an executive summary. [Detailed roles description here]"
        },
        {
             "role": "user",
             "content": idea
        }
    ]

    if not idea.strip():
        return "Error: The idea provided is empty. Please provide a valid business idea."

    try:
        response = client.chat.completions.create(
            model="gpt-4-turbo-preview",
            messages=messages,
            temperature=1,
            max_tokens=1451,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        # Correct way to access the response content
        simulation_output = response.choices[0].message.content.strip()
        return simulation_output
    except Exception as e:
        print(f"An error occurred: {e}")
        return "An error occurred while processing your request. Please try again."

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
