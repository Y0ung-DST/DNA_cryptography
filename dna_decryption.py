import json

dna = json.load(open("./dna.json", "r"))
user_input = input("Input : ")

rez = []
for i in range(0,len(user_input), 3):
    r = user_input[i:i+3]
    rez.append(dna[r])

print(f"Decryption: {''.join(str(s) for s in rez)}")
