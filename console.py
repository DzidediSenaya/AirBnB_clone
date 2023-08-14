#!/usr/bin/python3
"""Command interpreter entry point."""
import cmd
import re
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Defines the HolbertonBnB command interpreter.

    Attributes:
        prompt (str): The command prompt.
    """

    prompt = "(hbnb) "
    classes = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Place": Place,
        "Amenity": Amenity,
        "Review": Review
    }

    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program."""
        print("")
        return True

    def _get_obj_by_id(self, class_name, obj_id):
        """Retrieve object by class name and id."""
        obj_key = "{}.{}".format(class_name, obj_id)
        obj_dict = storage.all()
        return obj_dict.get(obj_key)

    def _print_instances(self, class_name=None):
        """Print string representations of instances."""
        obj_dict = storage.all()
        if class_name:
            class_type = HBNBCommand.classes.get(class_name)
            obj_list = [str(obj) for obj in obj_dict.values()
                        if isinstance(obj, class_type)]
        else:
            obj_list = [str(obj) for obj in obj_dict.values()]
        print(obj_list)

    def do_create(self, arg):
        """Usage: create <class>
        Create a new class instance and print its id.
        """
        if not arg:
            print("** class name missing **")
            return
        class_name = arg
        if class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        instance = HBNBCommand.classes[class_name]()
        instance.save()
        print(instance.id)

    def do_show(self, arg):
        """Usage: show <class> <id>
        Display the string representation of a class instance of a given id.
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_id = args[1]
        obj = self._get_obj_by_id(class_name, obj_id)
        if obj is None:
            print("** no instance found **")
            return
        print(obj)

    def do_destroy(self, arg):
        """Usage: destroy <class> <id>
        Delete a class instance of a given id."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_id = args[1]
        obj = self._get_obj_by_id(class_name, obj_id)
        if obj is None:
            print("** no instance found **")
            return
        del storage.all()["{}.{}".format(class_name, obj_id)]
        storage.save()

    def do_all(self, arg):
        """Usage: all or all <class>
        Display string representations of all instances of a given class.
        If no class is specified, displays all instantiated objects."""
        if not arg:
            self._print_instances()
        elif arg in HBNBCommand.classes:
            self._print_instances(arg)
        else:
            print("** class doesn't exist **")

    def do_count(self, arg):
        """Usage: count <class>
        Retrieve the number of instances of a given class."""
        if arg in HBNBCommand.classes:
            class_name = arg
            class_type = HBNBCommand.classes[class_name]
            obj_count = sum(1 for obj in storage.all().values()
                            if isinstance(obj, class_type))
            print(obj_count)
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """Usage: update <class> <id> <attribute_name> <attribute_value>
        Update a class instance of a given id by adding or updating
        a given attribute key/value pair."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_id = args[1]
        obj = self._get_obj_by_id(class_name, obj_id)
        if obj is None:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        attr_name, attr_value = args[2], args[3]
        setattr(obj, attr_name, attr_value)
        storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
