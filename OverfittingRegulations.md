Overfitting & Regularization

Overfitting occurs when a model learns the training data too well, capturing noise and fluctuations that don’t generalize to unseen data. This results in high accuracy on training data but poor performance on validation or test data. It is one of the most common issues encountered in deep learning.

To combat overfitting, regularization techniques like L1 and L2 are applied to penalize large weights. Dropout randomly deactivates neurons during training, encouraging the network to learn more robust features. Early stopping halts training when validation loss begins to rise, preventing the model from memorizing the data.