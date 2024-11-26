import random
import string
import time
import requests

def generate_code(length=16):
    characters = string.ascii_letters + string.digits
    code = ''.join(random.choice(characters) for _ in range(length))
    return f"https://discord.gift/{code}"

webhook_url = input("Enter the Discord webhook URL: ")

try:
    while True:
        code = generate_code()
        print(code)
        
        data = {"content": code}
        response = requests.post(webhook_url, json=data)
        
        if response.status_code == 204:
            print("Message sent successfully.")
        elif response.status_code == 429:
            retry_after = response.json().get('retry_after', 3) / 1000.0
            print(f"Failed to send the message: 429. Waiting for {retry_after:.2f} seconds.")
            time.sleep(retry_after)
        else:
            print(f"Failed to send the message: {response.status_code}")

        time.sleep(3)
except KeyboardInterrupt:
    print("\nScript stopped.")
except Exception as e:
    print(f"An error occurred: {e}")
