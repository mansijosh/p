import Pyro4

def main():
    # Connect to the server via the URI
    server_uri = input("Enter the server URI: ")  # Get server URI from user
    server = Pyro4.Proxy(server_uri)  # Proxy object to communicate with the server

    # Get the integer value from the user
    num = int(input("Enter a number to calculate the factorial: "))

    # Call the remote factorial function
    result = server.factorial(num)

    # Display the result
    print(f"The factorial of {num} is: {result}")

if __name__ == "__main__":
    main()
