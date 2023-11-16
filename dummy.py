import pickle

with open('random_forest_regression_model.pkl', 'rb') as file:
    content = file.read()

print(content)