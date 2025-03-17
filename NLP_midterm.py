from dependencies import *
from TextProcessor import TextProcessor

# Đọc dữ liệu từ file CSV
df = pd.read_csv("datasets\generated_soccer_questions.csv")

# Chuyển thành DataFrame
# df = pd.DataFrame(corpus, columns=["text", "label"])

# Hiển thị một số dòng của tập dữ liệu
print("Dữ liệu mẫu:")
print(df.head())

# Tiền xử lý văn bản
processor = TextProcessor(df)
    
X_tfidf, y_tfidf = processor.tfidf_vectorizer()
X_bow, y_bow = processor.bag_of_words_vectorizer()
X_one_hot, y_one_hot = processor.one_hot_encoding()
X_elmo, y_elmo = processor.elmo_embeddings()
    
X_train, X_test, y_train, y_test = train_test_split(X_bow, y_bow, test_size=0.3, random_state=42, stratify=y_bow)
    
print("TF-IDF Shape:", X_tfidf.shape)
print("BoW Shape:", X_bow.shape)
print("One-Hot Shape:", X_one_hot.shape)
print("ELMo Shape:", X_elmo.shape)

# Huấn luyện Naive Bayes với Laplace smoothing
nb_model = MultinomialNB(alpha=0.1)
nb_model.fit(X_train, y_train)
y_pred_nb = nb_model.predict(X_test)
nb_acc = accuracy_score(y_test, y_pred_nb)
print("Naive Bayes Accuracy:", nb_acc)
print(classification_report(y_test, y_pred_nb))

# Huấn luyện Logistic Regression với regularization cao hơn
lr_model = LogisticRegression(max_iter=1000, C=0.1)
lr_model.fit(X_train, y_train)
y_pred_lr = lr_model.predict(X_test)
lr_acc = accuracy_score(y_test, y_pred_lr)
print("Logistic Regression Accuracy:", lr_acc)
print(classification_report(y_test, y_pred_lr))

# Huấn luyện Decision Tree với độ phức tạp thấp hơn
dt_model = DecisionTreeClassifier(max_depth=5, min_samples_split=20, random_state=42)
dt_model.fit(X_train, y_train)
y_pred_dt = dt_model.predict(X_test)
dt_acc = accuracy_score(y_test, y_pred_dt)
print("Decision Tree Accuracy:", dt_acc)
print(classification_report(y_test, y_pred_dt))

# Biểu diễn bằng Doc2Vec
tagged_data = [TaggedDocument(words=text.split(), tags=[str(i)]) for i, text in enumerate(df["clean_text"])]
d2v_model = Doc2Vec(tagged_data, vector_size=100, window=5, min_count=2, workers=4, epochs=30)
X_d2v = np.array([d2v_model.infer_vector(text.split()) for text in df["clean_text"]])
X_train_d2v, X_test_d2v, y_train_d2v, y_test_d2v = train_test_split(X_d2v, y_bow, test_size=0.3, random_state=42, stratify=y_bow)

# Huấn luyện với Doc2Vec
lr_d2v = LogisticRegression(max_iter=1000, C=0.5)
lr_d2v.fit(X_train_d2v, y_train_d2v)
y_pred_d2v = lr_d2v.predict(X_test_d2v)
d2v_acc = accuracy_score(y_test_d2v, y_pred_d2v)
print("Logistic Regression (Doc2Vec) Accuracy:", d2v_acc)
print(classification_report(y_test_d2v, y_pred_d2v))

# So sánh mô hình
models = ["Naive Bayes", "Logistic Regression", "Decision Tree", "Logistic Regression (Doc2Vec)"]
accuracies = [nb_acc, lr_acc, dt_acc, d2v_acc]

plt.figure(figsize=(8,5))
sns.barplot(x=models, y=accuracies, palette="coolwarm")
plt.ylim(0, 1)
plt.ylabel("Accuracy")
plt.xlabel("Model")
plt.title("So sánh độ chính xác của các mô hình")
plt.xticks(rotation=15)
plt.show()

