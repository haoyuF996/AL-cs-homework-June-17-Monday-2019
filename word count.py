def extract_words_from_file(filename):
    '''Extract all words(split by space) in a .txt file and return a list of the words'''
    file = open(filename,'r')
    file_content = file.read()
    file.close()
    words = file_content.split()
    return words
def find_element_binary(alist,item):
    '''Binary search to check whether an element is in a list'''
    if len(alist)<=1:
        return False
    elif alist[len(alist)//2] == item:
        return True
    elif alist[len(alist)//2] < item:
        return find_element_binary(alist[len(alist)//2:],item)
    else:
        return find_element_binary(alist[:len(alist)//2],item)
def texts_to_words(text_list):
    '''Transfer all text into words(lowercased) and return a list with all the words'''
    words = []
    for i in text_list:
        my_substitutions = i.maketrans(
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&()*+,-./:;<=>?@[]^_`{|}~'\\",
      "abcdefghijklmnopqrstuvwxyz                                          ")
        cleaned_text = i.translate(my_substitutions)
        wds = cleaned_text.split()
        words += wds
    return words
def uniquelize(alist):
    '''Return a list contain all the elements but with same elements'''
    alist = ' '.join(alist).split()
    alist = list(set(alist))
    return alist
def word_not_in_count(file,vocab):
    '''Find the number of words that are in file but not in vocab'''
    words = uniquelize(texts_to_words(extract_words_from_file(file)))
    words_not_in = []
    vocab_list = extract_words_from_file(vocab)
    for i in words:
        if not find_element_binary(vocab_list,i):
            words_not_in.append(i)
    return len(words_not_in)
if __name__ == '__main__':
    import time
    time_start = time.time()
    file = r'AL-cs-homework-June-17-Monday-2019-master\ALice in Wondeland.txt'
    vocab = r'AL-cs-homework-June-17-Monday-2019-master\Vocabulary1.txt'
    print(f'There are {len(texts_to_words(extract_words_from_file(file)))} words in Alice in Wonderland, only {len(uniquelize(texts_to_words(extract_words_from_file(file))))} words are unique.')
    print(f'There are {word_not_in_count(file,vocab)} not in vocabulary')
    print(f'It takes {round(time.time()-time_start,3)}s')