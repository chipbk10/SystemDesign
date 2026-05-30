**Updated & Revised Summary for Documentation:**

### SRE Example: Real User Monitoring (RUM) - Page Load Time

**Objective**:  
Capture real page load times experienced by actual users and monitor them using Prometheus.

**How it works**:

1. **Browser Side (Client-side Measurement)**  
   SRE works with the frontend/software development team and instructs them to implement JavaScript code that uses the browser’s built-in **Performance API**.  
   This API is a helper provided by the browser to measure performance metrics such as page load time, DOMContentLoaded, Largest Contentful Paint, etc.  
   *Note*: The Performance API only measures the current website the user is on.

2. **Data Transmission**  
   Once the page finishes loading, the JavaScript sends the metric data to the company’s backend API (using `fetch()` or `navigator.sendBeacon()`).

3. **Backend Side**  
   The backend API receives the metrics from real users, aggregates them (average, p95, p99, etc.), and exposes the aggregated data via the `/metrics` endpoint.

4. **Prometheus Monitoring**  
   Prometheus pulls the aggregated metrics from the backend service’s `/metrics` endpoint (standard pull model).  
   SRE configures the appropriate alerts based on defined SLOs.

**Key SRE Responsibilities in this Example**:
- Defining what metrics should be collected from the browser.
- Instructing and guiding developers on how to implement the client-side measurement.
- Designing how metrics flow from browser to backend API.
- Defining aggregation logic, setting SLOs, and configuring alerts in Prometheus.
- Ensuring the overall observability of user experience.
