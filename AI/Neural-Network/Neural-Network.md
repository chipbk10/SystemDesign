### **Neural Network (NN)**

A neural network is basically a **function with many adjustable knobs (weights and biases)**.

*   You give it input, it produces output.
*   The goal: adjust those knobs so the output matches what you want.
*   How do we adjust them? → Using gradients and gradient descent.

***

### **1. Gradient**

The gradient is like the **slope of the hill** at your current position.

*   It tells you which direction the error increases or decreases.
*   In NN, it’s the **derivative of the loss** with respect to each weight.

***

### **2. Gradient Descent**

Imagine you’re on a hill and want to reach the valley (minimum error).

*   Look at the slope (gradient) and take a small step downhill.
*   Repeat until you’re at the bottom.
*   In NN, this means **updating weights** to reduce the loss.

***

### **3. Forward Propagation**

This is the **prediction step**:

*   Input flows through layers → **weighted sums → activation functions** → output.
*   You compute the prediction and then the error (loss).

***

### **4. Backpropagation**

This is the **learning step**:

*   Send the error backward through the network.
*   Compute how much each weight contributed to the error (using **chain rule**).
*   These gradients are then used in **gradient descent** to update weights.

***

✅ **In short:**  
Neural Network = **Forward pass (predict) + Backward pass (compute gradients) + Gradient descent (update weights)**.  
Repeat this many times until the network learns.
