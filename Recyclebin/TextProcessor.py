from dependencies import *

class TextProcessor:
    def __init__(self, df):
        self.df = df.copy()
        self.clean_text()
        self.elmo_model = hub.load("https://tfhub.dev/google/elmo/3")
        self.y = self.df["label"].astype(str)

    def clean_text(self):
        self.df["clean_text"] = self.df["text"].str.lower()
        self.df["clean_text"] = self.df["clean_text"].str.replace(r"[{}]".format(string.punctuation), "", regex=True)
        self.df["clean_text"] = self.df["clean_text"].str.replace(r"\d+", "", regex=True)
        # self.df["clean_text"] = self.df["clean_text"].apply(lambda x: " ".join(word_tokenize(x)))

    def tfidf_vectorizer(self, max_features=100):
        vectorizer = TfidfVectorizer(max_features=max_features)
        X_tfidf = vectorizer.fit_transform(self.df["clean_text"])
        return X_tfidf, self.y

    def bag_of_words_vectorizer(self, max_features=100):
        vectorizer = CountVectorizer(max_features=max_features)
        X_bow = vectorizer.fit_transform(self.df["clean_text"])
        return X_bow, self.y

    def one_hot_encoding(self):
        encoder = OneHotEncoder(sparse=False)
        one_hot_encoded = encoder.fit_transform(self.df[["clean_text"]])
        return one_hot_encoded, self.y

    def elmo_embeddings(self):
        def elmo_vectors(texts):
            return self.elmo_model.signatures["default"](tf.convert_to_tensor(texts))["elmo"]
        
        elmo_embeddings = elmo_vectors(self.df["clean_text"].tolist())
        return elmo_embeddings.numpy(), self.y