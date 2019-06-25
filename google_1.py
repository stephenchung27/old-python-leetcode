A = 'abcd aabc bd'
A = [1, 2, 1]
B = 'aaa aa'
B = [3, 2]

from collections import Counter

def solution(A, B):
    A_words = A.split(" ")
    B_words = B.split(" ")

    A_counts = []

    for word in A_words:
        smallest_letter = find_smallest_letter(word)
        letter_occurrences = find_number_of_occurrences(word, smallest_letter)
        A_counts.append(letter_occurrences)
    
    B_counts = []

    for word in B_words:
        smallest_letter = find_smallest_letter(word)
        letter_occurrences = find_number_of_occurrences(word, smallest_letter)
        B_counts.append(letter_occurrences)

    counts = [0] * len(B_words)

    for i in range(len(B_counts)):
        word_count = B_counts[i]
        for target_count in A_counts:
            if target_count < word_count:
                counts[i] += 1

    return [sum(target_count < word_count for target_count in A_counts) for word_count in B_counts]
    
    return counts

def find_smallest_letter(word):
    smallest = ord("z")
    for letter in word:
        smallest = min(smallest, ord(letter))
    return chr(smallest)

def find_number_of_occurrences(word, target):
    count = 0
    for letter in word:
        if letter == target:
            count += 1
    return count

print(solution(A, B))