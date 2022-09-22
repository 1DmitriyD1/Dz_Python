# 2-Напишите программу для. проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат. 
# Предикату можно заменить на понятие "бит".
# Должна получиться таблица истинности.
# not (X or Y or Z) == not(X) and not(Y) and not(Z)

print("----------------------")
print("| X", "Y", "Z" , "Result |", sep =" | ")
print("----------------------")
for X in range(2):
    for Y in range(2):
        for Z in range(2):
            res = not(X or Y or Z) == (not(X) and not(Y) and not(Z))
            print(f"| {X} | {Y} | {Z} |  {res}  |")
print("----------------------")