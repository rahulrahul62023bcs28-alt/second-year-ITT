passage = input("Enter a passage: ")

words = passage.split()

print(f"\n--- Statistics for Your passage ---")
print(f"Total length of passage (characters): {len(passage)}")

if words:
    largest_word = max(words, key=len)
    reversed_word = largest_word[::-1]

    print(f"\nLargest word: {largest_word}")
    print(f"Largest word reversed: {reversed_word}")

print("\nWord Repetitions:")
repeat_found = False
for w in set(words):
    count = words.count(w)
    if count > 1:
        print(f"'{w}': repeated {count} times")
        repeat_found = True

if not repeat_found:
    print("No repeated words found.")
