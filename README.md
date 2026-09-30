# SCAN Dataset Preprocessing

A data preprocessing project developed as part of the **Can Machines Think Like Us?** graduation research project.

The script processes verbal analogy questions from the **SCAN dataset** and converts them into a consistent four-option multiple-choice format for use in Large Language Model (LLM) evaluation experiments.

---

## 🎯 Purpose

The original SCAN questions contain varying numbers of answer choices. For the research experiments, a standardized format was needed so that each question contained exactly **four options**.

This script automates that preprocessing process while preserving the correct answer.

---

## ⚙️ What the Script Does

The preprocessing pipeline:

1. Reads a SCAN dataset partition from a text file.
2. Extracts the questions and their available answer choices.
3. Identifies the correct answer for each question.
4. Preserves the correct answer.
5. Randomly selects three incorrect choices as distractors.
6. Shuffles the four final choices.
7. Converts the correct answer position to a letter from `a` to `d`.
8. Saves the processed questions to a new text file.

---

## 🔄 Processing Flow

```text
Original SCAN Partition
        ↓
Extract Questions & Choices
        ↓
Identify Correct Answer
        ↓
Select 3 Distractors
        ↓
Create 4-Option Question
        ↓
Shuffle Choices
        ↓
Assign Correct Label (a–d)
        ↓
Save Processed Dataset
```

---

## 📁 Repository Structure

```text
scan-dataset-standardization/
│
├── README.md
└── scan_preprocessing.py
```

---

## 💻 Technologies

- Python
- File Processing
- Random Sampling
- Data Preprocessing

---

## 📊 SCAN Partitions

The SCAN data used in the project was distributed across four partitions:

| Partition | Questions |
|-----------|----------:|
| Partition 1 | 652 |
| Partition 2 | 427 |
| Partition 3 | 317 |
| Partition 4 | 220 |
| **Total** | **1,616** |

---

## 🧪 Example Output Format

Each processed question follows this structure:

```text
question
choice 1
choice 2
choice 3
choice 4
correct_answer_letter
```

The correct answer is represented by a letter from `a` to `d`.

---

## 🔗 Related Research

This preprocessing work was developed for the graduation research project:

**Can Machines Think Like Us? — The Ability of Large Language Models to Pass Verbal Analogical Reasoning in Aptitude Tests**

🔗 [View the Research Repository](https://github.com/ShaimaNabeel/llm-verbal-analogical-reasoning)

---
ر## ⚠️ Limitation & Reproducibility Note

The original preprocessing script uses random sampling and shuffling when selecting distractors and arranging the final answer choices.

Because a fixed random seed was not used during the original preprocessing, running the script multiple times may produce different distractor selections and answer-choice orders.

This does not change the purpose of the preprocessing pipeline, but it limits exact reproducibility of the generated dataset.

### Suggested Improvement

For future use, a fixed random seed can be added after importing the `random` module:

```python
import random

random.seed(42)
```

Using a fixed seed ensures that the same input produces the same randomly selected distractors and choice order across repeated runs.

---

## 📌 Dataset Availability

The original SCAN dataset is **not redistributed in this repository**.

This repository contains the preprocessing code developed for the research project. The original dataset remains subject to its source and applicable usage terms.

---

## 👩‍💻 Preprocessing Script by

**Shaima Albokhari**  
B.Sc. Computer Science — Taif University
