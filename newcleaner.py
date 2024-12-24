


import os
import re
import PyPDF2

# Path to the "Documents" directory
documents_dir = os.path.expanduser("~/Documents")

# File name to process (now a PDF file)
file_name = "dec23.pdf"  # Change this to your PDF file name
file_path = os.path.join(documents_dir, file_name)

# Check if the file exists
if not os.path.isfile(file_path):
    print(f"The file {file_path} does not exist.")
    exit()

# Output file name
output_file_name = "edu_emails.txt"
output_file_path = os.path.join(documents_dir, output_file_name)

# Print the file paths for verification
print(f"Processing file: {file_path}")
print(f"Output will be saved to: {output_file_path}")

# Regular expression to match .edu emails
edu_email_pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.edu\b')

# Initialize a set to track seen emails to avoid duplicates
seen_emails = set()

# Open and read the PDF file
with open(file_path, 'rb') as pdf_file:
    # Create PDF reader object
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    
    # Process each page in the PDF
    for page_num in range(len(pdf_reader.pages)):
        # Get the page
        page = pdf_reader.pages[page_num]
        
        # Extract text from the page
        text = page.extract_text()
        
        # Find all .edu emails in the text
        edu_emails = edu_email_pattern.findall(text)
        
        # Process found emails
        for email in edu_emails:
            if email not in seen_emails:
                seen_emails.add(email)

# Write the unique emails to the output file
with open(output_file_path, 'w') as outfile:
    for email in sorted(seen_emails):  # Sort emails for better readability
        outfile.write(email + '\n')

# Print the cleaned emails
print("Cleaned .edu emails saved to:", output_file_path)

# Verify the output file content
with open(output_file_path, 'r') as outfile:
    output_content = outfile.read()
    print("\nOutput file content:")
    print(output_content)
    
    
