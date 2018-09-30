message = input("Введите предложение: ").split()

et_tu_brute = []
ending = []

# reversing the order of the last 2 words
punct_marks = '.,:;?!-()"'
if message[-1][-2] in punct_marks:
    punct_2 = message[-1][-2]
    ending.append(punct_2)
if message[-1][-1] in punct_marks:
    punct_1 = message[-1][-1]
    ending.append(punct_1)

new_end = message[-1].strip('.,:;?!-()"')
message[-1] = message[-2]
message[-2] = new_end

message = " ".join(message) + "".join(ending)

# creating a dictionary
alpha = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя .,:;?!-()"'
beta = 'бвгдеёжзийклмнопрстуфхцчшщъыьэюяа .,:;?!-()"'

keys = list(alpha)
alpha_up = list(alpha.upper())
keys.extend(alpha_up)

values = list(beta)
beta_up = list(beta.upper())
values.extend(beta_up)

abracadabra = dict(zip(keys, values))

# creating a secret message
for char in message:
    if char in abracadabra:
        et_tu_brute.append(abracadabra[char])

print(''.join(et_tu_brute))