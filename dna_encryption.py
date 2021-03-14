import json

dna = json.load(open("./dna.json", "r"))
keys, values = list(dna.keys()), list(dna.values())
non_enc = [i for i in str(input("Input: "))]
_str = []

for i in non_enc:
  if i in values:
    _str.append(keys[values.index(i)])
  else:
    _str.append(i)

print(f"Encryption: {''.join(str(s) for s in _str)}")