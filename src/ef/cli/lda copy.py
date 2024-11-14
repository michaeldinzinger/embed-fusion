# import click
# import pickle
# import numpy as np
# import matplotlib.pyplot as plt
# from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
# from sklearn.model_selection import train_test_split
# from sklearn.datasets import load_iris
# from sklearn.metrics import accuracy_score
# from ef.utils import *


# @click.command()
# @click.argument("pretrained_model_name", type=click.Choice(EMBEDDING_MODELS), default=EMBEDDING_MODELS[0])
# def lda(pretrained_model_name: str):
#     """
#     Run Linear Discriminant Analysis.
#     """
#     click.echo('Running Linear Discriminant Analysis')

#     # Load a dataset (e.g., the Iris dataset)
#     data = load_iris()
#     X = data.data  # Features
#     y = data.target  # Target labels

#     print(X.shape)

#     # Split the data into training and testing sets
#     X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

#     # Create the LDA model
#     lda = LinearDiscriminantAnalysis(n_components=2)

#     # Fit the model to the training data
#     lda = lda.fit(X_train, y_train)

#     transformed = lda.transform(X_train)
#     print(transformed.shape)
#     print(transformed)

#     plt.scatter(transformed[:, 0], transformed[:, 1], c=y_train, edgecolors='k', cmap=plt.cm.Paired)
#     plt.xlabel('LD1')
#     plt.ylabel('LD2')
#     plt.title('LDA of Iris dataset')
#     plt.savefig('lda3.png')

#     # Predict the labels for the test set
#     y_pred = lda.predict(X_test)

#     # Evaluate the model's performance
#     accuracy = accuracy_score(y_test, y_pred)
#     print(f"Accuracy: {accuracy:.2f}")

#     # Print predicted and true labels
#     print("Predicted labels:", y_pred)
#     print("True labels:", y_test)