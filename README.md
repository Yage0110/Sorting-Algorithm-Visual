# Sorting Algorithm Visualizer

## Overview

This project is an algorithm visualizer built using Python and Pygame. It provides a graphical interface to visualize sorting algorithms, making it easier to understand how these algorithms work. The visualizer supports several sorting algorithms and offers various controls for user interaction.

### Features

- **Real-time Visualization:** Watch sorting algorithms in action.
- **Multiple Sorting Algorithms:** Supports various sorting algorithms including Bubble Sort, Insertion Sort, Selection Sort, Merge Sort, Quick Sort, and Heap Sort.
- **User Controls:** Reset the list, start sorting, switch between ascending and descending order, and choose sorting algorithms with keyboard inputs.
- **Dynamic Interface:** Responsive design to accommodate different screen sizes.

## Computational Architecture

The visualizer is structured around a few key components:

1. **DrawnInfo Class:** Handles the graphical representation of the sorting process.
2. **Sorting Algorithms:** Implements several sorting algorithms with visual feedback.
3. **Main Loop:** Manages user input, updates the display, and controls the sorting process.

### DrawnInfo Class

The `DrawnInfo` class is responsible for setting up the display window, managing graphical elements, and drawing the list of numbers as bars on the screen. It includes:

- **Initialization:** Sets up the display window and initializes the list.
- **Set List:** Updates the list and recalculates the dimensions of the bars.
- **Drawing Methods:** Draws the list, updates colors, and handles screen clearing.

### Sorting Algorithms

The sorting algorithms are implemented as generator functions, allowing the main loop to pause and resume the sorting process, creating a smooth animation effect.

- **Bubble Sort (`bubble_sort`):**
  - Iterates through the list, repeatedly swapping adjacent elements if they are in the wrong order.
  - Yields control to allow for real-time visualization.

- **Insertion Sort (`insertion_sort`):**
  - Builds the sorted list one element at a time, inserting each new element into its correct position.
  - Yields control to allow for real-time visualization.

- **Selection Sort (`selection_sort`):**
  - Finds the minimum element from the unsorted part of the list and swaps it with the first unsorted element.
  - Yields control to allow for real-time visualization.

- **Merge Sort (`merge_sort`):**
  - Divides the list into smaller sublists, sorts them recursively, and then merges them back together.
  - Yields control to allow for real-time visualization.

- **Quick Sort (`quick_sort`):**
  - Chooses a pivot element and partitions the list into smaller elements (less than pivot) and larger elements (greater than pivot).
  - Recursively sorts the sublists.
  - Yields control to allow for real-time visualization.

- **Heap Sort (`heap_sort`):**
  - Builds a heap structure (max heap or min heap) and repeatedly swaps the root of the heap with the last node.
  - Yields control to allow for real-time visualization.

### Main Loop

The main loop initializes the `DrawnInfo` object, handles user input, and manages the sorting process. Key functionalities include:

- **Event Handling:** Captures keyboard inputs to reset the list, start sorting, and switch between algorithms and order.
- **Drawing Updates:** Calls the drawing functions to update the display in real-time.
- **Sorting Control:** Pauses and resumes the sorting process using generator functions.

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/Yage0110/Sorting-Algorithm-Visual.git
    ```

2. **Navigate to the project directory:**

    ```bash
    cd Sorting-Algorithm-Visual
    ```

3. **Install the required packages:**

    ```bash
    pip install pygame
    ```

## Usage

1. **Run the visualizer:**

    ```bash
    python algorithm.py
    ```

2. **Controls:**

    - `R` - Reset the list
    - `SPACE` - Start sorting
    - `A` - Sort in ascending order
    - `D` - Sort in descending order
    - `I` - Use Insertion Sort
    - `B` - Use Bubble Sort
    - `S` - Use Selection Sort
    - `M` - Use Merge Sort
    - `Q` - Use Quick Sort
    - `H` - Use Heap Sort

## Detailed Functionality

### `DrawnInfo` Class

- **Attributes:**
  - `BLACK`, `WHITE`, `GREEN`, `RED`, `BLUE`: Color definitions for drawing.
  - `BACKG_CLR`: Background color of the window.
  - `GREYS`: Shades of grey used for bar colors.
  - `FONT`, `LARGER_FONT`: Font settings for displaying text.
  - `LR_PADDING`, `T_PADDING`: Padding for layout management.
  - `window`: The Pygame display surface.
  - `lst`: The list of values to be sorted.
  - `min_val`, `max_val`: Minimum and maximum values in the list.
  - `box_w`, `box_h`: Width and height of the bars representing list elements.
  - `start_x`: Starting x-coordinate for drawing bars.

- **Methods:**
  - `__init__(self, w, h, lst)`: Initializes the display window and list.
  - `set_list(self, lst)`: Updates the list and recalculates drawing parameters.
  - `draw(self)`: Draws the list of bars on the screen.
  - `draw_list(self, color_positions={}, clear_bg=False)`: Draws the bars with optional color highlighting.

### Sorting Algorithms

- **Bubble Sort (`bubble_sort`)**
  - Compares adjacent elements and swaps them if they are in the wrong order.
  - Iterates through the list multiple times, reducing the range each time.
  - Yields control to allow for real-time visualization.

- **Insertion Sort (`insertion_sort`)**
  - Builds a sorted list one element at a time.
  - Inserts each new element into its correct position.
  - Yields control to allow for real-time visualization.

- **Selection Sort (`selection_sort`)**
  - Finds the minimum element from the unsorted part of the list and swaps it with the first unsorted element.
  - Yields control to allow for real-time visualization.

- **Merge Sort (`merge_sort`)**
  - Divides the list into smaller sublists, sorts them recursively, and then merges them back together.
  - Yields control to allow for real-time visualization.

- **Quick Sort (`quick_sort`)**
  - Chooses a pivot element and partitions the list into smaller elements (less than pivot) and larger elements (greater than pivot).
  - Recursively sorts the sublists.
  - Yields control to allow for real-time visualization.

- **Heap Sort (`heap_sort`)**
  - Builds a heap structure (max heap or min heap) and repeatedly swaps the root of the heap with the last node.
  - Yields control to allow for real-time visualization.

### Main Loop

- **Initialization:** Sets up the Pygame environment and `DrawnInfo` object.
- **Event Handling:** Captures and processes keyboard inputs.
- **Sorting Control:** Manages the sorting process and updates the display.

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, feel free to fork the repository, create a branch, and submit a pull request.

## License

This project is licensed under the MIT License.

---

**Note:** This project is a valuable educational tool for understanding sorting algorithms and their behaviors. The real-time visualization provides a clear and intuitive way to observe the sorting process step by step.
