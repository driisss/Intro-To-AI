Backpropagation & Gradient Descent

Backpropagation is a method used to compute the gradient of the loss function with respect to each weight in the network. It applies the chain rule of calculus through multiple layers, propagating the error backward from the output to the input layer. This process ensures each weight is updated in a direction that minimizes the loss.

Gradient Descent is the optimization technique used alongside backpropagation. It adjusts weights iteratively based on the computed gradients. A suitable learning rate is essential; too high can lead to overshooting the optimal point, while too low slows down convergence. Together, these methods power the learning process in deep networks.