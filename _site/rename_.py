import os
import fileinput

def replace_in_files(files, old_string, new_string):
    for file_path in files:
        with fileinput.input(file_path, inplace=True) as file:
            for line in file:
                print(line.replace(old_string, new_string), end='')

files_to_modify = [
    "./_site/styleguide/index.html",
    "./_site/tag/apocalypse/index.html",
    "./_site/tag/technology/index.html",
    "./_site/tag/business/index.html",
    "./_site/tag/lifestyle/index.html",
    "./_site/tag/fashion/index.html",
    "./_site/tag/life/index.html",
    "./_site/tag/nature/index.html",
    "./_site/tag/notes/index.html",
    "./_site/tag/ai/index.html",
    "./_site/tag/work/index.html",
    "./_site/tag/travels/index.html",
    "./_site/tag/space/index.html",
    "./_site/tag/story/index.html",
    "./_site/tag/rest/index.html",
    "./tag/apocalypse/index.html",
    "./tag/technology/index.html",
    "./tag/business/index.html",
    "./tag/lifestyle/index.html",
    "./tag/fashion/index.html",
    "./tag/life/index.html",
    "./tag/nature/index.html",
    "./tag/notes/index.html",
    "./tag/ai/index.html",
    "./tag/work/index.html",
    "./tag/travels/index.html",
    "./tag/space/index.html",
    "./tag/story/index.html",
    "./tag/rest/index.html"
]

old_string = "The AI And Science Podcast"
new_string = "Interstellar Podcast"

replace_in_files(files_to_modify, old_string, new_string)
print("Replacement complete.")
