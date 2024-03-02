import hashlib
def calculate_sha256(input_data):
    sha256_hash = hashlib.sha256(input_data.encode()).hexdigest()
    return sha256_hash
def main():
    input_data = input("Enter hashing information: ") #Here you must enter any data that you want to turn into a hash
    sha256_hash = calculate_sha256(input_data)
    print("SHA-256 hash for the entered data:", sha256_hash)

if __name__ == "__main__":
    main()



