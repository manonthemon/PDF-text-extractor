import os, pyperclip, fitz

# Ask the user for the PDF file name or path
pdf_file = input("Enter the name or path of the PDF file: ")

# Change directory to where the PDF is located
pdf_dir = os.path.dirname(pdf_file)
if pdf_dir:
    os.chdir(pdf_dir)

# Open the PDF file
pdfFile = fitz.open(pdf_file)

# Concatenate text from all pages into a single string
text = ''
for page in pdfFile:
    text += page.get_text().strip() + ' '

# Copy the text to the clipboard
pyperclip.copy(text)

# Print the text to verify that it was copied correctly
print(text)
