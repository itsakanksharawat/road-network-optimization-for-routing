## 🚀 Road Network Optimization & Routing Evaluation System

## 📌 Problem
Raw road network data from OpenStreetMap contains excessive node density due to micro-segmentation and mapping artifacts. This significantly increases computational cost for routing and large-scale simulations without improving accuracy.

---

## 🚀 Solution

This project builds a **graph simplification and evaluation pipeline** that reduces structural complexity while preserving routing correctness.

It:
- Simplifies topology (removes redundant nodes & micro edges)
- Preserves connectivity using largest connected component
- Benchmarks routing performance before and after simplification

---

## ⚙️ System Pipeline

OpenStreetMap (OSMnx)  
↓  
Raw Graph Extraction  
↓  
Preprocessing  
↓  
Topology Simplification  
↓  
Routing Evaluation (Dijkstra)  
↓  
Performance & Accuracy Analysis  

---

## 📊 Results

### Graph Reduction
- Nodes: 373,126 → 82,450 (~78% reduction)
- Edges: 756,746 → 210,300 (~72% reduction)

### Routing Performance
- Raw Graph Time: 0.28 sec  
- Clean Graph Time: 0.09 sec  
- **Speed Improvement: ~3x faster**

### Accuracy
- Path length difference: ~1–2% (minimal deviation)

---

## 🧠 Key Insight
Naive graph simplification can break connectivity and routing correctness.  
This project ensures **routing-safe simplification** by operating on the largest connected component and validating path consistency.

---

## 📸 Visualization
- Raw graph (high density)
- Cleaned graph (simplified topology)
- Shortest path comparison (before vs after)

---

## 🛠️ Tech Stack
- Python
- OSMnx
- NetworkX
- Matplotlib

---

## ▶️ How to Run

```bash
python main.py
