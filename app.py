import streamlit as st
import os
import markdown
from pathlib import Path
import base64
from datetime import datetime
import pdfkit
import tempfile
from io import BytesIO
import weasyprint
from markdown import markdown as md_to_html
import re

# Page configuration
st.set_page_config(
    page_title="Medical Lab Markdown Manager",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(90deg, #2E86AB, #A23B72);
        padding: 1rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
    }
    .file-info {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 5px;
        border-left: 4px solid #2E86AB;
        margin: 1rem 0;
    }
    .download-section {
        background-color: #e8f4f8;
        padding: 1.5rem;
        border-radius: 10px;
        margin-top: 2rem;
    }
    .medical-theme {
        border-left: 4px solid #dc3545;
        padding-left: 1rem;
        background-color: #f8f9fa;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

def get_file_list(directory=".", extensions=[".md", ".markdown"]):
    """Get list of markdown files in directory"""
    files = []
    for ext in extensions:
        files.extend(Path(directory).glob(f"*{ext}"))
    return sorted([str(f) for f in files])

def load_markdown_file(file_path):
    """Load and return markdown file content"""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except Exception as e:
        st.error(f"Error loading file: {str(e)}")
        return None

def markdown_to_html(md_content):
    """Convert markdown to HTML with medical lab styling"""
    # Configure markdown extensions
    extensions = [
        'markdown.extensions.tables',
        'markdown.extensions.fenced_code',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc',
        'markdown.extensions.attr_list'
    ]
    
    html = markdown.markdown(md_content, extensions=extensions)
    
    # Add custom CSS for medical lab documents
    css_style = """
    <style>
        body { 
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: #333;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
        }
        h1 { 
            color: #2E86AB;
            border-bottom: 3px solid #2E86AB;
            padding-bottom: 10px;
        }
        h2 { 
            color: #A23B72;
            border-bottom: 1px solid #A23B72;
            padding-bottom: 5px;
        }
        h3 { color: #dc3545; }
        table {
            border-collapse: collapse;
            width: 100%;
            margin: 20px 0;
        }
        th, td {
            border: 1px solid #ddd;
            padding: 12px;
            text-align: left;
        }
        th {
            background-color: #2E86AB;
            color: white;
        }
        tr:nth-child(even) {
            background-color: #f2f2f2;
        }
        .medical-highlight {
            background-color: #fff3cd;
            border-left: 4px solid #ffc107;
            padding: 10px;
            margin: 10px 0;
        }
        code {
            background-color: #f8f9fa;
            padding: 2px 4px;
            border-radius: 3px;
            font-family: 'Courier New', monospace;
        }
        pre {
            background-color: #f8f9fa;
            padding: 15px;
            border-radius: 5px;
            overflow-x: auto;
        }
        blockquote {
            border-left: 4px solid #2E86AB;
            margin: 0;
            padding-left: 20px;
            font-style: italic;
            color: #666;
        }
    </style>
    """
    
    return css_style + html

def create_pdf_from_html(html_content, filename="document.pdf"):
    """Convert HTML to PDF using WeasyPrint"""
    try:
        # Create PDF in memory
        pdf_buffer = BytesIO()
        weasyprint.HTML(string=html_content).write_pdf(pdf_buffer)
        pdf_buffer.seek(0)
        return pdf_buffer.getvalue()
    except Exception as e:
        st.error(f"Error creating PDF: {str(e)}")
        return None

def create_download_link(content, filename, link_text="Download"):
    """Create a download link for file content"""
    b64 = base64.b64encode(content).decode()
    href = f'<a href="data:application/octet-stream;base64,{b64}" download="{filename}">{link_text}</a>'
    return href

def extract_metadata(md_content):
    """Extract metadata from markdown content"""
    metadata = {}
    
    # Extract title (first # heading)
    title_match = re.search(r'^#\s+(.+)$', md_content, re.MULTILINE)
    if title_match:
        metadata['title'] = title_match.group(1)
    
    # Count words
    word_count = len(re.findall(r'\b\w+\b', md_content))
    metadata['word_count'] = word_count
    
    # Count headings
    heading_count = len(re.findall(r'^#{1,6}\s+', md_content, re.MULTILINE))
    metadata['heading_count'] = heading_count
    
    # Estimate reading time (average 200 words per minute)
    metadata['reading_time'] = max(1, round(word_count / 200))
    
    return metadata

def main():
    # Header
    st.markdown("""
    <div class="main-header">
        <h1>🏥 Medical Lab Markdown Manager</h1>
        <p>Load, View, Edit, and Convert Markdown Files to PDF</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Sidebar
    st.sidebar.title("📁 File Manager")
    
    # File selection method
    file_method = st.sidebar.radio(
        "Choose file input method:",
        ["Select from directory", "Upload file", "Create new"]
    )
    
    md_content = None
    filename = None
    
    if file_method == "Select from directory":
        # Get list of markdown files
        md_files = get_file_list()
        
        if md_files:
            selected_file = st.sidebar.selectbox(
                "Select a markdown file:",
                md_files,
                format_func=lambda x: os.path.basename(x)
            )
            
            if selected_file:
                filename = os.path.basename(selected_file)
                md_content = load_markdown_file(selected_file)
        else:
            st.sidebar.warning("No markdown files found in current directory")
    
    elif file_method == "Upload file":
        uploaded_file = st.sidebar.file_uploader(
            "Upload a markdown file",
            type=['md', 'markdown', 'txt'],
            help="Upload your markdown file to view and convert"
        )
        
        if uploaded_file:
            filename = uploaded_file.name
            md_content = uploaded_file.read().decode('utf-8')
    
    elif file_method == "Create new":
        filename = st.sidebar.text_input("Filename:", value="new_document.md")
        st.sidebar.markdown("**Create new markdown content below:**")
        md_content = ""  # Will be handled in the editor
    
    # Main content area
    if md_content is not None or file_method == "Create new":
        # Create tabs
        tab1, tab2, tab3, tab4 = st.tabs(["📝 Editor", "👀 Preview", "📊 Info", "📥 Download"])
        
        with tab1:
            st.subheader("Markdown Editor")
            
            if file_method == "Create new":
                # Template selection for new files
                template = st.selectbox(
                    "Select a template:",
                    [
                        "Blank",
                        "Medical Lab Memo",
                        "Training Session",
                        "Lab Report",
                        "Meeting Notes"
                    ]
                )
                
                templates = {
                    "Medical Lab Memo": """# MEMORANDUM

**TO:** Medical Laboratory Staff  
**FROM:** [Your Name]  
**DATE:** {}  
**RE:** [Subject]

## Introduction

[Your content here]

## Key Points

- Point 1
- Point 2
- Point 3

## Action Items

- [ ] Task 1
- [ ] Task 2
- [ ] Task 3

---

**Contact:** [Your contact information]
""".format(datetime.now().strftime("%B %d, %Y")),
                    
                    "Training Session": """# Training Session: [Topic]

**Date:** {}  
**Duration:** [Duration]  
**Instructor:** [Name]

## Learning Objectives

- Objective 1
- Objective 2
- Objective 3

## Session Content

### Introduction
[Content]

### Main Topics
[Content]

### Practical Exercises
[Content]

## Resources

- Resource 1
- Resource 2

## Assessment

[Assessment criteria]
""".format(datetime.now().strftime("%B %d, %Y")),
                    
                    "Lab Report": """# Laboratory Report

**Sample ID:** [ID]  
**Date:** {}  
**Technician:** [Name]

## Test Results

| Test | Result | Reference Range | Status |
|------|--------|-----------------|--------|
| Test 1 | [Value] | [Range] | [Normal/Abnormal] |
| Test 2 | [Value] | [Range] | [Normal/Abnormal] |

## Observations

[Your observations]

## Conclusions

[Your conclusions]

## Recommendations

[Your recommendations]
""".format(datetime.now().strftime("%B %d, %Y"))
                }
                
                if template != "Blank" and template in templates:
                    md_content = templates[template]
            
            # Markdown editor
            edited_content = st.text_area(
                "Edit your markdown content:",
                value=md_content if md_content else "",
                height=500,
                help="Write your markdown content here. Use standard markdown syntax."
            )
            
            # Update content
            md_content = edited_content
            
            # Save functionality
            if st.button("💾 Save Changes"):
                if filename and md_content:
                    try:
                        with open(filename, 'w', encoding='utf-8') as f:
                            f.write(md_content)
                        st.success(f"✅ File saved successfully: {filename}")
                    except Exception as e:
                        st.error(f"❌ Error saving file: {str(e)}")
        
        with tab2:
            st.subheader("Markdown Preview")
            if md_content:
                # Render markdown
                st.markdown(md_content, unsafe_allow_html=True)
            else:
                st.info("No content to preview. Please add some markdown content in the Editor tab.")
        
        with tab3:
            st.subheader("Document Information")
            
            if md_content:
                metadata = extract_metadata(md_content)
                
                col1, col2 = st.columns(2)
                
                with col1:
                    st.markdown("""
                    <div class="file-info">
                        <h4>📄 File Details</h4>
                        <p><strong>Filename:</strong> {}</p>
                        <p><strong>Size:</strong> {} characters</p>
                        <p><strong>Lines:</strong> {}</p>
                    </div>
                    """.format(
                        filename or "Untitled",
                        len(md_content),
                        md_content.count('\n') + 1
                    ), unsafe_allow_html=True)
                
                with col2:
                    st.markdown("""
                    <div class="file-info">
                        <h4>📊 Content Analysis</h4>
                        <p><strong>Words:</strong> {}</p>
                        <p><strong>Headings:</strong> {}</p>
                        <p><strong>Reading time:</strong> {} min</p>
                    </div>
                    """.format(
                        metadata.get('word_count', 0),
                        metadata.get('heading_count', 0),
                        metadata.get('reading_time', 0)
                    ), unsafe_allow_html=True)
                
                # Title if found
                if 'title' in metadata:
                    st.markdown(f"""
                    <div class="medical-theme">
                        <h4>📋 Document Title</h4>
                        <p><strong>{metadata['title']}</strong></p>
                    </div>
                    """, unsafe_allow_html=True)
        
        with tab4:
            st.subheader("Download Options")
            
            if md_content:
                st.markdown("""
                <div class="download-section">
                    <h4>📥 Available Download Formats</h4>
                </div>
                """, unsafe_allow_html=True)
                
                col1, col2 = st.columns(2)
                
                with col1:
                    # Markdown download
                    st.markdown("**📝 Markdown Format**")
                    md_bytes = md_content.encode('utf-8')
                    st.download_button(
                        label="Download as .md",
                        data=md_bytes,
                        file_name=filename or "document.md",
                        mime="text/markdown"
                    )
                    
                    # HTML download
                    st.markdown("**🌐 HTML Format**")
                    html_content = markdown_to_html(md_content)
                    st.download_button(
                        label="Download as .html",
                        data=html_content.encode('utf-8'),
                        file_name=filename.replace('.md', '.html') if filename else "document.html",
                        mime="text/html"
                    )
                
                with col2:
                    # PDF download
                    st.markdown("**📄 PDF Format**")
                    
                    if st.button("🔄 Generate PDF"):
                        with st.spinner("Generating PDF..."):
                            try:
                                html_content = markdown_to_html(md_content)
                                pdf_content = create_pdf_from_html(html_content)
                                
                                if pdf_content:
                                    st.download_button(
                                        label="Download PDF",
                                        data=pdf_content,
                                        file_name=filename.replace('.md', '.pdf') if filename else "document.pdf",
                                        mime="application/pdf"
                                    )
                                    st.success("✅ PDF generated successfully!")
                                else:
                                    st.error("❌ Failed to generate PDF")
                            except Exception as e:
                                st.error(f"❌ Error generating PDF: {str(e)}")
                                st.info("💡 Try installing WeasyPrint: pip install weasyprint")
                
                # Advanced options
                st.markdown("---")
                st.markdown("**⚙️ Advanced Options**")
                
                if st.checkbox("Include metadata in downloads"):
                    metadata = extract_metadata(md_content)
                    st.json(metadata)
                
                if st.checkbox("Custom CSS for PDF"):
                    custom_css = st.text_area(
                        "Custom CSS:",
                        value="/* Add your custom CSS here */",
                        height=100
                    )
            else:
                st.info("Please load or create markdown content to enable downloads.")
    
    else:
        # Welcome screen
        st.markdown("""
        ## Welcome to Medical Lab Markdown Manager! 🏥
        
        This application helps you manage markdown files for medical laboratory documentation:
        
        ### Features:
        - 📝 **Edit** markdown files with syntax highlighting
        - 👀 **Preview** rendered markdown content
        - 📊 **Analyze** document statistics and metadata
        - 📥 **Download** in multiple formats (MD, HTML, PDF)
        - 🏥 **Medical templates** for lab documentation
        
        ### Getting Started:
        1. Use the sidebar to select a file input method
        2. Choose or upload a markdown file
        3. Edit, preview, and download as needed
        
        ### Supported File Types:
        - `.md` - Markdown files
        - `.markdown` - Markdown files
        - `.txt` - Text files
        """)
        
        # Show available files
        md_files = get_file_list()
        if md_files:
            st.markdown("### 📁 Available Files:")
            for file in md_files[:10]:  # Show first 10 files
                st.markdown(f"- `{os.path.basename(file)}`")
            if len(md_files) > 10:
                st.markdown(f"... and {len(md_files) - 10} more files")

if __name__ == "__main__":
    main()