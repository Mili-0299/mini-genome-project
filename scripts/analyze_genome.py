# analyze_genome.py
from pathlib import Path

def gc_content(seq):
    gc = seq.count('G') + seq.count('C')
    return round(gc / len(seq) * 100, 2)

data_file = Path("../data/sample_genome.fasta")
results_file = Path("../results/summary.txt")

with open(data_file) as f:
    lines = [line.strip() for line in f if line.strip()]

seqs = {}
for line in lines:
    if line.startswith(">"):
        header = line[1:]
        seqs[header] = ""
    else:
        seqs[header] += line

with open(results_file, "w") as out:
    for header, seq in seqs.items():
        out.write(f"Sequence: {header}\n")
        out.write(f"Length: {len(seq)}\n")
        out.write(f"GC content: {gc_content(seq)}%\n")
        out.write(f"A: {seq.count('A')} C: {seq.count('C')} G: {seq.count('G')} T: {seq.count('T')}\n")
        out.write("-"*30 + "\n")

print("Analysis complete! Check results/summary.txt")
