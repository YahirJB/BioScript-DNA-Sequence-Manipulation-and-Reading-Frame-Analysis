from DNASeqLib import myfunctions

def extract_orfs(DNAstrand):    # Find the orfs patter in the strand
    orf_pattern = 
    orfs = orf_pattern.findall(DNAstrand)
    return orfs


def filter(orfs, min_length, max_length):   # filter for minimim and maximim squence len
    filtered_orfs =
    return filtered_orfs

def translate_orfs(orfs):   # translate the ORFs into amino acid sequences
    amino_acids = []
    for orf in orfs:

    return amino_acids

def display(orfs, amino_acids): # displays the results
    for i, (orf, amino_acid) in enumerate(zip(orfs, amino_acids), start=1):
        print(f"ORF {i}:")
        print(f"DNA Sequence: {orf}")
        print(f"Amino Acid Sequence: {amino_acid}\n")
