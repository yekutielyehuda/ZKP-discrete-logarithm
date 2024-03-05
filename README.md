# Zero-Knowledge Proof (ZKP) with Schnorr Protocol

This Python script demonstrates how to implement a Zero-Knowledge Proof (ZKP) for the discrete logarithm problem using the Schnorr protocol. The Schnorr protocol allows one party (the prover) to prove to another party (the verifier) that they possess knowledge of a secret value, without revealing the actual secret value itself.

## Requirements

- Python 3.x
- `pycryptodome` library (install via `pip install pycryptodome`)

## Usage

1. Clone or download the repository.

2. Install the required library using pip:

```
pip install pycryptodome
```


3. Run the Python script:

```
python schnorr_zkp.py
```


This will generate a key pair, perform the ZKP protocol, and verify the proof.

## How It Works

1. **Key Pair Generation**:
- Generate a prime number `p` and a generator `g`.
- Choose a random private key `x` and compute the corresponding public key `y`.

2. **Prover**:
- Generate a random nonce `k`.
- Compute a commitment `A = g^k mod p`.
- Compute a challenge `e` based on `A`.
- Compute a response `s`.

3. **Verifier**:
- Compute `v = g^s * y^e mod p`.
- Verify the equality of `e` and `e_prime`.

4. **Result**:
- If the verification is successful, the proof is considered valid.

## Limitations and Security Considerations

- This script provides a simplified demonstration and should not be used in production without further security considerations.
- In practice, additional measures such as using secure random number generators, protecting against side-channel attacks, and considering cryptographic assumptions and parameters are essential.
- Always consult with cryptography experts and follow best practices when implementing cryptographic protocols.

## References

- [Schnorr Signature Algorithm - Wikipedia](https://en.wikipedia.org/wiki/Schnorr_signature)
- [pycryptodome Documentation](https://pycryptodome.readthedocs.io/en/latest/)
