class A:
    varA = "hello friends"

class B:
    varB = "how are you all"

class C(A, B):
    varC = "i am fine"

c1 = C()
print(c1.varA)
print(c1.varB)
print(c1.varC)