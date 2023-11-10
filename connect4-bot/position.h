#include <stdint.h>
#include <string>

#define WIDTH 7
#define HEIGHT 6

class Position{
private:
    /*
    Private variables for each Position object

    @var red_pos: Bit-string representing positions of red tokens
    @var yellow_pos: Bit-string representing positions of yellow tokens
    @var turn: 0 if red's turn in current position, 1 if yellow's turn
    */
    uint64_t red_pos;
    uint64_t yellow_pos;
    int turn;
public:
    /*
    Default constructor for Position
    Starts game with empty board on red's turn
    */
    Position();

    /*
    Constructor for Position with specific board configuration

    @param r: Represents where red tokens are on the board
    @param y: Represents where yellow tokens are on the board
    @param t: 0 if red's turn, 1 if yellow's turn
    */
    Position(uint64_t r, uint64_t y, int t);

    /*
    Checks if a column is playable

    @param col: index of column being checked
    @return true if column is not full, false otherwise
    */
    bool can_play(int col) const;

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

    /*
    Evaluates if playing the move at col results in
    the next player winning the game

    @param col: index of column of potential move
    @return true if playing at col would lose, false otherwise
    */
    bool losing_move(int col) const;

    /*
    Generates string representation of Connect 4 position

    @return the string representation of the position
    */
    std::string to_string() const;
};