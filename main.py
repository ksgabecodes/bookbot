def count_characters(text):
    lbook_contents=text.lower()
    char_dict={}
    unique_chars=set(lbook_contents)
    for uchar in unique_chars:
        cur_count=0
        for char in lbook_contents:
            if char==uchar:
                cur_count+=1
        char_dict[uchar]=cur_count
    return char_dict

def count_words(text):
    wordcount=0
    split_text=text.split()
    for word in split_text:
        wordcount += 1
    return wordcount


def main():
    book_contents=""
    counted_characters={}
    with open("books/frankenstein.txt") as f:
        book_contents = f.read()
    print(book_contents)
    print(count_words(book_contents))
    counted_characters=count_characters(book_contents)
    print(counted_characters)
    return


main()