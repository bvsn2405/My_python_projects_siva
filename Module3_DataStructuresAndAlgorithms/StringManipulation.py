def string_manipulation():
    str1 = "hello Siva , Good morning"
    for ch in str1:
        print(ch)
    str2 = ""
    for a in range(-1, -len(str1) - 1, -1):
        str2 = str2 + str1[a]
    print(str2)
    print(len(str1))
    print(str1 * 10)
    print('Siva' not in str1)
    print(f'length of the string : {len(str1)}')
    print(f'Convert the 1st letter of the string to upper case: {str1.capitalize()}')
    print('Occurrence of O in str1 is :', str1.count('o'))
    print('String ends with \'morning \':', str1.endswith('morning '))
    print('Index of \'morning \':', str1.find('morning'))
    print('String can be splits as :', str1.split())
    print('String can be splits as :', str1.split('o'))
    print('Every word of the string will be starts with Capital letter:', str1.title())
    print('All the upper case letters in string into lower case letters :', str1.lower())
    print('All the lower case letters in string into upper case letters :', str1.upper())
    print('checks weather the letters in string all are lower case letters or not:', str1.islower())
    print('checks weather the letters in string all are lower case letters or not:', str1.isupper())
    print('swaps the letters case in the string upper to lower and lower to upper :', str1.swapcase())
    str4 = 'Hi Siva Good Morning'
    print(' replace the word with given word:', str4.replace('Siva', 'Abhi'))
    str3 = 'w'
    str5 = '2'
    print(str3.isdigit())
    print(str5.isdigit())
    print(str3.isalpha())
    print(str5.isalpha())


if __name__ == '__main__':
    string_manipulation()
