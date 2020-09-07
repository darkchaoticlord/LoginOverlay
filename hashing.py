from hash_algorithms.sha1 import sha1
from hash_algorithms.sha256 import sha256
from hash_algorithms.sha512 import sha512
from hash_algorithms.md5 import md5


def main() -> None:
    """
    The main function that is the first function called. Here,
    the starting text-based menu has been set up to allow
    users to decide what action to perform next.

    Returns: None (void function)

    """
    while True:
        print("Welcome to the Cryptography Program!")
        print("Your options are:")
        print("0 - [Exit Program]")
        print("1 - Get the Hash for a message")

        try:
            choice: int = int(input("Enter your choice: "))
        except ValueError:
            print("Value provided is not a number! Try again!")
        else:
            if choice == 0:
                print("Goodbye!")
                break
            elif choice == 1:
                hash_menu()
            else:
                print("No option available for this option number! Try again!")


def hash_menu() -> None:
    """
    This is the text-based menu for trying out various hashing algorithms
    built within this project. This allows users to choose what algorithm
    to use when creating a hash value for a message (string).

    [NOTE]: This is mainly built for quick usage of the hash algorithms.

    Returns: None (void function)

    """
    while True:
        print("This is the hashing program menu.")
        print("Choose your hashing alogrithm from the options below:")
        print("0 - [Exit Program]")
        print("1 - SHA-1")
        print("2 - SHA-256")
        print("3 - SHA-512")
        print("4 - MD5")

        try:
            choice: int = int(input("Enter your choice: "))
        except ValueError:
            print("Value provided is not a number! Try again!")
        else:
            if choice == 0:
                print("Exiting Hashing Program...")
                break

            message: str = input("Enter the message to calculate hash: ")

            if choice == 1:
                print(f"The SHA-1 hash value for '{message}' is calculated to be: {hash_value(message, 'SHA-1')}")
            elif choice == 2:
                print(f"The SHA-256 hash value for '{message}' is calculated to be: {hash_value(message, 'SHA-256')}")
            elif choice == 3:
                print(f"The SHA-512 hash value for '{message}' is calculated to be: {hash_value(message, 'SHA-512')}")
            elif choice == 4:
                print(f"The MD5 hash value for '{message}' is calculated to be: {hash_value(message, 'MD5')}")
            else:
                print("No option available for this option number! Try again!")


def hash_value(message: str, alg_name: str) -> str:
    """
    This a tiny function that, given the message and the name of the Hashing
    Algorithm, provides the hash value for that message.

    Args:
        message: A string containing the text to be hashed.
        alg_name: The name of the alogrithm.

    Returns: The hash value for the message provided.

    """
    if alg_name == "SHA-1":
        return sha1(message)
    elif alg_name == "SHA-256":
        return sha256(message)
    elif alg_name == "SHA-512":
        return sha512(message)
    elif alg_name == "MD5":
        return md5(message)


if __name__ == '__main__':
    main()
