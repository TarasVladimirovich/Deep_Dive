import pickle

ser = pickle.dumps('Python Pickle Peppers')
print(ser)
deser = pickle.loads(ser)
print(deser)