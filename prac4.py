import networkx as nx
import matplotlib.pyplot as plt

colors = ["Red", "Blue", "Green"]
states = ["WA", "NT", "SA", "Q", "NSW", "V"]
neighbors = {
    "WA": ["NT", "SA"],
    "NT": ["WA", "SA", "Q"],
    "SA": ["WA", "NT", "Q", "NSW", "V"],
    "Q": ["NT", "SA", "NSW"],
    "NSW": ["Q", "SA"],
    "V": ["SA", "NSW"],
}
colors_of_states = {}


def promising(state, color):
    for neighbor in neighbors.get(state):
        color_of_neighbor = colors_of_states.get(neighbor)
        if color_of_neighbor == color:
            return False
    return True


def get_color_for_state(state):
    for color in colors:
        if promising(state, color):
            return color


def main():
    for state in states:
        colors_of_states[state] = get_color_for_state(state)
    print(colors_of_states)


def visualize_colored_graph(neighbors, colors_of_states):
    G = nx.Graph()

    # Add edges
    for state, neighbor_list in neighbors.items():
        for neighbor in neighbor_list:
            G.add_edge(state, neighbor)

    # Get colors for visualization
    node_colors = [colors_of_states.get(node, "gray") for node in G.nodes]

    # Draw graph
    pos = nx.spring_layout(G)  # layout of the graph
    nx.draw(
        G,
        pos,
        with_labels=True,
        node_color=node_colors,
        font_weight="bold",
        node_size=700,
    )
    plt.show()


main()

visualize_colored_graph(neighbors, colors_of_states)
