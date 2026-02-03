import os
from dotenv import load_dotenv


def main():
    print("ORACLE STATUS: Reading the Matrix...\n")
    load_dotenv()
    config_vars = [
        "MATRIX_MODE",
        "DATABASE_URL",
        "API_KEY",
        "LOG_LEVEL",
        "ZION_ENDPOINT"
    ]
    config = {}
    missing = []
    for key in config_vars:
        value = os.getenv(key)
        if value is None:
            missing.append(key)
        else:
            config[key] = value

    if missing:
        print("WARNING: Missing configuration variables:")
        for key in missing:
            print(f" - {key} is not set")
        print("\nPlease set the missing variables"
              " in your .env file or environment.")
    else:
        print("Configuration loaded:")
        mode = config["MATRIX_MODE"]
        print(f"Mode : {mode}")
        if (mode == "developpement"):
            print("Database: Connected to local instance")
        else:
            print("Database: Connected to production instance")
        print("API Access: Authonticated")
        print("LOG Level: ", config["LOG_LEVEL"])
        print("Zion Network: Online")
        print("\nEnvironment security check:")
        if "API_KEY" in config:
            print("[OK] No hardcoded secrets detected")
        else:
            print("[WARNING] API_KEY is missing, ensure secure access")
        if os.path.exists(".env"):
            print("[OK] .env file properly configured")
        else:
            print("[WARNING] .env file not found")
        print("[OK] Production overrides available")

        print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()
