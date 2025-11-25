### What are weights? Why do we need them?

- Weights tell the network **how important each input is**
  - Imagine you’re predicting whether someone will buy a product. Inputs could be age, income, and browsing time.
  - Not all inputs matter equally (e.g., income might matter more than age)
  - Higher weight means more influence
- Without weights, every input would contribute equally, which is rarely true in real-world data.
- Who decide the value of a height? @Todo

### Why do we mulitple and sum them up?

- The neuron needs a **single combined signal** to decide what to do next.
  - If you have 10 inputs, you can’t pass all 10 separately to the next layer as **it would explode in complexity**.
  - Summing (weighted inputs) creates one number that represents the overall “evidence” for activation.
  - This is similar to how humans combine multiple factors before making a decision: you mentally add up pros and cons.
