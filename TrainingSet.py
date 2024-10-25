from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

# Create a synthetic dataset for binary classification
X, y = make_classification(n_samples=1000, n_features=your_input_dimension, n_classes=2, random_state=42)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model.fit(X_train, y_train, epochs=50, batch_size=10, validation_data=(X_test, y_test))
