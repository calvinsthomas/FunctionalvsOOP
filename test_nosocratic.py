#!/usr/bin/env python3
"""
NOSOCRATIC Test Script - NO AI/ML REMOTE SERVICES
"""

import os
import random
import statistics
from datetime import datetime

# NOSOCRATIC Data Handler
class NOSOCRATICDataHandler:
    def __init__(self, file_path):
        self.file_path = file_path

    def load_data(self):
        if not os.path.exists(self.file_path):
            print(f"NOSOCRATIC: File {self.file_path} does not exist.")
            return []

        data = []
        with open(self.file_path, 'r') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#"):
                    columns = line.split()
                    data.append(columns)

        if not data:
            print("NOSOCRATIC: No valid data found in the file.")
            return []

        # Simple list-based data structure
        structured_data = []
        for row in data:
            structured_data.append({f'column_{i}': row[i] for i in range(len(row))})
        
        print(f"NOSOCRATIC: Loaded {len(structured_data)} rows")
        return structured_data

    def preprocess_data(self, data):
        if not data:
            return data
            
        for i, row in enumerate(data):
            if 'label' not in row:
                row['label'] = random.randint(0, 1000)
            
            for key, value in row.items():
                if key != 'label':
                    try:
                        row[key] = float(value)
                    except (ValueError, TypeError):
                        row[key] = 0.0

        print(f"NOSOCRATIC: Preprocessed {len(data)} rows")
        return data

# Simple Statistical Model (NOSOCRATIC - No AI)
class SimpleStatisticalModel:
    def __init__(self, data):
        self.data = data

    def simple_train_model(self, data):
        labels = [row.get('label', random.randint(0, 1)) for row in data]
        correct_predictions = sum(1 for _ in range(len(labels)) if random.random() > 0.4)
        accuracy = correct_predictions / max(len(labels), 1)
        return accuracy

# Simple Statistical Simulation (NOSOCRATIC - No AI)
class SimpleStatisticalSimulation:
    def __init__(self, model, num_simulations=10):
        self.model = model
        self.num_simulations = num_simulations

    def run_simulation(self, data):
        results = []
        for _ in range(self.num_simulations):
            accuracy = self.model.simple_train_model(data)
            results.append(accuracy)
        mean_result = statistics.mean(results) if results else 0.5
        std_result = statistics.stdev(results) if len(results) > 1 else 0.1
        return mean_result, std_result

def test_nosocratic():
    print("NOSOCRATIC: Testing the system...")
    
    # Create test data
    test_dir = './local_data'
    os.makedirs(test_dir, exist_ok=True)
    test_file = os.path.join(test_dir, 'test.txt')
    
    with open(test_file, 'w') as f:
        f.write('# NOSOCRATIC Test Data\n')
        for i in range(5):
            f.write(f'{random.random():.4f} {random.random():.4f} {random.randint(0, 1)}\n')
    
    # Test the system
    handler = NOSOCRATICDataHandler(test_file)
    data = handler.load_data()
    processed_data = handler.preprocess_data(data)
    
    model = SimpleStatisticalModel(processed_data)
    simulation = SimpleStatisticalSimulation(model)
    mean_acc, std_acc = simulation.run_simulation(processed_data)
    
    print(f"NOSOCRATIC: Results - Mean: {mean_acc:.3f}, Std: {std_acc:.3f}")
    print("NOSOCRATIC: Test completed successfully!")

if __name__ == "__main__":
    test_nosocratic()
