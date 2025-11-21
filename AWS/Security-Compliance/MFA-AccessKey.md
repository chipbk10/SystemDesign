## ✅ MFA (Multi-Factor Authentication)

What it is: An extra security layer requiring something you know (password) and something you have (MFA device or app).
Why: Protects your AWS account from unauthorized access even if your password is compromised.
How: After entering your password, you enter a one-time code from your MFA device (e.g., Authenticator app or hardware token).


## ✅ Access Keys

- What they are:
  - Access Key ID + Secret Access Key = credentials for programmatic access to AWS (CLI, SDK, API).

- Who uses them: IAM Users or temporary credentials from STS.

- **Important**:

  - Permanent keys → stored on client side (~/.aws/credentials or env vars).
  - Temporary keys → **include a Session Token** (from STS AssumeRole).

- **Best practice**: Never hardcode keys, rotate regularly, prefer temporary credentials.
