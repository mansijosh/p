import time

class Server:
    def __init__(self, server_id):
        self.server_id = server_id
        self.active_connections = 0

    def handle_request(self):
        self.active_connections += 1
        print(f"Server {self.server_id} → handling request (Connections: {self.active_connections})")

    def finish_request(self):
        if self.active_connections > 0:
            self.active_connections -= 1

class LoadBalancer:
    def __init__(self, servers, algorithm):
        self.servers = servers
        self.algorithm = algorithm
        self.last_server = -1

    def distribute_request(self):
        if self.algorithm == "round_robin":
            self.last_server = (self.last_server + 1) % len(self.servers)
            server = self.servers[self.last_server]

        elif self.algorithm == "least_connections":
            server = min(self.servers, key=lambda s: s.active_connections)

        else:
            raise ValueError("Unsupported algorithm")

        server.handle_request()

    def finish_some_requests(self):
        # Simulate some servers finishing their requests
        for server in self.servers:
            if server.active_connections > 0:
                server.finish_request()

def simulate_requests(algorithm, num_requests=9):
    print(f"\n Simulation: {algorithm.replace('_', ' ').title()} Load Balancing\n")
    servers = [Server(i) for i in range(3)]
    lb = LoadBalancer(servers, algorithm)

    for i in range(num_requests):
        print(f"\nIncoming Request {i + 1}")
        lb.distribute_request()
        time.sleep(0.4)
        if i % 3 == 2:  # every 3rd request, simulate some request completions
            print("\n Simulating request completion...")
            lb.finish_some_requests()

    print("\n Final server states:")
    for server in servers:
        print(f"Server {server.server_id} active connections: {server.active_connections}")
    print("-" * 40)

if __name__ == "__main__":
    simulate_requests("round_robin")
    simulate_requests("least_connections")