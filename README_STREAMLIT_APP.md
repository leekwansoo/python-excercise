# 🏥 Medical Lab Markdown Manager

A comprehensive Streamlit application for managing markdown files in medical laboratory environments. Load, edit, preview, and convert markdown documents to PDF with specialized medical lab templates.

## ✨ Features

### 📝 **Markdown Editor**
- Syntax-highlighted markdown editing
- Real-time preview
- Medical lab templates (Memo, Training Session, Lab Report)
- Auto-save functionality

### 👀 **Live Preview**
- Rendered markdown with medical lab styling
- Professional formatting for medical documents
- Support for tables, code blocks, and medical terminology

### 📊 **Document Analysis**
- Word count and reading time estimation
- Heading structure analysis
- Metadata extraction
- File size and statistics

### 📥 **Multi-Format Export**
- **Markdown (.md)** - Original format
- **HTML (.html)** - Web-ready format with custom CSS
- **PDF (.pdf)** - Professional print-ready documents

### 🏥 **Medical Lab Focus**
- Templates for lab memos, training materials, and reports
- Medical terminology support
- Professional styling for clinical documents
- Compliance-ready formatting

## 🚀 Quick Start

### Installation

1. **Run the setup script:**
   ```bash
   python setup.py
   ```

2. **Or install manually:**
   ```bash
   pip install -r requirements.txt
   ```

### Launch the Application

```bash
streamlit run app.py
```

Your browser will open to `http://localhost:8501`

## 📋 Usage Guide

### 1. **Load Files**
- **Select from directory**: Choose from existing .md files
- **Upload file**: Browse and upload markdown files
- **Create new**: Start with templates or blank document

### 2. **Edit Content**
- Use the built-in editor with syntax highlighting
- Apply medical lab templates for standard documents
- Save changes directly to files

### 3. **Preview & Analyze**
- View rendered markdown with professional styling
- Check document statistics and metadata
- Verify formatting before export

### 4. **Export Documents**
- Download as markdown, HTML, or PDF
- Apply custom styling for professional appearance
- Generate reports ready for medical lab use

## 🏥 Medical Lab Templates

### **Lab Memo Template**
Professional memorandum format for laboratory communications

### **Training Session Template**
Structured format for educational materials and session plans

### **Lab Report Template**
Standardized reporting format with test results tables

### **Meeting Notes Template**
Organized format for laboratory meetings and documentation

## 🛠️ Technical Requirements

### **Dependencies**
- Python 3.7+
- Streamlit 1.28+
- Markdown 3.5+
- WeasyPrint 60+ (for PDF generation)

### **Optional Dependencies**
- PDFKit + wkhtmltopdf (alternative PDF generation)
- Pillow (image processing)
- ReportLab (advanced PDF features)

## 💡 Tips & Best Practices

### **For Medical Lab Use**
1. **Standardization**: Use templates for consistent documentation
2. **Version Control**: Save different versions with date stamps
3. **Backup**: Regular backups of important documents
4. **Compliance**: Follow institutional guidelines for documentation

### **Performance Tips**
1. **Large Files**: Break large documents into sections
2. **PDF Generation**: May take time for complex documents
3. **File Organization**: Keep related files in the same directory

### **Troubleshooting PDF Generation**
1. **Windows**: Install GTK3 runtime if WeasyPrint fails
2. **Alternative**: Use pdfkit with wkhtmltopdf
3. **Simple Solution**: Export as HTML and print to PDF from browser

## 📁 File Structure

```
medical-lab-markdown-manager/
├── app.py                          # Main Streamlit application
├── setup.py                        # Setup and installation script
├── requirements.txt                 # Python dependencies
├── README.md                       # This documentation
├── sample_lab_report.md            # Sample file for testing
└── [your markdown files]           # Your lab documents
```

## 🔧 Advanced Configuration

### **Custom CSS for PDF**
Add custom styling in the Download tab for personalized PDF appearance:

```css
/* Custom medical lab styling */
.lab-header {
    background-color: #2E86AB;
    color: white;
    padding: 20px;
    text-align: center;
}

.test-results {
    background-color: #f8f9fa;
    border-left: 4px solid #28a745;
    padding: 15px;
}
```

### **Template Customization**
Modify templates in `app.py` to match your laboratory's specific needs and branding.

## 🚨 Important Notes

### **Data Privacy**
- Handle patient information according to HIPAA guidelines
- Use anonymized data for testing and examples
- Implement proper access controls for sensitive documents

### **Quality Assurance**
- Review all generated documents before official use
- Maintain version control for critical documents
- Regular backups of important laboratory documentation

## 📞 Support & Troubleshooting

### **Common Issues**

1. **PDF Generation Fails**
   - Install WeasyPrint dependencies
   - Try alternative: export HTML and print to PDF
   - Check system requirements

2. **File Loading Errors**
   - Verify file encoding (UTF-8 recommended)
   - Check file permissions
   - Ensure valid markdown syntax

3. **Performance Issues**
   - Break large documents into smaller sections
   - Close unused browser tabs
   - Restart the Streamlit application

### **Getting Help**
- Check error messages in the Streamlit interface
- Review browser console for JavaScript errors
- Verify all dependencies are properly installed

## 🎯 Future Enhancements

- Integration with laboratory information systems (LIS)
- Collaborative editing features
- Advanced template management
- Automated report generation
- Version control integration
- Mobile-responsive design improvements

---

**Built specifically for medical laboratory professionals** 🏥  
*Streamline your documentation workflow with professional markdown management*