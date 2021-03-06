# Chapter 8 Review

Every Python object has an identity, a type, and a value. Only the value 
of an object changes over time.

If two variables refer to immutable objects that have equal values 
(a == b is True), in practice it rarely matters if they refer to copies 
or are aliases referring to the same object because the value of an 
immutable object does not change, with one exception. The exception is 
immutable collections such as tuples and frozensets: if an immutable 
collection holds references to mutable items, then its value may actually
change when the value of a mutable item changes. In practice, this 
scenario is not so common. What never changes in an immutable collection 
are the identities of the objects within.

The fact that variables hold references has many practical consequences 
in Python programming:
- Simple assignment does not create copies.

- Augmented assignment with += or \*= creates new objects if the lefthand 
variable is bound to an immutable object, but may modify a mutable object
in place.

- Assigning a new value to an existing variable does not change the object
previously bound to it. This is called a rebinding: the variable is now 
bound to a different object. If that variable was the last reference to 
the previous object, that object will be garbage collected.

- Function parameters are passed as aliases, which means the function may
change any mutable object received as an argument. There is no way to 
prevent this, except making local copies or using immutable objects 
(e.g., passing a tuple instead of a list).

- Using mutable objects as default values for function parameters is 
dangerous because if the parameters are changed in place, then the default
is changed, affecting every future call that relies on the default.

In CPython, objects are discarded as soon as the number of references to 
them reaches zero. They may also be discarded if they form groups with 
cyclic references but no outside references. In some situations, it may be
useful to hold a reference to an object that will not by itself keep an 
object alive. One example is a class that wants to keep track of all its 
current instances. This can be done with weak references, a low-level 
mechanism underlying the more useful collections WeakValueDictionary, 
WeakKeyDictionary, WeakSet, and the finalize function from the weakref 
module.
