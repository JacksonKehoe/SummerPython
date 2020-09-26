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
    return (len(dna1)>len(dna2))



def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """
    count = 0
    for char in dna:
        if char in nucleotide:
            count = count + 1

    return count
    
    


def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """
    if dna2 in dna1:
        return True
    else:
        return False

def is_valid_sequence(dna):
    """ (str) -> bool

    Return False if a nucleotide in the DNA sequence is not 'A', 'T', 'C',
    and 'G' characters. Otherwise returns True.

    >>> is_valid_sequence('ATCGGC')
    True
    >>> is_valid_sequence('ATQCGGCB')
    False

    """

    valid = 0
    non_valid = 0

    for char in dna:
        if char not in 'ATCG':
            non_valid = non_valid + 1
        else:
            valid = valid + 1
    if non_valid == 0:
        return True
    else:
        return False

def insert_sequence(dna1, dna2, index):
    """ (str, str, int) -> str

    Returns the second strand of dna into the first dna sequence at the given
    index. 

    >>> insert_sequence('CCGG' , 'AT', 2)
        'CCATGG'
    >>> insert_sequence('ATCGCCTG', 'ATCG', 6)
        'ATCGCCATCGTG'
    >>> insert_sequence('ATCG', 'ATT', 0)
        'ATTATCG'
    >>> insert_sequence('ATCG', 'ATT', 4)
        'ATCGATT'
    """
    
    return dna1[:index] + dna2 + dna1[index:]

def get_complement(nuc):
    """ (str) -> str

    Returns the complement of the given nucleotide

    >>> get_complement('A')
        'T'
    >>> get_complement('T')
        'A'
    >>> get_complement('C')
        'G'
    >>> get_complement('G')
        'C'
    """

    if nuc == 'A':
        return 'T'
    elif nuc == 'T':
        return 'A'

    if nuc =='C':
        return 'G'
    elif nuc == 'G':
        return 'C'
    
def get_complementary_sequence(dna):
    """ (str) -> str

    Returns the complementary dna sequence of a given strand

    >>> get_complementary_sequence('ATCG')
    'TAGC'
    >>> get_complementary_sequence('AATTCCGG')
    'TTAAGGCC'
    """

    comp_seq = ''
    for nuc in dna:
        comp_seq = comp_seq + get_complement(nuc)
    return comp_seq
        
    



   
