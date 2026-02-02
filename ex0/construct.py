import os
import sys


def main():
    print("MATRIX STATUS: You're still plugged in\n")
    print(f"Current Python: {sys.executable}")
    if (sys.prefix != sys.base_prefix):
        print("In virtual environment:",
              os.path.basename(os.environ['VIRTUAL_ENV']))
        print("\nEnvironment Path:", os.environ['VIRTUAL_ENV'])
        print("\nSUCCESS: You're in an isolated environment! Safe"
              " to install packages without affecting the global system.")
        print("Package installation path:")
        print(f"{os.environ.get("VIRTUAL_ENV")}/lib"
              f"/python{sys.version_info.major}.{sys.version_info.minor}/"
              f"site-packages")
    else:
        print("Virtual Environment: None detected\n")
        print("WARNING: You're in the global environment! The "
              "machines can see everything you install.")
        print("\nTo enter the construct, run:"
              "\npython -m venv matrix_env"
              "\nsource matrix_env/bin/activate # On Unix"
              "\nmatrix_env"
              "\nScripts"
              "\nactivate # On Windows")
        print("\nThen run this program again.")


if __name__ == "__main__":
    main()
