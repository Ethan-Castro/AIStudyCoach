import openai
import streamlit as st

openai.api_key = st.secrets['openai_key']

# Streamlit app
def main():
    st.title("Academic Coach Chatbot")
    st.write("This chatbot is here to help you excel academically using resources from top institutions and professionals.")

    user_input = st.text_input("Hey! Introduce yourself, and let me know what you need help on.")
    if user_input:
        response = get_openai_response(user_input)
        st.write(f"Bot: {response}")

def get_openai_response(user_message):
    """Get a response from OpenAI's GPT-4 model using the ChatCompletion method."""
    response = openai.ChatCompletion.create(
        model="gpt-4", 
        messages=[
    {
      "role": "system",
      "content": "Hey! I'm your coach. I want to see you do your best, and I will do whatever I can to make that happen.\n\nUse resources like the Harvard Academic Resource Center's website, other IVY League school tips, as well as top tips from proven professionals.\n\nAlways give clear precise instructions and motivation."
    },
    {
      "role": "user",
      "content": "Hey, I am Ethan and I go to Brooklyn College. I am double majoring in Health & Nutrition Science as well as Computer Science"
    },
    {
      "role": "assistant",
      "content": "Hi Ethan, it's nice to meet you! That's impressive, tackling two demanding yet varied fields like Health & Nutrition Science and Computer Science. It's clear you have a diverse range of interests. How can I support your academic journey? \nAre you looking for help to balance these two studies or support in a specific subject? Maybe you need assistance with managing time or reducing stress? Please let me know, so we can devise a plan that will maximize your academic success."
    },
    {
      "role": "user",
      "content": "Hey! I am doing pretty good in everything, the only issue is my school is not challenging enough. Is there any way you can help me with that?"
    },
    {
      "role": "assistant",
      "content": """Ethan, to challenge yourself:
1. Take advanced or grad courses.
2. Explore Ivy League online courses.
3. Join research projects.
4. Engage in academic clubs or societies.
5. Participate in events like Hackathons.
6. Teach or tutor."""
    }
  ],
  temperature=1,
  max_tokens=1000,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
    return response.choices[0].message['content']

if __name__ == "__main__":
    main()
