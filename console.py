#!/usr/bin/python3
"""Defines the HolbertonBnB command interpreter."""
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
    prompt = "(hbnb) "
    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    def emptyline(self):
        pass

    def default(self, arg):
        command, args = arg.split(" ", 1)

        if command in ["all", "show", "destroy", "count", "update"]:
            method_name = "do_" + command
            if hasattr(self, method_name):
                getattr(self, method_name)(args)
            else:
                print("*** Unknown command: {}".format(command))
        else:
            print("*** Unknown syntax: {}".format(arg))

    def do_all(self, args):
        arglist = args.split()
        if len(arglist) > 0 and arglist[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            obj_list = []
            for obj in storage.all().values():
                if len(arglist) > 0 and arglist[0] == obj.__class__.__name__:
                    obj_list.append(str(obj))
                elif len(arglist) == 0:
                    obj_list.append(str(obj))
            print(obj_list)

    def do_count(self, args):
        arglist = args.split()
        if len(arglist) == 0:
            print("** class name missing **")
            return
        class_name = arglist[0]
        count = sum(1 for obj in storage.all().values() if isinstance(obj, globals()[class_name]))
        print(count)

    def do_show(self, args):
        arglist = args.split()
        if len(arglist) != 2:
            print("** syntax error: show <class name> <id>")
            return

        class_name, instance_id = arglist
        if class_name not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return

        key = "{}.{}".format(class_name, instance_id)
        if key in storage.all():
            print(storage.all()[key])
        else:
            print("** no instance found **")

    def do_destroy(self, args):
        arglist = args.split()
        if len(arglist) != 2:
            print("** syntax error: destroy <class name> <id>")
            return

        class_name, instance_id = arglist
        if class_name not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return

        key = "{}.{}".format(class_name, instance_id)
        if key in storage.all():
            del storage.all()[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_update(self, args):
        arglist = args.split()
        if len(arglist) < 3:
            print("** syntax error: update <class name> <id> <attribute> <value>")
            return

        class_name, instance_id, attribute = arglist[:3]
        if class_name not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return

        key = "{}.{}".format(class_name, instance_id)
        if key in storage.all():
            obj = storage.all()[key]
            if len(arglist) == 3:
                print("** value missing **")
            else:
                value = arglist[3]
                setattr(obj, attribute, value)
                storage.save()
        else:
            print("** no instance found **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
