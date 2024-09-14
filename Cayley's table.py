from itertools import chain, combinations

# Функция для проверки замкнутости подгруппы
def check_closure(subset, cayley_table):
    for a in subset:
        for b in subset:
            if cayley_table[a][b] not in subset:
                return False
    return True

# Функция для проверки обратимости подгруппы
def check_invertibility(subset, cayley_table):
    for a in subset:
        has_inverse = False
        for b in subset:
            if cayley_table[a][b] in subset and cayley_table[b][a] in subset:
                has_inverse = True
                break
        if not has_inverse:
            return False
    return True

# Функция для нахождения всех нормальных подгрупп
def find_normal_subgroups(cayley_table):
    n = len(cayley_table)
    elements = set(range(n))
    all_subgroups = []
    for subset in powerset(elements):
        if subset and subset != elements:
            if check_closure(subset, cayley_table) and check_invertibility(subset, cayley_table):
                all_subgroups.append(subset)
    return all_subgroups

def powerset(s):
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

def is_associative(cayley_table):
    for i in range(len(cayley_table)):
        for j in range(len(cayley_table)):
            for k in range(len(cayley_table)):
                if cayley_table[cayley_table[i][j]][k] != cayley_table[i][cayley_table[j][k]]:
                    return False
    return True

def is_commutative(cayley_table):
    for i in range(len(cayley_table)):
        for j in range(len(cayley_table)):
            if cayley_table[i][j] != cayley_table[j][i]:
                return False
    return True

def has_identity_element(cayley_table):
    for i in range(len(cayley_table)):
        has_identity = True
        for j in range(len(cayley_table)):
            if cayley_table[i][j] != j:
                has_identity = False
                break
        if has_identity:
            return True
    return False

def is_invertible(cayley_table):
    for i in range(len(cayley_table)):
        has_inverse = True
        for j in range(len(cayley_table)):
            found_identity = False
            for k in range(len(cayley_table)):
                if cayley_table[i][k] == j and cayley_table[k][i] == j:
                    found_identity = True
                    break
            if not found_identity:
                has_inverse = False
                break
        if not has_inverse:
            return False
    return True

def determine_structure_type(cayley_table, elems):
    if is_associative(cayley_table):
        if is_invertible(cayley_table):
            if has_identity_element(cayley_table):
                return 'ГРУППА'
            else:
                return 'ОБРАТНАЯ ПОЛУГРУППА'
        else:
            if has_identity_element(cayley_table):
                return "МОНОИД"
            else:
                return "ПОЛУГРУППА"
    else:
        if has_identity_element(cayley_table):
            if is_invertible(cayley_table):
                return "ЛУПА (пупа)"
            else:
                return "УНИТАРНАЯ МАГМА"
        else:
            if is_invertible(cayley_table):
                return "КВАЗИГРУППА"
            else:
                return "МАГМА"

def table_properties(cayley_table_example):
    properties = []
    if is_commutative(cayley_table_example):
        properties.append('is_commutative')
    else:
        properties.append('is_not_commutative')
    if is_associative(cayley_table_example):
        properties.append('is_associative')
    else:
        properties.append('is_not_associative')
    if is_invertible(cayley_table_example):
        properties.append('is_invertible')
    else:
        properties.append('is_not_invertible')
    if has_identity_element(cayley_table_example):
        properties.append('has_identity_element')
    else:
        properties.append('hasn\'t_identity_element')
    return properties

# Ввод элементов и таблицы Кэли
n = int(input("Введите порядок таблицы Кэли: "))
elements = [0] * n
print("Введите элементы таблицы:")
for i in range(n):
    elements[i] = int(input())
print("Введите элементы таблицы построчно:")
cayley_table_example = []
for i in range(n):
    row = list(map(int, input().split()))  # Предполагается, что элементы таблицы являются целыми числами, а не буквами
    cayley_table_example.append(row)

# Определим тип структуры
print("Тип структуры:", determine_structure_type(cayley_table_example, elements))
print("Свойства таблицы:", *table_properties(cayley_table_example))

# Поиск нормальных подгрупп
normal_subgroups = find_normal_subgroups(cayley_table_example)
print("Найденные нормальные подгруппы:")
for subgroup in normal_subgroups:
     print(subgroup)