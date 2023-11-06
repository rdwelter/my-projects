#include <stdint.h>

#define WIDTH 7
#define HEIGHT 6

class Position{
private:
    uint64_t board;
    int turn;
public:
    /*
    Checks if a column is playable

    @param col: index of column being checked
    @return true if column is not full, false otherwise
    */
    bool canPlay(int col) const;

    /*
    Plays a token for the current player

    @param col: index of column where player is placing token
    */
    void play(int col);

    /*
    Evaluates if playing the move at col wins

    @param col: index of column of potential move
    @return true if playing at col would win, false otherwise
    */
    bool winning_move(int col) const;
};