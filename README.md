# SMART Method Application

This project implements the SMART (Simple Multi-Attribute Rating Technique) method using Streamlit for the user interface. The SMART method is used for multi-criteria decision making, allowing users to input criteria weights, directions, and utilities for different alternatives to determine the best alternative based on weighted scores.

## Features

- Input criteria weights and directions
- Input utilities for different alternatives
- Compute the best alternative using the SMART method
- Display results in a styled table
- Example button to pre-fill inputs with sample data

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/smart-method-app.git
    ```
2. Navigate to the project directory:
    ```bash
    cd smart-method-app
    ```
3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the Streamlit application:
    ```bash
    streamlit run smart.py
    ```
2. Open your web browser and go to `http://localhost:8501`.

3. Input the number of criteria and alternatives.

4. Fill in the criteria weights, directions, and utilities for each alternative.

5. Click the "Apply SMART" button to compute the best alternative.

6. Optionally, click the "Example" button to load sample data and see how the application works.

## Example

The example button pre-fills the inputs with the following data:

- Criteria Weights: `[0.4, 0.3, 0.2, 0.1]`
- Directions: `['min', 'max', 'max', 'min']`
- Utilities:
    ```
    [
        [10000, 8, 7, 500],
        [12000, 9, 8, 550],
        [9500, 7, 6, 600],
        [11000, 8, 7, 480],
        [10500, 6, 8, 520],
        [11500, 8, 7, 530],
        [9000, 7, 9, 490],
        [10200, 9, 6, 570]
    ]
    ```

### Example Results

After applying the SMART method to the example data, the results are as follows:

| Alternative   | Score   |
|---------------|---------|
| Alternative 1 | 0.616667|
| Alternative 2 | 0.475000|
| Alternative 3 | 0.433333|
| Alternative 4 | 0.500000|
| Alternative 5 | 0.400000|
| Alternative 6 | 0.391667|
| Alternative 7 | 0.791667|
| Alternative 8 | 0.565000|

The best alternative given by the SMART method is: **Alternative 7**
