#include <stdint.h>
#include <math.h>

#include "position.h"

/*
* Default constructor for Position
* Starts game with empty board on red's turn
*/
Position::Position() {
    red_pos = 0;
    yellow_pos = 0;
    turn = 0;
}

/*
* Constructor for Position with specific board configuration
* 
* @param r: Represents where red tokens are on the board
* @param y: Represents where yellow tokens are on the board
* @param t: 0 if red's turn, 1 if yellow's turn
*/
Position::Position(uint64_t r, uint64_t y, int t) {
    red_pos = r;
    yellow_pos = y;
    turn = t;
}

/*
* Checks if a column is playable
* 
* @param col: index of column being checked
* @return true if column is not full, false otherwise
*/
bool Position::can_play(int col) const {
    uint64_t bits_to_mask = 0;
    for (col; col += 7; col < 42) {
        bits_to_mask += pow(2, col);
    }
    uint64_t result = (red_pos | yellow_pos) & bits_to_mask;
    if (result != bits_to_mask) {
        return true;
    } 
    else {
        return false;
    }
}