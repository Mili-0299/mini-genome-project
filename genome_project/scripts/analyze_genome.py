import os
from collections import Counter
import matplotlib.pyplot as plt

# Define paths
script_dir = os.path.dirname(os.path.abspath(__file__))
data_file = os.path.join(script_dir, '../data/sample_genome.fasta')
results_dir = os.path.join(script_dir, '../results')
os.makedirs(results_dir, exist_ok=True)

# Read genome
with open(data_file, 'r') as file:
    lines = file.readlines()
    genome = ''.join([line.strip() for line in lines if not line.startswith('>')])

# Basic stats
length = len(genome)
gc_content = (genome.count('G') + genome.count('C')) / length * 100
base_counts = Counter(genome)

# Save summary
summary_file = os.path.join(results_dir, 'summary.txt')
with open(summary_file, 'w') as f:
    f.write(f"Genome length: {length}\n")
    f.write(f"GC content: {gc_content:.2f}%\n")
    f.write("Base composition:\n")
    for base, count in base_counts.items():
        f.write(f"{base}: {count}\n")

# Visualization
plt.bar(base_counts.keys(), base_counts.values(), color=['red', 'green', 'blue', 'orange'])
plt.title('Base Composition')
plt.xlabel('Base')
plt.ylabel('Count')
plt.savefig(os.path.join(results_dir, 'base_composition.png'))

print(f"Analysis complete. Results saved to {results_dir}")
