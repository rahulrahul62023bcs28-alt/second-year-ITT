def get_length(s):
    count = 0
    for char in s:
        count += 1
    return count

def reverse_string(s):
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str

passage = input("Enter a passage: ")

words = []
current_word = ""
for char in passage:
    if char == " ":
        if current_word != "":
            words += [current_word]
            current_word = ""
    else:
        current_word += char
if current_word != "":
    words += [current_word]

word_counts = {}
largest_word = ""
max_len = 0

for w in words:
    current_w_len = get_length(w)
    if current_w_len > max_len:
        max_len = current_w_len
        largest_word = w

    if w in word_counts:
        word_counts[w] += 1
    else:
        word_counts[w] = 1

print(f"\n--- Statistics for Your passage ---")
print(f"Total length of passage (characters): {get_length(passage)}")

print("\nWord Repetitions:")
repeat_found = False
for w in word_counts:
    if word_counts[w] > 1:
        print(f"'{w}': repeated {word_counts[w]} times")
        repeat_found = True

if not repeat_found:
    print("No repeated words found.")

print(f"\nLargest word: {largest_word}")
print(f"Largest word reversed: {reverse_string(largest_word)}")
