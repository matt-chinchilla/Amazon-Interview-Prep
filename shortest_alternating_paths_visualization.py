import matplotlib.pyplot as plt
import matplotlib.patches as patches
from collections import defaultdict, deque
from typing import List
import numpy as np

class SolutionWithVisualization:
    def __init__(self):
        self.RED = 0
        self.BLUE = 1
        self.steps_data = []
        
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        # Build graph
        graph = defaultdict(lambda: defaultdict(list))
        
        for x, y in redEdges:
            graph[self.RED][x].append(y)
        for x, y in blueEdges:
            graph[self.BLUE][x].append(y)
            
        ans = [float("inf")] * n
        queue = deque([(0, self.RED, 0), (0, self.BLUE, 0)])
        seen = {(0, self.RED), (0, self.BLUE)}
        
        # Store initial state
        self.steps_data.append({
            'queue': list(queue),
            'seen': set(seen),
            'ans': ans.copy(),
            'current': None,
            'neighbors_added': []
        })
        
        step = 0
        while queue and step < 20:  # Limit steps for visualization
            node, color, steps = queue.popleft()
            ans[node] = min(ans[node], steps)
            
            neighbors_added = []
            for neighbor in graph[color][node]:
                if (neighbor, 1 - color) not in seen:
                    seen.add((neighbor, 1 - color))
                    queue.append((neighbor, 1 - color, steps + 1))
                    neighbors_added.append((neighbor, 1 - color, steps + 1))
            
            # Store step data
            self.steps_data.append({
                'queue': list(queue),
                'seen': set(seen),
                'ans': ans.copy(),
                'current': (node, color, steps),
                'neighbors_added': neighbors_added
            })
            step += 1
                    
        return [x if x != float("inf") else -1 for x in ans]
    
    def visualize_algorithm(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]):
        # Run algorithm
        result = self.shortestAlternatingPaths(n, redEdges, blueEdges)
        
        # Create visualization
        fig = plt.figure(figsize=(20, 12))
        
        # Graph layout - arrange nodes in a circle
        angles = np.linspace(0, 2*np.pi, n, endpoint=False)
        pos = {i: (np.cos(angles[i]), np.sin(angles[i])) for i in range(n)}
        
        # Show initial graph structure
        ax1 = plt.subplot(2, 3, 1)
        self.draw_graph(ax1, n, redEdges, blueEdges, pos, "Initial Graph Structure")
        
        # Show key steps
        key_steps = [0, 2, 4, 6] if len(self.steps_data) > 6 else list(range(min(4, len(self.steps_data))))
        
        for i, step_idx in enumerate(key_steps):
            if step_idx < len(self.steps_data):
                ax = plt.subplot(2, 3, i + 2)
                self.draw_step(ax, n, redEdges, blueEdges, pos, self.steps_data[step_idx], 
                             f"Step {step_idx}", step_idx)
        
        # Show final results
        ax_final = plt.subplot(2, 3, 6)
        self.draw_final_results(ax_final, n, pos, result, "Final Distances")
        
        plt.tight_layout()
        plt.savefig('shortest_alternating_paths_visualization.png', dpi=300, bbox_inches='tight')
        plt.show()
        
        # Print step-by-step explanation
        self.print_step_explanation()
    
    def draw_graph(self, ax, n, redEdges, blueEdges, pos, title):
        ax.set_title(title, fontsize=12, fontweight='bold')
        ax.set_xlim(-1.5, 1.5)
        ax.set_ylim(-1.5, 1.5)
        ax.set_aspect('equal')
        
        # Draw nodes
        for i in range(n):
            circle = plt.Circle(pos[i], 0.1, color='lightgray', zorder=2)
            ax.add_patch(circle)
            ax.text(pos[i][0], pos[i][1], str(i), ha='center', va='center', 
                   fontweight='bold', zorder=3)
        
        # Draw red edges
        for x, y in redEdges:
            self.draw_arrow(ax, pos[x], pos[y], 'red', 0.02)
        
        # Draw blue edges
        for x, y in blueEdges:
            self.draw_arrow(ax, pos[x], pos[y], 'blue', -0.02)
        
        # Legend
        red_patch = patches.Patch(color='red', label='Red Edges')
        blue_patch = patches.Patch(color='blue', label='Blue Edges')
        ax.legend(handles=[red_patch, blue_patch], loc='upper right')
        
        ax.axis('off')
    
    def draw_step(self, ax, n, redEdges, blueEdges, pos, step_data, title, step_num):
        ax.set_title(f"{title}", fontsize=12, fontweight='bold')
        ax.set_xlim(-1.5, 1.5)
        ax.set_ylim(-1.5, 1.5)
        ax.set_aspect('equal')
        
        # Draw all edges lightly
        for x, y in redEdges:
            self.draw_arrow(ax, pos[x], pos[y], 'lightcoral', 0.02, alpha=0.3)
        for x, y in blueEdges:
            self.draw_arrow(ax, pos[x], pos[y], 'lightblue', -0.02, alpha=0.3)
        
        # Draw nodes
        for i in range(n):
            color = 'lightgray'
            if step_data['current'] and i == step_data['current'][0]:
                color = 'yellow'  # Current node
            elif any(i == item[0] for item in step_data['queue']):
                color = 'orange'  # In queue
            
            circle = plt.Circle(pos[i], 0.1, color=color, zorder=2)
            ax.add_patch(circle)
            
            # Show distance
            dist = step_data['ans'][i] if step_data['ans'][i] != float('inf') else '∞'
            ax.text(pos[i][0], pos[i][1]-0.25, f"d:{dist}", ha='center', va='center', 
                   fontsize=8, zorder=3)
            ax.text(pos[i][0], pos[i][1], str(i), ha='center', va='center', 
                   fontweight='bold', zorder=3)
        
        # Show queue state
        queue_text = "Queue: " + str([(node, "R" if color == 0 else "B", steps) 
                                     for node, color, steps in step_data['queue']])
        ax.text(-1.4, -1.3, queue_text, fontsize=8, ha='left', va='top')
        
        if step_data['current']:
            node, color, steps = step_data['current']
            current_text = f"Processing: ({node}, {'Red' if color == 0 else 'Blue'}, {steps})"
            ax.text(-1.4, -1.1, current_text, fontsize=8, ha='left', va='top', 
                   fontweight='bold', color='red')
        
        ax.axis('off')
    
    def draw_final_results(self, ax, n, pos, result, title):
        ax.set_title(title, fontsize=12, fontweight='bold')
        ax.set_xlim(-1.5, 1.5)
        ax.set_ylim(-1.5, 1.5)
        ax.set_aspect('equal')
        
        # Draw nodes with final distances
        for i in range(n):
            color = 'lightgreen' if result[i] != -1 else 'lightcoral'
            circle = plt.Circle(pos[i], 0.1, color=color, zorder=2)
            ax.add_patch(circle)
            ax.text(pos[i][0], pos[i][1], str(i), ha='center', va='center', 
                   fontweight='bold', zorder=3)
            ax.text(pos[i][0], pos[i][1]-0.25, str(result[i]), ha='center', va='center', 
                   fontsize=10, fontweight='bold', color='red', zorder=3)
        
        ax.axis('off')
    
    def draw_arrow(self, ax, start, end, color, offset=0, alpha=1.0):
        # Calculate perpendicular offset for parallel edges
        dx, dy = end[0] - start[0], end[1] - start[1]
        length = np.sqrt(dx**2 + dy**2)
        if length > 0:
            perp_x, perp_y = -dy/length * offset, dx/length * offset
            start = (start[0] + perp_x, start[1] + perp_y)
            end = (end[0] + perp_x, end[1] + perp_y)
        
        ax.annotate('', xy=end, xytext=start,
                   arrowprops=dict(arrowstyle='->', color=color, lw=2, alpha=alpha))
    
    def print_step_explanation(self):
        print("\n" + "="*80)
        print("ALGORITHM EXPLANATION:")
        print("="*80)
        print("This algorithm finds shortest paths with alternating edge colors using BFS.")
        print("\nKey concepts:")
        print("- RED = 0, BLUE = 1")
        print("- State: (node, last_edge_color, distance)")
        print("- Must alternate colors: if last edge was red, next must be blue")
        print("- BFS ensures shortest path is found first")
        print("\nStep-by-step execution:")
        
        for i, step in enumerate(self.steps_data[:8]):  # Show first 8 steps
            if i == 0:
                print(f"\nInitial: Queue has (0,RED,0) and (0,BLUE,0)")
                print(f"         We can start with either color from node 0")
            else:
                current = step['current']
                if current:
                    node, color, steps = current
                    color_name = "RED" if color == 0 else "BLUE"
                    print(f"\nStep {i}: Processing node {node} (last edge: {color_name}, distance: {steps})")
                    print(f"         Answer[{node}] = min({step['ans'][node]}, {steps}) = {min(step['ans'][node], steps)}")
                    
                    if step['neighbors_added']:
                        print(f"         Added to queue: {[(n, 'RED' if c == 0 else 'BLUE', d) for n, c, d in step['neighbors_added']]}")

# Example usage
def main():
    # Example 1: Complex interconnected graph
    print("Example 1 - Complex Graph:")
    n = 5
    redEdges = [[0, 1], [1, 2], [2, 3], [0, 4], [4, 3]]
    blueEdges = [[1, 0], [2, 1], [3, 2], [4, 0], [3, 4], [1, 4]]
    
    solution = SolutionWithVisualization()
    result = solution.shortestAlternatingPaths(n, redEdges, blueEdges)
    print(f"Input: n={n}")
    print(f"Red edges: {redEdges}")
    print(f"Blue edges: {blueEdges}")
    print(f"Output: {result}")
    solution.visualize_algorithm(n, redEdges, blueEdges)
    
    # Example 2: Graph with multiple possible alternating paths
    print("\n" + "="*50)
    print("Example 2 - Multiple Alternating Paths:")
    n = 6
    redEdges = [[0, 1], [1, 3], [3, 5], [0, 2], [2, 4]]
    blueEdges = [[1, 2], [2, 3], [3, 4], [4, 5], [0, 3], [1, 4]]
    
    solution2 = SolutionWithVisualization()
    result2 = solution2.shortestAlternatingPaths(n, redEdges, blueEdges)
    print(f"Input: n={n}")
    print(f"Red edges: {redEdges}")
    print(f"Blue edges: {blueEdges}")
    print(f"Output: {result2}")
    solution2.visualize_algorithm(n, redEdges, blueEdges)
    
    # Example 3: Graph with some unreachable nodes
    print("\n" + "="*50)
    print("Example 3 - Some Unreachable Nodes:")
    n = 4
    redEdges = [[0, 1], [2, 3]]
    blueEdges = [[1, 2], [0, 3]]
    
    solution3 = SolutionWithVisualization()
    result3 = solution3.shortestAlternatingPaths(n, redEdges, blueEdges)
    print(f"Input: n={n}")
    print(f"Red edges: {redEdges}")
    print(f"Blue edges: {blueEdges}")
    print(f"Output: {result3}")
    solution3.visualize_algorithm(n, redEdges, blueEdges)

if __name__ == "__main__":
    main()
