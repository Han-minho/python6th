words = ['apple','bat','bar','atom','book']
by_letters = {}

for word in words:
    letter = word[0]
    if letter not in by_letters:
        by_letters[letter] = [word]
    else:
        by_letters[letter].append(word)

print(by_letters)
try:
    print(by_letters['c']) # KeyError :
except KeyError:
    words.append('c')
    print("KeyError입니다.")
    print(f"{words}")
finally:
    print("KeyError | 입니다.")
