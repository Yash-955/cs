import re
spam_keywords = [
"free", "winner", "cash", "prize", "money", "congratulations", "urgent", "claim",
"discount", "buy", "cheap", "limited offer", "guaranteed", "offer", "deal",
"risk-free", "click here", "exclusive", "now"
]
def clean_text(text):
# Remove non-alphabetic characters and convert to lowercase
text = re.sub(r'[^a-zA-Z\s]', '', text.lower())
return text
def is_spam(email_text):
# Clean the email text
cleaned_text = clean_text(email_text)
# Check for the presence of spam keywords
for word in spam_keywords:
if word in cleaned_text:
return True # If any keyword is found, classify as spam
return False # If no keywords are found, classify as ham
# Taking input from the user
email = input("Please enter the email text to check for spam:\n")
# Check if the email is spam or not
if is_spam(email):
print("This email is classified as Spam.")
else:
print("This email is classified as Ham (Not Spam).")