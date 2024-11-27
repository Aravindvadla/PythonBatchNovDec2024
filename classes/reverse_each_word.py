# Input a sentence from the user
sentence = input("Enter a sentence to reverse each word: ")

# Reverse each word using string slicing
reversed_sentence = " ".join([word[::-1] for word in sentence.split()])

# Print the reversed words
print("Reversed words in sentence:", reversed_sentence)
