a = b'r\xc3\xa9sum\xc3\xa9'
a1 = a.decode("UTF8")
print('a1:', a1)
a2 = a1.encode("Latin1")
print('a2:', a2)
a3 = a2.decode("Latin1")
print('a3:', a3)