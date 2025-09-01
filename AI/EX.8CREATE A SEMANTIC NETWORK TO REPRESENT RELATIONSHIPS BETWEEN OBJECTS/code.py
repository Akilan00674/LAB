import networkx as nx
import matplotlib.pyplot as plt

# -------------------------------
# Create Semantic Network Graphx
# -------------------------------
G = nx.DiGraph()

# Add nodes and relationships
G.add_edges_from([
    ("CropDiseaseDetectionSystem", "Camera", {"label": "has-a"}),
    ("CropDiseaseDetectionSystem", "Dataset", {"label": "has-a"}),
    ("CropDiseaseDetectionSystem", "AI_Model", {"label": "has-a"}),
    ("CropDiseaseDetectionSystem", "MobileApp", {"label": "has-a"}),

    ("AI_Model", "CNN_Model", {"label": "is-a"}),
    ("CNN_Model", "ResNet", {"label": "is-a"}),
    ("CNN_Model", "VGG", {"label": "is-a"}),
    ("AI_Model", "YOLO", {"label": "is-a"}),

    ("CropDiseaseDetectionSystem", "Blight", {"label": "detects"}),
    ("CropDiseaseDetectionSystem", "Rust", {"label": "detects"}),
    ("CropDiseaseDetectionSystem", "Mosaic", {"label": "detects"}),
])

# -------------------------------
# Define Properties
# -------------------------------
properties = {
    "Camera": ["Resolution=1080p", "Lens=Macro"],
    "Dataset": ["Size=10k Images", "Type=Labeled"],
    "AI_Model": ["Accuracy=92%"],
    "MobileApp": ["Platform=Android/iOS"],
    "Blight": ["Type=Fungal"],
    "Rust": ["Type=Fungal"],
    "Mosaic": ["Type=Viral"]
}

# -------------------------------
# Query Functions
# -------------------------------
def is_a(graph, x, y):
    """Check if x is-a y"""
    return graph.has_edge(x, y) and graph[x][y]["label"] == "is-a"

def has_a(graph, x, y):
    """Check if x has-a y"""
    return graph.has_edge(x, y) and graph[x][y]["label"] == "has-a"

def detects(graph, x, y):
    """Check if x detects y"""
    return graph.has_edge(x, y) and graph[x][y]["label"] == "detects"

def get_properties(node):
    """Return properties of a node"""
    return properties.get(node, [])

# -------------------------------
# Example Queries
# -------------------------------
print("OUTPUT\n")

print("Is CropDiseaseDetectionSystem an AI_Application?", 
      is_a(G, "CropDiseaseDetectionSystem", "AI_Application"))

print("Does CropDiseaseDetectionSystem have a Camera?", 
      has_a(G, "CropDiseaseDetectionSystem", "Camera"))

print("Does CropDiseaseDetectionSystem detect Rust?", 
      detects(G, "CropDiseaseDetectionSystem", "Rust"))

print("What properties does the Dataset have?", 
      get_properties("Dataset"))

print("What properties does the AI_Model have?", 
      get_properties("AI_Model"))

# -------------------------------
# Draw Semantic Network Diagram
# -------------------------------
pos = nx.spring_layout(G, seed=42)

# Draw nodes and edges
nx.draw(G, pos, with_labels=True, node_color="lightyellow", node_size=2500,
        font_weight="bold", arrows=True, edgecolors="black")

# Draw edge labels
nx.draw_networkx_edge_labels(
    G, pos,
    edge_labels=nx.get_edge_attributes(G, "label"),
    font_color="blue"
)

plt.axis("off")
plt.title("Semantic Network - Crop Disease Detection", fontsize=14, fontweight="bold")
plt.show()
