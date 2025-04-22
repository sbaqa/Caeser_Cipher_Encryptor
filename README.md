## Encrypt or decrypt your data with Caeser_Cipher_Encryptor app https://replit.com/@SviatoslavBordovski/Caesar-Cipher-Encryptor
# 🔐 Caesar Cipher Encryptor

Welcome to the **Caesar Cipher Encryptor**!  
This Python-based application allows you to encrypt and decrypt messages using the classic Caesar cipher technique.  
Whether you're looking to secure your messages or just have some fun with cryptography, this tool has you covered.

---

## 🧠 What is a Caesar Cipher?

The Caesar cipher is one of the simplest and most well-known encryption techniques.  
It's a type of substitution cipher where each letter in the plaintext is shifted a certain number of places down or up the alphabet. For example, with a shift of 3:

- **Plaintext:** `HELLO`
- **Ciphertext:** `KHOOR`

This method was reportedly used by Julius Caesar to communicate with his generals.

---

## 🚀 Features

- **Encryption:** Convert your plaintext messages into ciphertext by shifting letters.
- **Decryption:** Revert your ciphertext back to plaintext using the correct shift value.
- **User-Friendly Interface:** Simple command-line prompts guide you through the process.
- **Input Validation:** Ensures that the shift value is within the acceptable range.

---

## 🛠️ Getting Started

Follow these steps to set up and run the application locally:

### Prerequisites

- [Python 3.x](https://www.python.org/downloads/)

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/sbaqa/Caeser_Cipher_Encryptor.git
   cd Caeser_Cipher_Encryptor
   ```

2. **Create and activate a virtual environment:**
  ```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Run program**
  ```bash
python caesar_cipher.py


### 🧪 Example Usage

```shell
Do you want to (E)ncrypt or (D)ecrypt? E
Enter your message: Hello World
Enter shift value (1-25): 3
Encrypted message: Khoor Zruog

