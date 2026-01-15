import nltk
import re
import string  
# Download required NLTK resources (run once)
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
#input text 
text = """Hello! I’m Hang Nguyen, and I'm 20 years old, an English Language Teaching student and lifelong learner. I enjoy linguistics, storytelling, and tech. I balance study & creativity, aiming for growth + impact. Contact: hang.nguyen@email.com
 | Skills: Teaching{ELT}, Research[Syntax], Tools: VS-Code, GitHub. Fun facts: I like symbols !@#$%^&*()_-+=[]{};:"'<>,.?/"""
print("Orginal Text:\n",text)
print("-" * 50)
#tokenization
tokens = word_tokenize(text)
print("Tokens:\n",tokens)
print("-" * 50)
#lowercasing
lower_tokens = [token.lower() for token in tokens]
print("Lowercased Tokens:\n",lower_tokens)              
print("-" * 50)
#stopword removal
stop_words = set(stopwords.words('english'))
filtered_tokens = [token for token in lower_tokens if token not in stop_words]
print("Filtered Tokens (Stopwords Removed):\n",filtered_tokens)
print("-" * 50)
#punctuation removal
punctuation_removed_tokens = [token for token in filtered_tokens if token not in string.punctuation]
print("Punctuation Removed Tokens:\n",punctuation_removed_tokens)
print("-" * 50)
#stemming
stemmer = PorterStemmer()       
stemmed_tokens = [stemmer.stem(token) for token in punctuation_removed_tokens]
print("Stemmed Tokens:\n",stemmed_tokens)
print("-" * 50) 
#lemmatization
lemmatizer = WordNetLemmatizer()            
lemmatized_tokens = [lemmatizer.lemmatize(token) for token in punctuation_removed_tokens]
print("Lemmatized Tokens:\n",lemmatized_tokens)
print("-" * 50)
#text normalization 
def normalize_text(text):
    # Lowercasing
    text = text.lower()
    # Remove punctuation
    text = re.sub(f"[{re.escape(string.punctuation)}]", "", text)
    # Tokenization
    tokens = word_tokenize(text)
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    tokens = [token for token in tokens if token not in stop_words]
    # Lemmatization
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(token) for token in tokens]
    return tokens   
normalized_tokens = normalize_text(text)
print("Normalized Tokens:\n",normalized_tokens)
print("-" * 50)
#extract email addresses
email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
emails = re.findall(email_pattern, text)
print("Extracted Email Addresses:\n",emails)
print("-" * 50)
#extract name 
name_pattern = r'I’m ([A-Za-z ]+),'
name_match = re.search(name_pattern, text)
name = name_match.group(1) if name_match else "Name not found"
print("Extracted Name:\n",name)
print("-" * 50)
#extract age
age_pattern = r'(\d{1,3}) years old'
age_match = re.search(age_pattern, text)
age = age_match.group(1) if age_match else "Age not found"
print("Extracted Age:\n",age)
print("-" * 50)
