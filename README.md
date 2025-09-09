
# 🔍 Chrome Profile Finder (Python)

## 📖 Overview
Chrome Profile Finder is a lightweight **Python tool** that scans a Windows system to detect and list all Google Chrome user profiles.  
It is designed for **educational purposes** and **authorized security audits only**, helping security researchers and IT professionals understand browser data storage.


## 🚀 Features
- 🔍 Detects all Chrome user profiles installed on a Windows machine.
- ⚡ Simple and fast script — no external dependencies.
- 🖥️ Works as a standalone `.py` script or packaged `.exe`.
- 🛡️ Great for security research and troubleshooting.



## 🛠️ Tech Stack
| Technology        | Purpose                              |
|-------------------|--------------------------------------|
| **Python 3.x**    | Core programming language            |
| **os module**     | File system navigation               |
| **PyInstaller**   | Build `.exe` executable              |



## 📂 Code
python
import os

def find_chrome_profiles():
    chrome_profiles = []
    chrome_profile_path = os.path.join(os.path.expanduser('~'), 'AppData', 'Local', 'Google', 'Chrome', 'User Data')

    if os.path.exists(chrome_profile_path):
        profiles = os.listdir(chrome_profile_path)
        for profile in profiles:
            if profile.startswith('Profile'):
                chrome_profiles.append(profile)
    return chrome_profiles

if __name__ == "__main__":
    profiles = find_chrome_profiles()
    if profiles:
        print("Chrome profiles found:")
        for profile in profiles:
            print(profile)
    else:
        print("No Chrome profiles found.")




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


