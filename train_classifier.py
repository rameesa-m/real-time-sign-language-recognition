import pickle
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from keras.preprocessing.sequence import pad_sequences  # Import pad_sequences from Keras

# Load data from pickle file
data_dict = pickle.load(open('C://Users/ramip/Downloads/sign_language_project/data/data.pickle', 'rb'))

# Pad or truncate sequences to have a uniform length
max_seq_length = 100  # Set the maximum sequence length
data_padded = pad_sequences(data_dict['data'], maxlen=max_seq_length, dtype='float32', padding='post', truncating='post')

# Convert labels to NumPy array
labels = np.asarray(data_dict['labels'])

# Split data into train and test sets
x_train, x_test, y_train, y_test = train_test_split(data_padded, labels, test_size=0.2, shuffle=True, stratify=labels)

# Initialize and train the RandomForestClassifier
model = RandomForestClassifier()
model.fit(x_train, y_train)

# Predict on the test set
y_predict = model.predict(x_test)

# Calculate accuracy score
score = accuracy_score(y_predict, y_test)

# Print accuracy score
print('{}% of samples were classified correctly!'.format(score * 100))

# Save the model to a pickle file
with open('model.p', 'wb') as f:
    pickle.dump({'model': model}, f)