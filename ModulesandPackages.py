# #Modules and Packages

# #module = piece of software that has a specific functionality
# #e.g. ping pong game ... one module = responsible for game logic; one module = draws game on screen
# #each module is a different file, which can be edited separately (like components in RPA?)

# #Writing modules
# #modules in python are files with a .py extension .. name of module = name of file
# #module can have a set of functions, classes, or variables defined and implemented

# #module example
# mygame/
# mygame/game.py
# mygame/draw.py

# #modules are imported from other modules using import command (like invoke workflow in RPA)

# #game.py will implement game; it will use function draw_game from file draw.py (draw module) that implements logic for drawing game on screen

# #game.py
# #import draw module
# from platform import python_implementation
# import draw

# def play_game():
#     ...

# def main():
#     result = play_game()
#     draw.draw_game(result)

# #this means that if this script is executed, then main() will be executed
# if __name__ == "__main__":
#     main()

# #draw module may look something like this

# #draw.py
# def draw_game():
#     ...

# def clear_screen(screen):
#     ...

# #in this example, the game module imports the draw module, which enables it to use functions implemented in that module
# #main function would use local function play_game to run the game, and then draw the result of the game using function in the draw module called draw_game
# #to use draw_game in the draw module, we would need to specify in which module the function is implemented using the dot operator
# #to reference draw_game function from the game module, we would need to import the draw module and only then call draw.draw_game()

# #when import draw directive will run, Python interpreter will look for a file in the directory from which the script was executed (with .py suffix; import draw will look for draw.py)
# #if found, will import it; if not, will look for built-in modules

# #.pyc is a compiled Python file ... Python compiles files into Python bytecode so that it won't have to parse the files each time modules are loaded
# #if .pyc file exists, it get loaded instead of the .py file

# #Importing module objects to the current namespace

# #import draw_game function directly into the main script's namespace by using the from command

# #game.py
# #import the draw module
# from draw import draw_game

# def main():
#     result = play_game()
#     draw_game(result)

# #in this eample, draw_game does not precede with the name of the module it is imported from becasue we've specified the module name in the import command

# #easier to use the functions inside the current module because you don't need to specify which module the function comes from
# #however any namespace cannot have two objects with the exact same name so the import comman may replace an existing object in the namespace

# #Importing all objects from a module

# #may use import command to import all objects from a specified module

# #game.py
# #import the draw module
# from draw import *

# def main():
#     result = play_game()
#     draw_game(result)

# #might be risky, as changes in module might affect the module which imports it but it is shorter and does not require to specify which objects you with to import from the module

# #Custom import name
# #can load modules under any name we want; useful when we want to import a module conditionally to use the same name in the rest of the code

# #e.g. have two draw modules with slightly different names

# #game.py
# #import the draw module
# if visual_mode:
#     #in visual mode, we draw using graphics
#     import draw_visual as draw
# else:
#     #in textual mode, we print out text
#     import draw_textual as draw

# def main():
#     result = play_game()
#     #this can either be visual or textual depending on visual_mode
#     draw.draw_game(result)

# #Module initialization
# #first time a module is loaded into a running Python script, it's initialized by executing code in the module once
# #if another module in your code imports the same module again, it will not be loaded twice but once only - so local variables inside the module act as a singleton - they are intiialized once
# #useful to know - you can rely on this behavior for initializing objects

# #draw.py

# def draw_game():
#     #when clearing the screen, we can use the main screen object initialized in this module
#     clear_screen(main_screen)
#     ...

# def clear_screen(screen):
#     ...

# class Screen():
#     ...

# #initialize main_screen as a singleton
# main_screen = Screen()

# #Extending module load path
# #couple of ways to tell Python interpreter where to look for modules, aside from the default (local directory and built-in modules)
# # could use environment variable PYTHONPATH to specify additional directories to look for modules in, like this:
# PYTHONPATH=/foo python game.py 
# #this will execute game.py and will enable the script to load modules from the foo directory as well as the local directory

# #another method is sys.path.append function ... may execute before running an import command
# sys.path.append("/foo")
# #will add foo directory to list of paths to look for modules in

# #Exploring built-in modules
# #built-in modules in Python standard library
# #two important functions when exploring modules in Python - dir and help
# #to import module urllib, which enables us to create read data from URLs, we simply import the module:

# #import the library
# import urllib

# #use it
# urllib.urlopen(...)

# #we can look for which functions are implemented in each module by using the dir function
# import urllib
# dir(urllib)

# #when find the function in the modeule we want to use, can read about it using help function
# help(urllib.urlopen)

# #Writing packages
# #packages are namespaces which contain multiple packages and modules themselves
# #packages = directories
# #each package in Python is a directory which MUST contain a special file called __init__.py
# #__init__.py can be empty, and it indicates that directory it is in is a Python package, so it can be imported the same way a module can be imported
# #if we create a directory called foo, which markes the package name, we can then create a module inside that package called bar
# #we must not forget to add __init__.py to file inside foo directory

# #to use module bar, we can import it in two ways

# #must use foo prefix whenever we accss module bar
# import foo.bar 

# #or

# #do not need to use foo prefix because import module in our module's namespace
# from foo import bar

# #__init__.py file can also decide which modules the package exports as the API, while keeping other modules internal, by overriding the __all__ variable:
# __init__.py:
# __all__ = ["bar"]

# #Exercise
# #print an alphabetically sorted list of all function is the re module which contain the word find

import re
dir(re)

find_members =[]
for member in dir(re):
    if "find" in member:
        find_members.append(member)
    else:
        continue
print(sorted(find_members))
