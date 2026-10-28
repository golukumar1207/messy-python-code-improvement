# Messy Python Code Improvement

**Author:** Golu Kumar  
**Course:** B.Tech Computer Science & Engineering  
**University:** JECRC University, Jaipur  

---

## 📌 Project Summary

This project showcases the systematic refactoring of messy, unstructured legacy Python code into clean, modular, and maintainable software utilizing AI development workflows.

---

## 🧹 Refactoring Improvements

| Area | Before (`messy_code.py`) | After (`improved_code.py`) |
| :--- | :--- | :--- |
| **Data Representation** | Nested untyped lists (`[["laptop", 55000, 2]]`) | Immutable `@dataclass` models (`Item`, `InvoiceLine`) |
| **Naming Conventions** | Cryptic variables (`t`, `p`, `q`, `d`, `net`) | Meaningful self-documenting identifiers (`unit_price`, `discount_amount`) |
| **Business Logic** | Hardcoded magic numbers (`0.15`, `0.18`) scattered in loops | Configurable module-level constants (`DISCOUNT_TIERS`, `STANDARD_TAX_RATE`) |
| **Modularity** | Monolithic global script execution | Dedicated `BillingCalculator` class with clear single responsibilities |
| **Output Presentation** | Messy string concatenations | Formatted tabular invoice output |

---

## 🚀 Execution

Compare the execution of both scripts:

```bash
# Run original messy script
python messy_code.py

# Run refactored, clean script
python improved_code.py
```
