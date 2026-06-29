cli = displays a basic menu and inputs the action the user wishes to perform
exceptions = defines custom named errors
models = models defines the Product class and the rules a product must follow
reports = information regarding the inventory of products
repository = save and retrieve data from json file
services = holds the business rules and coordinates each action, it takes input from cli and orchestrates repository, models and validators to carry it out
validators = checks the data entered and makes sure its reasonable

services.py will be coordinator that coordinates an action by sending and receiving data from different modules(files) and then sends a suitable response to the cli to be displayed

it is done so that the cli can be swapped out by a web api later and so that services will be the coordinator of all files and the files will be independent of each other and will be easily swappable. The imports flow in one direction only, never in a loop: the more stable file gets imported by the less stable one, never the reverse. For example, services imports the files it coordinates and is imported by almost nothing.
