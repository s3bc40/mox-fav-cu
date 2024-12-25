from src import favorites

def deploy():
    favorites_contact = favorites.deploy()
    starting_number = favorites_contact.retrieve()
    print(f"Starting number is {starting_number}")

def moccasin_main():
    deploy()

if __name__ == "__main__":
    moccasin_main()