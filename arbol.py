import json
from graphviz import Digraph
import sys

def add_nodes_edges(graph, data, parent=None):
    if not isinstance(data, dict):
        return

    node_id = str(id(data))
    label = data.get('type', 'Unknown')
    
    if 'name' in data:
        label += f": {data['name']}"
    elif 'value' in data:
        label += f": {data['value']}"
    elif 'operator' in data:
        label += f": {data['operator']}"
    
    graph.node(node_id, label)
    
    if parent:
        graph.edge(parent, node_id)
    
    for key, value in data.items():
        if isinstance(value, dict):
            add_nodes_edges(graph, value, node_id)
        elif isinstance(value, list):
            for item in value:
                if isinstance(item, dict):
                    add_nodes_edges(graph, item, node_id)

def generate_graph(ast):
    dot = Digraph(comment='JSON Tree')
    add_nodes_edges(dot, ast)
    dot.render('json_tree', view=True)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        ast = json.loads(sys.argv[1])
        generate_graph(ast)
    else:
        print("No AST data provided.")
