# first block - printing chars with even indices
def char_even(word):
    chars = []
    indx = 0
    for indx in range(0, len(word)):
        if indx % 2 != 0 and word[indx] not in ["а","к"]:
            chars.append(word[indx])
        indx += 1
    chars_fin = " ".join(chars)
    return chars_fin
users_word = input("Введите слово: ")
result = char_even(users_word)
print(result)

# second block - asking the word N times
users_num = input("Введите число: ")
for item in range (int(users_num)):
    word = input("Введите слово: ")
    print(word)
    if word == "программирование":
        break

# third block - reversing the 2nd half of the word
def reverse(word):
    word2 = []
    indx = 0
    num = 1
    for indx in range(0, (len(word) // 2)):
        word2.append(word[indx])
        indx += 1
    for indx in range((len(word)) - (len(word) // 2)):
        word2.append(word[len(word) - num])
        num += 1
    final_word_halfrev = "".join(word2)
    return final_word_halfrev
users_word = input("Введите слово: ")
result = reverse(users_word)
print(result)






