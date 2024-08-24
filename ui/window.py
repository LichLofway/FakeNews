import tkinter as tk
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import nltk
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('punkt')
nltk.download('punkt_tab')
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.tokenize import word_tokenize
import wget

def standardize_text(text):
    text = text.replace(r"[^A-Za-z0-9\(\),!?@\'\`\"_n]", " ")
    text = text.replace(r'[^?!\.\w\s]',' ')
    text = text.lower()
    return text

def lemmatization(text):
    lemmatizer=WordNetLemmatizer()

    tokens = word_tokenize(text)
    lemmatized_text = [lemmatizer.lemmatize(word) for word in tokens if not word in stopwords.words('english')]
    text = ' '.join(lemmatized_text)
    return text

def load_model(filename):
    load_model = pickle.load(open(filename, 'rb'))
    return load_model


root = tk.Tk()
root.title("Check news")
root.geometry("800x400")
label = tk.Label(root, text="Title of article:")
label.pack(pady=5)

entry = tk.Text(root, width=50, height=2)
entry.pack(pady=5)

tf = tk.Label()
tf.pack(pady=5)


filename_m = 'files/linear_model.bin'
filename_v = 'files/vectorization.bin'
model = load_model(filename_m)
vectorization = load_model(filename_v)

def on():
    tf["text"] =  " "
    text = entry.get("1.0", "end")
    text = lemmatization(standardize_text(text))
    x_test = vectorization.transform([text])
    y_pred = model.predict(x_test)[0]
    ans = "It's Fake information"
    if y_pred:
        ans = "It's True information"
    tf["text"] = ans


button = tk.Button(root, text="Check", command=on)
button.pack(pady=20)

root.mainloop()
