import re

from nltk.corpus import stopwords

from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()


def process_text(text):
    for i in range(len(text)):
        r = re.sub('[^a-zA-Z]', ' ', text[i])

        r = text.lower()

        r = r.split()

        r = [word for word in r if word not in stopwords.words('english')]

        r = [lemmatizer.lemmatize(word) for word in r]

        r = ' '.join(r)

        return r
        # assign corpus to data['text']

# data['text'] = corpus

# data.head()

print(process_text("On the right to access information"))
