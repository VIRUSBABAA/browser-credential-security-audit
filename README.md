
# 🔐 Chrome Credential Security Audit Tool (Python)

## 📖 Overview
This project is a **Python-based Proof-of-Concept (PoC)** security audit tool that demonstrates the risks of storing credentials in browsers like Google Chrome.  
It retrieves and decrypts locally saved login credentials for **educational purposes** and **authorized penetration testing only**.  
The tool also demonstrates secure handling of sensitive data, local database access, and optional integration with alerting systems (e.g., Discord webhooks for security notifications).

---

## 🚀 Features
- 🔍 Extract and decrypt saved Chrome credentials.
- 🌐 Retrieves the machine’s external IP address (via API).
- 📂 Saves findings to a local report file.
- 🔔 Optional Discord webhook integration for alerting (security teams only).
- 🔑 Demonstrates AES decryption using Chrome’s local encryption key.
- 🖥️ Built for Windows environments.

---

## 🛠️ Tech Stack
| Technology              | Purpose                                            |
|-------------------------|----------------------------------------------------|
| **Python 3.x**          | Core programming language                          |
| **SQLite3**             | Accessing Chrome's local credential database       |
| **PyCryptodome**        | AES decryption of stored passwords                 |
| **pywin32 (win32crypt)**| Windows DPAPI decryption                           |
| **Requests**            | API calls for external IP retrieval & notifications|
| **PyInstaller**         | Optional `.exe` packaging                          |

---

## 📂 How It Works
1. Retrieves Chrome’s AES encryption key from the local `Local State` file.
2. Creates a safe copy of Chrome’s `Login Data` SQLite database.
3. Decrypts saved credentials using Windows DPAPI and AES-GCM.
4. Generates a local report of URLs, usernames, and passwords.
5. (Optional) Sends the report to a configured webhook (for internal security alerting only).



## ▶️ Usage

1. Clone this repository:

bash
git clone https://github.com/your-username/chrome-profile-finder.git
cd chrome-profile-finder


2. Run the script:

bash
python chrome_profiles.py



## 🔧 Build a `.exe` (Windows)

You can make this a portable executable using **PyInstaller**:

1. Install PyInstaller:

bash
pip install pyinstaller


2. Build the `.exe`:

bash
pyinstaller --onefile chrome_profiles.py


3. Your `.exe` will be in the `dist` folder:


dist/chrome_profiles.exe


## 🔒 Disclaimer

This project is for **educational purposes only**.
Do **not** use it on devices you do not own or have explicit permission to test.
Unauthorized use of this tool may violate laws.


## 👤 Author

**Muhammad Subhan**
Cybersecurity Student | Scam Analyst | Security Researcher

* 🌐 [LinkedIn](https://www.linkedin.com/in/muhammad-subhan-28a638327)
* 🌐 [Portfolio](https://www.virusbaba.com)


