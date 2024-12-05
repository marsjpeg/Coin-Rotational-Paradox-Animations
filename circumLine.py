from manim import *

class RollingCircleOnLine1(Scene):
    def construct(self):
        line = Line(start=3 * LEFT, end=3 * RIGHT)
        line.set_color(WHITE)
        
        # Defining circle and line
        rolling_circle = Circle(radius=1)
        rolling_circle.set_color(DARK_BLUE)
        rolling_circle.set_fill(DARK_BLUE, opacity=0.5)
        radius_line = Line(rolling_circle.get_center(), rolling_circle.get_center() + DOWN)
        radius_line.set_color(PINK)

        rolling_circle_with_radius = VGroup(rolling_circle, radius_line)

        rolling_circle_with_radius.move_to(line.get_start() + UP * rolling_circle.radius)

        position_tracker = ValueTracker(0)

        # Updater for the circle's rolling 
        def update_circle(mob):
            pos = position_tracker.get_value()
            new_center = line.point_from_proportion(pos) + UP * rolling_circle.radius

            mob.move_to(new_center)
            # Rotate the circle and the radius line to simulate rolling
            mob.rotate(-2 * PI * pos / 90, about_point=new_center)

        rolling_circle_with_radius.add_updater(update_circle)

        # Add the line and the rolling circle and animate
        self.add(line, rolling_circle_with_radius)
        self.play(position_tracker.animate.set_value(1), run_time=3, rate_func=linear)

        # Kinda finicky btw, it does NOT wait 10 ms or s (just how Manim is I guess?)
        self.wait(10)


