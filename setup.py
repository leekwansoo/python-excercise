#!/usr/bin/env python3
"""
Setup script for Medical Lab Markdown Manager
"""

import subprocess
import sys
import os

def install_requirements():
    """Install required packages"""
    print("🚀 Installing required packages...")
    
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ All packages installed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error installing packages: {e}")
        return False

def install_weasyprint_dependencies():
    """Install WeasyPrint dependencies for Windows"""
    if sys.platform == "win32":
        print("🔧 Installing WeasyPrint dependencies for Windows...")
        try:
            # Try to install GTK3 runtime for Windows
            print("📝 Note: WeasyPrint requires GTK3 runtime on Windows.")
            print("   If PDF generation fails, please install GTK3 runtime from:")
            print("   https://github.com/tschoonj/GTK-for-Windows-Runtime-Environment-Installer")
            
            subprocess.check_call([sys.executable, "-m", "pip", "install", "weasyprint"])
            print("✅ WeasyPrint installed!")
            return True
        except subprocess.CalledProcessError:
            print("⚠️  WeasyPrint installation may need manual setup on Windows")
            print("   Alternative: Use pdfkit with wkhtmltopdf")
            return False
    else:
        print("✅ WeasyPrint should work on this platform")
        return True

def create_sample_files():
    """Create sample markdown files for testing"""
    print("📁 Creating sample files...")
    
    sample_content = """# Sample Medical Lab Document

**Date:** October 24, 2025  
**Lab:** Clinical Chemistry  
**Technician:** Sample User  

## Test Results

| Test Name | Result | Reference Range | Status |
|-----------|--------|-----------------|--------|
| Glucose | 95 mg/dL | 70-100 mg/dL | Normal |
| Cholesterol | 180 mg/dL | <200 mg/dL | Normal |
| Hemoglobin | 14.2 g/dL | 12.0-16.0 g/dL | Normal |

## Quality Control

- ✅ All controls within acceptable limits
- ✅ Calibration verified
- ✅ Maintenance up to date

## Notes

This is a sample document for testing the Markdown Manager application.

### Code Example

```python
# Sample lab calculation
def calculate_creatinine_clearance(creatinine, age, weight, gender):
    if gender.lower() == 'female':
        factor = 0.85
    else:
        factor = 1.0
    
    clearance = ((140 - age) * weight * factor) / (72 * creatinine)
    return clearance
```

## Conclusion

All test results are within normal limits. No further action required.
"""
    
    try:
        with open("sample_lab_report.md", "w", encoding="utf-8") as f:
            f.write(sample_content)
        print("✅ Sample file created: sample_lab_report.md")
        return True
    except Exception as e:
        print(f"❌ Error creating sample file: {e}")
        return False

def main():
    """Main setup function"""
    print("🏥 Medical Lab Markdown Manager Setup")
    print("=" * 50)
    
    # Check Python version
    if sys.version_info < (3, 7):
        print("❌ Python 3.7 or higher is required")
        sys.exit(1)
    
    print(f"✅ Python {sys.version} detected")
    
    # Install requirements
    if not install_requirements():
        print("❌ Setup failed at package installation")
        sys.exit(1)
    
    # Install WeasyPrint dependencies
    install_weasyprint_dependencies()
    
    # Create sample files
    create_sample_files()
    
    print("\n" + "=" * 50)
    print("🎉 Setup completed successfully!")
    print("\n📋 Next steps:")
    print("1. Run the app: streamlit run app.py")
    print("2. Open your browser to the provided URL")
    print("3. Try loading the sample file: sample_lab_report.md")
    print("\n💡 Tips:")
    print("- Place your markdown files in the same directory")
    print("- Use the templates for creating new documents")
    print("- PDF generation requires WeasyPrint or wkhtmltopdf")
    
    return True

if __name__ == "__main__":
    main()