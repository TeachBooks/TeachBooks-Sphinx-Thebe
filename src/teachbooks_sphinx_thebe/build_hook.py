import os
import shutil
import sysconfig
from hatchling.builders.hooks.plugin.interface import BuildHookInterface

class CustomBuildHook(BuildHookInterface):
    def initialize(self, version, build_data):
        """Run after package installation"""
        site_packages = sysconfig.get_paths()["purelib"]
        sphinx_thebe_path = os.path.join(site_packages, "sphinx_thebe")
        teachbooks_path = os.path.join(site_packages, "teachbooks_sphinx_thebe")
        if os.path.exists(sphinx_thebe_path) and os.path.exists(teachbooks_path):
            shutil.rmtree(sphinx_thebe_path)
            shutil.move(teachbooks_path, sphinx_thebe_path)
            print("Files moved successfully!")
        else:
            print("Something went wrong!")