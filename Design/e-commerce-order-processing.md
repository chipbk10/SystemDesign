I.**Requirements**:
1.**From the front-end side**:
- The customer adds items to their shopping cart
- He goes through the checkout process, entering details like shipping address and payment information (e.g., credit card number)
- He taps on "Pay" (or checkout) button to confirm the purchase

2.**From the back-end side**:
- The front-end sends a http POST request to back-end Order service `/api/orders`, including details (like items - product ids & quantities, customer info - email, shipping address, payment details)
- Expectation: the user expects a quick confirmation (e.g., after few seconds: a payment confirmation pop-up, and a confirmation email)

II.**Analysis**:
- The order might include following jobs:
  - **payment**: make a purchase (e.g., via Stripe or Paypal)
  - **inventory**: check if the item quantity is available in stock
  - **email**: sends a confirmation email to the customer
  - **shipping**: contact with seller (or warehouse), and arrange with logistic company
- The **payment** success is a hard requirement before accepting an order. If the card fails, we don't want to reverse inventory or proceed further. Therefore, the payment acts as a gatekeeper and will be implemented synchronously.
  - if payment fails, we return `Payment declined` to the user immediately.
  - if payment succeeds: save the order to the database with status `Confirmed`
- Others (inventory, email, shipping) can run in background in parallel

III.**Implementation**
- @Todo: why not: `load balancer` + `circuit breaker` + service + `retries`
- @Todo: why need to use message queue? What happens if a task fails? retries?
  - option1: parallel async calls (or in-memory queue) risk loss if the API crashes mid-process.
  - option2: Writing order directly to a DB (e.g., MySQL) bottlenecks at high volume and **lacks worker distribution**

- @Todo: inventory database? sql or no-sql?
- @Todo: global users? one user in Asia sends an order request to US?
