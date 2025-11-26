## Gradient Descent

- **Gradient Descent** is a method used to find the best parameters (w1, w2, ...) for a model by minimizing its error
- Analogy:
  - Imagine you're on a hill, and want to reach the lowest point (the minimum)
  - At each step, you look at the slope (gradient) and **move downhill** in the direction that reduces the **error** (the gap between the **guessed value** and the **actual value**)
  - The size of each step is controlled by the **learning rate**
  - Repeat until you're close enough to the bottom (minimum error)

## Example

- Given **inputs** - x values, and the actual **outputs** - **y_actual** values
- We need to find out the relationship between **x** and **y_actual** values
- Let's say, we guess the relationship is just a straight line:
  - `y = w1x + w0`
  - w1: weight for the feature x
  - w0: bias term
  
- At the beginning, **start with random values** for w0, and w1
- Compute the **error** (or the **loss function**):
  - `Loss = 1/n (y_pred - y_actual)^2`
  - `Loss = Aw1^2 + Bw1 + Cw0^2 + Dw0 + Ew1w0 + F`
  - it's a **quadratic surface** in w1 and w0

- Gradient Descent:
  - at w1: `GD_w1 = 2Aw1 + B + Ew0`
  - at w0: `GD_w0 = 2Cw0 + D + Ew1`

- We calculate new (w1, w0):
  - `w1_new = w1 - alpha (2Aw1 + B + Ew0)`
  - `w0_new = w0 - alpha (2Cw0 + D + Ew1)`
  - where alpha is **learning rate**.
    - if **learning rate** is too large, you might overshoot and never converge
    - if **learning rate** is too small, training becomes very slow

- We repeat the **training** process (the Gradient Descent steps) until one of these **stopping criteria** is met:
  - **Loss become very small**
  - **Gradient becomes very small**
  - **Maximum number of iterations**
  - **Model performance stops improving**
