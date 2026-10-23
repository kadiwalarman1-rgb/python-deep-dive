#!/usr/bin/env python3
"""Lab 44: Projectile motion and 1D elastic collision simulations."""

from vector_class import Vector


class PhysicsObject:
    def __init__(self, position, velocity, mass=1.0):
        """Initialize a physics object with position, velocity, and mass."""
        if not isinstance(position, Vector) or not isinstance(velocity, Vector):
            raise TypeError("Position and velocity must be Vector objects.")
        if isinstance(mass, bool) or not isinstance(mass, (int, float)) or mass <= 0:
            raise ValueError("Mass must be a positive number.")
        self.position = position
        self.velocity = velocity
        self.mass = float(mass)
        self.forces = Vector(0, 0)

    def apply_force(self, force):
        """Apply a force to the object."""
        if not isinstance(force, Vector):
            raise TypeError("Force must be a Vector object.")
        self.forces = self.forces + force

    def update(self, dt):
        """Update velocity and position using semi-implicit Euler integration."""
        if isinstance(dt, bool) or not isinstance(dt, (int, float)) or dt <= 0:
            raise ValueError("Time step must be a positive number.")
        acceleration = self.forces / self.mass
        self.velocity = self.velocity + acceleration * dt
        self.position = self.position + self.velocity * dt
        self.forces = Vector(0, 0)

    def __str__(self):
        return (
            f"Object(pos={self.position}, "
            f"vel={self.velocity}, mass={self.mass})"
        )


def simulate_projectile():
    """Simulate projectile motion under gravity."""
    print("=== Projectile Motion Simulation ===")
    projectile = PhysicsObject(Vector(0, 0), Vector(10, 15), mass=1.0)
    gravity = Vector(0, -9.81)
    dt = 0.1
    time = 0.0
    next_report = 0.5

    print(f"Initial state: {projectile}")
    print(f"Gravity: {gravity}")
    print(f"Time step: {dt:.1f}s")
    print()

    while projectile.position.y >= 0:
        previous_position = projectile.position
        previous_time = time

        projectile.apply_force(gravity * projectile.mass)
        projectile.update(dt)
        time += dt

        landed = False
        if projectile.position.y < 0:
            current_position = projectile.position
            denominator = previous_position.y - current_position.y
            fraction = previous_position.y / denominator if denominator else 1.0
            landing_x = previous_position.x + (
                current_position.x - previous_position.x
            ) * fraction
            projectile.position = Vector(landing_x, 0)
            time = previous_time + dt * fraction
            landed = True

        if time + 1e-9 >= next_report:
            print(
                f"t={time:.2f}s: pos=({projectile.position.x:.2f}, "
                f"{projectile.position.y:.2f}), "
                f"vel=({projectile.velocity.x:.2f}, "
                f"{projectile.velocity.y:.2f})"
            )
            next_report += 0.5

        if landed:
            break

    print(f"\nProjectile landed at t={time:.2f}s")
    print(f"Final position: {projectile.position}")
    print(f"Range: {projectile.position.x:.2f} meters")


def simulate_collision():
    """Simulate a one-dimensional elastic collision and check momentum."""
    print("\n=== Elastic Collision Simulation ===")
    obj1 = PhysicsObject(Vector(0, 0), Vector(5, 0), mass=2.0)
    obj2 = PhysicsObject(Vector(10, 0), Vector(-3, 0), mass=1.0)

    print("Before collision:")
    print(f"Object 1: {obj1}")
    print(f"Object 2: {obj2}")

    momentum_before = obj1.velocity * obj1.mass + obj2.velocity * obj2.mass
    print(f"Total momentum before: {momentum_before}")

    m1, m2 = obj1.mass, obj2.mass
    u1, u2 = obj1.velocity.x, obj2.velocity.x
    v1 = ((m1 - m2) * u1 + 2 * m2 * u2) / (m1 + m2)
    v2 = ((m2 - m1) * u2 + 2 * m1 * u1) / (m1 + m2)

    obj1.velocity = Vector(v1, 0)
    obj2.velocity = Vector(v2, 0)

    print("\nAfter collision:")
    print(f"Object 1: {obj1}")
    print(f"Object 2: {obj2}")

    momentum_after = obj1.velocity * obj1.mass + obj2.velocity * obj2.mass
    print(f"Total momentum after: {momentum_after}")

    # Vector.__sub__ and Vector.__abs__ are implemented in vector_class.py.
    momentum_difference = abs(momentum_before - momentum_after)
    print(f"Momentum conserved: {momentum_difference < 0.001}")


if __name__ == "__main__":
    simulate_projectile()
    simulate_collision()
