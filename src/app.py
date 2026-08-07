import os

def run():
    api_key = os.environ.get("PAYMENT_API_KEY", "")
    print(api_key)

if __name__ == "__main__":
    run()
