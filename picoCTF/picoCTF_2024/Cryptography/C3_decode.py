import sys

# Ciphertext
chars = "DLSeGAGDgBNJDQJDCFSFnRBIDjgHoDFCFtHDgJpiHtGDmMAQFnRBJKkBAsTMrsPSDDnEFCFtIbEDtDCIbFCFtHTJDKerFldbFObFCFtLBFkBAAAPFnRBJGEkerFlcPgKkImHnIlATJDKbTbFOkdNnsgbnJRMFnRBNAFkBAAAbrcbTKAkOgFpOgFpOpkBAAAAAAAiClFGIPFnRBaKliCgClFGtIBAAAAAAAOgGEkImHnIl"

lookup1 = "\n \"#()*+/1:=[]abcdefghijklmnopqrstuvwxyz"
lookup2 = "ABCDEFGHIJKLMNOPQRSTabcdefghijklmnopqrst"

out = ""

# Reverse the convertation
prev = 0
for char in chars:
    cur = lookup2.index(char)
    out += lookup1[(cur + prev) % 40]
    prev = (cur + prev) % 40

# print(out) # I'm getting new script


# Adding the new script
chars = ""
for line in out:
    chars += line
b = 1 / 1

# According to description I should convert the result to flag format.
sonuc = "picoCTF{"
for i in range(len(chars)):
    if i == b * b * b:
        sonuc += chars[i]
        b += 1 / 1

sonuc += "}"
print(sonuc)

# /C3_decode.py 
# picoCTF{*********}
