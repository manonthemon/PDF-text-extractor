import os, pyperclip, fitz
from googletrans import Translator
translator = Translator()

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
print("This text has been copied to clipboard")

# Ask the user if they want to translate the text
response = input("Would you like to translate it? (Y/N)")
if response.lower() == "y":
    target_lang = input("Enter the target language code (e.g., 'es' for Spanish): ")

    # Translate the text to the target language
    translated = translator.translate(text, dest=target_lang)

    # Access the translated text
    translated_text = translated.text

    # Copy the translated text to the clipboard
    pyperclip.copy(translated_text)

    # Print the translated text to verify that it was copied correctly
    print(translated_text)
    print("This translation has been copied to the clipboard")
else:
    print("Translation skipped.") # Notify user that the translation was skipped
