from together_api import Summarizer
import docx


def read_text_from_docx(file_path):
    """
    Read text from a Word document.
    """
    try:
        doc = docx.Document(file_path)
        paragraphs = [paragraph.text for paragraph in doc.paragraphs]
        return '\n'.join(paragraphs)
    except Exception as e:
        print(f"Error reading document: {e}")
        return None


def summarize_chunk(summarizer, chunk):
    """
    Generate a summary for a chunk of text.
    """
    return summarizer.generate_summary(chunk)




def divide_into_chunks(text, word_per_chunk):
    """
    Divide input text into chunks based on word count.
    """
    chunks = []
    words = text.split()
    num_chunks = len(words) // word_per_chunk
    for i in range(num_chunks):
        start = i * word_per_chunk
        end = (i + 1) * word_per_chunk
        chunks.append(" ".join(words[start:end]))
    # Adding the remaining words as the last chunk
    if len(words) % word_per_chunk != 0:
        chunks.append(" ".join(words[num_chunks * word_per_chunk:]))
    return chunks


def remove_incomplete_sentence(biography):
    """
    Remove incomplete sentence at the end of the biography.
    """
    last_full_stop_index = biography.rfind('.')
    
    if last_full_stop_index != -1:
        return biography[:last_full_stop_index + 1]
    else:
        return biography



# def biography(file_path, word_per_chunk=1000, output_file="summarized_document.docx"):
def biography(input_text, word_per_chunk=1000, output_file="summarized_document.docx"):

    """
    Summarize a document and save the summary to a new document.
    """
    # input_text = read_text_from_docx(file_path)
    # if input_text is None:
    #     return

    summarizer = Summarizer()
    biography = input_text
    while True:
        chunks = divide_into_chunks(biography, word_per_chunk)
        summary = ""
        for chunk in chunks:
            summary += summarize_chunk(summarizer, chunk) + "\n"
        total_tokens = len(summary.split())
        if total_tokens <= 600:
            break
        biography = summary

    
    summary = remove_incomplete_sentence(summary)
    return summary


if __name__ == "__main__":
    document_path = "Transkript_sample.docx"
    biography(document_path)