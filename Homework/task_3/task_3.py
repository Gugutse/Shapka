
# coding: utf-8

# In[ ]:


import random

def give_random(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        lines = [line.rstrip() for line in lines]
    return random.choice(lines)

def name():
    random_name = give_random('names.tsv')
    return random_name

def adverb():
    random_adverb = give_random('adverbs_of_manner.tsv')
    return random_adverb

def intensifier(adverb):
    random_intensifier = give_random('intensifiers.tsv')
    result = random_intensifier + ' ' + adverb
    return result

def adjective(name):
    random_adjective = give_random('adjectives.tsv')
    result = random_adjective + ' ' + name
    return result

def places():
    random_place = give_random('places.tsv')
    result = ' in ' + random_place
    return result

def verb_cont():
    random_verb = give_random('verbs.tsv')
    verb = list(random_verb)
    if verb[-1] in 'aeuoi':
        del verb[-1]
    inter_result = ''.join(verb)
    result = inter_result + 'ing'
    return result

def random_affir_sentence():
    affir_sentence = name() + ' is ' + verb_cont() + ' ' + adjective(name()) + places() + ' ' + intensifier(adverb()) + '.'
    return affir_sentence

def random_interrog_sentence():
    interrog_sentence = 'Is ' + name() + ' ' + verb_cont() + ' ' + adjective(name()) + places() + '?'
    return interrog_sentence

def random_neg_sentence():
    neg_sentence = name() + ' isn\'t ' + verb_cont() + ' ' + adjective(name()) + places() + '.'
    return neg_sentence

def random_incent_sentence():
    incent_sentence = name() + ',' + ' let\'s ' + give_random('verbs.tsv') + ' ' + name() + '!'
    return incent_sentence

def random_cond_sentence():
    cond_sentence = 'If ' + name() + ' is ' + verb_cont() + ' ' + name() + ', ' + name() + ' is ' + verb_cont() + ' ' + name() + '.'
    return cond_sentence



def text():
    list = [random_affir_sentence(), random_interrog_sentence(), random_neg_sentence(), random_incent_sentence(), random_cond_sentence()]
    return random.choice(list)


def main():
    with open('sentences.txt', 'w') as f:
        for i in range(5):
            print(text(), file=f)


if __name__ == '__main__':
    main()

