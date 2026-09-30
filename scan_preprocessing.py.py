"""
SCAN Dataset Preprocessing

This script preprocesses SCAN verbal analogy questions by:
1. Extracting questions, answer choices, and correct answers.
2. Reducing each question to four answer choices.
3. Ensuring that the correct answer is preserved.
4. Randomly selecting three distractors.
5. Shuffling the final choices.
6. Saving the standardized questions in a simplified format.
"""

import random


# --------------------------------------------------
# Configuration
# --------------------------------------------------

INPUT_FILE = "scan_partition1.txt"
OUTPUT_FILE = "partition1.txt"


# --------------------------------------------------
# Data containers
# --------------------------------------------------

questions = []
answers = []
numbers = []
extracted_texts = []


# --------------------------------------------------
# Data extraction
# --------------------------------------------------

def find_line_after_blank(input_file):
    """
    Extract questions from lines that directly follow blank lines.
    """
    with open(input_file, "r", encoding="utf-8") as infile:
        previous_line_was_blank = False

        for line in infile:
            if previous_line_was_blank:
                questions.append(line.strip())
                previous_line_was_blank = False

            elif line.strip() == "":
                previous_line_was_blank = True


def find_number_before_blank(input_file):
    """
    Extract numeric answer indices that appear immediately
    before blank lines.
    """
    with open(input_file, "r", encoding="utf-8") as infile:
        previous_line = None

        for line in infile:
            line = line.strip()

            if line == "":
                if previous_line and previous_line.isdigit():
                    numbers.append(int(previous_line))

            previous_line = line


def extract_lines_between_blank_and_number(input_file):
    """
    Extract answer choices located between a blank line
    and the following numeric answer index.
    """
    with open(input_file, "r", encoding="utf-8") as infile:
        save_lines = False
        buffer = []

        for line in infile:
            line = line.strip()

            if line == "":
                save_lines = True
                buffer = []

            elif line.isdigit():
                save_lines = False

                if buffer:
                    extracted_texts.append(buffer)

            elif save_lines:
                buffer.append(line)


# --------------------------------------------------
# Choice reduction
# --------------------------------------------------

def reduce_choices(choices, correct_answer):
    """
    Reduce the available choices to exactly four:
    one correct answer and three randomly selected distractors.

    Returns:
        final_choices: Shuffled list containing four choices.
        correct_letter: Letter (a-d) corresponding to the correct answer.
    """

    if correct_answer not in choices:
        raise ValueError(
            f"Correct answer '{correct_answer}' is not in the choices list."
        )

    choices_without_correct = [
        choice for choice in choices
        if choice != correct_answer
    ]

    selected_incorrect = random.sample(choices_without_correct, 3)

    final_choices = selected_incorrect + [correct_answer]
    random.shuffle(final_choices)

    correct_index = final_choices.index(correct_answer)
    correct_letter = chr(ord("a") + correct_index)

    return final_choices, correct_letter


# --------------------------------------------------
# Main processing
# --------------------------------------------------

# Extract data from the original SCAN partition
find_line_after_blank(INPUT_FILE)
find_number_before_blank(INPUT_FILE)
extract_lines_between_blank_and_number(INPUT_FILE)

# Adjust answer indices to match the extracted choice structure
updated_numbers = [number + 1 for number in numbers]

# Extract the correct answer for each question
for i, sublist in enumerate(extracted_texts):

    if i < len(updated_numbers):
        index = updated_numbers[i]

        if index < len(sublist):
            answers.append(sublist[index])
        else:
            answers.append("Invalid index")

    else:
        answers.append("No answer available")


# Process questions and save the standardized dataset
question_count = 0

with open(OUTPUT_FILE, "w", encoding="utf-8") as outfile:

    for i, question in enumerate(questions):

        if i >= len(answers):
            outfile.write(f"{question}\n")
            outfile.write(
                "Error: No corresponding answer for this question.\n\n"
            )
            continue

        correct_answer = answers[i]

        current_choices = (
            extracted_texts[i]
            if i < len(extracted_texts)
            else []
        )

        if correct_answer not in current_choices:
            outfile.write(f"{question}\n")
            outfile.write(
                f"Error: Correct answer '{correct_answer}' "
                "is not in the choices list.\n\n"
            )
            continue

        try:
            final_choices, correct_letter = reduce_choices(
                current_choices,
                correct_answer
            )

        except ValueError as error:
            outfile.write(f"{question}\n")
            outfile.write(f"Error: {error}\n\n")
            continue

        # Write question
        outfile.write(f"{question}\n")

        # Write four answer choices
        for choice in final_choices:
            outfile.write(f"{choice}\n")

        # Write the correct answer label
        outfile.write(f"{correct_letter}\n\n")

        question_count += 1


# --------------------------------------------------
# Summary
# --------------------------------------------------

print(f"Total number of questions processed: {question_count}")
print(f"Results have been written to {OUTPUT_FILE}.")


# Original SCAN partition distribution:
# Partition 1: 652 questions
# Partition 2: 427 questions
# Partition 3: 317 questions
# Partition 4: 220 questions
# Total: 1,616 questions
