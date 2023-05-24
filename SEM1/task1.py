# Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей. Дано: a, b, c - стороны
# предполагаемого треугольника. Требуется сравнить длину каждого отрезка - стороны с суммой двух других. Если хотя бы 
# в одном случае отрезок окажется больше суммы двух других, то треугольника с такими сторонами не существует.
# Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.

a = int(input())
b = int(input())
c = int(input())
if a < b + c and b < a + c and c < a + b:
     print("Треугольник существует")
else:
     print("Треугольник не существует")
if a == b == c:
    print("Равностороний")
elif a == b or a == c or b == c:
    print("Равнобедренный")
else:
    print("Разносторонний")