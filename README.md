# Shuffler - Flagyard CTF Walkthrough

This is a walkthrough for solving the **Shuffler** challenge from the **Flagyard CTF**. The challenge involves reversing a custom encryption process to retrieve the original input that satisfies the conditions.

## Challenge Description

The challenge provides:
1. A Python encryption script:
    ```python
    import random
    import hashlib
    encrypted = ''
    data = input('Hello enter the string you want to encrypt: \n')
    data += "A"
    if len(data) == 40:
        if hashlib.md5(data[:39].encode()).hexdigest() == "ac9dc5b77c199d4737f5010da0fcdd24":
            print("You got a hidden gem")
            for i in range(40):
                encrypted += chr(ord(data[i]) ^ (i << 3))
            simp = [encrypted[i:i+8] for i in range(0, len(data), 8)]
            random.shuffle(simp)
            with open('flag.enc', 'w', encoding="utf-8") as file:
                file.write(''.join(simp))
        else:
            print('We Only Encrypt Strings with length = 39')
    ```
2. A file named `flag.enc` containing the encrypted output:
    ```
    ¤ð´éÙÜÉÎĵĻġĭđĚōŹ±¾¥¯ÍÖÙrzgiY@@FdqySR[
    ```

### Goal

Reverse the encryption process to retrieve the original input string of length 39 that satisfies the `MD5` hash condition.

---

## Solution

### Step 1: Understand the Encryption Logic

The encryption script performs the following steps:
1. **Input Validation**:
   - Appends the letter "A" to the user-provided string, making the length 40.
   - Ensures the first 39 characters produce the MD5 hash `ac9dc5b77c199d4737f5010da0fcdd24`.
   
2. **Encryption**:
   - Applies XOR encryption:
     ```python
     encrypted += chr(ord(data[i]) ^ (i << 3))
     ```
   - Divides the encrypted result into chunks of 8 characters and shuffles them.

3. **Output**:
   - Writes the shuffled chunks to `flag.enc`.

---

### Step 2: Reversing the Process

To reverse the process:
1. **Unshuffle**:
   - Generate all possible permutations of the 8-character chunks to find the correct order.
2. **Decrypt**:
   - Reverse the XOR encryption using the formula:
     ```python
     decrypted[i] = chr(ord(encrypted[i]) ^ (i << 3))
     ```
3. **Validate**:
   - Compute the MD5 hash of the first 39 characters to find the valid input string.

---

### Step 3: Implementation

The following Python script reverses the encryption:

```python
import hashlib
import itertools

# Encrypted text from flag.enc
encrypted_text = "¤ð´éÙÜÉÎĵĻġĭđĚōŹ±¾¥¯ÍÖÙrzgiY@@FdqySR["

# Divide encrypted text into 8-character chunks
chunks = [encrypted_text[i:i+8] for i in range(0, len(encrypted_text), 8)]

# Try all permutations of the chunks to find the correct order
for perm in itertools.permutations(chunks):
    encrypted = ''.join(perm)
    decrypted = ''
    
    # Decrypt the text using XOR
    for i in range(40):
        decrypted += chr(ord(encrypted[i]) ^ (i << 3))
    
    # Check if the decrypted text satisfies the MD5 condition
    if hashlib.md5(decrypted[:39].encode()).hexdigest() == "ac9dc5b77c199d4737f5010da0fcdd24":
        print("Original input:", decrypted[:39])
        break
```
### Step 4: Output
When you run the script, it finds the original input string:

Original input: {The_correct_input_string}
Replace {The_correct_input_string} with the actual solution.

---

### Notes
This solution brute-forces the order of chunks using permutations, which can be computationally expensive. However, given the fixed number of chunks, it is feasible.
Ensure Python 3.x is installed to run the script.

### Contact me: 

<a href="https://www.instagram.com/t2tt/" style="color: white; text-decoration: none;">
  <img src="https://upload.wikimedia.org/wikipedia/commons/9/95/Instagram_logo_2022.svg" alt="Instagram" width="30" />
</a>
