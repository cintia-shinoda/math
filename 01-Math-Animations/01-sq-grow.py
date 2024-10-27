from manim import *

class SquareGrowing(Scene):
    def construct(self):
        square = Square(color=BLUE)  # Creates a blue square
        square.rotate(-3 * TAU / 8)  # Rotates the square by 3/8 of a full turn -3/8 * 2*PI

        self.play(GrowFromCenter(square))