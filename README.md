# 🧩 Sudoku CSP Solver

## 📌 Overview
This project implements a **Sudoku Solver** using the **Constraint Satisfaction Problem (CSP)** approach.  
It solves standard 9×9 Sudoku puzzles using **backtracking search** with constraint checking and heuristic improvements.

---

## ⚙️ Features
- Backtracking search algorithm
- Constraint checking (row, column, 3×3 box)
- Domain generation for empty cells
- MRV (Minimum Remaining Values) heuristic for optimization
- Supports multiple difficulty levels:
  - Easy
  - Medium
  - Hard
  - Very Hard

---

## 🧠 Algorithm Used

### 1. Backtracking Search
The solver tries numbers recursively in empty cells and backtracks when a constraint violation occurs.

### 2. Constraint Checking
A number is only placed if:
- It does not already exist in the same row
- It does not exist in the same column
- It does not exist in the same 3×3 subgrid

### 3. MRV Heuristic
The algorithm selects the cell with the **minimum number of possible valid values**, reducing search space and improving performance.

---

## 📂 Input Format

Each Sudoku puzzle is stored in a `.txt` file with 9 lines:

Example:

004030050
609400000
005100489
000060930
300807002
026040000
453009600
000004705
090050200


- `0` represents an empty cell
- Each line must contain exactly 9 digits
- Total 9 lines per file

---

## 🚀 How to Run

### 1. Run the solver
bash
python sudoku_solver.py
2. Ensure input files exist:
easy.txt
medium.txt
hard.txt
veryhard.txt
📊 Output

For each puzzle, the program prints:

Initial Sudoku board
Solved board (if solution exists)
Backtracking statistics:
Number of calls
Number of failures
📈 Results Summary
Puzzle	Status
Easy	Solved ✔
Medium	Solved ✔
Hard	Likely Solved ✔
Very Hard	Possibly No Solution / Inconsistent ❌
🧩 Key Learnings
Sudoku is a classic CSP problem
Backtracking is effective for constraint-based problems
Heuristics like MRV significantly improve performance
Input consistency is critical for solvability
👨‍💻 Author

Muhammad Uzair Hussain 

📜 License

This project is for educational purposes only.
