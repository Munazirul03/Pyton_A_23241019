# Tabel Kebenaran (Logika Bolean)
# and or not xor

# NOT
print("************ logika not ************")
x = False 
y = not x
print("nilai dari x =", x)
print("nilai dari y =", y)

# and(Hanya bernilai benar ketika semuanya benar)
# (jika salah satu ada yang salah maka semuanya salah)
print("************ logika and ************")
x = False
y = True
z = x and y 
print(x, "and", y, "=",z)
      
x = True 
y = False
z = x and y 
print(x, "and", y, "=",z)

# OR (Akan bernilai True, selama ada satu aja yang True,)
# (bernilai salah, ketika keduanya salah)
print("************ logika or ************")
x = False
y = True
z = x and y 
print(x, "and", y, "=",z)
      
x = True 
y = False
z = x and y 
print(x, "and", y, "=",z)




