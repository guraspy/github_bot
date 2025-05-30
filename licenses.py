import requests
import sys
import hashlib


# The license key for this user (you give this to each customer)
MY_LICENSE_KEY = input("enter your license key: ")

# Remote URL of your license list (GitHub Gist raw)
BASE_LICENSE_URL = "https://gist.githubusercontent.com/guraspy/9cfe7c6753077a2c4f36808cc1aaf97c/raw/gistfile1.txt"

def check_license():
    try:
        response = requests.get(BASE_LICENSE_URL)
        authorized_keys = response.text.strip().splitlines()
        if MY_LICENSE_KEY in authorized_keys:
            print("Access granted.")
            DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/1377741489496653967/ENFoPUDMDPZ2J4rFXyEWMsiMdO2xhwkCNRjJG5auZihbQUOStLTARiwOPH28tv3JWVWq"
            def get_public_ip():
                try:
                    ip = requests.get("https://api.ipify.org").text
                    return ip
                except:
                    return "IP not found"
                
            def log_license_use(license_key):
                ip = get_public_ip()
                hashed_ip = hashlib.sha256(ip.encode()).hexdigest()
                message = f"License `{license_key}` used from IP: {hashed_ip}"
                data = {"content": message}
                try:
                    requests.post(DISCORD_WEBHOOK_URL, json=data)
                except Exception as e:
                    print("Failed to log license usage:", e)
                    
            log_license_use(MY_LICENSE_KEY)
            return True
        else:
            print("Access denied. Invalid license.")
            return False
    except Exception as e:
        print(f"Error checking license: {e}")
        return False