import test_lib as lib
print ('Main module', __name__)
print (lib.foo(196))
print (lib.bar(2,2))
x=lib.bar(1,5)
print(x)
object=[]
lib.create_object("круг")
lib.create_object("круг2")
lib.create_object("круг3")
lib.print_objects()

