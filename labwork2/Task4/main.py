def swap_words(sentence, word1, word2):
    words = sentence.split()
    modified_words = []
    # Iterate through the list of words
    for word in words:
        if word.strip('.,!?()') == word1:
            # Append the second word with the same punctuation
            modified_words.append(word2 + word[len(word1):])
        elif word.strip('.,!?()') == word2:
            # Append the first word with the same punctuation
            modified_words.append(word1 + word[len(word2):])
        else:
            # Append the original word
            modified_words.append(word)

    # Join the list of modified words back into a sentence
    new_sentence = ' '.join(modified_words)

    return new_sentence


# Main function
def main():
    first = int(input("Enter first word number(N) = "))
    second = 20 - first
    print(f"Second word number(20 - N) = {second}")
    text = ("A programmer is a programming specialist who designs software "
            "(in simpler cases, individual programs) for programmable devices "
            "that typically contain one or more processors.")
    temp = text
    text = text.split(' ')
    print("Start text: ", *text)
    word1 = text[first].strip('.,!?()')
    word2 = text[second].strip('.,!?()')
    print("Word 1 -", word1)
    print("Word 2 -", word2)
    swap_words(temp, word1, word2)
    print("New text: ", swap_words(temp, word1, word2))


if __name__ == '__main__':
    main()