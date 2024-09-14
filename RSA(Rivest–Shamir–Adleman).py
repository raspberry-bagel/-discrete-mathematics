# список первых простых чисел для последующей проверки
import random
first_primes_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
31, 37, 41, 43, 47, 53, 59, 61, 67,
71, 73, 79, 83, 89, 97, 101, 103,
107, 109, 113, 127, 131, 137, 139,
149, 151, 157, 163, 167, 173, 179,
181, 191, 193, 197, 199, 211, 223,
227, 229, 233, 239, 241, 251, 257,
263, 269, 271, 277, 281, 283, 293,
307, 311, 313, 317, 331, 337, 347]

# выбираем р из такого промежутка, который определяет длину числа в битах. Например,
# при n = 3 будет выбрано число из промежутка чисел от 5 (101 в двоичной СС) до 7 (111 в двоичной СС)

def n_bit_random(n):
    return random.randrange(2**(n-1)+1, 2**n - 1)
    # первая проверка на простоту
    
def low_level_prime(n):
    while True:
        pc = n_bit_random(n)
        
    for i in first_primes_list:
        if pc % i == 0 and i**2 <= pc:
            break
        else:
            return pc
            
# проверка на простоту по методу Миллера Рабина
def Miller_Rabin_passed(mrc):
    max_Divisions_Two = 0
    ec = mrc-1
    while ec % 2 == 0:
        ec >>= 1
        max_Divisions_Two += 1
    assert(2**max_Divisions_Two * ec == mrc-1)
    
    def trialComposite(round_tester):
        if pow(round_tester, ec, mrc) == 1:
            return False
        for i in range(max_Divisions_Two):
            if pow(round_tester, 2**i * ec, mrc) == mrc-1:
                return False
        return True
        
    number_Rabin_Trials = 20

    for i in range(number_Rabin_Trials):
        round_tester = random.randrange(2, mrc)
        if trialComposite(round_tester):
            return False
    return True
    
# генерируем p c длиной 8 бит
while True:
    bit = 8
    prime_candidate = low_level_prime(bit)
    if not Miller_Rabin_passed(prime_candidate):
        continue
    else:
        p = prime_candidate
        break
    
# генерируем q с длиной 8 бит
while True:
    bit = 8
    prime_candidate = low_level_prime(bit)
    if not Miller_Rabin_passed(prime_candidate):
        continue
    else:
        q = prime_candidate
        break

# находим функцию Эйлера, для нашего n будет: phi(n) = phi(p*q) = (p-1)*(q-1)
n = p*q
def euler(p, q):
    return (p-1)*(q-1)
    
# теперь есть возможность сгенерировать открытый ключ e, который должен удовлетворять 2 условиям:
# 1) взаимно простое с phi(n)
# 2) меньше phi(n)
def GCD(n, m):
    if m == 0:
        return n
    else:
        return GCD(m, n % m)
        
for i in range(phi_n-1, 3, -1):
    if GCD(i, phi_n) == 1:
        e = i
        break
print('Открытый ключ: ', (e, n))

# генерируем закрытый ключ, зная, что он обратен нашему e по модулю phi(n)
for i in range(100000, 3, -1):
    if (e*i) % phi_n == 1:
        d = i
        break
print('Закрытый ключ: ', (d, n))

# ключи получены, можно написать функции шифрования и дешифрования сообщений.
# чтобы зашифровать сообщение понадобится представить буквы в виде чиcел,
# с этим может помочь таблица символов Unicode

def encryption(text, key):
    e, n = key
    text_a = []
    for i in range(len(text)):
        text_a.append(ord(text[i]))
    for i in range(len(text_a)):
        text_a[i] = ((text_a[i]**e) % n)
    return text_a
    
def decryption(text_encryption, key):
    d, n = key
    text_b = []
    for i in range(len(text_encryption)):
        text_b.append((text_encryption[i]**e) % n)
    text_decryption = ''
    for i in range(len(text_b)):
        text_decryption += chr(text_b[i])
    return text_decryption
    
# проверим работу на сообщении, содержащее буквы разного регистра, цифры и иные симоволы.
# выведем зашифрованное сообщение, затем расшифрованно, должны совпасть
x = encryption('LaTeX-BIT2023', (e, n))
print(x)
print(decryption(x, (d, n)))



