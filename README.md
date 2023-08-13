HBNB Console
The HBNB Console is a command-line tool designed to manage database objects within a project. It offers a variety of commands that facilitate interactions with database instances, including creation, display, update, and deletion.

Description
The HBNB Console provides a range of commands for handling database objects efficiently. These commands enable users to carry out tasks such as creating, viewing, modifying, and removing instances of different classes.

Available Commands
quit: Exit the program.
EOF: Exit the program using Ctrl+D.
create: Create a new instance of a class and save it to the JSON file.
show: Display the string representation of an instance.
destroy: Delete an instance.
all: Display all instances or all instances of a specific class.
update: Update an instance's attribute and save the change to the JSON file.
For more details on each command, type help <command> within the console.

How to Use
Starting the Console
To begin using the HBNB Console, open your terminal and navigate to the project directory.

Using the Commands
Creating a New Instance: Use the create command followed by the class name to create a new instance.

Displaying an Instance: Employ the show command along with the class name and instance ID to see the instance's string representation.

Deleting an Instance: Utilize the destroy command along with the class name and instance ID to delete an instance.

Listing Instances: To list instances of a specific class or all instances, use the all command.

Updating an Instance: Update an instance's attribute with the update command. Provide the class name, instance ID, attribute name, and new attribute value.

Exiting the Console
To exit the console, type quit or use Ctrl+D (EOF).

Examples
Creating a New Instance
$ create User

Displaying an Instance
$ show User 12345

Deleting an Instance
$ destroy User 12345

Listing Instances
$ all
$ all User

Updating an Instance
$ update User 12345 name "John Doe"
