# -*- coding: utf-8 -*-

from __future__ import print_function
import re, sys, time

from Solver import *
from utils import *




# Python 2 compatability
if sys.version_info[0] == 2:
    input = raw_input





def render(i):
    rank, fil = divmod(i - A0, 16)
    return chr(fil + ord('a')) + str(-rank)

def print_pos(pos):
    print()
    uni_pieces = {'R':'车', 'N':'马', 'B':'相', 'A':'仕', 'K':'帅', 'P':'兵', 'C':'炮',
                  'r':'俥', 'n':'傌', 'b':'象', 'a':'士', 'k':'将', 'p':'卒', 'c':'砲', '.':'．'}
    for i, row in enumerate(pos.board.split()):
        print(' ', 9-i, ''.join(uni_pieces.get(p, p) for p in row))
    print('    ａｂｃｄｅｆｇｈｉ\n\n')

def main(mode):
    hist = [Position(initial, 0, mode)]
    
    # AI first 
    if mode == 's':
        move_maker = Searcher()
    elif mode == 'a':
        move_maker = AlphaZero()
    else:
        raise ValueError('mode must be s or a')
    first_move = True
    while True:
        # Fire up the engine to look for a move.
        start = time.time()
        # find a new move. 
        if mode == 's':
            for _depth, move, score in move_maker.search(hist[-1], hist):
                if time.time() - start > THINK_TIME:
                    break

            if score == MATE_UPPER:
                print("Checkmate!")

            # The black player moves from a rotated position, so we have to
            # 'back rotate' the move before printing it.
            print("Think depth: {} My move: {}".format(_depth, render(255-move[0] - 1) + render(255-move[1]-1)))
            hist_move = move
            hist.append(hist[-1].move(hist_move))

        elif mode == 'a':
            #here, we need a convert function to convert the hist[-1] to tensorflow model input.
            if first_move:
                his_move = AlphaZero.transform_move(move_maker.first_move)
                first_move = False
            else:
                move = move_maker.search()
                his_move = AlphaZero.transform_move(move)
            hist.append(hist[-1].move(his_move))
        else:
            raise ValueError('mode must be s or a')


        print_pos(hist[-1])

        if hist[-1].score <= -MATE_LOWER:
            print("You lost")
            break

        # We query the user until she enters a (pseudo) legal move.
        hist_move = None
        while hist_move not in hist[-1].gen_moves():
            match = re.match('([a-i][0-9])'*2, input('Your move: '))
            if match:
                if mode == 's':
                    move = Searcher.parse(match.group(1)), Searcher.parse(match.group(2))
                    hist_move = move 
                    # move is a tuple of number
                elif mode == 'a':
                    move = AlphaZero.parse(match.group(1), match.group(2))
                    # move is a tuple of tuple.
                    hist_move = AlphaZero.transform_move(move)
                    move_maker.move(move)
                    
                else:
                    raise ValueError('mode must be s or a')
            else:
                # Inform the user when invalid input (e.g. "help") is entered
                print("Please enter a move like h2e2")
        hist.append(hist[-1].move(hist_move))

        # After our move we rotate the board and print it again.
        # This allows us to see the effect of our move.
        print_pos(hist[-1].rotate())

        if hist[-1].score <= -MATE_LOWER:
            print("You won")
            break



if __name__ == '__main__':
    args = sys.argv[1:]
    mode = args[0] if args else 's'
    main(mode)
