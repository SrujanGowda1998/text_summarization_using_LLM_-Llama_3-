import streamlit as st
from data_reader import read_text_from_docx, biography
from docx import Document
import io

# This must be the first Streamlit command used.
st.set_page_config(page_title="Text Summarizer", layout="wide")

# Custom header with HTML and CSS
header_html = """
    <div style="background-color:#47b8d6; padding:10px; border-radius:10px">
    <h1 style="color:white; text-align:center;">Text Summarizer</h1>
    <p style="color:white; text-align:center;">Upload a text file of any length and get a short summary within seconds.</p>
    </div>
    """
st.markdown(header_html, unsafe_allow_html=True)

# Inject CSS for "Generate new biography" button color
st.markdown("""
<style>
.stButton>button {
    border: 1px solid #4CAF50;
    border-radius: 4px; /* Match Streamlit's default button radius */
    color: black; /* Match Streamlit's default button text color */
    background-color: #D0E7D2; /* Custom button color */
    font-size: 16px; /* Adjust to match Streamlit's default button size, if needed */
}
</style>
""", unsafe_allow_html=True)

def create_word_document(biography_text):
    doc = Document()
    doc.add_paragraph(biography_text)
    doc_io = io.BytesIO()
    doc.save(doc_io)
    doc_io.seek(0)
    return doc_io

if 'biography_generated' not in st.session_state:
    st.session_state.biography_generated = False

if not st.session_state.biography_generated:
    uploaded_file = st.file_uploader("Choose a Word file", type=['docx'], key="file_uploader")
    if uploaded_file is not None:
        with st.spinner('Processing the document and generating the summary...'):
            document_text = read_text_from_docx(uploaded_file)
            biography_text = biography(document_text)
            st.session_state.biography_text = biography_text  # Store biography text in session state
            st.session_state.biography_generated = True
            st.experimental_rerun()
else:
    st.success("Summary generated successfully.")
    
    # Add a heading for the biography preview
    st.markdown("""
        <h2 style='text-align: left; margin-top: 20px;'>Summary</h2>
        """, unsafe_allow_html=True)
    
    st.write(st.session_state.biography_text)
    doc_io = create_word_document(st.session_state.biography_text)
    st.download_button(label="Download summary in Word Format",
                       data=doc_io,
                       file_name="Summary.docx",
                       mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document")
    if st.button("Generate new summary"):
        st.session_state.biography_generated = False
        st.session_state.biography_text = ""
        st.experimental_rerun()