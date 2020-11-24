word = input()


def word_convert(word):
    array = []
    bool_array = [True for i in range(len(word))]
    diff = 96

    for i in range(len(word)-1, -1, -1):
        if bool_array[i] == False:
            continue
        if word[i] == '#':
            array += [word[i-2]+word[i-1]]
            bool_array[i] = False
            bool_array[i-1] = False
            bool_array[i-2] = False
        else:
            array += [word[i]]


    for i in range(len(array)):
        array[i] = chr(int(array[i])+diff)
    array = array[::-1]
    new_word = ''
    for i in array:
        new_word += i
    return new_word
word = word_convert(word)
print(word)

