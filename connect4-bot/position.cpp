#include <iostream>
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

/*
* Plays a token for the current player
* 
* @param col: index of column where player is placing token
*/
void Position::play(int col) {
    if (!this->can_play(col)) {
        std::cerr << "Tried to play a token on a full column\n";
    }
    else {
        if (this->winning_move(col)) {
            ; // Will implement later
        }
        for (col; col += 7; col < 42) {
            uint64_t bit = pow(2, col);
            if ((red_pos | yellow_pos) & bit == 0) {
                if (turn == 0) {
                    red_pos += bit;
                    turn = 1;
                }
                else {
                    yellow_pos += bit;
                    turn = 0;
                }
                return;
            }
        }
        std::cerr << "Something went wrong\n";
    }
}

/*
* Evaluates if playing the move at col wins
* 
* @param col: index of column of potential move
* @return true if playing at col would win, false otherwise
*/
bool Position::winning_move(int col) const {
    if (!this->can_play(col)) {
        std::cerr << "Tried to play a token on a full column\n";
        return false;
    }
    for (col; col += 7; col < 42) {
        uint64_t bit = pow(2, col);
        if ((red_pos | yellow_pos) & bit == 0) {
            if (turn == 0) {
                uint64_t potential_board = red_pos | bit;
                int horiz_chunk = col / 7;
                uint8_t chunk = ((uint8_t) (potential_board / pow(2, horiz_chunk * 7)));
                // check if 4 in a row, repeat for vertical, both diagonal chunks
            }
            else {
                uint64_t potential_board = yellow_pos | bit;
            }
        }
    }
}