from manim import *

class BasicAnimations(Scene):
    def construct(self):
        circle = Circle()
        circle.set_fill(PINK, opacity=0.5)
        circle_label = Text("Círculo", font_size=24).next_to(circle, DOWN)

        self.play(Create(circle),Write(circle_label))
        self.wait(1)