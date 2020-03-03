def foo(x):
    print ('foo', x)
def bar (a,b):
    """Складывает и возвращает сумму а и б"""
    return a+b
print ('Library imported or started')
if __name__=="__main__":
    print ('Libriry executed separately')
else:
    print ('Library is just imported')
object=[]
def create_object (name):
    object.append("object["+name+"]")
def print_objects():
    print ('Все объекты')
    for obj in object:
        print (obj)