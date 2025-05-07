import Pyro4

# Define the factorial function that will be remotely accessed
@Pyro4.expose
class FactorialServer:
    def factorial(self, n):
        if n == 0 or n == 1:
            return 1
        else:
            return n * self.factorial(n - 1)

# Set up the Pyro4 daemon and register the object
def main():
    daemon = Pyro4.Daemon()  # Create a Pyro daemon
    uri = daemon.register(FactorialServer())  # Register the server object
    print("Server is running. URI:", uri)  # Print the URI for client to connect to
    daemon.requestLoop()  # Start the Pyro4 event loop

if __name__ == "__main__":
    main()
