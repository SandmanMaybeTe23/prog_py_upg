word_saver=[]
number_saver=[]
translation_numbers_saver=[]
translation_words_saver=[]

coded_world=0


def coding():
    for a in number_saver:
        translation_numbers_saver.append(a+5)


numbers=input("say a str ")

for y in numbers:
    word_saver.append(y)
print(word_saver)

for z in word_saver:
    number_saver.append(ord(z))
print(number_saver)


coding()

print(translation_numbers_saver)

for b in translation_numbers_saver:
    translation_words_saver.append(chr(b))
print(translation_words_saver)


coded_world=translation_words_saver

print(coded_world)