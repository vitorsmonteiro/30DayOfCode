# Enter your code here. Read input from STDIN. Print output to STDOUT
def returneventext(text):
    new_text = text[::2] + " " + text[1::2]
    return new_text

T = int(input())
texts = []
for i in range(T):
    text = input()
    even_text = returneventext(text)
    texts.append(even_text)

for j in range(T):
    print(texts[j])
