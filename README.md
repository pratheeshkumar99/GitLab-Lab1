# MLOps Lab 1 – GitHub Actions & Python Testing

## Base Lab
Built on top of **Lab 1** by Professor Ramin Mohammadi:
[raminmohammadi/MLOps – Github_Labs/Lab1](https://github.com/raminmohammadi/MLOps/tree/main/Github_Labs/Lab1)

---

## What I Changed

### `calculator.py` — 8 New Functions
The original had 4 functions (add, subtract, multiply, sum-of-three). I added:

| Function | Description |
|----------|-------------|
| `fun5` | Division with `ZeroDivisionError` handling |
| `fun6` | Exponentiation with overflow protection |
| `fun7` | Factorial of a non-negative integer |
| `fun8` | Statistical analysis (mean, median, mode, std dev, variance) |
| `fun9` | Fibonacci sequence generator |
| `fun10` | Polynomial evaluation using Horner's method |
| `fun11` | Quadratic equation solver (handles 2 roots, 1 root, no real roots) |
| `fun12` | Matrix multiplication with full input validation |


### Tests
Extended both `test_pytest.py` and `test_unittest.py` to cover all 12 functions, including edge cases (e.g., float inputs, zero division, identity matrix, repeated quadratic roots).


## Project Structure

```
GitLab-Lab1/
├── .github/workflows/
│   ├── pytest_action.yml
│   └── unittest_action.yml
├── src/
│   └── calculator.py
├── test/
│   ├── test_pytest.py
│   └── test_unittest.py
├── requirements.txt
└── README.md
```

---

## Setup & Run

```bash
# 1. Clone and enter the repo
git clone https://github.com/pratheeshkumar99/GitLab-Lab1.git
cd GitLab-Lab1

# 2. Create and activate virtual environment
python -m venv lab_01
source lab_01/bin/activate        # Windows: lab_01\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt
pip install pytest pytest-cov pytest-html flake8

# 4a. Run pytest (with coverage)
pytest --cov=src --cov-report=term -v

# 4b. Run unittests
python -m unittest test.test_unittest -v

# 4c. Run linter
flake8 src/ test/ --max-line-length=88
```

CI runs automatically on every push. Check the **Actions** tab for results.
