def f(x,l=[]):
    for i in range(x):
        l.append(i*i)
    print(l)
replicate="def f(x,l=[]):" \
    " for i in range(x): " \
        "l.append(i*i)" \
    " print(l) " \
          "replicate=" " " \
  "f(2) " \
  "f(3,[3,2,1]) " \
  "f(3)" \
  "print(replicate)"
f(2)
f(3,[3,2,1])
f(3)
print(replicate)

