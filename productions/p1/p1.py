from productions.production_base import Production

class P1(Production):
    """Production P0: Mark quadrilateral element for refinement.
    It sets value of attribute R of the hyperedge with label Q to 1
    """

    def __init__(self):
        super().__init__(
            name="P0",
            description="Mark quadrilateral element for refinement"
        )

    def can_apply(self, graph):
        """Check if P1 can be applied to the graph.

        Args:
            refinement_criterion: External condition (e.g., error estimate) to decide if element should be refined
        """

        hyperedge = None

        for edge in graph.edges:
            if edge.label == "Q" and len(edge.nodes) == 4 and edge.R == 1:
                hyperedge = edge
  
        if not hyperedge:
            return False, None
        
        edges_found = []

        nodes = hyperedge.nodes

        for i in range(4):
            node1 = nodes[i]
            node2 = nodes[(i + 1) % 4]
            found_edge = graph.get_edge_between(node1, node2)

            if found_edge is None:
                break

            edges_found.append(found_edge)
          
        return True, {
            'hyperedge': hyperedge,
            'nodes': hyperedge.nodes,
            'edges': edges_found
        }

    def apply(self, graph, matched_elements):
        """Apply P1 to mark the quadrilateral for refinement."""
        edges = matched_elements['edges']

        # Mark the hyperedge for refinement
        for edge in edges:
            edge.R = 1

        print(f"[{self.name}] Marked quadrilateral hyperedge for refinement (R: 0 -> 1)")
        print(f"[{self.name}] Hyperedge: {edges}")

        return {
            'marked_hyperedge': matched_elements['hyperedge'],
            'nodes': matched_elements['nodes'],
            'edges': matched_elements['edges']
        }
