#!/usr/bin/python3

"""

The entry point of the command interpreter

"""
import cmd
from models.base_model import BaseModel
from models import storage
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
    """Class implement command intrepreter"""

    prompt = "(hbnb) "

    def do_EOF(self, line):
        """Ctrl + D stops the console"""
        return True

    def do_quit(self, line):
        """quit command will exit the console"""
        return True

    def emptyline(self):
        """Do nothing when getting an empty line"""
        return

    def do_create(self, line):
        if not line:
            print("** class name missing ** ")
        elif line == "BaseModel":
            new_obj = BaseModel()
            print(new_obj.id)
            storage.save()
        else:
            print("** class doesn't exist **")

    def do_ll(self, line):
        """It is overwhelming writing that long command"""
        self.do_create("BaseModel")

    def do_reset(self, line):
        """Delete all the content of the file"""
        with open(FileStorage._FileStorage__file_path, "w") as f:
            FileStorage._FileStorage__objects = {}
            f.write("")

    def do_show(self, line):
        """String representation of an instance based on the class name"""
        args = line.split()

        if not line:
            print("** class name missing **")
        elif args[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(args) != 2:
            print("** instance id missing **")
        elif args[1] not in storage.all().keys():
            print("** no instance found **")
        else:
            print(storage.all()[args[1]])

    def complete_show(self, text, line, begidx, endidx):
        """Auto completion by providing available IDs"""
        if line.startswith("show BaseModel "):
            IDs = storage.all().keys()
            completions = [arg for arg in IDs if arg.startswith(text)]
            return completions
        elif line.startswith("show "):
            return ["BaseModel"]

    def do_destroy(self, line):
        """String representation of an instance based on the class name"""
        args = line.split()

        if not line:
            print("** class name missing **")
        elif args[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(args) != 2:
            print("** instance id missing **")
        elif args[1] not in storage.all().keys():
            print("** no instance found **")
        else:
            del storage.all()[args[1]]
            storage.save()

    def complete_destroy(self, text, line, begidx, endidx):
        """Auto completion by providing available IDs"""
        if line.startswith("destroy BaseModel "):
            IDs = storage.all().keys()
            completions = [arg for arg in IDs if arg.startswith(text)]
            return completions
        elif line.startswith("destroy "):
            return ["BaseModel"]

    def do_all(self, line):
        """ Prints all string representation of all instances"""
        if not line or line == "BaseModel":
            instances =  storage.all().values()
            instance_strings = [str(rep) for rep in instances]
            print(instance_strings)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
