import sys

print(sys.hash_info.width)
print(sys.hash_info.hash_bits)
print(sys.hash_info.algorithm)
# print(hash(([])))  # typeError
# List, Set - TypeError: unhashable
print(hash({}))
# hash is changed from run to run but equal during program run 
