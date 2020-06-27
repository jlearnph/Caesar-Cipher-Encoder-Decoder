# Caesar-Cipher-Encoder-Decoder

This is a caesar cipher message encoder / decoder

Caesar cipher is one of the simplest and most widely known encryption techniques.
It is a type of substitution cipher in which each letter in the plaintext is replaced 
by a letter some fixed number of positions down the alphabet. 

For example.

A left shift of 3 means:
  * D -> A
  * E -> B
  * 3 -> 0

A right shift of 5 means:
  * G -> L
  * Z -> E
  * 9 -> 4

This leaves any symbols such as periods, commas, exclamation marks untouched.

### Program Flow:
1. Accept choice from user for encryption or decryption.
2. Accept string from user.
3. Accept shift from user.
4. Call user defined functions encrypt() or decrypt() according to user choice in step 1.
5. Exit
