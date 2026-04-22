import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import rcParams

# Set Korean font for matplotlib (if needed)
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['axes.unicode_minus'] = False

def load_correlation_data(file_path):
    """Load and clean the correlation data from Excel file"""
    try:
        df_raw = pd.read_excel(file_path, header=None)
        
        # Extract Intraassay data (rows 4-8)
        intraassay_data = []
        for i in range(4, 9):
            if i < len(df_raw):
                row = df_raw.iloc[i]
                numeric_values = []
                for val in row[1:]:  # skip first column
                    if pd.notna(val) and isinstance(val, (int, float)):
                        numeric_values.append(val)
                if len(numeric_values) >= 5:
                    intraassay_data.append(numeric_values)
        
        # Extract Interassay data (rows 14-18)  
        interassay_data = []
        for i in range(14, 19):
            if i < len(df_raw):
                row = df_raw.iloc[i]
                numeric_values = []
                for val in row[1:]:  # skip first column
                    if pd.notna(val) and isinstance(val, (int, float)):
                        numeric_values.append(val)
                if len(numeric_values) >= 5:
                    interassay_data.append(numeric_values)
        
        # Create DataFrames
        intraassay_df = pd.DataFrame(intraassay_data, 
                                   columns=['Sample', 'Measurement_1', 'Measurement_2', 'Mean', 'SD', 'CV_percent'])
        
        interassay_df = pd.DataFrame(interassay_data, 
                                   columns=['Sample', 'Day_1', 'Day_2', 'Mean', 'SD', 'CV_percent'])
        
        return intraassay_df, interassay_df
    
    except Exception as e:
        print(f"Error loading data: {e}")
        return None, None

def create_correlation_plots(intraassay_df, interassay_df):
    """Create correlation plots for both datasets"""
    
    # Set up the plot style
    plt.style.use('default')
    sns.set_palette("husl")
    
    # Create figure with subplots
    fig = plt.figure(figsize=(20, 12))
    
    # Define columns for correlation analysis
    intra_columns = ['Measurement_1', 'Measurement_2', 'Mean', 'SD', 'CV_percent']
    inter_columns = ['Day_1', 'Day_2', 'Mean', 'SD', 'CV_percent']
    
    # Calculate correlation matrices
    intra_corr = intraassay_df[intra_columns].corr()
    inter_corr = interassay_df[inter_columns].corr()
    
    # Plot 1: Intraassay Correlation Heatmap
    plt.subplot(2, 3, 1)
    sns.heatmap(intra_corr, annot=True, cmap='coolwarm', center=0, 
                square=True, fmt='.3f', cbar_kws={'shrink': 0.8})
    plt.title('Intraassay Correlation Matrix', fontsize=14, pad=20)
    plt.xticks(rotation=45, ha='right')
    plt.yticks(rotation=0)
    
    # Plot 2: Interassay Correlation Heatmap
    plt.subplot(2, 3, 2)
    sns.heatmap(inter_corr, annot=True, cmap='coolwarm', center=0, 
                square=True, fmt='.3f', cbar_kws={'shrink': 0.8})
    plt.title('Interassay Correlation Matrix', fontsize=14, pad=20)
    plt.xticks(rotation=45, ha='right')
    plt.yticks(rotation=0)
    
    # Plot 3: CV% Comparison
    plt.subplot(2, 3, 3)
    plt.scatter(intraassay_df['CV_percent'], interassay_df['CV_percent'], 
                s=100, alpha=0.7, c='red', edgecolors='black')
    plt.plot([0, max(intraassay_df['CV_percent'].max(), interassay_df['CV_percent'].max())], 
             [0, max(intraassay_df['CV_percent'].max(), interassay_df['CV_percent'].max())], 
             'k--', alpha=0.5)
    plt.xlabel('Intraassay CV%')
    plt.ylabel('Interassay CV%')
    plt.title('Intraassay vs Interassay CV%')
    plt.grid(True, alpha=0.3)
    
    # Plot 4: Measurement Comparison (Intraassay)
    plt.subplot(2, 3, 4)
    plt.scatter(intraassay_df['Measurement_1'], intraassay_df['Measurement_2'], 
                s=100, alpha=0.7, c='blue', edgecolors='black')
    plt.xlabel('Measurement 1')
    plt.ylabel('Measurement 2')
    plt.title('Intraassay: Measurement 1 vs 2')
    plt.grid(True, alpha=0.3)
    
    # Plot 5: Day Comparison (Interassay)
    plt.subplot(2, 3, 5)
    plt.scatter(interassay_df['Day_1'], interassay_df['Day_2'], 
                s=100, alpha=0.7, c='green', edgecolors='black')
    plt.xlabel('Day 1')
    plt.ylabel('Day 2')
    plt.title('Interassay: Day 1 vs Day 2')
    plt.grid(True, alpha=0.3)
    
    # Plot 6: SD vs CV% for both datasets
    plt.subplot(2, 3, 6)
    plt.scatter(intraassay_df['SD'], intraassay_df['CV_percent'], 
                s=100, alpha=0.7, c='blue', edgecolors='black', label='Intraassay')
    plt.scatter(interassay_df['SD'], interassay_df['CV_percent'], 
                s=100, alpha=0.7, c='red', edgecolors='black', label='Interassay')
    plt.xlabel('Standard Deviation')
    plt.ylabel('CV%')
    plt.title('SD vs CV% Comparison')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    plt.tight_layout(pad=3.0)
    return fig

def print_correlation_summary(intraassay_df, interassay_df):
    """Print correlation analysis summary"""
    
    print("="*80)
    print("CORRELATION ANALYSIS SUMMARY")
    print("="*80)
    
    print("\nINTRASSAY DATA:")
    print("-" * 40)
    print(intraassay_df.to_string(index=False))
    
    print("\nINTRASSAY CORRELATION MATRIX:")
    print("-" * 40)
    intra_columns = ['Measurement_1', 'Measurement_2', 'Mean', 'SD', 'CV_percent']
    intra_corr = intraassay_df[intra_columns].corr()
    print(intra_corr.round(3).to_string())
    
    print("\n\nINTERASSAY DATA:")
    print("-" * 40)
    print(interassay_df.to_string(index=False))
    
    print("\nINTERASSAY CORRELATION MATRIX:")
    print("-" * 40)
    inter_columns = ['Day_1', 'Day_2', 'Mean', 'SD', 'CV_percent']
    inter_corr = interassay_df[inter_columns].corr()
    print(inter_corr.round(3).to_string())
    
    print("\n\nSUMMARY STATISTICS:")
    print("-" * 40)
    print(f"Intraassay CV% - Mean: {intraassay_df['CV_percent'].mean():.3f}, "
          f"Std: {intraassay_df['CV_percent'].std():.3f}")
    print(f"Interassay CV% - Mean: {interassay_df['CV_percent'].mean():.3f}, "
          f"Std: {interassay_df['CV_percent'].std():.3f}")
    
    # Strong correlations
    print("\nSTRONG CORRELATIONS (|r| > 0.7):")
    print("-" * 40)
    
    # Check intraassay strong correlations
    for i in range(len(intra_corr.columns)):
        for j in range(i+1, len(intra_corr.columns)):
            corr_val = intra_corr.iloc[i, j]
            if abs(corr_val) > 0.7:
                print(f"Intraassay: {intra_corr.columns[i]} - {intra_corr.columns[j]}: {corr_val:.3f}")
    
    # Check interassay strong correlations
    for i in range(len(inter_corr.columns)):
        for j in range(i+1, len(inter_corr.columns)):
            corr_val = inter_corr.iloc[i, j]
            if abs(corr_val) > 0.7:
                print(f"Interassay: {inter_corr.columns[i]} - {inter_corr.columns[j]}: {corr_val:.3f}")

def main():
    """Main function to run correlation analysis"""
    
    # File path
    file_path = "data/상관성.xlsx"
    
    # Load data
    print("Loading correlation data...")
    intraassay_df, interassay_df = load_correlation_data(file_path)
    
    if intraassay_df is not None and interassay_df is not None:
        # Print summary
        print_correlation_summary(intraassay_df, interassay_df)
        
        # Create plots
        print("\nCreating correlation plots...")
        fig = create_correlation_plots(intraassay_df, interassay_df)
        
        # Save the plot
        plt.savefig('correlation_analysis.png', dpi=300, bbox_inches='tight')
        print("Plot saved as 'correlation_analysis.png'")
        
        # Save cleaned data
        intraassay_df.to_csv('intraassay_data.csv', index=False)
        interassay_df.to_csv('interassay_data.csv', index=False)
        print("Data saved as CSV files")
        
        # Show the plot
        plt.show()
        
    else:
        print("Failed to load data. Please check the file path and format.")
        
        # Create sample data for demonstration
        print("\nCreating sample data for demonstration...")
        np.random.seed(42)
        
        sample_intra = pd.DataFrame({
            'Sample': range(1, 6),
            'Measurement_1': [6.67, 2.59, 1.34, 2.91, 0.78],
            'Measurement_2': [6.80, 2.57, 1.32, 2.88, 0.79],
            'Mean': [6.735, 2.58, 1.33, 2.895, 0.785],
            'SD': [0.092, 0.014, 0.014, 0.021, 0.007],
            'CV_percent': [1.365, 0.548, 1.063, 0.733, 0.901]
        })
        
        sample_inter = pd.DataFrame({
            'Sample': range(1, 6),
            'Day_1': [6.37, 2.96, 1.53, 2.64, 0.75],
            'Day_2': [6.74, 2.58, 1.33, 2.90, 0.79],
            'Mean': [6.555, 2.77, 1.43, 2.77, 0.77],
            'SD': [0.262, 0.269, 0.141, 0.184, 0.028],
            'CV_percent': [3.991, 9.700, 9.890, 6.637, 3.673]
        })
        
        print_correlation_summary(sample_intra, sample_inter)
        fig = create_correlation_plots(sample_intra, sample_inter)
        plt.savefig('sample_correlation_analysis.png', dpi=300, bbox_inches='tight')
        plt.show()

if __name__ == "__main__":
    main()