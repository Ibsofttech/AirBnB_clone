#!/usr/bin/python3
"""Airbnb console"""
import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):

    __myClass = ["BaseModel", "User", "Place", "State", "City",
                 "Amenity", "Review"]

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """Exit the program"""
        print()
        return True

    def emptyline(self):
        """show the prompt again, just like infinit loop"""
        pass

    def do_create(self, arg):
        """ Creates a new instance of BaseModel"""
        line = arg.split()
        if not len(line):
            print("** class name missing **")
        elif line[0] not in self.__myClass:
            print("** class name missing **")
        else:
            new_line = eval(line[0])()
            new_line.save()
            print(new_line.id)

    def do_show(self, arg):
        """Prints the string representation of an instance
        based on the class name and id"""
        line = arg.split()

        if not len(line):
            print("** class name missing **")
        elif line[0] not in self.__myClass:
            print("** class name missing **")
        elif len(line) == 1:
            print("** instance id missing **")
        else:
            key = f"{line[0]}.{line[1]}"
            if key not in storage.all():
                print("** no instance found **")
            else:
                print(storage.all()[key])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        line = arg.split()

        if not len(line):
            print("** class name missing **")
        elif line[0] not in self.__myClass:
            print("** class name missing **")
        elif len(line) == 1:
            print("** instance id missing **")
        else:
            key = f"{line[0]}.{line[1]}"
            if key not in storage.all():
                print("** no instance found **")
            else:
                del (storage.all()[key])
            storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances
        based or not on the class name"""
        line = arg.split()

        if not len(line):
            print([str(val) for val in storage.all().values()])
        elif line[0] not in self.__myClass:
            print("** class doesn't exist **")
        else:
            all_list = []
            for key, val in storage.all().items():
                if key.startswith(line[0]):
                    all_list.append(str(val))
            print(all_list)

    def do_update(self, arg):
        """Updates an instance based on the class name and
        id by adding or updating attribute """
        line = arg.split()

        if not len(line):
            print("** class name missing **")
        elif line[0] not in self.__myClass:
            print("** class name missing **")
        elif len(line) == 1:
            print("** instance id missing **")
        else:
            key = f"{line[0]}.{line[1]}"
            if key in storage.all():
                if len(line) < 3:
                    print(f"** attribute name missing **")
                elif len(line) < 4:
                    print(f"** value missing **")
                else:
                    obj = storage.all()[key]
                    try:
                        setattr(obj, line[2], eval(line[3]))
                    except NameError:
                        setattr(obj, line[2], line[3])
                    obj.save()
            else:
                print(f"** no instance found **")

    def default(self, arg):
        """handles special commands and unknown commands"""
        line = arg.split('.')

        if line[0] in self.__myClass:
            if line[1] == "all()":
                self.do_all(line[0])
            elif line[1] == "count()":
                count = 0
                for k in storage.all().keys():
                    if k.startswith(line[0]):
                        count = count + 1
                print(count)
            elif line[1].startswith("show"):
                id_len = line[1].split('"')[1]
                self.do_show(f"{line[0]} {id_len}")
            elif line[1].startswith("destroy"):
                id_len = line[1].split('"')[1]
                self.do_destroy(f"{line[0]} {id_len}")
            elif line[1].startswith("update"):
                new_id = line[1].split('(')[1].split(')')[0].split(',')
                _id = new_id[0].strip('"')
                _name = new_id[1].strip('" ')
                _value = new_id[2].strip(' ')
                print(f"{line[0]} {_id} {_name} {_value}")
                self.do_update()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
