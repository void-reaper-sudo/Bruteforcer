# filepath: /bruteforce-cli/bruteforce-cli/src/bruteforce/cli.py
import argparse
from .bruteforce import PasswordCracker

def main():
    parser = argparse.ArgumentParser(description="Password Cracking Tool")
    parser.add_argument("target", help="Target IP or URL")
    parser.add_argument("username", help="Username for authentication")
    parser.add_argument("wordlist", help="Path to the wordlist file")
    parser.add_argument("protocol", choices=["http", "ssh", "ftp"], help="Protocol to use (HTTP, SSH, or FTP)")

    args = parser.parse_args()

    cracker = PasswordCracker(args.target, args.protocol, args.username, args.wordlist)
    cracker.crack_password()

if __name__ == "__main__":
    main()