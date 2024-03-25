# a = 'qwerty'
# for i in a:
#     print(i)

# line = ""
# for i in range(5):
#     line = ""
#     for j in range(5):
#         line += "*"
#     print(line)

# text = 'СъЕШЬ ещё этих МяГкИх французских булок'
# print(len(text))  #подсчет количества символов в строке
# print('ещё' in text) #проверка есть ли в строке эти символы
# print(text.lower()) #подъем в верхний регистр
# print(text.upper()) #опуск в нижний регистр
# print(text.replace('ещё', 'ЕЩЁ')) #замена текста

#Срезы
text = 'съешь ещё этих мягких французских булок'
print(text[0])                          # c
print(text[1])                          # ъ
print(text[len(text)-1])                # к
print(text[-5])                         # б
print(text[:])                          # съешь ещё этих мягких французских булок
print(text[:2])                         # съ
print(text[len(text)-2:])               # ок
print(text[2:9])                        # ешь ещё
print(text[6:-18])                      # ещё этих мягких
print(text[0:len(text):6])              # сеикакл
print(text[::6])                        # сеикакл
text = text[2:9] + text[-5] + text[:2]  # ...
print(text)