#!/usr/local/bin/python3
import os

location = "Nextcloud/2 Studium/23 Notizen/23.03 3. Semester/"

os.chdir(os.path.expanduser("~")) # go to users folder
os.chdir(location)

all_files = os.listdir()

with open(".gitignore") as f:
        ignores = f.read().splitlines()

files = [file for file in all_files if not file in ignores]

cleaned_files = []
dirs = {}


#build the top level and extract directories and the Markdown files present
for file in all_files: 
    if not file in ignores:  #compare with .gitignore 
        if not file.startswith("."): #check if it is system file 
            #for all dirs
            if os.path.isdir(file):
                if not file in ["images"]:
                    dirs[file] = []


#prettyfiyng the directory names
dir_names = {
    "VL_Ethik": "- Ethik der Soz. Marktwirtschaft",
    "VL_Makro1": "- Makroökonomik I",
    "VL_Mikro2": "- Mikroökonomik II",
    "VL_Monetaer": "- Monetäre Ökonomik",
    "VL_Wachstum": "- Wachstum und Nachhaltigkeit",
    "VL_Soziologie": "- Wirtschaftssoziologie"
}

result_list = ["- [Startseite](README.md)"]

# now parse the directories
for name, file_list in dirs.items():

    os.chdir(name)

    result_list.append(dir_names[name])

    files = sorted(os.listdir())

    for file in files:
        if not file in ignores:
            if file.endswith(".md"):
                if file == "README.md":
                    string = f"    - [Übersicht]({name}/{file})"
                else:
                    string = f"    - [{file[11:-3]}]({name}/{file})"
            
                result_list.append(string)
    
    result_list.append("")
    os.chdir("..")

# write it all to the SUMMARY file

with open("SUMMARY.md", "w") as f:
    f.writelines(line + '\n' for line in result_list)
