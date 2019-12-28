"""
Specify the kinds of objects to create using a prototypical instance,
and create new objects by copying this prototype.
"""

from copy import deepcopy
from datetime import datetime

class Prototype:
    def clone(self):
        pass


class CloneableComponent(Prototype):
    """
    Example class to be copied.
    """
    def __init__(self, primitive, object):
        self.primitive = primitive
        self.object = object
        self.circular_ref = None
    
    def display(self):
        pass

    def clone(self):
        new_object = deepcopy(self)
        new_object.circular_ref =  deepcopy(self.circular_ref)
        new_object.circular_ref.prototype = new_object
        return new_object

class ComponentWithBackReference:
    def __init__(self, prototype):
        self.prototype = prototype

def main():
    original = CloneableComponent(123, datetime.now())
    original.circular_ref = ComponentWithBackReference(original)
    copy = original.clone()

    if original.primitive is copy.primitive:
        print("Primitive field values have been carried over to a clone.")
    else:
        print("Primitive field values have not been copied.")

    if original.object is copy.object:
        print("Simple component has not been cloned.")
    else:
        print("Simple component has been cloned.")

    if original.circular_ref is copy.circular_ref:
        print("Component with back reference has not been cloned.")
    else:
        print("Component with back reference has been cloned.")

    if original.circular_ref.prototype is copy.circular_ref.prototype:
        print("Component with back reference is linked to original object.")
    else:
        print("Component with back reference is linked to the clone.")

if __name__ == "__main__":
    main()