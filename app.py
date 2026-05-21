import os
import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader

from langchain.text_splitter import RecursiveCharacterTextSplitter

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from langchain_groq import ChatGroq



load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")

if not groq_api_key:
    st.error("GROQ_API_KEY not found in .env file")
    st.stop()




st.set_page_config(
    page_title="Fast PDF Chatbot",
    page_icon="📄",
    layout="wide"
)



st.markdown("""
<style>

.stTextInput input {
    border-radius: 10px;
}

.stButton button {
    width: 100%;
    border-radius: 10px;
    height: 45px;
    font-size: 16px;
}

</style>
""", unsafe_allow_html=True)




@st.cache_resource
def load_llm():

    model = ChatGroq(
        groq_api_key=groq_api_key,
        model_name="llama-3.1-8b-instant",
        temperature=0
    )

    return model




def get_pdf_text(pdf_docs):

    text = ""

    for pdf in pdf_docs:

        try:

            pdf_reader = PdfReader(pdf)

            for page in pdf_reader.pages:

                page_text = page.extract_text()

                if page_text:
                    text += page_text + "\n"

        except Exception as e:

            st.error(f"PDF Reading Error: {str(e)}")

    return text


#

def get_text_chunks(text):

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    chunks = text_splitter.split_text(text)

    return chunks




def create_vector_store(chunks):

    vectorizer = TfidfVectorizer(
        stop_words="english"
    )

    vectors = vectorizer.fit_transform(chunks)

    st.session_state.chunks = chunks
    st.session_state.vectorizer = vectorizer
    st.session_state.vectors = vectors




def retrieve_relevant_chunks(question, top_k=3):

    question_vector = st.session_state.vectorizer.transform(
        [question]
    )

    similarity = cosine_similarity(
        question_vector,
        st.session_state.vectors
    )[0]

    top_indices = similarity.argsort()[-top_k:][::-1]

    relevant_chunks = []

    for idx in top_indices:

        relevant_chunks.append(
            st.session_state.chunks[idx]
        )

    return "\n\n".join(relevant_chunks)



def user_input(user_question):

    if "chunks" not in st.session_state:

        st.warning("Please upload and process PDF first.")
        return

    try:

        relevant_text = retrieve_relevant_chunks(
            user_question,
            top_k=3
        )

        prompt = f"""
You are a helpful PDF assistant.

Answer the question ONLY from the provided context.

Rules:
1. Give complete and accurate answers.
2. Do not repeat sentences.
3. If answer is partially available, say so.
4. If answer is not available, say:
   "Answer is not available in the context."

Context:
{relevant_text}

Question:
{user_question}

Answer:
"""

        model = load_llm()

        response = model.invoke(prompt)

        st.subheader("Reply")

        st.write(response.content)

    except Exception as e:

        st.error(f"Error: {str(e)}")




def main():

    st.title("Chat with PDF using Groq 🚀")

    user_question = st.text_input(
        "Ask a Question from the PDF Files"
    )

    if user_question:

        with st.spinner("Generating Answer..."):

            user_input(user_question)

  

    with st.sidebar:

        st.header("Menu")

        pdf_docs = st.file_uploader(
            "Upload PDF Files",
            accept_multiple_files=True
        )

        if st.button("Submit & Process"):

            if pdf_docs:

                try:

                    with st.spinner("Processing PDFs..."):

                        # READ PDF
                        raw_text = get_pdf_text(pdf_docs)

                        if not raw_text.strip():

                            st.error("No text found in PDF")
                            return

                        # CHUNKS
                        text_chunks = get_text_chunks(raw_text)

                        # VECTOR STORE
                        create_vector_store(text_chunks)

                        st.success(
                            "PDF Processing Completed Successfully"
                        )

                except Exception as e:

                    st.error(f"Processing Error: {str(e)}")

            else:

                st.warning("Please upload at least one PDF")




if __name__ == "__main__":

    main()
    
    
    
    
    
    
        