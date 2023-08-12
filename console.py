#!/usr/bin/python3
"""
Command interpreter entry point.
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
    Custom command interpreter class.
    """
    prompt = '(hbnb) '

    valid_classes = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
    }

    def do_quit(self, arg):
        """
        Quit command to exit the program.
        """
        return True

    def do_EOF(self, arg):
        """
        Exit the program at end of file (Ctrl+D).
        """
        print()  # Print a new line before exiting
        return True

    def emptyline(self):
        """
        Override to not execute anything on an empty line.
        """
        pass

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id.
        """
        if not arg:
            print("** class name missing **")
            return
       try:
    new_instance = eval(arg)()
    new_instance.save()
    print(new_instance.id)
except NameError:
    print("** class doesn't exist **")

    def do_show(self, arg):
        """
        Prints the string representation of an instance based on
        the class name and id.
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in storage.classes.keys():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = args[0] + "." + args[1]
        if key in storage.all():
            print(storage.all()[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id.
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in storage.classes.keys():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = args[0] + "." + args[1]
        if key in storage.all():
            storage.all().pop(key)
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """
        Prints all string representation of all instances based or not
        on the class name.
        """
        args = arg.split()
        obj_list = []
        if not args:
            for key, value in storage.all().items():
                obj_list.append(str(value))
            print(obj_list)
            return
        if args[0] not in storage.classes.keys():
            print("** class doesn't exist **")
            return
        for key, value in storage.all().items():
            if key.startswith(args[0]):
                obj_list.append(str(value))
        print(obj_list)

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id by adding or
        updating attribute (save the change into the JSON file).
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in storage.classes.keys():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = args[0] + "." + args[1]
        if key not in storage.all():
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        instance = storage.all()[key]
        setattr(instance, args[2], args[3].strip("\""))
        instance.save()

    def do_count(self, arg):
        """
        Retrieves the number of instances of a class.
        """
        if not arg:
            print("** class name missing **")
            return
        if arg not in storage.classes.keys():
            print("** class doesn't exist **")
            return
        count = 0
        for key in storage.all():
            if key.startswith(arg + "."):
                count += 1
        print(count)

    def do_update_dict(self, arg):
        """
        Updates an instance based on the class name and id with a dictionary.
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in storage.classes.keys():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = args[0] + "." + args[1]
        if key not in storage.all():
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** dictionary missing **")
            return
        instance = storage.all()[key]
        try:
    new_dict = eval(args[2])
except SyntaxError:
    print("** invalid dictionary format **")
    return
        for k, v in new_dict.items():
            setattr(instance, k, v)
        instance.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
