
from vpython import * # Python library used to create 3D objects and animations
import math
import random

# ==========================================================
# 3D SOLAR SYSTEM - LIVE INTERACTIVE EDITION
# ==========================================================

# -------------------- SCENE -------------------------------

# canvas() for creates the 3D scene
scene = canvas(
    title="<b>✦ SOLAR SYSTEM</b> | Interactive 3D Universe",
    width=1600,
    height=850,
    background=vector(0.003, 0.004, 0.018),
    resizable=True,
    align="none"
)

scene.center = vector(0, 0, 0)
scene.range = 38
scene.autoscale = False
scene.forward = vector(-1, -0.35, -1)
scene.up = vector(0, 1, 0)
scene.userspin = True
scene.userzoom = True

# -------------------- LIGHTING ----------------------------

scene.lights = []

distant_light(
    direction=vector(1, -1, 1),
    color=vector(0.35, 0.35, 0.4)
)

local_light(
    pos=vector(0, 0, 0),
    color=vector(1, 0.85, 0.65)
)

# -------------------- STARFIELD ---------------------------

random.seed(12)

star_positions = []

for i in range(550):
    x = random.uniform(-90, 90)
    y = random.uniform(-65, 65)
    z = random.uniform(-90, 90)

    # Keep the stars away from the central solar system
    if math.sqrt(x*x + y*y + z*z) > 48:
        star_positions.append(vector(x, y, z))

stars = points(
    pos=star_positions,
    color=vector(0.85, 0.88, 1),
    size=vector(0.7, 0.7, 0.7)
)

# -------------------- SUN ---------------------------------

# sphere() for creates a 3D sphere
sun_glow_outer = sphere(
    pos=vector(0, 0, 0),
    radius=2.6,
    color=vector(1, 0.25, 0.02),
    opacity=0.07,
    emissive=True
)

sun_glow_inner = sphere(
    pos=vector(0, 0, 0),
    radius=2.1,
    color=vector(1, 0.55, 0.05),
    opacity=0.13,
    emissive=True
)

sun = sphere(
    pos=vector(0, 0, 0),
    radius=1.65,
    color=vector(1, 0.76, 0.12),
    emissive=True
)

sun_label = label(
    pos=vector(0, 2.5, 0),
    text="SUN",
    height=16,
    color=vector(1, 0.85, 0.2),
    box=False,
    line=False
)

# -------------------- PLANET DATA -------------------------

# Planet sizes, distances and speeds are visually scaled.
# They are NOT to astronomical scale.

planet_data = [
    {
        "name": "Mercury",
        "distance": 4.5,
        "radius": 0.28,
        "color": vector(0.65, 0.62, 0.58),
        "speed": 1.6,
        "rotation": 1.2
    },
    {
        "name": "Venus",
        "distance": 6.5,
        "radius": 0.48,
        "color": vector(0.95, 0.65, 0.3),
        "speed": 1.2,
        "rotation": 0.8
    },
    {
        "name": "Earth",
        "distance": 9,
        "radius": 0.55,
        "color": vector(0.15, 0.45, 1),
        "speed": 0.95,
        "rotation": 2.0
    },
    {
        "name": "Mars",
        "distance": 11.5,
        "radius": 0.4,
        "color": vector(0.95, 0.25, 0.12),
        "speed": 0.75,
        "rotation": 1.7
    },
    {
        "name": "Jupiter",
        "distance": 15.5,
        "radius": 1.15,
        "color": vector(0.85, 0.62, 0.42),
        "speed": 0.45,
        "rotation": 2.5
    },
    {
        "name": "Saturn",
        "distance": 20,
        "radius": 0.95,
        "color": vector(0.85, 0.77, 0.55),
        "speed": 0.32,
        "rotation": 2.2
    },
    {
        "name": "Uranus",
        "distance": 24,
        "radius": 0.72,
        "color": vector(0.35, 0.85, 0.9),
        "speed": 0.22,
        "rotation": 1.8
    },
    {
        "name": "Neptune",
        "distance": 28,
        "radius": 0.7,
        "color": vector(0.2, 0.3, 1),
        "speed": 0.16,
        "rotation": 1.5
    }
]

planets = []

# -------------------- CREATE PLANETS ----------------------

for data in planet_data:

    distance = data["distance"]

    # Orbit path
    orbit_points = []

    for i in range(181):
        angle = 2 * math.pi * i / 180

        orbit_points.append(
            vector(
                distance * math.cos(angle),
                0,
                distance * math.sin(angle)
            )
        )
    # curve() for Draws lines and orbital paths
    curve(
        pos=orbit_points,
        color=vector(0.12, 0.18, 0.32),
        radius=0.012
    )

    # Initial planet position
    initial_angle = random.uniform(0, 2 * math.pi)

    initial_position = vector(
        distance * math.cos(initial_angle),
        0,
        distance * math.sin(initial_angle)
    )

    # Planet
    planet = sphere(
        pos=initial_position,
        radius=data["radius"],
        color=data["color"],
        shininess=0.8
    )

    # Planet label
    #label() for displays text in the 3D scene
    planet_label = label(
        pos=initial_position,
        text=data["name"],
        height=12,
        color=vector(0.85, 0.9, 1),
        box=False,
        line=False
    )

    # Saturn's rings
    saturn_ring = None

    if data["name"] == "Saturn":

    # ring() for creates a ring-shaped object
        saturn_ring = ring(
            pos=initial_position,
            axis=vector(0, 1, 0),
            radius=1.55,
            thickness=0.28,
            color=vector(0.85, 0.72, 0.5),
            opacity=0.8
        )

    planets.append({
        "object": planet,
        "label": planet_label,
        "distance": distance,
        "angle": initial_angle,
        "speed": data["speed"],
        "rotation": data["rotation"],
        "ring": saturn_ring
    })

# -------------------- EARTH'S MOON ------------------------

moon = sphere(
    pos=vector(9, 0, 0),
    radius=0.16,
    color=vector(0.78, 0.82, 0.9),
    shininess=0.8
)

moon_orbit_angle = 0

# -------------------- INTERFACE ---------------------------

scene.append_to_caption("\n")

scene.append_to_caption(
    "<b>✦ INTERACTIVE UNIVERSE</b>\n"
)

scene.append_to_caption(
    "DRAG: Rotate the universe    |    "
    "SCROLL: Zoom in / out\n"
)

scene.append_to_caption(
    "8 PLANETS    |    1 STAR    |    "
    "SATURN RINGS    |    EARTH'S MOON\n"
)

scene.append_to_caption(
    "<i>Planetary distances and sizes are visually scaled "
    "for presentation.</i>\n"
)

scene.append_to_caption(
    "LIVE SIMULATION • REAL-TIME ANIMATION\n"
)

# -------------------- ANIMATION ---------------------------

print("========================================")
print("  3D INTERACTIVE SOLAR SYSTEM STARTED")
print("========================================")
print("Drag the mouse to rotate.")
print("Scroll to zoom.")
print("Close the browser tab or stop Python to exit.")

elapsed_time = 0

while True:

    # rate() for controls animation speed
    rate(60)

    dt = 1 / 60
    elapsed_time += dt

    # Sun glow animation
    pulse = math.sin(elapsed_time * 1.5)

    sun_glow_outer.radius = 2.6 + 0.08 * pulse
    sun_glow_inner.radius = 2.1 + 0.04 * pulse

    # Animate planets
    for item in planets:

        item["angle"] += item["speed"] * dt

        distance = item["distance"]
        angle = item["angle"]

        new_position = vector(
            distance * math.cos(angle),
            0,
            distance * math.sin(angle)
        )

        # Move planet
        item["object"].pos = new_position

        # Rotate planet
        item["object"].rotate(
            angle=item["rotation"] * dt,
            axis=vector(0, 1, 0)
        )

        # Update label
        item["label"].pos = new_position

        # Move Saturn's rings
        if item["ring"] is not None:
            item["ring"].pos = new_position

    # Animate Earth's Moon
    moon_orbit_angle += 2.5 * dt

    earth = planets[2]["object"]

    moon_distance = 0.9

    moon.pos = earth.pos + vector(
        moon_distance * math.cos(moon_orbit_angle),
        0.12,
        moon_distance * math.sin(moon_orbit_angle)
    )
