from itertools import permutations
import random

class Node:
    def __init__(self, value: str, prohibited: set[str]) -> None:
        self.value = value
        self.edges = set()
        self.prohibited = prohibited

    def add_edge(self, other):
        self.edges.add(other)
    
    def __repr__(self):
        return self.value

nodes = set()
nodes.add(Node("Matt", {"Alyssa"}))
nodes.add(Node("Alyssa", {"Matt"}))
nodes.add(Node("Adam", set()))
nodes.add(Node("Julie", {"Garth"}))
nodes.add(Node("Garth", {"Julie"}))
nodes.add(Node("Colton", {"Emma"}))
nodes.add(Node("Emma", {"Colton"}))

acceptable_sequences = [tuple(person.value for person in chain) for chain in permutations(nodes, len(nodes)) if all([chain[(i + 1) % len(chain)].value not in chain[i].prohibited for i in range(len(chain))])]
previously_used_chains = set([('Adam', 'Garth', 'Emma', 'Julie', 'Alyssa', 'Colton', 'Matt')])
deduplicated_sequences = [chain for chain in acceptable_sequences if chain[0] == "Adam" and chain not in previously_used_chains]
print(deduplicated_sequences[random.randint(0, len(deduplicated_sequences) - 1)])
print(deduplicated_sequences[random.randint(0, len(deduplicated_sequences) - 1)])
print(deduplicated_sequences[random.randint(0, len(deduplicated_sequences) - 1)])
print(deduplicated_sequences[random.randint(0, len(deduplicated_sequences) - 1)])
print(deduplicated_sequences[random.randint(0, len(deduplicated_sequences) - 1)])
print(deduplicated_sequences[random.randint(0, len(deduplicated_sequences) - 1)])
print(deduplicated_sequences[random.randint(0, len(deduplicated_sequences) - 1)])
print(deduplicated_sequences[random.randint(0, len(deduplicated_sequences) - 1)])
print(deduplicated_sequences[random.randint(0, len(deduplicated_sequences) - 1)])
print(deduplicated_sequences[random.randint(0, len(deduplicated_sequences) - 1)])
