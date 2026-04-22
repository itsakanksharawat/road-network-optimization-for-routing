 # Road Network Preprocessing for Simulation

## 📌 Problem

Raw road network data from OpenStreetMap is highly detailed and fragmented, making it inefficient for traffic simulation and routing tasks. The presence of redundant nodes, micro-segments, and noisy intersections increases computational complexity without adding meaningful information.

---

## 🚀 Solution

This project builds a preprocessing pipeline that converts raw OpenStreetMap road data into a simplified graph structure optimized for simulation.

The pipeline reduces graph complexity by:

* Removing insignificant road segments (micro edges)
* Eliminating redundant intermediate nodes (degree-2 nodes)
* Cleaning isolated and irrelevant structures

---

## ⚙️ Pipeline Overview

```
OpenStreetMap Data (OSMnx)
        ↓
Raw Graph Extraction (no simplification)
        ↓
Preprocessing
  - Convert to undirected graph
  - Remove isolated nodes
  - Compute structural statistics
        ↓
Topology Cleaning
  - Remove micro edges (< 5m)
  - Remove degree-2 nodes (graph simplification)
        ↓
Cleaned Graph Output (GraphML)
```

---

## 📥 Input

* Source: OpenStreetMap (via OSMnx)
* Location: Dehradun, Uttarakhand, India
* Format: Graph (NetworkX MultiDiGraph)

---

## 📤 Output

* Simplified road network graph (`.graphml`)
* Reduced node and edge complexity
* Suitable for:

  * Traffic simulation
  * Routing systems
  * Graph-based ML tasks

---

## 📊 Results

| Metric | Before           | After            |
| ------ | ---------------- | ---------------- |
| Nodes  | (fill after run) | (fill after run) |
| Edges  | (fill after run) | (fill after run) |

---

## 🧠 Key Techniques

* **Graph Simplification (Topology-based)**

  * Removed degree-2 nodes to reduce unnecessary intermediate points
* **Edge Filtering**

  * Eliminated short edges representing over-segmented roads
* **Graph Transformation**

  * Converted to undirected graph for simplified processing

---

## 📸 Visualization

### Raw Road Network

![Raw Graph](data/images/raw_graph.png)

### Cleaned Road Network

![Cleaned Graph](data/images/cleaned_graph.png)

---

## 🛠️ Tech Stack

* Python
* OSMnx
* NetworkX
* Matplotlib

---

## ▶️ How to Run

```bash
# Step 1: Download raw data
python step1_data_gathering.py

# Step 2: Preprocess graph
python step2_preprocessing.py

# Step 3: Clean topology
python step3_topology_cleaning.py
```

---

## 🎯 Use Cases

* Traffic simulation systems
* Route optimization engines
* Autonomous vehicle simulation environments
* Graph-based machine learning pipelines

---

## 📌 Key Outcome

This project demonstrates how to transform large-scale geospatial road data into an efficient graph representation by reducing structural complexity while preserving connectivity.

---

## 🧾 Resume Highlight

> Built a road network preprocessing pipeline using OSMnx and NetworkX to transform raw OpenStreetMap data into a simplified graph structure by removing redundant nodes and micro edges, improving suitability for simulation and routing applications.

