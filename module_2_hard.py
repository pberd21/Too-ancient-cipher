def generate_password(n):
    result = ""
    used_pairs = set()
    
    for i in range (1, n):
        for j in range (i, n):
            if n % (i + j ) == 0:
                pair = f'{i}{j}'
                if pair not in used_pairs:
                    result += pair
                    used_pairs.add(pair)
    return result
n = int(input("Введите число от 3 до 20: "))
result = generate_password(n)
print(result)