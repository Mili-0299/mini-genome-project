import os

# Define paths relative to this script
script_dir = os.path.dirname(os.path.abspath(__file__))
data_file = os.path.join(script_dir, '..', 'data', 'sample_genome.fasta')
results_dir = os.path.join(script_dir, '..', 'results')
os.makedirs(results_dir, exist_ok=True)

# Read genome
with open(data_file, 'r') as file:
    genome = ''.join([line.strip() for line in file if not line.startswith('>')])

print('Genome data loaded:')
print(genome)

# Write summary
summary_file = os.path.join(results_dir, 'summary.txt')
with open(summary_file, 'w') as f:
    f.write('Genome length: ' + str(len(genome)) + '\n')

print(f'Results saved to {summary_file}')
