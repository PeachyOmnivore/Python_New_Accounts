import csv # Library that helps read and write CSV files
import secrets # This helps generate random passwords
import subprocess # This calls the useradd command, which creates and adds each user account.
from pathlib import Path # This library helps to locate the data files for each user account

# After importing the libraries that help you execute your script, you need to get the current working directory and find the subdirectory where the CSV files are stored. Use cwd for “current working directory” and identify the path of the Python directory as a string: 
cwd = Path.cwd() /"drive/MyDrive/Colab Notebooks" # -- this path will need to be changed to soruce of CSV file -- #

# use a with statement and an as keyword. The with statement helps with resource management, and the as keyword creates an alias for the resource you want to call.
with open(cwd / "data/users_in.csv", "r") as  file_input, open(cwd / "data/users_out.csv", "w") as file_output:
    
    # use a DictReader object so that each row in the file is read into a dict() with the field names and values, like this: {"username": "amanda", "password": "", "real_name": "Amanda Alonso"}.
    reader = csv.DictReader(file_input)


# The input for the script is now complete! Now you need to set up the output. You create a DictWriter and use the same field names from the input, like so:
writer = csv.DictReader(file_output, fieldnames=reader.fieldnames)
writer.writeheader()

for user in reader:
    # use the secrets library that you imported at the beginning of the script to generate a random password of eight hex bytes, which equals 16 characters in total. Then, run the /sbin/useradd command to create each user. The check=True parameter causes the script to exit with a CalledProcessError if the command fails for any reason.
    user["password"] = secrets.token_hex(8)
    useradd_cmd = ["/sbin/useradd",
                   "-c", user["real-name"],
                   "m"
                   ,
                   "-G", "users",
                   "-p", user["password"],
                   user["username"]]
    subprocess.run(useradd_cmd, check=True)

    # write the records back to the output file, including the passwords. When you run the code, the new user accounts and their passwords are generated into a new CSV file.
    writer.writerow(user)
