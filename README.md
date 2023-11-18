
# 🚨 Open Redirect Detector

This Python script, part of the [pentestfunctions](https://github.com/pentestfunctions/open-redirect-attack) repository, is aimed at detecting open redirect vulnerabilities in web applications.

## 🎯 Features

- 🔍 Efficiently detects open redirect vulnerabilities.
- 📝 Reads payloads from a file (`payloads.txt`) for testing.
- 🛡 Handles SSL warnings and allows bypassing SSL verification for testing purposes.
- 📊 Limits the number of potential open redirects found to avoid overwhelming output.

## ⚙️ Usage

To use this script, run it with Python and input the target URL when prompted:

```bash
python openredirect.py
```

## 📚 How It Works

1. The user inputs the target URL.
2. The script reads open redirect payloads from `payloads.txt`.
3. Each payload is tested against the target URL.
4. The script identifies potential open redirect vulnerabilities based on HTTP response codes and other indicators.

## 🛠️ Installation

Requirements include Python 3.x, `requests`, and `urllib3`. Install them using:

```bash
pip install requests urllib3
```

## 🛑 Disclaimer

This tool is for educational and ethical testing purposes only. Unauthorized testing can be illegal and against the terms of service of web applications.

## 🛡️ Shields

- ![Python](https://img.shields.io/badge/python-3.x-blue.svg)
- ![Security](https://img.shields.io/badge/security-penetration%20testing-brightgreen.svg)
- ![License](https://img.shields.io/badge/license-MIT-green.svg)


## Ideas to add:
- Add in double parameters (detect parameter being tested and double it)
- Try a double-URL and triple-URL encoded version of payloads
- If extension checked, try ?image_url={payload}/.jpg
- Extract target domain and see if it can redirect to any other TLD using the same domain (If domain.com try redirect to domain.co.uk)
- Add in the option to auto replace 'whitelisted.com' with a whitelisted domain automatically from payloads.txt
