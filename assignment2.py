def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """
    return len(dna)

def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """
    return len(dna1) > len(dna2)


def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """
    num_nucleotides = 0
    for char in dna:
        if char == nucleotide:
            num_nucleotides = num_nucleotides + 1
        
    return num_nucleotides



def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False
    """
    return dna2 in dna1
    

def is_valid_sequence(sequence):
    """ (str) -> bool

    Return True if and only if the DNA sequence is valid

    >>> is_valid_sequence('ATCGGC')
    True
    >>> is_valid_sequence('ATCBGC')
    False
    >>> is_valid_sequence('DATCGGC')
    False
    >>> is_valid_sequence('AAAAAA')
    True
    """
    
    sequence_valid = True
    for char in sequence:
        if char not in 'ATCG':
            sequence_valid = False
            

    
    return sequence_valid

    

def insert_sequence(seq1, seq2, index):
    """ (str, str, int) -> str

    Return the DNA sequence obtained by inserting
    the second DNA sequence into the first DNA sequence
    at the given index.

    >>> insert_sequence('CCGG', 'AT', 2)
    'CCATGG'
    >>> insert_sequence('CTTGG', 'A', 0)
    'ACTTGG'
    >>> insert_sequence('CTT', 'AGG', 3)
    'CTTAGG'
    """

    seq1 = seq1[:index] + seq2 + seq1[index:]

    return seq1    



def get_complement(nucleotide):
    """ (str) -> str

    Return the nucleotide's complement.

    >>> get_complement('A')
    'T'
    >>> get_complement('T')
    'A'
    >>> get_complement('C')
    'G'
    >>> get_complement('G')
    'C'
    """

    if nucleotide == 'A':
        return 'T'
    elif nucleotide == 'T':
        return 'A'
    elif nucleotide == 'C':
        return 'G'
    else:
        return 'C'
    

  
def get_complementary_sequence(sequence):

    """ (str) -> str

    Return the DNA sequence that is complementary
    to the given DNA sequence.

    >>> get_complementary_sequence('ACGTTA')
    'TGCAAT'
    >>> get_complementary_sequence('TGGCCA')
    'ACCGGT'
    >>> get_complementary_sequence('CCATTG')
    'GGTAAC'
    """
    complementary_sequence = ''

    for char in sequence:
         complementary_sequence = complementary_sequence + get_complement(char)

    return complementary_sequence















    
