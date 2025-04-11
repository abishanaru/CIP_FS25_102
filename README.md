# Data Collection, Integration and Preprocessing (CIP)
This is a course of the masters program Applied Information and Data Science at the Applied University of Lucerne.

## About the Project
This project investigates parking space availability in Zurich and Basel, Switzerland, analyzing patterns and correlations with weather conditions. The study examines daily, weekly, and seasonal variations in parking occupancy while considering factors such as working hours versus non-working hours, weekdays versus weekends, and weather impacts.

## Research Questions
1. How does parking availability change throughout the day, week, and across seasons?
2. What is the relationship between weather conditions and parking availability?
3. How does parking availability in Zurich compare to Basel?

## Data Sources
- Parking data from Zurich: Parkendd API
- Parking data from Basel: Open data portal
- Weather data: Wunderground.com (scraped)

## Key Features
- Time-based analysis of parking patterns
- Weather correlation studies
- Cross-city comparison between Zurich and Basel
- Interactive visualizations using Plotly
- Statistical analysis of parking trends

## Requirements
The following Python libraries are required:
```python
requests==2.31.0
pandas==2.1.0
numpy==1.24.3
plotly==5.18.0
matplotlib==3.8.0
seaborn==0.13.0
dash==2.14.0
selenium==4.15.2
beautifulsoup4==4.12.2
```

## Project Structure
- `main.ipynb`: Main analysis notebook
- `data/`: Raw and processed data files

## Installation
1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run Jupyter notebook: `jupyter notebook main.ipynb`

## Usage
The analysis is presented in two formats:
1. Jupyter notebook: Includes detailed explanations, code, and visualizations. The notebook is structured to follow the research questions systematically, providing insights into parking patterns and their correlations with various factors.
2. PDF Report: A comprehensive summary of the project findings, methodology, and conclusions. Find it in `parking_analysis_report.pdf`.

## Contributors
- Sandra Deck
- Abishan Arumugavel