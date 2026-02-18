from openai import AzureOpenAI
import os
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

# Initialize the Azure OpenAI client
client = AzureOpenAI(
    api_key=os.getenv("API_KEY"),
    api_version=os.getenv("API_VERSION"),
    azure_endpoint=os.getenv("BASE_URL")
)
deployment_name = os.getenv("DEPLOYMENT_NAME")

def get_response(conversation):
    messages = [{"role": "system", "content": "You are a helpful assistant."}
    ]
    messages.extend(conversation)
    response = client.chat.completions.create(
        model=deployment_name,
        messages=messages,
        temperature=0.7,
        max_tokens=800
    )
    return response.choices[0].message.content

def main():
    st.set_page_config(
        page_title="Azure OpenAI Chat",
        page_icon="",
        layout="wide"
    )

    st.title(" Azure OpenAI Chat Interface")
    st.markdown("Chat with GPT-5-mini via Azure OpenAI Service")

    # Initialize session state
    if "messages" not in st.session_state:
        st.session_state.messages = []


    # Sidebar
    with st.sidebar:
        st.header(" Settings")
        st.info(f"**Deployment:** {deployment_name}")
        if st.button(" Clear Conversation"):
            st.session_state.messages = []
            st.rerun()


    # Display chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])


    # User input
    if prompt := st.chat_input("Type your message..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)


        # Generate response
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = get_response(st.session_state.messages)
                st.markdown(response)


        st.session_state.messages.append({"role": "assistant", "content": response})


if __name__ == "__main__":
    main()
