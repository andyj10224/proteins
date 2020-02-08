#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 19:35:02 2020

@author: andyjiang
"""

from rdkit import Chem
from rdkit.Chem import AllChem

peptideFile = open("peptideFile.mol", "w")


"""

ala = 'N[C@@H](C)C(=O)O'
ala2 = '[NH3+][C@@H](C)C(=O)[O-]' 
test = '[' + ala[0:1] + 'H3+]' + ala[1:len(ala)-1] + '[' + ala[len(ala)-1:len(ala)] + '-]'
gly = 'N[C@@H]C(=O)O'

"""

peptides = {
        
        'alanine' : 'N[C@@H](C)C(=O)O',
        'glycine' : 'NCC(=O)O',
        'aspartic acid' : 'N[C@@H](CC(=O)[O-])C(=O)O',
        'glutamic acid' : 'N[C@@H](CCC(=O)[O-])C(=O)O',
        'lysine' : 'N[C@@H](CCCC[NH3+])C(=O)O',
        'arginine' : 'N[C@@H](CCCNC(=[NH2+])N)C(=O)O',
        'histidine' : 'N[C@@H](CC1NC=NC1=)C(=O)O',
        'valine' : 'N[C@@H](C(C)C)C(=O)O',
        'isoleucine' : 'N[C@@H](C(CC)C)C(=O)O',
        'serine' : 'N[C@@H](CO)C(=O)O',
        'threonine' : 'N[C@@H](C(O)C)C(=O)O',
        'tyrosine' : 'N[C@@H](Cc1ccc(O)cc1)C(=O)O',
        'asparagine' : 'N[C@@H](CC(=O)N)C(=O)O',
        'glutamine' : 'N[C@@H](CCC(=O)N)C(=O)O',
        'tryptophan' : 'N[C@@H](CC1=CNc2ccccc21)C(=O)O',
        'phenylalanine' : 'N[C@@H](Cc1ccccc1)C(=O)O',
        'proline' : 'N1[C@@H](CCC1)C(=O)O',
        'methionine' : 'N[C@@H](CCSC)C(=O)O',
        'leucine' : 'N[C@@H](CC(C)C)C(=O)O',
        'cysteine' : 'N[C@@H](CS)C(=O)O',
        
        
        }





mol = Chem.MolFromSmiles(peptides['proline'])

mol = Chem.AddHs(mol)

#AllChem.EmbedMolecule(mol)
#AllChem.MMFFOptimizeMolecule(mol)

molBlock = Chem.MolToMolBlock(mol)

peptideFile.write(molBlock)

peptideFile.close()

"""

peptideFile = open("peptideFile.mol", "r")

pepLines = peptideFile.readlines()

print(pepLines[4][0:33].split())

peptideFile.close()

"""