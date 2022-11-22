#!/usr/bin/env bash

# take 3 inputs: receptor (.pdb), ligand (.sdf), config (.txt), all in the same directory
RECEPTOR=${1?Error: no receptor given}

LIGAND=${2?Error: no ligand given}

CONFIG=${3?Error: no configfile given}

RNAME=${RECEPTOR%.*}
LNAME=${LIGAND%.*}
echo $RNAME
echo $LNAME

# convert protein receptor from .pdb to .pdbqt
obabel ${RNAME}.pdb -xr -O ${RNAME}.pdbqt

# convert ligand from .sdf to .pdbqt 
mk_prepare_ligand.py -i ${LNAME}.sdf -o ${LNAME}.pdbqt

# run docking (ligand_out.pdbqt is auto-generated)
vina --receptor ${RNAME}.pdbqt --ligand ${LNAME}.pdbqt --config $CONFIG --log ${RNAME}_${LNAME}_log.txt
