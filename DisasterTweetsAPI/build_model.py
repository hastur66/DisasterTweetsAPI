import pandas as pd
from sklearn.model_selection import train_test_split
from model import NLPModel

def build_model():
    model = NLPModel()

    with open('lib/data/train.csv') as f:
        data = pd.read_csv(f)

    # pos_neg = data[(data['Sentiment'] == 0) | (data['Sentiment'] == 4)]

    # pos_neg['Binary'] = pos_neg.apply(lambda x: 0 if x['Sentiment'] == 0 else 1, axis=1)

    model.vectorizer_fit(data.loc[:, 'text'])
    print("Vectorizer fit complete")

    X = model.vectorizer_transform(data.loc[:, 'text'])
    print("Vectorizer transform complete")
    y = data.loc[:, 'target']

    X_train, X_test, y_train, y_test = train_test_split(X, y)

    model.train(X_train, y_train)
    print("Nodel training complete")

    model.pickle_clf()
    model.pickle_vectorizer()
    return

if __name__=='__main__':
    build_model()