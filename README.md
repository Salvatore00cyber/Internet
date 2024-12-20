![Logo](slv.jpg)
## Double uses [whatsmyname](https://salvatore00cyber.github.io/Salvatoremprocco/) for username search
## Also some email modules from [Poastal](https://github.com/Salvatore00cyber/Internet.git)

#created tools using Internet && Salvatore <>
# Open Source Contributions are appreciate.
Enum-Salvatore (A Private Detective Alias) is a Python tool that provides three options for enumerating information: searching by username, searching by email, and searching by domain. It utilizes separate modules for each type of search.

## Features

- **Search by Username**: To search for related information.
- **Search by Email**: To search for related information.
- **Search by Domain**: To search for related subdomains.

## Prerequisites

- Python 3

## Installation

1. Clone the repository:

    ```
    git clone https://github.com/Salvatore00cyber/Internet.git
    ```

2. Install the required modules:

    ```
    pip install -r requirements.txt
    ```
- Add Github token to make it work as intended. Add tokens in [APIKEYS](apikeys.py)

## Usage

1. Run the script:

    ```
    python Enum-Salvatore.py
    ```

2. Follow the on-screen instructions to choose an option and provide necessary input.

## Example

Here's an example of how to use the script:

```
×××××××××××××××××××××××××××××××××××××××××××××
×             Enumeration Cyber Sec         ×
××××××××××××××÷÷÷××××××××××××××××××××××××××××     #internet
×  options :                                ×
×                                           ×
× 1:=> Search by Username                   ×
× 2:=> Search by Email                      ×
× 3:=> Subdomain enumeration                ×
×                                           ×
××××××××××××××××××Salvatore××××××××××××××××××
Enter your choice (1/2/3): 2
Enter the email to search: example@gmail.com
```

## Explanation of Modules

- Follow this [USERNAME-README](./modules/username_enumeration/README.md) for username

- Follow this [EMAIL-README](./modules/email_enumeration/README.md) for email

- Subdomain enumeration using crt.sh API and google dorking to find subdomains.

---
