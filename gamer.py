import pygame
import sys
import math
import random
import time
\
# Initialize pygame
pygame.init()

# Define some constants
WIDTH, HEIGHT = 800, 600
FPS = 60
CAR_WIDTH, CAR_HEIGHT = 40, 70
TRACK_COLOR = (50, 50, 50)

# Create screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racing Game - Power-Ups with Car Classes")

# Define colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Power-up types
SPEED_BOOST = 1
MISSILE = 2
INVISIBILITY = 3
AUTO_DRIVE = 4

# Power-up class to create power-ups
class PowerUp:
    def __init__(self, x, y, power_up_type):
        self.x = x
        self.y = y
        self.type = power_up_type
        self.size = 20
        self.color = YELLOW
        if self.type == SPEED_BOOST:
            self.color = (0, 255, 255)
        elif self.type == MISSILE:
            self.color = (255, 0, 255)
        elif self.type == INVISIBILITY:
            self.color = (0, 255, 0)
        elif self.type == AUTO_DRIVE:
            self.color = (255, 165, 0)

    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.size)

# Base Car class
class Car:
    def __init__(self, x, y, color, speed, handling, acceleration, braking):
        self.x = x
        self.y = y
        self.width = CAR_WIDTH
        self.height = CAR_HEIGHT
        self.angle = 0
        self.speed = speed
        self.handling = handling
        self.acceleration = acceleration
        self.braking = braking
        self.color = color
        self.max_speed = speed
        self.current_speed = 0
        self.speed_boost_active = False
        self.invisibility_active = False
        self.auto_drive_active = False
        self.missile_ready = True

    def draw(self):
        car_surface = pygame.Surface((self.width, self.height))
        car_surface.fill(self.color)
        rotated_car = pygame.transform.rotate(car_surface, self.angle)
        car_rect = rotated_car.get_rect(center=(self.x, self.y))
        screen.blit(rotated_car, car_rect.topleft)

    def move(self):
        if self.auto_drive_active:
            # Auto-drive controls the car movement automatically
            self.x += self.current_speed * math.cos(math.radians(self.angle))
            self.y -= self.current_speed * math.sin(math.radians(self.angle))
        else:
            # Regular player movement
            if self.current_speed > self.max_speed:
                self.current_speed = self.max_speed
            if self.current_speed < 0:
                self.current_speed = 0

            # Move car based on current speed and angle
            self.x += self.current_speed * math.cos(math.radians(self.angle))
            self.y -= self.current_speed * math.sin(math.radians(self.angle))

    def accelerate(self):
        if not self.speed_boost_active:
            self.current_speed += self.acceleration
        else:
            self.current_speed += self.acceleration * 2  # Double speed for boost

    def brake(self):
        self.current_speed -= self.braking

    def turn_left(self):
        self.angle += self.handling

    def turn_right(self):
        self.angle -= self.handling

    def update(self):
        self.move()

    def activate_speed_boost(self):
        self.speed_boost_active = True
        pygame.time.set_timer(pygame.USEREVENT + 1, 5000)  # 5 seconds speed boost

    def activate_invisibility(self):
        self.invisibility_active = True
        pygame.time.set_timer(pygame.USEREVENT + 2, 5000)  # 5 seconds invisibility

    def activate_auto_drive(self):
        self.auto_drive_active = True
        pygame.time.set_timer(pygame.USEREVENT + 3, 5000)  # 5 seconds auto-drive

    def deactivate_speed_boost(self):
        self.speed_boost_active = False

    def deactivate_invisibility(self):
        self.invisibility_active = False

    def deactivate_auto_drive(self):
        self.auto_drive_active = False

    def use_missile(self, other_car):
        if self.missile_ready:
            self.missile_ready = False
            # Slow down the other car
            other_car.current_speed -= 1
            pygame.time.set_timer(pygame.USEREVENT + 4, 2000)  # Cooldown for missile (2 seconds)
        
    def missile_cooldown(self):
        self.missile_ready = True

# Speedster class (high speed, low acceleration and braking)
class Speedster(Car):
    def __init__(self, x, y):
        super().__init__(x, y, RED, speed=8, handling=5, acceleration=0.2, braking=0.1)

# Drifter class (high handling, high acceleration)
class Drifter(Car):
    def __init__(self, x, y):
        super().__init__(x, y, BLUE, speed=5, handling=8, acceleration=0.3, braking=0.2)

# Tank class (high braking, average speed)
class Tank(Car):
    def __init__(self, x, y):
        super().__init__(x, y, GREEN, speed=6, handling=4, acceleration=0.1, braking=0.3)

# All-Rounder class (balanced stats)
class AllRounder(Car):
    def __init__(self, x, y):
        super().__init__(x, y, YELLOW, speed=6, handling=6, acceleration=0.2, braking=0.2)

# Main game loop
def main():
    running = True
    player1_car = Speedster(WIDTH // 4, HEIGHT // 2)  # Example: Player 1 picks Speedster
    player2_car = Drifter(WIDTH // 4 + 100, HEIGHT // 2)  # Example: Player 2 picks Drifter

    # Power-up generation
    power_ups = []
    for _ in range(5):  # Generate 5 random power-ups
        x = random.randint(100, WIDTH - 100)
        y = random.randint(100, HEIGHT - 100)
        power_up_type = random.choice([SPEED_BOOST, MISSILE, INVISIBILITY, AUTO_DRIVE])
        power_ups.append(PowerUp(x, y, power_up_type))

    while running:
        screen.fill(TRACK_COLOR)
        pygame.draw.rect(screen, WHITE, (50, 50, WIDTH - 100, HEIGHT - 100), 5)  # Draw simple track

        # Event handling (for power-up timers)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.USEREVENT + 1:
                player1_car.deactivate_speed_boost()
                player2_car.deactivate_speed_boost()
            if event.type == pygame.USEREVENT + 2:
                player1_car.deactivate_invisibility()
                player2_car.deactivate_invisibility()
            if event.type == pygame.USEREVENT + 3:
                player1_car.deactivate_auto_drive()
                player2_car.deactivate_auto_drive()
            if event.type == pygame.USEREVENT + 4:
                player1_car.missile_cooldown()
                player2_car.missile_cooldown()

        # Player 1 controls (arrow keys)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player1_car.turn_left()
        if keys[pygame.K_RIGHT]:
            player1_car.turn_right()
        if keys[pygame.K_UP]:
            player1_car.accelerate()
        if keys[pygame.K_DOWN]:
            player1_car.brake()

        # Player 2 controls (WASD, Q and E)
        if keys[pygame.K_a]:
            player2_car.turn_left()
        if keys[pygame.K_d]:
            player2_car.turn_right()
        if keys[pygame.K_w]:
            player2_car.accelerate()
        if keys[pygame.K_s]:
            player2_car.brake()

        # Power-up pickup logic
        for power_up in power_ups[:]:
            if (player1_car.x - power_up.x)**2 + (player1_car.y - power_up.y)**2 < (CAR_WIDTH / 2 + power_up.size)**2:
                if power_up.type == SPEED_BOOST:
                    player1_car.activate_speed_boost()
                elif power_up.type == MISSILE:
                    player1_car.use_missile(player2_car)
                elif power_up.type == INVISIBILITY:
                    player1_car.activate_invisibility()
                elif power_up.type == AUTO_DRIVE:
                    player1_car.activate_auto_drive()
                power_ups.remove(power_up)  # Remove power-up from the screen

            if (player2_car.x - power_up.x)**2 + (player2_car.y - power_up.y)**2 < (CAR_WIDTH / 2 + power_up.size)**2:
                if power_up.type == SPEED_BOOST:
                    player2_car.activate_speed_boost()
                elif power_up.type == MISSILE:
                    player2_car.use_missile(player1_car)
                elif power_up.type == INVISIBILITY:
                    player2_car.activate_invisibility()
                elif power_up.type == AUTO_DRIVE:
                    player2_car.activate_auto_drive()
                power_ups.remove(power_up)

        # Update car positions
        player1_car.update()
        player2_car.update()

        # Draw cars
        player1_car.draw()
        player2_car.draw()

        # Draw power-ups
        for power_up in power_ups:
            power_up.draw()

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
