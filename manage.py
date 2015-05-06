#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
<<<<<<< HEAD
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mealsignups.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
=======
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "j5project.settings")

from django.core.management import execute_from_command_line

execute_from_command_line(sys.argv)
>>>>>>> 3a1f8995b920f5b589524f1d4298648a31a043f4
