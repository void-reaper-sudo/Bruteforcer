# README for Bruteforce CLI

# Bruteforce CLI

Bruteforce CLI is a command-line tool designed for password cracking across various protocols including HTTP, SSH, and FTP. This tool is intended for educational and legal purposes only. Please ensure you have permission to test the systems you are targeting.

## Features

- Supports multiple protocols: HTTP, SSH, and FTP.
- Utilizes a wordlist for password attempts.
- Displays results in a user-friendly table format.
- Rate limiting to avoid overwhelming the target service.

## Installation

To install the Bruteforce CLI, clone the repository and install the required dependencies:

```bash
git clone <repository-url>
cd bruteforcer
pip install -r requirements.txt
```

Alternatively, you can install it as a package:

```bash
pip install .
```

## Usage

After installation, you can run the tool by typing the following command in your terminal:

```bash
bruteforce
```

You will be prompted to enter the target IP address, username, wordlist file, and the protocol you wish to use.

## Example

```bash
bruteforce
Enter target IP: 192.168.1.1
Enter username: admin
Enter wordlist: passwords.txt
Enter protocol (HTTP, SSH or FTP): SSH
```

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Disclaimer

This tool is intended for educational purposes only. The author does not take any responsibility for any illegal use of this software. Always ensure you have permission before testing any systems.
