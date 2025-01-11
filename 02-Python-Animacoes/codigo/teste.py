from manim import *

class Teste(Scene):
    def construct(self):
        s = Square()

        self.play(Create(s))
        self.wait(2)