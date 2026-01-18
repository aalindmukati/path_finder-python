# path_finder-python 🧭

A terminal-based **pathfinding visualizer** written in Python using the `curses` library.
This project demonstrates **Breadth-First Search (BFS)** to find the shortest path through a maze from a start point (`O`) to a goal (`X`), with real-time animation directly in the terminal.

---

## 📌 Features

* Uses **Breadth-First Search (BFS)** to guarantee the shortest path
* Real-time **terminal animation** using `curses`
* Color-coded visualization:

  * Walls and maze layout
  * Explored path highlighted during traversal
* Simple, self-contained Python script
* No external dependencies beyond the Python standard library

---

## 🧠 How It Works

* The maze is defined as a 2D list:

  * `#` = wall
  * `" "` (space) = open path
  * `O` = starting point
  * `X` = destination
* BFS is implemented using `queue.Queue`
* Each step:

  * Explores valid neighboring cells (up, down, left, right)
  * Avoids walls and revisiting cells
  * Animates the current path using `curses`
* Once `X` is found, the shortest path is returned and displayed

---

## ▶️ How to Run

### Requirements

* Python **3.7+**
* Unix-based terminal (Linux or macOS recommended)

  * `curses` is **not natively supported on Windows CMD**
  * Windows users should run via **WSL** or Git Bash with `windows-curses`

### Run the Program

```bash
python path_finder.py
```

The maze will animate automatically.
Press **any key** after completion to exit.

---

## 🎨 Color Legend

| Symbol          | Meaning               |
| --------------- | --------------------- |
| `#`             | Wall                  |
| `O`             | Start                 |
| `X`             | Goal                  |
| Highlighted `X` | Current explored path |

---

## ⚠️ Notes & Limitations

* The maze is **hardcoded**
* Only supports **4-directional movement** (no diagonals)
* Terminal window must be large enough to display the maze
* Animation speed is fixed via `time.sleep(0.08)`

---

## 🔧 Possible Improvements

* Load maze from a file
* Add diagonal movement
* Implement A* or Dijkstra’s algorithm
* Add step-by-step mode
* Make maze size dynamic
* Add path length statistics

---

## ✅ Output

After completion, the terminal prints:

```
Shortest Path Found
```
