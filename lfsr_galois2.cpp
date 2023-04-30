#include <stdint.h>
#include <stdio.h>
#include <bitset>
#include <iostream>

//#define FIRST_SHIFT 1

#define MASK42   0x3FFFFFFFFFF

#define COUNT           100
#define CHECK_MSB_BIT   41

//#define LDEBUG           1    

#define NSHIFT          663124934834


#define TZ

#ifdef TZ

// From: TZ 
#define TOGGLE_MASK      0x3DC83D9C541   // 111101110010000011110110011100010101000001
#define TOGGLE_MASK_REV  0x20A8E6F04EF   // 100000101010001110011011110000010011101111


#define TOGGLE_MASK_REV  0xA8E6F04EF     // 101010001110011011110000010011101111

#else
// From: http://www.cdg.org/technology/cdma_technology/a_ross/LongCode.asp 
#define TOGGLE_MASK      ((uint64_t)0x3B907B38A81) //111011100100000111101100111000101010000001
#define TOGGLE_MASK_REV  ((uint64_t)0x20547378277) //100000010101000111001101111000001001110111

#endif

void HexToBin(char* hexdec);

uint64_t LFSR_Galois(void)
{
    uint64_t start_state;
    // start_state = 0x20000000000;         // Shift 0
    start_state = 0xA8E6F04EF;           // Shift 1
    uint64_t lfsr = start_state;
    unsigned period = 2;

    do
    {
        unsigned msb = lfsr >> CHECK_MSB_BIT;

        printf("%5d) msb=%d l=%12llX ", period, msb, lfsr);

#ifdef FIRST_SHIFT
        lfsr = (lfsr << 1) & MASK42;
        printf("shl=%12llX ", lfsr);
#endif 
        if (msb) {                           
#ifdef FIRST_SHIFT
            lfsr = (lfsr ^ TOGGLE_MASK_REV) & MASK42 | 0x1;
            printf("xsl=%12llX ", lfsr);
#else
            lfsr = (lfsr ^ TOGGLE_MASK_REV) & MASK42;
            printf("xsl=%12llX ", lfsr);
            lfsr = (lfsr << 1);
            printf("shl=%12llX ", lfsr);
#endif

        }else {
#ifndef FIRST_SHIFT
            lfsr = (lfsr << 1);
            printf("shl=%12llX ", lfsr);
#endif
        }

        ++period;

        char hexdec[64];
        sprintf(hexdec, "%llX", lfsr);
        HexToBin(hexdec);
        printf("\n");
    }
    while(period < COUNT );

    return lfsr;
}

uint64_t LFSR_Galois2(uint64_t shift)
{
    uint64_t start_state = 0xA8E6F04EF;
    uint64_t lfsr = start_state;

    int i = 2;
    
    if(shift == 1)
        return lfsr;

    while(i <= shift )
    {
        unsigned msb = lfsr >> CHECK_MSB_BIT;
#ifdef LDEBUG
        printf("%5d) msb=%d l=%12llX ", i, msb, lfsr);
#endif

#ifdef FIRST_SHIFT
        lfsr = (lfsr << 1) & MASK42;

#ifdef LDEBUG
        printf("shl=%12llX ", lfsr);
#endif 

#endif 
        if (msb) {                           
#ifdef FIRST_SHIFT
            lfsr = (lfsr ^ TOGGLE_MASK_REV) & MASK42 | 0x1;

#ifdef LDEBUG
            printf("xsl=%12llX ", lfsr);
#endif

#else
            lfsr = (lfsr ^ TOGGLE_MASK_REV) & MASK42;
            printf("xsl=%12llX ", lfsr);
            lfsr = (lfsr << 1);
            printf("shl=%12llX ", lfsr);
#endif

        }else {
#ifndef FIRST_SHIFT
            lfsr = (lfsr << 1);
            printf("shl=%12llX ", lfsr);
#endif
        }

        //++period;
#ifdef LDEBUG
        char hexdec[64];
        sprintf(hexdec, "%llX", lfsr);
        HexToBin(hexdec);
        printf("\n");
#endif

        i++;
    }
    

    return lfsr;
}


void HexToBin(char* hexdec)
{
 
    long int i = 0;
 
    while (hexdec[i]) {
 
        switch (hexdec[i]) {
        case '0':
            printf("0000");
            break;
        case '1':
            printf("0001");
            break;
        case '2':
            printf("0010");
            break;
        case '3':
            printf("0011");
            break;
        case '4':
            printf("0100");
            break;
        case '5':
            printf("0101");
            break;
        case '6':
            printf("0110");
            break;
        case '7':
            printf("0111");
            break;
        case '8':
            printf("1000");
            break;
        case '9':
            printf("1001");
            break;
        case 'A':
        case 'a':
            printf("1010");
            break;
        case 'B':
        case 'b':
            printf("1011");
            break;
        case 'C':
        case 'c':
            printf("1100");
            break;
        case 'D':
        case 'd':
            printf("1101");
            break;
        case 'E':
        case 'e':
            printf("1110");
            break;
        case 'F':
        case 'f':
            printf("1111");
            break;
        default:
            printf("\nInvalid hexadecimal digit %c",
                   hexdec[i]);
        }
        i++;
    }
}

unsigned Polinomial[42] = {1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1,
                           1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1};
uint64_t create_mask()
{
    uint64_t mask = 0;
    for(int i=0; i < 42; i++)
    {
        char hexdec[64];
        uint64_t sb = (uint64_t)((uint64_t)(Polinomial[i]) << i);
        mask = (mask |  sb) & MASK42;
    }
    return mask;
}

int main()
{
    /*
    printf("-#######################################################\n");
    uint64_t mm = create_mask();
    printf("%llX\n", mm);         
    // mask =     20A8E6F04EF
    //            20000000000
    //              A8E6F04EF
    // rev_mask
    //printf("%llX\n", 0x);
    printf("-#######################################################\n");
    */
#if 1
    uint64_t res = LFSR_Galois2(NSHIFT);
    char hexdec[64];
    printf("Shift %lld:\t%llX\t", NSHIFT, res);
    sprintf(hexdec, "%llX", res);
    HexToBin(hexdec);
    printf("\n");
#endif
   
    return 0;
}