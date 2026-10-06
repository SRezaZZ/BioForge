# BioForge

A DNA sequence analysis pipeline written in Python.

The program reads a FASTA file, validates sequences, detects ORFs, translates them, applies filters, and generates a final report.

---

## How to Run

```bash
python main.py --input input/input.fasta.txt --out output/ --min-length 2
```

Three arguments are required:

| Argument | Description |
|---|---|
| `--input` | Path to the input FASTA file |
| `--out` | Path to the output directory |
| `--min-length` | Minimum protein length for filtering |

Outputs:
- `output/report.txt` — report of final ORFs
- `output/bioforge.log` — execution log

---

## Project Structure

```
BioForge-main/
├── main.py
├── parser.py
├── exceptions.py
├── data/
│   ├── amino_weights.txt
│   └── codon_table.txt
├── input/
│   └── input.fasta.txt
├── dna_operations/
│   └── DNASequence.py
├── orf_dir/
│   ├── orf_class.py
│   ├── orf_maker.py
│   └── translator.py
├── Filter/
│   └── filters.py
└── output/
    ├── annotation.py
    ├── log.py
    └── report.py
```

---

## Pipeline

FASTA → Parsing → Validation → ORF Detection → Translation → Filtering → Annotation → Report → Log

---

## Design Decisions

### 1. Why is `DnaSequence` a Class?

It holds both data (the DNA sequence) and behavior (complement, reverse_complement, dna_to_rna, gc_content, etc.).
If it were just a function, the sequence would have to be passed to every function separately. Now the sequence is stored in one place and the methods use it.

### 2. Why is `ORF` a Class?

Each ORF has several pieces of information that belong together: codons, protein, strand, frame, start position, and completeness.
Keeping them in a class is much cleaner than having them scattered around.

### 3. Why is `parser` a Function?

The `load_fasta` function only does one thing: reads a file and returns a dictionary of records.
It doesn't keep any state between calls, so a Function is enough.

### 4. Where is Inheritance used?

In `Filter/filters.py`:
- `LengthFilter` and `WeightFilter` inherit from `Filter`.
- All of them share a common method called `matches`.

In `exceptions.py` as well:
- `FastaFormatError`, `InvalidSequenceError`, and `DataFileError` inherit from `BioForgeError`.

### 5. Where is Polymorphism used?

In `apply_filters`:

```python
for current_filter in filters:
    filtered_orfs = [orf for orf in filtered_orfs if current_filter.matches(orf)]
```

This function doesn't know what class `current_filter` belongs to; it just calls `matches`.
Each filter has its own implementation but looks the same from the outside.

### 6. Where is Composition used?

In `main.py`, we use `logger` and `reporter` without inheriting from them.
This means `main` **has** a logger and a reporter (has-a).

`orf_maker_construction` also creates an `ORF` object and uses it — this is another example of Composition.

### 7. Why is `load_amino_weights` a Function?

Because it only reads a file and returns a dictionary of weights. It has no state.
However, the filters are Classes because they have min and max values.

### 8. Why is `orf_maker` a Function?

`orf_maker_construction` and `orf_maker_inputs` are both stateless.
They take input and return output; they don't store any data between calls.
So there was no need for a Class.

---

## Exceptions

| Exception | Purpose |
|---|---|
| `BioForgeError` | Base class for all project errors |
| `FastaFormatError` | FASTA structure errors |
| `InvalidSequenceError` | Invalid DNA sequence |
| `DataFileError` | Errors in data files |

---

## Sample Output

`output/report.txt`:

```
============================================================
BioForge Report
============================================================
ID:        BFG_001
Strand:    forward
Frame:     0
Start Pos: 0
Protein:   MLS
Complete:  True
------------------------------------------------------------
ID:        BFG_002
Strand:    forward
Frame:     0
Start Pos: 3
Protein:   MG
Complete:  True
------------------------------------------------------------
ID:        BFG_003
Strand:    reverse_complement
Frame:     2
Start Pos: 9
Protein:   MKA
Complete:  False
------------------------------------------------------------
Total ORFs: 3
```

`output/bioforge.log`:

```
2026-10-06 ... - BioForge pipeline started
2026-10-06 ... - Total ORFs found: 4
2026-10-06 ... - Amino weights loaded: 20 entries
2026-10-06 ... - After filters: 3
2026-10-06 ... - Report written to output\report.txt
2026-10-06 ... - BioForge pipeline finished
```

---

Good luck :)