import streamlit as st
import uet_chatbot

knowledge = uet_chatbot.load_knowledge()

st.set_page_config(page_title="UET Lahore AI Assistant", page_icon="🎓", layout="wide")

st.markdown(
    """
    <style>
    :root {
        --uet-blue: #0b3d91;
        --uet-light-blue: #eaf3ff;
        --uet-border: #c8d8f0;
    }

    [data-testid="stAppViewContainer"] {
        background: #ffffff;
        color: #172033;
    }

    [data-testid="stAppViewContainer"] p,
    [data-testid="stAppViewContainer"] span,
    [data-testid="stAppViewContainer"] label {
        color: #172033;
    }

    [data-testid="stSidebar"] {
        background: var(--uet-blue);
    }

    [data-testid="stSidebar"] * {
        color: #ffffff;
    }

    h1, h2, h3 {
        color: var(--uet-blue);
    }

    [data-testid="stChatMessage"] {
        border: 1px solid var(--uet-border);
        border-radius: 8px;
        background: var(--uet-light-blue);
    }

    [data-testid="stChatInput"] {
        border: 2px solid var(--uet-blue) !important;
        background: #ffffff !important;
    }

    [data-testid="stChatInput"] textarea {
        color: #172033 !important;
        background: #ffffff !important;
        caret-color: var(--uet-blue) !important;
    }

    [data-testid="stChatInput"] textarea::placeholder {
        color: #5c6b82 !important;
        opacity: 1;
    }

    [data-testid="stChatInput"]:focus-within {
        border-color: var(--uet-blue) !important;
        box-shadow: 0 0 0 2px rgba(11, 61, 145, 0.15) !important;
    }

    [data-testid="stSidebar"] button {
        border: 1px solid #ffffff;
        background: #ffffff;
        color: var(--uet-blue) !important;
    }

    [data-testid="stSidebar"] button p,
    [data-testid="stSidebar"] button span {
        color: var(--uet-blue) !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("🎓 UET Lahore AI Assistant")
st.caption("Ask about Admissions, Departments, GPA, Hostels, Timetable")

# Sidebar with UET info
with st.sidebar:
    st.header("Quick Links")
    st.button("Admissions 2026")
    st.button("Departments")
    st.button("GPA Calculator")
    st.button("Contact UET Office")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Assalamualaikum! I'm UET AI. Ask me anything about UET Lahore, UET, admissions, or academics."}
    ]

# Show chat
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# User input
if prompt := st.chat_input("Type your question..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)
    
    ai_reply = uet_chatbot.get_response(prompt, knowledge)
    
    st.session_state.messages.append({"role": "assistant", "content": ai_reply})
    with st.chat_message("assistant"):
        st.write(ai_reply)