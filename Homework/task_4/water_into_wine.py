
# coding: utf-8

# In[ ]:


import re

def stand_in(stem, flexion, n_stem, text):

    base = r'\b%s%s\b' % (stem, flexion)
    trans = r'%s\1' % (n_stem)
    n_text = re.sub(base, trans, text)

    base = r'\b%s%s\b' % ((stem.capitalize()), flexion)
    trans = r'%s\1' % (n_stem.capitalize())
    n_n_text = re.sub(base, trans, n_text)

    return(n_n_text)


with open('Лингвистика.txt') as l:
    linguistics = l.readlines()
    linguistics = [line.strip().replace(chr(769), '') for line in linguistics]

with open('Шашлык.txt', 'w') as f:
    for line in linguistics:
        awesome_text_1 = stand_in('язык', '(|[ауеи]|ом|ов|ам|ами|ах)','шашлык', line)
        print(awesome_text_1, file=f)


with open('Философия.txt') as l:
    philosophy = l.readlines()
    philosophy = [line.strip().replace(chr(769), '') for line in philosophy]

with open('Астро.txt', 'w') as f:
    for line in philosophy:
        awesome_text_2 = stand_in('философи', '([яиюй]|ей|ям|ями|ях)','астрологи', line)
        print(awesome_text_2, file=f)


with open('Финляндия.txt') as l:
    finland = l.readlines()
    finland = [line.strip().replace(chr(769), '') for line in finland]

with open('Малайзия.txt', 'w') as f:
    for line in finland:
        awesome_text_3 = stand_in('финлянди', '([яиюй]|ей|ям|ями|ях)','малайзи', line)
        print(awesome_text_3, file=f)

