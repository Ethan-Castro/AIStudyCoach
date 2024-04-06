import openai
import streamlit as st
from openai import OpenAI
api = st.secrets["openai_key"]
client = OpenAI(api)

def generate_business_simulation(idea):
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {
                "role": "system",
                "content": "The point of the program is that someone gives in their business or product Idea, and you will make code to give it the team, what each person does, and have each person do the task. CEO: Our visionary CEO is a dynamic leader who sets the strategic direction for the company. With a keen eye for innovation and a passion for driving growth, they inspire the team to push boundaries and achieve extraordinary results. The CEO's strong business acumen, coupled with their ability to make bold decisions, has been instrumental in positioning the company as a market leader. Project Manager: The Project Manager is a highly organized and efficient individual who ensures the smooth execution of projects across the company. With exceptional communication skills and a meticulous attention to detail, they coordinate cross-functional teams, set clear goals, and manage timelines and resources effectively. The Project Manager's proactive approach and ability to anticipate challenges have been crucial in delivering successful outcomes consistently. Engineers: Our talented team of engineers comprises skilled professionals who are at the forefront of technological innovation. With diverse expertise spanning software development, hardware design, and system architecture, they collaborate to create cutting-edge solutions that address complex problems. The engineers' deep technical knowledge, coupled with their creativity and problem-solving abilities, enables them to develop robust and scalable products that exceed customer expectations. Sales Team: The sales team consists of persuasive and customer-centric individuals who are passionate about driving revenue growth. With exceptional interpersonal skills and a deep understanding of the market, they build strong relationships with clients and identify opportunities for collaboration. The sales team's ability to articulate the value proposition of our products and services, combined with their negotiation prowess, has been instrumental in expanding our customer base and driving business success. Marketing Team: Our creative and data-driven marketing team is responsible for crafting compelling brand narratives and executing impactful campaigns. With a deep understanding of consumer behavior and market trends, they develop strategies that resonate with our target audience and differentiate us from competitors. The marketing team's expertise in digital marketing, content creation, and brand management has been crucial in building brand awareness, generating leads, and fostering customer loyalty. HR Team: The HR team is dedicated to creating a positive and inclusive work environment that nurtures talent and drives employee engagement. With a focus on attracting, developing, and retaining top talent, they implement progressive HR policies and initiatives that align with our company values. The HR team's commitment to employee well-being, professional development, and diversity and inclusion has been instrumental in building a high-performing and motivated workforce."
            },
            {
                "role": "user",
                "content": idea
            }
        ],
        temperature=0.7,
        max_tokens=1500,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    simulation_output = response.choices[0].message.content.strip()
    return simulation_output

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
