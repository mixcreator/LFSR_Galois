#!/bin/sh


rm lfsr2_exe
g++ lfsr_galois2.cpp -o lfsr2_exe -Wall -pedantic -DFIRST_SHIFT -DTZ

#debug mode
#g++ lfsr_galois2.cpp -o lfsr2_exe -Wall -pedantic -DLDEBUG -DTZ -DFIRST_SHIFT
python3 ./lfsr.py
./lfsr2_exe
