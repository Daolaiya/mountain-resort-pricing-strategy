# Mountain Resort Pricing Strategy
## About
- LinkedIn --> https://www.linkedin.com/in/damilola-olaiya/

## Hypothesis
- How can Big Mountain Resort create a ticket pricing strategy that will (1) better leverage the client's facilities
and (2) either cut costs or give more confidence in increasing ticket prices without undermining ticket sales in the long run?

## Setup
```bash
pip install -r requirements.txt
```

## Notebook run order
Run the notebooks in order from the `notebooks/` directory:

1. `02_data_wrangling.ipynb` — produces `data/ski_data_cleaned.csv` and `data/state_summary.csv`
2. `03_exploratory_data_analysis.ipynb` — produces `data/ski_data_step3_features.csv`
3. `04_preprocessing_and_training.ipynb` — trains models and saves `models/ski_resort_pricing_model.pkl`
4. `05_modeling.ipynb` — loads the saved model and runs business scenario analysis

Notebook 05 requires the model file from notebook 04. If `models/ski_resort_pricing_model.pkl` is missing, run notebook 04 first.
