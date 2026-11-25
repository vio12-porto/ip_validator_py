from ip_validator import IPValidator

def main():
    validator = IPValidator()

    while True:
        ip = input("Enter an IPv4 address to validate (or 'exit' to quit): ")
        if ip.lower() == 'exit':
            print("Exiting the validator, bye!")
            break
        if validator.is_valid_ipv4(ip):
            print(f"😊{ip} is a valid IPv4 address.")
        else:
            print(f"🫠{ip} is not a valid IPv4 address.")

if __name__ == "__main__":
    main()