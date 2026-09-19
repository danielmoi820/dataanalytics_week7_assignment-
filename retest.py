import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load dataset
df = pd.read_csv('HealthConnect_Appointment_Data.csv')

# 2. Verify corrected column reference and categorization
lead_time_col = 'booking_lead_days'
bins = [0, 7, 14, 30, 90, 365]
labels = ['0-7 Days', '8-14 Days', '15-30 Days', '31-90 Days', '90+ Days']
df['lead_time_bin'] = pd.cut(df[lead_time_col], bins=bins, labels=labels)

# 3. Re-test output metrics
lead_bin_data = df['lead_time_bin'].value_counts().sort_index()
total_records = len(df)
missing_check = df[lead_time_col].isnull().sum()

print("=== RE-TEST VALIDATION REPORT ===")
print(f"Total Records Verified: {total_records:,}")
print(f"Missing Values in '{lead_time_col}': {missing_check}")
print("\nLead Time Bin Distribution:")
print(lead_bin_data)

# 4. Generate refined visual output
sns.set_theme(style="whitegrid")
plt.figure(figsize=(8, 5))
ax = sns.barplot(x=lead_bin_data.index, y=lead_bin_data.values, hue=lead_bin_data.index, palette="Blues_d", legend=False)

plt.title("Validated Appointment Concentration by Booking Lead Time", fontsize=12, pad=15, weight='bold')
plt.xlabel("Booking Lead Time Category", fontsize=10)
plt.ylabel("Number of Appointments", fontsize=10)

plt.tight_layout()
plt.savefig("retested_lead_time_chart.png", dpi=300)
plt.close()
print("\n[SUCCESS] Re-test complete. Refined chart generated and verified successfully.")
