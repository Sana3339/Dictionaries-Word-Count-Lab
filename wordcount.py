'''
Open file
Create empty dictionary
Loop through file
    assign to variable 'line' - split open file by spaces to variable

    Loop through word in line
    check to see if word is in dictionary
        if not
            add to dictionary with a value of 1
        else
            increment value by one

'''

def count_words(filename):

    text_file = open(filename)

    dict_of_words = {}

    for line in text_file:
        new_line = line.rstrip().split(" ")

        for word in new_line:
            if word not in dict_of_words:
                dict_of_words[word] = 1
            else:
                dict_of_words[word] += 1

    for word, number in dict_of_words.items():
        print(f'{word}:{number}')


#print(count_words('test.txt'))
print(count_words('twain.txt'))