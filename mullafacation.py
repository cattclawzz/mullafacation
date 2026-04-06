def mullafacation(x,y):
    mullac = {
        1: x * 2,
        2: 0,
        3: x ** 2,
        4: 1,
        ">=5": round(x/y)*y
    }
    return mullac[">=5"] if y >= 5 else mullac[y]

print("\n".join([f"11 M {i} = {mullafacation(11, i)}" for i in range(1,6)]))