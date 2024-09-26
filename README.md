# Python Keylogger for Windows

Upon execution, the malware immediately initiates its process by adding itself to the Windows registry if not already present. It then changes its working directory to the system's temporary folder (`Temp`), an area often overlooked by regular users, granting the necessary permissions to execute its tasks without restrictions. This is crucial, as after each system reboot, the registry triggers the keylogger from the `System32` directory, which lacks write permissions for standard users. By operating from the `Temp` directory, the malware ensures it can create and modify log files without permission issues. The malware captures every keystroke, compiling detailed logs in a `.txt` file. Every 10 minutes, these logs are sent to a specified email address, after which the log file is cleared, maintaining a continuous and covert monitoring cycle.

### ⚠️ Disclaimer

This project is intended **exclusively for educational purposes**. It is designed to provide an understanding of how malware operates and interacts with operating system structures. This software should only be used in environments where all parties involved have granted explicit permission.

**Unauthorized use** of this software to monitor individuals without their knowledge and consent is illegal and unethical. The author does not endorse or condone any form of malicious activity. Users are responsible for ensuring they comply with all applicable laws and regulations in their jurisdiction.

By using this project, you agree to take full responsibility for your actions and adhere strictly to legal and ethical standards.