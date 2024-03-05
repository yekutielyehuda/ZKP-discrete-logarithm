from Crypto.Util import number
from Crypto.Hash import SHA256

def generate_key_pair():
    p = number.getPrime(256)
    g = 2  # generator
    x = number.getRandomRange(2, p-2)  # private key
    y = pow(g, x, p)  # public key
    return p, g, x, y

def schnorr_prove(p, g, x, y):
    # Step 1: Generate a random nonce
    k = number.getRandomRange(1, p-1)

    # Step 2: Compute commitment
    A = pow(g, k, p)

    # Step 3: Compute challenge
    h = int(SHA256.new(str(A).encode()).hexdigest(), 16)
    e = h % (p - 1)

    # Step 4: Compute response
    s = (k + e * x) % (p - 1)

    return A, s, e

def schnorr_verify(p, g, y, A, s, e):
    # Compute v = g^s * y^e mod p
    v = (pow(g, s, p) * pow(y, e, p)) % p

    # Compute h = H(A)
    h = int(SHA256.new(str(A).encode()).hexdigest(), 16)

    # Compute e_prime = h mod (p - 1)
    e_prime = h % (p - 1)

    # Verify the equality of e and e_prime
    return e == e_prime

# Main code
if __name__ == "__main__":
    # Generate key pair
    p, g, x, y = generate_key_pair()

    # Prover
    A, s, e = schnorr_prove(p, g, x, y)

    # Verifier
    if schnorr_verify(p, g, y, A, s, e):
        print("Proof is valid.")
    else:
        print("Proof is invalid.")
