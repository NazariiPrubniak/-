from string import punctuation


A_or_B = ''

while True:
    print("A) Sort words with alphabet\nB) Get numbers of all letters in text")
    a_or_b = input("Choose A or B: ")

    if a_or_b in ['A', 'B']:
        break
    else:
        print('Try Again, Please')


text = input("Write some text here")

if a_or_b == 'A':
    words = text.split()
    words = set([word for word in words if len(word) > 2])
    words = list(words)
    words.sort(reverse=0)
    print('Words sort with alphabet:', end="\n\t")
    print(', '.join(words))
else:
    chars = {}
    for char in text:
        if char not in punctuation and char != " ":
            chars[char] = chars[char]+1 if char in chars else 1
    print("Number of all letters in text:")
    for i in chars.items():
        print(f"\t{i[0]}: {i[1]}")