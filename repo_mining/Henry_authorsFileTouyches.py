import subprocess
import os

def collect_authors_and_dates(file_list):
    author_dict = {}

    for file in file_list:
        command = f"git log --format='%aN|%ad' -- {file}"
        result = subprocess.run(command, shell=True, capture_output=True, text=True)

        if result.returncode == 0:
            log_output = result.stdout.splitlines()

            for entry in log_output:
                author, date_str = entry.split('|')
                author_date_tuple = (author, date_str)
                
                if file in author_dict:
                    author_dict[file].append(author_date_tuple)
                else:
                    author_dict[file] = [author_date_tuple]

    return author_dict

source_files = ["rootbeerlib/src/main/java/com/scottyab/rootbeer/RootBeerNative.java", "rootbeerlib/build.gradle", "rootbeerlib/src/main/jniLibs/armeabi-v7a/libtool-checker.so",
                "rootbeerlib/src/main/jni/Application.mk"] #there are more files but I only included a few for the sake of space

authors_data = collect_authors_and_dates(source_files)

# Print or process authors_data as needed
print(authors_data)
