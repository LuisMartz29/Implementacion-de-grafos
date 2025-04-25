import networkx as nx
import random


def generate_social_graph(num_nodes, avg_edges):
    """Generates a random social graph."""
    G = nx.erdos_renyi_graph(n=num_nodes, p=avg_edges / num_nodes)
    for node in G.nodes:
        G.nodes[node]['name'] = f'User{node}'
    return G


def display_suggestions(graph, user):
    """Displays friend suggestions for a user based on friends of friends."""
    if user not in graph.nodes:
        print(f"El usuario {user} no existe.")
        return

    friends = set(graph.neighbors(user))
    suggestions = set()

    for friend in friends:
        suggestions.update(set(graph.neighbors(friend)) - friends - {user})

    if suggestions:
        print(f"Sugerencias de amigos de {graph.nodes[user]['name']}:\n")
        for suggestion in suggestions:
            print(f"- {graph.nodes[suggestion]['name']}")
    else:
        print(f"No hay sugerencias disponibles de {graph.nodes[user]['name']}.")


def main():
    num_users = 20  # Number of users in the graph
    avg_friends = 4  # Average number of friends per user

    print("Generating social graph...")
    social_graph = generate_social_graph(num_users, avg_friends)

    print("\nGenerated Users:")
    for node in social_graph.nodes(data=True):
        print(node)

    while True:
        print("\nOptions:")
        print("1. Search for a user and see friend suggestions")
        print("2. Exit")

        choice = input("Opcion: ")
        if choice == "1":
            user_id = int(input("Escoge un Usuario ID (0 to {}): ".format(num_users - 1)))
            display_suggestions(social_graph, user_id)
        elif choice == "2":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
