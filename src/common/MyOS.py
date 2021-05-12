import os
import shutil


def create_dir(path):
    try:
        if not os.path.isdir(path):
            os.makedirs(path)
    except OSError:
        print("Creation of the directory <%s> failed" % path)


def get_dir_content(path):
    if os.path.isdir(path):
        print("Getting content of <%s>" % path)
        return os.listdir(path)
    else:
        print("Path <%s> does not exist" % path)
        return []


def delete_full_dir(path):
    try:
        #os.rmdir(path)
        if os.path.isdir(path):
            print("Deleting path... <%s>" % path)
            shutil.rmtree(path)
        else:
            print("Path <%s> does not exist" % path)
    except OSError:
        print("Deletion of the directory <%s> failed" % path)
    else:
        print("Successfully deleted the directory <%s>" % path)


def count_number_of_files_png(path):
    return count_number_of_files(path, ".png")


def count_number_of_files(path, extension):
    file_entries = len([f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f)) and f.endswith(extension)])
    return file_entries


def get_xml_files(path):
    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f)) and f.endswith("xml")]
    return files
