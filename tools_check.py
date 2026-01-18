import sys
import shutil

print("Python Version: ")
print(sys.version + "\n")

print("pip available:")
print("pip:", shutil.which("pip"))
print("pip3:", shutil.which("pip3"))
print()

print("Python interpreter path:")
print(sys.executable)