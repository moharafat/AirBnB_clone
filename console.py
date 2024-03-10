#!/usr/bin/env python3
"""Module for class HBNBCommand that contains the
entry point of the command interpreter
"""
import cmd
import re
from tracemalloc import get_object_traceback
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models import storage


class HBNBCommand(cmd.Cmd):
    """contains the entry point of the command interpreter
    """

    MODELS = [
        'BaseModel', 'User', 'Amenity', 'City',
        'Place', 'Review', 'State'
        ]
    prompt = "(hbnb)"
    COMMANDS = {'all', 'show', 'count', 'destroy', 'update'}

    def default(self, line):
        args = line.split('.')
        if len(args) != 2:
            print(f"*** Unknown syntax: {line}")
            return
        model, command = args[0], args[1]
        if model not in self.MODELS:
            print(f"*** Unknown syntax: {line}")
            return
        id_pattern = fr"\(['\"](.+?)['\"]\)$"
        flag = 0
        for c in self.COMMANDS:
            command_pattern = fr"^{c}\((.*?)\)"
            match = re.match(command_pattern, command)
            if match:
                if c == 'count':
                    print(self.class_count(model))
                    return
                if c == 'update':
                    arguments_regex = r"['\"]([^'\"]*)['\"]"
                    arg_match = re.findall(arguments_regex, command)
                    self.onecmd(f"update {model} {' '.join(arg_match)}")
                    return
                flag = 1
                match = re.search(id_pattern, command)
                if match:
                    self.onecmd(f"{c} {model} {match.group(1)}")
                else:
                    self.onecmd(f"{c} {model}")
        if not flag:
            print(f"*** Unknown syntax: {line}")

    def class_count(self, class_name):
        """count instances of class
        """
        count = 0
        all_objects = storage.all()
        for obj_id, _ in all_objects.items():
            pattern = fr"^{class_name}\."
            if re.search(pattern, obj_id):
                count += 1
        return count

    def do_create(self, line):
        """create command
        """
        if not line:
            print("** class name missing **")
        elif line not in self.MODELS:
            print("** class doesn't exist **")
        else:
            new_model = eval(f"{line}()")
            new_model.save()
            print(f'{new_model.id}')

    def help_create(self):
        """help for create command
        """
        print('\n'.join([
            'Usage: create [model]',
            'Creates a new instance of [model], \
saves it (to [file.json] and prints the [id])',
            'Ex: create BaseModel'
            ]))

    def complete_create(self, text, line, begidx, endidx):
        """auto complete for create
        """
        if not text:
            completions = self.MODELS[:]
        else:
            completions = [
                f for f in self.MODELS
                if f.startswith(text)
                ]
        return completions

    def get_obj(self, instance_id, model):
        """get the instance from the storage
        """
        all_objects = storage.all()
        for obj_id, obj in all_objects.items():
            pattern = fr"\.{instance_id}$"
            if re.search(pattern, obj_id):
                obj_dict = obj.to_dict()
                new_obj = eval(f'{model}(**{obj_dict})')
                return new_obj
        return

    def do_show(self, line):
        """show command
        """
        args = line.split()
        if len(args) == 0:
            print('** class name missing **')
            return
        model = args[0]
        if model not in self.MODELS:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print('** instance id missing **')
            return
        instance_id = args[1]
        new_obj = self.get_obj(instance_id, model)
        if new_obj:
            print(new_obj)
        else:
            print('** no instance found **')

    def help_show(self):
        """help for show command
        """
        print('\n'.join([
            'Usage: show <model> <id>',
            'Prints the string representation of an instance \
based on the class nam and [id]',
            'Ex: show BaseModel 1234-1234-1234'
            ]))

    def complete_show(self, text, line, begidx, endidx):
        """auto complete for create
        """
        if not text:
            completions = self.MODELS[:]
        else:
            completions = [
                f for f in self.MODELS
                if f.startswith(text)
                ]
        return completions

    def do_destroy(self, line):
        """destroy command
        """
        args = line.split()
        if len(args) == 0:
            print('** class name missing **')
            return
        model = args[0]
        if model not in self.MODELS:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print('** instance id missing **')
            return
        instance_id = args[1]
        all_objects = storage.all()
        for obj_id, _ in all_objects.items():
            pattern = fr"\.{instance_id}$"
            if re.search(pattern, obj_id):
                del all_objects[obj_id]
                storage.save()
                return
        print('** no instance found **')

    def help_destroy(self):
        """help for destroy command
        """
        print('\n'.join([
            'Usage: destroy <model> <id>',
            'Deletes an instance based on the class name and id, \
(save the change into the JSON file [file.json])',
            'Ex: destroy BaseModel 1234-1234-1234'
            ]))

    def complete_destroy(self, text, line, begidx, endidx):
        """auto complete for create
        """
        if not text:
            completions = self.MODELS[:]
        else:
            completions = [
                f for f in self.MODELS
                if f.startswith(text)
                ]
        return completions

    def do_all(self, line):
        """all command
        """
        if not line:
            all_objects = storage.all()
            for obj_id, obj in all_objects.items():
                obj_dict = obj.to_dict()
                class_name = obj_dict['__class__']
                new_obj = eval(f'{class_name}(**{obj_dict})')
                print(new_obj)
        else:
            if line not in self.MODELS:
                print("** class doesn't exist **")
                return
            all_objects = storage.all()
            for obj_id, obj in all_objects.items():
                pattern = fr"^{line}\."
                if re.search(pattern, obj_id):
                    obj_dict = obj.to_dict()
                    new_obj = eval(f"{line}(**{obj_dict})")
                    print(new_obj)

    def help_all(self):
        """help for all command
        """
        print('\n'.join([
            'Usage: all <model>',
            'Prints all string representation of all instances \
based or not on the class name',
            'Ex: $ all BaseModel or $ all',
            ]))

    def complete_all(self, text, line, begidx, endidx):
        """auto complete for create
        """
        if not text:
            completions = self.MODELS[:]
        else:
            completions = [
                f for f in self.MODELS
                if f.startswith(text)
                ]
        return completions

    def do_update(self, line):
        """update command
        """
        args = line.split()
        if len(args) == 0:
            print('** class name missing **')
            return
        model = args[0]
        if model not in self.MODELS:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print('** instance id missing **')
            return
        instance_id = args[1]
        new_obj = self.get_obj(instance_id, model)
        if not new_obj:
            print('** no instance found **')
            return
        if len(args) == 2:
            print('** attribute name missing **')
            return
        attr_name = args[2]
        if len(args) == 3:
            print('** value missing **')
            return
        value = args[3]
        setattr(new_obj, attr_name, value)
        storage.all()[f'{model}.{instance_id}'] = new_obj
        new_obj.save()

    def help_update(self):
        """help for update command
        """
        print('\n'.join([
            'Usage: update <class name> <id> <attribute name> \
                "<attribute value>"',
            'Updates an instance based on the class name and id by \
adding or updating attribute (save the change into the JSON file).',
            'Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com"',
                        ]))

    def complete_update(self, text, line, begidx, endidx):
        """auto complete for create
        """
        if not text:
            completions = self.MODELS[:]
        else:
            completions = [
                f for f in self.MODELS
                if f.startswith(text)
                ]
        return completions

    def do_EOF(self, arg):
        """exits the command
        """
        return True

    def do_quit(self, arg):
        """Quit command to exit the program
        """
        return True

    def help_quit(self):
        """help for quit method
        """
        print("Quit command to exit the program")

    def emptyline(self):
        """emptlyine + enter
        """
        return


if __name__ == "__main__":
    HBNBCommand().cmdloop()
