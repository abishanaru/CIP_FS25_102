
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

def prepare_data():
    # Load data from CSV files
    parkhaus_data = pd.read_csv("parkhaus_data_2024.csv")
    weather_data = pd.read_csv("weather_2024_lszh.csv")

    # Convert timestamps
    parkhaus_data['timestamp'] = pd.to_datetime(parkhaus_data['timestamp'])
    parkhaus_data.set_index('timestamp', inplace=True)
    weather_data['date'] = pd.to_datetime(weather_data['date'])
    weather_data.set_index('date', inplace=True)

    # Calculate occupancy (assuming total capacity is constant)
    total_capacity = 77  # Based on data analysis
    parkhaus_data['occupancy'] = total_capacity - parkhaus_data['free']
    
    # Add time-based features
    parkhaus_data['hour'] = parkhaus_data.index.hour
    parkhaus_data['day_of_week'] = parkhaus_data.index.dayofweek
    parkhaus_data['date'] = parkhaus_data.index.date

    # Convert the date to datetime for merging
    parkhaus_data['date'] = pd.to_datetime(parkhaus_data['date'])
    
    # Create daily averages for parking data
    daily_parking = parkhaus_data.groupby('date')['occupancy'].mean().reset_index()
    daily_parking.set_index('date', inplace=True)

    # Merge weather and parking data
    merged_df = pd.merge(daily_parking, weather_data, left_index=True, right_index=True)

    # Select features
    features = ['day_avg_temp', 'max_wind_speed', 'sea_level_pressure']
    X = merged_df[features]
    y = merged_df['occupancy']

    return X, y

def train_model(X, y):
    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Initialize and train the model
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    # Make predictions
    y_pred = model.predict(X_test)
    
    # Calculate metrics
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    
    return model, mse, r2, X_test, y_test, y_pred

def main():
    # Prepare data
    X, y = prepare_data()
    
    # Train and evaluate model
    model, mse, r2, X_test, y_test, y_pred = train_model(X, y)
    
    print(f"Mean Squared Error: {mse:.2f}")
    print(f"R² Score: {r2:.2f}")
    
    # Feature importance
    feature_importance = pd.DataFrame({
        'feature': X.columns,
        'importance': model.feature_importances_
    }).sort_values('importance', ascending=False)
    
    print("\nFeature Importance:")
    print(feature_importance)

if __name__ == "__main__":
    main()
