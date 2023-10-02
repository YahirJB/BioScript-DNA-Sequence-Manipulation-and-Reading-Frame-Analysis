from DNASeqLib import myfunctions

rna_codon_table = {
    "UUU": "F", "UUC": "F", "UUA": "L", "UUG": "L",
    "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S",
    "UAU": "Y", "UAC": "Y", "UAA": "Stop", "UAG": "Stop",
    "UGU": "C", "UGC": "C", "UGA": "Stop", "UGG": "W",
    "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
    "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
    "CAU": "H", "CAC": "H", "CAA": "Q", "CAG": "Q",
    "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R",
    "AUU": "I", "AUC": "I", "AUA": "I", "AUG": "M",
    "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
    "AAU": "N", "AAC": "N", "AAA": "K", "AAG": "K",
    "AGU": "S", "AGC": "S", "AGA": "R", "AGG": "R",
    "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",
    "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
    "GAU": "D", "GAC": "D", "GAA": "E", "GAG": "E",
    "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G"
}

def extract_orfs(DNAstrand):    # Find the orfs patter in the strand
    s = len(DNAstrand)
    i = 0
    orfs = []
    while i < s:
        codon = DNAstrand[i:i+3]
        amino_acid = rna_codon_table.get(codon)
        if amino_acid == "M":
            start_index = i
            while i < s - 2:
                codon = DNAstrand[i:i+3]
                amino_acid = rna_codon_table.get(codon)
                if amino_acid == "Stop":
                    end_index = i + 2
                    orf_seq = DNAstrand[start_index:end_index + 1]
                    orfs.append(orf_seq)
                    break
                i += 3
        else:
            i += 3
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
