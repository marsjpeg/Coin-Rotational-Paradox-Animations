from manim import *
import numpy as np

class MovingCircle(Scene):
    def construct(self):
        large_circle = Circle(radius=3)
        large_circle.set_color(DARK_BLUE)
        large_circle.set_fill(DARK_BLUE, opacity=0.5)
        
        small_circle = Circle(radius=1)
        small_circle.set_fill(WHITE, opacity=0.2)
        small_circle.set_color(WHITE)
        
        # Position the small circle to start on large circle
        small_circle.move_to(large_circle.point_at_angle(0) + 0.9)

        radius_line = Line(small_circle.get_center(), small_circle.get_center() - RIGHT)
        radius_line.set_color(PINK)

        # Updater to move small circle around large circle
        def update_small_circle(mob, dt):
            mob.rotate_about_origin(dt * 2 * PI / 5) 

        def update_radius_line(line):
            center = small_circle.get_center()
            angle = np.angle(complex(center[0], center[1])) * 4
            line.put_start_and_end_on(center, center - small_circle.radius * np.array([np.cos(angle), np.sin(angle), 0]))
            
            
        # Add the updater to the small circle
        small_circle.add_updater(update_small_circle)
        radius_line.add_updater(update_radius_line)
        
        self.add(large_circle, small_circle, radius_line)
        
        self.wait(30) 
    