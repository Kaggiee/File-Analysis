def main():
    """
    This function will open and read and close the files, clean up the list, and use union,
    intersection, difference, and symmetric difference to determine how to sort the words.
    """
    # Open each file.
    file1 = open('9-file1.txt', 'r', encoding='UTF-8')
    file2 = open('9-file2.txt', 'r', encoding='UTF-8')

    # Read each file.

    text1 = file1.read()
    text2 = file2.read()

    # Close each file.
    file1.close()
    file2.close()

    # Call the word_format function to clean up the list.
    set1 = set(word_format(text1.split()))
    set2 = set(word_format(text2.split()))

    # Get the union of the sets and print the items in it.
    union = sorted(set1.union(set2))
    pstring = ''
    print('\nThese are the unique words that are contained in both files:')
    # Print (union).
    for item in union:
        pstring = pstring + item + ' '

    print(pstring + '\n')

    # Get the intersection of the sets and print the items in it.
    inter = sorted(set1.intersection(set2))
    pstring = ''
    print('These are the words that appear in both files:')
    for item in inter:
        pstring = pstring + item + ' '

    print(pstring + '\n')

    # Get the difference between set1 and set2 and print the items in it
    diff1 = sorted(set1.difference(set2))
    pstring = ''
    print('These are the words that appear in the first file but do not appear in the second file:')
    for item in diff1:
        pstring = pstring + item + ' '
    print(pstring + '\n')

    # Get the difference between set2 and set1 and print the items in it.
    diff2 = sorted(set2.difference(set1))
    pstring = ''
    print('These are the words that appear in the second file but do not appear in the first file:')
    for item in diff2:
        pstring = pstring + item + ' '

    print(pstring + '\n')

    # Get the symmetric difference between set1 and set2 and print the items in it.
    symdif = sorted(set1.symmetric_difference(set2))
    pstring = ''
    print('These are the words that appear in the first file or'
        ' the second file but do not appear in both files:')
    for item in symdif:
        pstring = pstring + item + ' '

    print(pstring + '\n')

def word_format(word_list):
    """
    This function takes each word in a list and strips periods and commas before converting
    them all to lowercase.
    """
    for word in range(len(word_list)):
        word_list[word] = word_list[word].rstrip('.')
        word_list[word] = word_list[word].rstrip(',')
        word_list[word] = word_list[word].lower()

    return word_list

# Call the main function.
if __name__ == '__main__':
    main()
