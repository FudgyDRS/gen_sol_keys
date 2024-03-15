import csv
import os
import json
from solders.keypair import Keypair

def generate_keypairs(num_keypairs):
    keypairs = []
    for _ in range(num_keypairs):
        keypair = Keypair()
        private_key_bytes = json.dumps(keypair.to_bytes_array())
        private_key_base58 = keypair.__str__()
        public_key = str(keypair.pubkey())
        keypairs.append((private_key_bytes, private_key_base58, public_key))
    return keypairs

def generate_keypair_csv(file_path, keypairs):
    # Check if the CSV file exists
    csv_exists = os.path.exists(file_path)
    with open(file_path, mode='a', newline='') as csvfile:
        fieldnames = ['private_key_bytes', 'private_key_base58', 'public_key']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        # Write header if the file is newly created
        if not csv_exists:
            writer.writeheader()
        for private_key_bytes, private_key_base58, public_key in keypairs:
            writer.writerow({
                'private_key_bytes': private_key_bytes,
                'private_key_base58': private_key_base58,
                'public_key': public_key
            })

def generate_public_key_csv(file_path, keypairs):
    with open(file_path, mode='a', newline='') as csvfile:
        fieldnames = ['public_key']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        for _, _, public_key in keypairs:
            writer.writerow({'public_key': public_key})

# Prompt the user to input the number of keypairs to generate
num_keypairs = int(input("Enter the number of keypairs to generate: "))

# Generate keypairs
keypairs = generate_keypairs(num_keypairs)

# Example usage
csv_file_path_keypairs = 'keypairs.csv'
generate_keypair_csv(csv_file_path_keypairs, keypairs)

csv_file_path_public_keys = 'public_keys.csv'
generate_public_key_csv(csv_file_path_public_keys, keypairs)