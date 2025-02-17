import sysconfig
import os 
import shutil

def overwrite_files():
    print("Running the Files Overwriting method!")

    site_packages = sysconfig.get_paths()["purelib"]
    print("site packages: ", site_packages)

    teachbooks_path = None 
    for file_name in os.listdir(site_packages):
        full_file_path = os.path.join(site_packages, file_name)
        if file_name.startswith("teachbooks_sphinx_thebe") \
            and os.path.isdir(full_file_path) \
                and not file_name.endswith(".dist-info"):
            teachbooks_path = full_file_path
            print("Teachbooks-Sphinx-Thebe package path found! :)", teachbooks_path)
            break 
    
    if not teachbooks_path:
        print("Couldn't find TeachBooks-Sphinx-Thebe path :(")
        return
    
    sphinx_thebe_path = os.path.join(site_packages, "sphinx_thebe")

    if os.path.exists(sphinx_thebe_path):
        print("Found sphinx-thebe directory: ", sphinx_thebe_path)
        shutil.rmtree(sphinx_thebe_path)
        os.makedirs(sphinx_thebe_path)
        shutil.copytree(teachbooks_path, sphinx_thebe_path, dirs_exist_ok=True)
        print("Great success!")
    else: 
        print("Something went wrong! :(")

if __name__ == "__main__":
    overwrite_files()
