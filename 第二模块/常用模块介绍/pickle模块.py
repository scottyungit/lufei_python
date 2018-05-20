import pickle

# d={"name":"Alex","age":22}
# f=open("data.pkl","wb")
# pickle.dump(d,f)

f=open("data.pkl","rb")
d=pickle.load(f)
print(d)