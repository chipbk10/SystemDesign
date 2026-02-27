***

# ✅ **NFC Summary**

### **1. Your iPhone = NFC Reader**

*   The iPhone contains an **NFC controller**.
*   It can open an ISO7816 session and communicate with ID documents.
*   Adding the NFC entitlement only enables communication — **not access to protected data**.

***

### **2. The ID Document = Secure Cryptographic Chip**

*   Passports and ID cards contain a **secure smartcard chip**, not a simple NFC chip.
*   This chip:
    *   generates random challenges
    *   stores private keys
    *   enforces access control
    *   performs cryptography
    *   returns signed identity data only after authentication

***

### **3. Access Requires User‑Provided Secret**

Depending on the document type:

*   **MRZ** → Passports (BAC)
*   **CAN or PIN** → National ID cards (PACE)
*   **Reader certificate** → High‑security biometrics (EAC)

Your app must ask the user for MRZ/CAN/PIN because only the document holder should unlock the chip.

***

### **4. Challenge–Response**

When scanned:

1.  The ID chip sends a **random challenge**.
2.  Your app computes the response using a **symmetric key derived from MRZ/CAN/PIN**.
3.  If correct → secure messaging starts.
4.  Then the chip allows reading of identity data.

**This prevents unauthorized reading and cloning.**

***

### **5. Data Returned After Authentication**

Once secure messaging is established, the chip can return:

*   **DG1**: Name, DOB, nationality, document number
*   **DG2**: Facial image
*   **DG11 / DG12**: Optional personal details
*   **SOD**: Digital signatures + hashes for validation

Sensitive biometrics (e.g., fingerprints) require EAC and are not available to normal apps.

***

### **6. Server‑Side Validation**

Your server must validate:

*   SOD signature (authenticity)
*   Hash values (integrity)
*   Optional chip authentication results (anti‑cloning)

***

# 🎯 **In one sentence**

Your iPhone (NFC reader) talks to the secure chip inside the ID document, proves access rights using MRZ/CAN/PIN via challenge‑response, establishes secure messaging, reads identity data, and sends it to your server for verification.

***
