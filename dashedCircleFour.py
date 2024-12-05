from manim import *
import numpy as np

class MovingCircleWithDash(Scene):
    def construct(self):
        # Define large and small circles
        large_circle = Circle(radius=3)
        large_circle.set_color(DARK_BLUE)
        large_circle.set_fill(DARK_BLUE, opacity=0.5)
        
        small_circle = Circle(radius=1)
        small_circle.set_fill(WHITE, opacity=0.2)
        small_circle.set_color(WHITE)
        
        circle = Circle(radius=4)
        circle.set_color(WHITE)
        
        # Dashed version of the circle
        dotted_circle = DashedVMobject(circle, 50, 0.1)
        
        small_circle.move_to(large_circle.point_at_angle(0) + 0.9)

        radius_line = Line(small_circle.get_center(), small_circle.get_center() - RIGHT)
        radius_line.set_color(PINK)

        # Create an updater to move the small circle around the large circle
        def update_small_circle(mob, dt):
            mob.rotate_about_origin(dt * 2 * PI / 5)

        def update_radius_line(line):
            center = small_circle.get_center()
            angle = np.angle(complex(center[0], center[1])) * 4
            line.put_start_and_end_on(center, center - small_circle.radius * np.array([np.cos(angle), np.sin(angle), 0]))
            
            
        small_circle.add_updater(update_small_circle)
        radius_line.add_updater(update_radius_line)
        
        # Add circles to the scene
        self.add(large_circle, small_circle, radius_line, dotted_circle)
        
        self.wait(30)  