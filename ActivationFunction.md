Activation Functions

Activation functions introduce non-linearity into the output of a neuron, allowing neural networks to model complex relationships in data. Without them, a neural network would behave like a simple linear regression model regardless of its depth. Common activation functions include Sigmoid, which maps values between 0 and 1, and Tanh, which maps between -1 and 1.

ReLU (Rectified Linear Unit) is widely used due to its computational simplicity and ability to mitigate the vanishing gradient problem. However, it can lead to "dead neurons," which is addressed by variants like Leaky ReLU. Choosing the right activation function is crucial for network performance and convergence.