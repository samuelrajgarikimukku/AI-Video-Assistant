import streamlit as st
from main import run_pipeline
from core.RAG_engine import ask_question
from utils.cleanup import cleanup

st.set_page_config(
    page_title="AI Video Assistant",
    page_icon="🎥",
    layout="wide"
)

st.title("🎥 AI Video Assistant")
st.caption("Whisper + LangChain + Chroma + RAG")

source = st.text_input(
    "Enter YouTube URL or Local Audio Path"
)

if "result" not in st.session_state:
    st.session_state.result = None

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if st.button("Analyze Video", use_container_width=True):

    if not source:
        st.warning("Please enter a YouTube URL or file path.")
        st.stop()

    with st.spinner("Processing video... This may take a few minutes..."):

        result = run_pipeline(source)
        st.session_state.result = result
        st.session_state.chat_history = []

    st.success("Analysis Complete!")

if st.session_state.result:

    result = st.session_state.result

    st.header(result["title"])

    tab1, tab2 = st.tabs(["📄 Summary", "💬 Chat"])

    with tab1:

        with st.expander("Summary", expanded=True):
            st.markdown(result["summary"])

        with st.expander("Action Items"):
            st.markdown(result["action_items"])

        with st.expander("Key Decisions"):
            st.markdown(result["key_decisions"])

        with st.expander("Open Questions"):
            st.markdown(result["open_questions"])

    with tab2:

        question = st.chat_input("Ask something about the video...")

        if question:

            st.session_state.chat_history.append(
                ("user", question)
            )

            answer = ask_question(
                result["rag_chain"],
                question
            )

            st.session_state.chat_history.append(
                ("assistant", answer)
            )

        for role, message in st.session_state.chat_history:

            with st.chat_message(role):
                st.markdown(message)