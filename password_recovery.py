import hashlib
import itertools
import random
import string
import timeit

def generate_salt():
    """Generate a random 16-character alphanumeric salt."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=16))

def generate_hash(password, salt):
    """Generate a SHA256 hash from the password concatenated with salt."""
    password_salt = password + salt
    hash_object = hashlib.sha256(password_salt.encode())
    hash_digest = hash_object.hexdigest()
    hash_object = hashlib.sha256(hash_digest.encode())
    final_hash = hash_object.hexdigest()
    return final_hash

def find_password(stored_hash, salt):
    """Attempt to recover the password by checking all combinations."""
    chars = string.ascii_letters
    for password in itertools.product(chars, repeat=4):
        password = ''.join(password)
        if generate_hash(password, salt) == stored_hash:
            return password
    return None

def automated_recovery():
    user_password = input("Enter a password (4 characters, letters only): ")
    if len(user_password) == 4:
        user_salt = generate_salt()

        # Measure hash generation time
        start_time_hash = timeit.default_timer()
        stored_hash = generate_hash(user_password, user_salt)
        hash_time = timeit.default_timer() - start_time_hash

        print(f"Generated hash: {stored_hash}")
        print(f"Used salt: {user_salt}")
        print(f"Time to create hash: {hash_time:.6f} seconds")

        # Measure password recovery time
        start_time_recovery = timeit.default_timer()
        recovered_password = find_password(stored_hash, user_salt)
        recovery_time = timeit.default_timer() - start_time_recovery

        if recovered_password:
            print(f"Recovered password: {recovered_password}")
        else:
            print("No matching password found.")
        print(f"Time to recover password: {recovery_time:.6f} seconds")
    else:
        print("Invalid input. The password must be 4 characters.")

if __name__ == "__main__":
    automated_recovery()
