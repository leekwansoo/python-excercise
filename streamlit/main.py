# Main File for Streamlit App Service
import streamlit as st
import pandas as pd 
import matplotlib.pyplot as plt
import base64
try:
    from PyPDF2 import PdfReader
    PYPDF2_AVAILABLE = True
except ImportError:
    PYPDF2_AVAILABLE = False 
# excel and csv file processing
def file_process_csv(file_path):
    # save this file in the data directory
    data = pd.read_csv(file_path)
    df = pd.DataFrame(data)
    st.write("Displaying CSV file...")
    st.write(df.head())
    # df.plot(kind="scatter", x="sepal_length", y="sepal_width")
    # st.write(f"{df.head()}")
    df.plot(kind="scatter", x=df.columns[0], y=df.columns[1])
    st.pyplot(plt.gcf()) # Display the current figure
    plt.close()  # Close the figure to free memory
    return {"result": "CSV file processed successfully!"}

def extract_text_from_pdf(file_path):
    """Extract text content from PDF file"""
    if not PYPDF2_AVAILABLE:
        return "PyPDF2 not available. Install it with: pip install PyPDF2"
    
    try:
        reader = PdfReader(file_path)
        text_content = ""
        
        for page_num, page in enumerate(reader.pages, 1):
            text = page.extract_text()
            text_content += f"\n--- Page {page_num} ---\n{text}\n"
        
        return text_content
    except Exception as e:
        return f"Error extracting text: {str(e)}"

def file_process_pdf(file):
    st.write("Processing PDF file...")
    
    # Add option to choose display method
    display_option = st.radio(
        "How would you like to view the PDF?",
        ["Embedded PDF Viewer", "Extract Text Content", "Download Only"],
        key="pdf_display_option"
    )
    
    try:
        # Read the PDF file as binary
        with open(file, "rb") as f:
            pdf_bytes = f.read()
        
        if display_option == "Embedded PDF Viewer":
            # Encode PDF to base64 for embedding
            base64_pdf = base64.b64encode(pdf_bytes).decode('utf-8')
            
            # Display PDF using HTML iframe
            pdf_display = f'''
            <iframe src="data:application/pdf;base64,{base64_pdf}" 
                    width="700" height="800" type="application/pdf">
            </iframe>
            '''
            
            st.write("Displaying PDF file:")
            st.markdown(pdf_display, unsafe_allow_html=True)
            
        elif display_option == "Extract Text Content":
            st.write("Extracting text from PDF...")
            text_content = extract_text_from_pdf(file)
            
            st.text_area("PDF Text Content:", text_content, height=400)
            
        elif display_option == "Download Only":
            st.write("PDF saved successfully. Use the download button below.")
        
        # Always provide a download button
        st.download_button(
            label="Download PDF",
            data=pdf_bytes,
            file_name=file.split('/')[-1] if '/' in file else file.split('\\')[-1],  # Handle both path separators
            mime="application/pdf"
        )
        
        return {"result": f"PDF file processed successfully! File size: {len(pdf_bytes)} bytes"}
        
    except Exception as e:
        st.error(f"Error processing PDF: {str(e)}")
        return {"result": f"Error processing PDF: {str(e)}"}

