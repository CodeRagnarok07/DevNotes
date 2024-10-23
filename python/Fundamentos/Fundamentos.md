

### manejo de la memoria



```python

a = "a"
id_a = id(a)
print(id_a) # 123214234324

# get reference number
import sys
b = "b"
obj = [a,2,3,b]
sys.getrefcount(obj) # 3 if is 0 call the garbage collection

# get data from the reference
import ctypes
a = ["hola", "mundo", 2]
a_id = id(a)
print(a_id)
a_info = ctypes.cast(a_id, ctypes.py_object).value
print(a_info)

## or 

def get_by_address(address):
    return [x for x in globals().values() if id(x)==address]

var = 'I need to be accessed by id!'
address = id(var)
print(address)
var2 = get_by_address(address)
```





- https://realpython.com/pointers-in-python/




