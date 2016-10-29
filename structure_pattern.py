def check_structure(pattern, structure, pattern_level=2):
        return bin(pattern)[2:].zfill(len(structure)) == ''.join('0' if i.isdigit() else '1' for i in structure)
