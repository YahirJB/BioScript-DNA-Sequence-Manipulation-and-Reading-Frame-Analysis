def validate(DNAstrand):
    s = len(DNAstrand)
    i = 0
    while i < s:
        if DNAstrand[i] != 'A' or DNAstrand != 'T' or DNAstrand != 'G' or DNAstrand != 'C':
            return "It's not a valid DNA Sequence"
        else:
            return "It is a valid DNA Sequence"
        
def reverse(DNAstrand):
    Reversed_Strand = DNAstrand[::-1]
    return Reversed_Strand

def Reverse_Complement(DNAstrand):
    Reversed_Strand = reverse(DNAstrand)
    s = len(Reversed_Strand)
    i = 0
    Rcomplement_Strand = ""
    while i < s:
        if(Reversed_Strand[i] == 'A'):
            Rcomplement_Strand += "T"
        if(Reversed_Strand[i] == 'T'):
            Rcomplement_Strand += "A"
        if(Reversed_Strand[i] == "C"):
            Rcomplement_Strand += "G"
        if(Reversed_Strand[i] == "G"):
            Rcomplement_Strand += "C"
        i+=1
    return Rcomplement_Strand

def complement(DNAstrand):
    s = len(DNAstrand)
    i = 0
    Complement_Strand = ""
    while i < s:
        if(DNAstrand[i] == 'A'):
            Complement_Strand += "T"
        if(DNAstrand[i] == 'T'):
            Complement_Strand += "A"
        if(DNAstrand[i] == "C"):
            Complement_Strand += "G"
        if(DNAstrand[i] == "G"):
            Complement_Strand += "C"
        i+=1
    return Complement_Strand

def translate(DNAstrand):
    RNA_Strand = DNAstrand.replace("T", "U",)
    return RNA_Strand

def change_frame(DNAstrand, offset):
    if offset != 0 and offset != 1 and offset != 2:     # checking offset value 
        raise ValueError("Offset must be 0,1, or 2")
    
    new_reading_frame = ""  # making empty string for the new strand
    for i in range(offset, len(DNAstrand), 3):  # starting from the offset value and going through the strand and adding a colon to end of each codon
        codon = DNAstrand[i:i+3]
        new_reading_frame += codon + '-'

    new_reading_frame = new_reading_frame.rstrip('-')   # getting rid of any trailing
    new_reading_frame = new_reading_frame.strip('-')    # getting rid of any leading

    return new_reading_frame


