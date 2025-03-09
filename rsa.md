# <u> TA-2 Engineering  Mathematics project
Made by</u> -  Aaryan and Swadhin

## <u> RSA encryption and decryption algorithm
> R- Rivet
S-  Shamir
A- Adleman</u> were the three brilliant mathematician who had created RSA encryption and decryption.
---
## How does RSA encryption works?

It relies on the difficulty in factoring large numbers

```Can you tell what two numbers multiplied together will produce the number 8,616,460,799?```

It is the product of two prime numbers, 89,681 and 96,079.
### RSA relies on factors and large prime numbers.
---
# How to create RSA key?

1. Choose two very large prime numbers, "p" & "q".
1. `N=p×q`
1. `T=(p-1)(q-1)`           (Euler Totient)
<br>

1. Choose two numbers "e" and "d" such that 
  `(e×d)mod T= 1` <br>
  e- encryption<br>
  d- decryption


  <br>

5. Keys
    ><u>Publish</u> - (N,e)    ```<---Public Key (only used to encrypt the message)``` <br>
   ><u>Keep</u> - (N,d)       ```<---Private key (only used to decrypt the message)```

<br>

6. Encryption and decryption
    >  c= p^e^mod N ` (encryption formula) `  
`c- cipher text`<br><br>
p= c^d^mod N<br>
`p- plain text`

---

# Example

### <u>Encryption</u>

Let p=2, q=7        ``` we are taking small numbers for our easiness``` <br>
Therefore, N=2×7 <br>
=> N=14 <br>
Now, T=1×6<br>
=> T=6

Using `(e×d)mod T= 1` , we get: e=5 and d=11

Pubic key: (5,14)
Private key: (11,14)


Let our message be "B", converting B to number B=2
Therefore, p=2 (plain text, the message to be encrypted)

>Calculating the cipher text, <br>
 c= p^e^mod N <br>
=> c=2^5^ mod 14 <br>
=> c=32 mod 14 <br>
=> c=4   ` This is the encrypted message , i.e 4 or 'D'`

### <u>Decryption</u>
 >p= c^d^mod N <br>
 =>p=4^11^mod 14 <br>
 =>p=2 `This is the decrypted message, i.e. 2 or 'B' `

This is similarly used for all the words to encrypt the entire message.

---

A very large chunk of internet traffic is still authenticated using RSA. Most online banking transactions involve some form of RSA. 

---

- [wiki/RSA_numbers](https://en.wikipedia.org/wiki/RSA_numbers)