# Составить генератор (yield), который переведет символы строки из верхнего
# регистра в нижний.
def ss(stroka):
    for n in stroka:
        yield stroka.join(str(n).lower())


stroka = "Developers are building the future on GitHub every day"
sus = [char for char in ss(stroka)]
print("".join(sus))
