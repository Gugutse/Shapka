
# coding: utf-8

# In[3]:


import os
import re

directory_path = '.'

# нахождение самого частовстречающегося элемента
def most_common(l):
    i_set = set(l)
    most_common = None
    q_most_common = 0
    for item in i_set:
        q = l.count(item)
        if q > q_most_common:
            q_most_common = q
            most_common = item
    return(most_common)


# нахождение количества уникальных элемента
def q_uniq_el(l):
    uniq_el = set()
    for name in l:
        uniq_el.add(name)
    return(len(uniq_el))


# максимальная глубина папки
def max_level(directory_path):
    level = 0
    count_fol = directory_path.count('/')
    for r, d, f in os.walk(directory_path):
        a = dirpath.count('/') - count_fol + 1
        if a > level:
            level = a
    return(level)
           

# получаем список названий папок
def folder_names(directory_path):
    fol_names = []
    for r, d, f in os.walk(directory_path):
        for dirs in d:
            fol_names.append(dirs)
    return(fol_names)

           
# количество папок с кириллическими символами
def russian_names():
    fol = folder_names(directory_path)
    r = re.compile('^[А-Яа-яЁё]+$')
    rus = [i for i in filter(r.match, fol)]
    return(len(rus))
           

# на какую букву начинается название большинства папок
def most_common_first_char():
    chars = []
    for name in folder_names(directory_path):
        name = name.lower()
        chars.append(name[0])
    return(most_common(chars))
           

# папка с наибольшим количеством файлов
def max_files(directory_path):
    dict = {}
    for r, d, f in os.walk(directory_path):
        dict[r] = [len(d)]
    values =list(dict.values())
    keys =list(dict.keys())
    return(keys[values.index(max(values))])


#в скольких папках встречается несколько файлов с одним и тем же расширением
def fol_w_rep_ext(directory_path):
    fol_w_rep_ext = 0
    for r, d, f in os.walk(directory_path):
        ext_l = []
        for filename in f:
            basename, ext = os.path.splitext(filename)
            ext_l.append(ext)
        uniq_ext = q_uniq_el(ext_l)
        if len(f) != uniq_ext:
            fol_w_rep_ext += 1
    return(fol_w_rep_ext)
           

# сколько в папках встречается разных названий файлов без учёта расширений
def files_uniq(directory_path):
    files_names = []
    for r, d, f in os.walk(directory_path):
        for filename in f:
            basename = os.path.splitext(filename)[0]
            files_names.append(basename)
    return(q_uniq_el(files_names))
            

# файлы с каким расширением чаще всего встречаются в папках
def most_common_ext(directory_path):
    ext_names = []
    for r, d, f in os.walk(directory_path):
        for filename in f:
            ext = os.path.splitext(filename)[1]
            ext_names.append(ext)
    return(most_common(ext_names))

ans_1 = "1. Какова максимальная глубина папки в этом дереве: "+str(max_level(directory_path))+'\n'
ans_2 = "2. Cколько в дереве папок с полностью кириллическими названиями: "+str(russian_names())+'\n'
ans_3 = "3. Файлы с каким расширением чаще всего встречаются в папках: "+most_common_ext(directory_path)+'\n'
ans_4 = "4. На какую букву начинается название большинства папок: "+most_common_first_char()+'\n'
ans_5 = "5. Сколько в папках встречается разных названий файлов без учёта расширений: "+str(files_uniq(directory_path))+'\n'
ans_6 = "6. В скольких папках встречается несколько файлов с одним и тем же расширением: "+str(fol_w_rep_ext(directory_path))+'\n'
ans_7 = "7. В какой папке лежит больше всего файлов: "+max_files(directory_path)+'\n'

def main():
    with open('answers.txt', 'w') as a:
        print(ans_1 + ans_2 + ans_3 + ans_4 + ans_5 + ans_6 + ans_7, file=a)

        
        
if __name__ == '__main__':
   main()

