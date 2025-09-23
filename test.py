import pdfplumber
import re
import os
import glob

directory_path = "/mnt/c/users/lauki/OneDrive - Blackstone/Downloads/citi"
pdf_files = glob.glob(os.path.join(directory_path, "*.pdf"))
activities = []
for pdf_file in pdf_files:
    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            activities += re.findall(r"(\d{2}\/\d{2})\s+\d{2}\/\d{2}\s+(.*?)\s+-?\$(\d{1,3}(?:,\d{3})*(?:\.\d{2})?|\d+(?:\.\d{2})?)", text)

# match = re.findall(r"\s+-?\$(\d{1,3}(?:,\d{3})*(?:\.\d{2})?|\d+(?:\.\d{2})?)", text)

print(activities)