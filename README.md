# 🏓 Pong Game

A classic **two-player Pong game** built with **Python Turtle** and **Object-Oriented Programming (OOP)**.

This project was created to practice Python OOP, game loops, collision detection, keyboard events, object interaction, and basic game-state management.

---

# 🎯 Learning Goals

The main goal of this project is to understand how different Python classes and objects work together to build a complete program.

Through this project, I practiced:

* Creating classes and objects
* Using inheritance with the `Turtle` class
* Creating reusable methods
* Separating program logic into multiple files
* Handling keyboard events
* Building a continuous game loop
* Detecting collisions
* Managing game state
* Working with coordinates
* Increasing game difficulty dynamically
* Managing scores and winning conditions
* Using Git and GitHub for project development

---

# 📊 Project Status

**Status:** ✅ Completed

The core Pong gameplay is implemented, including:

* Two-player controls
* Ball movement
* Wall collision
* Paddle collision
* Increasing ball speed
* Paddle screen boundaries
* Score tracking
* Ball reset
* Winning condition
* Game Over

### Possible future improvements

* Restart button
* Start screen
* Pause functionality
* Sound effects
* Difficulty levels
* Maximum ball-speed limit
* Display the winning player's name

---

# 🛠️ Technologies Used

* **Python 3**
* **Turtle Graphics**
* **Object-Oriented Programming**
* **Git**
* **GitHub**

---

# 📋 Requirements

You only need:

* Python 3.x
* A code editor such as VS Code
* Git (optional, if cloning the repository)

### Python libraries

This project uses Python's built-in `turtle` module.

```python
from turtle import Turtle, Screen
```

No external packages are required.

---

# ▶️ How to Run the Project

## 1. Clone the repository

```bash
git clone <your-repository-url>
```

## 2. Open the project folder

```bash
cd Pong-Game
```

## 3. Run the game

```bash
python main.py
```

If your system uses `python3`:

```bash
python3 main.py
```

The Pong game window will open.

---

# 🎮 Game Features

* 👥 Two-player gameplay
* 🏓 Two controllable paddles
* ⚽ Automatic ball movement
* 🧱 Ball bounces off the top and bottom walls
* 🏓 Ball bounces off paddles
* ⚡ Ball speed increases after every paddle hit
* 🚧 Paddles cannot leave the screen
* 🏆 Separate scores for both players
* 🔄 Ball resets after a player misses
* 🔢 Ball speed resets after each point
* 🏆 Winning score condition
* 🛑 Game Over when a player reaches the winning score

---

# 🎮 Controls

| Player       | Move Up | Move Down |
| ------------ | ------- | --------- |
| Left Player  | `W`     | `S`       |
| Right Player | `↑`     | `↓`       |

> Click inside the game window before using the keyboard controls.

---

# 📁 Project Structure

```text
Pong-Game/
│
├── main.py
├── paddle.py
├── ball.py
├── scoreboard.py
└── README.md
```

---

# 🧠 Project Logic at a Glance

The easiest way to understand this project is:

```text
                    main.py
                 Game Controller
                       │
       ┌───────────────┼───────────────┐
       ↓               ↓               ↓
  paddle.py         ball.py       scoreboard.py
       │               │               │
       ↓               ↓               ↓
   Paddle          Ball Logic       Score Logic
   Movement        Movement         Left Score
   Boundaries      Collision        Right Score
                   Speed            Game Over
                   Reset
```

### One-line memory trick

> **`main.py`**** controls → ****`paddle.py`**** moves paddles → ****`ball.py`**** controls the ball → ****`scoreboard.py`**** manages scores and Game Over.**

---

# 🔵 `main.py` — Game Controller

### Responsibility

`main.py` is the **brain of the game**.

It:

* Creates the game screen
* Creates the paddles
* Creates the ball
* Creates the scoreboard
* Connects keyboard controls
* Runs the game loop
* Detects collisions
* Detects when a player misses
* Updates scores
* Checks the winning condition

### Objects created

```python
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()
```

---

# 🔄 Main Game Loop

The game continuously runs inside:

```python
while is_game_on:
```

Each loop follows this basic sequence:

```text
Move Ball
   ↓
Check Wall Collision
   ↓
Check Paddle Collision
   ↓
Check if Ball Missed
   ↓
Update Score
   ↓
Check Winning Condition
   ↓
Repeat
```

---

## 1. Move the Ball

```python
ball.move()
```

The ball calculates its next X and Y position.

---

## 2. Wall Collision

```python
if ball.ycor() > 280 or ball.ycor() < -280:
    ball.bounce_y()
```

When the ball reaches the top or bottom boundary:

```text
Top Wall
──────────────
      ⚪
       ↕
──────────────
Bottom Wall
```

`bounce_y()` reverses the vertical direction.

---

## 3. Paddle Collision

The game checks:

```python
ball.distance(paddle)
```

and the ball's X position.

If the ball hits a paddle:

```python
ball.bounce_x()
ball.increase_speed()
```

The sequence is:

```text
Ball hits paddle
       ↓
Reverse horizontal direction
       ↓
Increase ball speed
       ↓
Continue moving
```

---

## 4. Player Misses the Ball

### Right paddle misses

```python
if ball.xcor() > 380:
    ball.reset_position()
    scoreboard.l_point()
```

Meaning:

```text
Ball crosses right boundary
          ↓
Right player missed
          ↓
Left player gets 1 point
          ↓
Ball returns to center
```

### Left paddle misses

```python
if ball.xcor() < -380:
    ball.reset_position()
    scoreboard.r_point()
```

Meaning:

```text
Ball crosses left boundary
          ↓
Left player missed
          ↓
Right player gets 1 point
          ↓
Ball returns to center
```

---

# 🟢 `paddle.py` — Paddle Logic

### Responsibility

`paddle.py` contains the `Paddle` class.

It handles:

* Creating paddles
* Moving paddles
* Preventing paddles from leaving the screen

### Movement

```python
def go_up(self):
    if self.ycor() < UP_LIMIT:
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)
```

```python
def go_down(self):
    if self.ycor() > DOWN_LIMIT:
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
```

The boundary checks prevent the paddle from moving outside the game screen.

---

# 🔴 `ball.py` — Ball Logic

### Responsibility

`ball.py` contains the `Ball` class.

It handles:

* Ball movement
* Horizontal bouncing
* Vertical bouncing
* Ball speed
* Ball reset

### Ball movement

```python
new_x = self.xcor() + self.x_move
new_y = self.ycor() + self.y_move
self.goto(new_x, new_y)
```

The direction is controlled by:

```text
x_move → horizontal direction
y_move → vertical direction
```

For example:

```text
x_move = +10 → Right
x_move = -10 → Left

y_move = +10 → Up
y_move = -10 → Down
```

---

## `bounce_x()`

```python
def bounce_x(self):
    self.x_move *= -1
```

Changes:

```text
+10 → -10
-10 → +10
```

This makes the ball move in the opposite horizontal direction.

---

## `bounce_y()`

```python
def bounce_y(self):
    self.y_move *= -1
```

Changes:

```text
+10 → -10
-10 → +10
```

This makes the ball move in the opposite vertical direction.

---

## `increase_speed()`

```python
def increase_speed(self):
    self.move_speed *= 0.9
```

The game uses:

```python
time.sleep(ball.move_speed)
```

Therefore:

```text
0.100 seconds
      ↓
0.090 seconds
      ↓
0.081 seconds
      ↓
0.073 seconds
```

**Smaller delay = faster ball.**

The ball becomes progressively faster after each paddle hit.

---

## `reset_position()`

When a player misses:

```python
def reset_position(self):
    self.goto(0, 0)
    self.move_speed = 0.1
    self.x_move *= -1
```

It:

1. Moves the ball back to the center
2. Resets the ball speed
3. Changes the starting horizontal direction

---

# 🟡 `scoreboard.py` — Score & Game Over

### Responsibility

`scoreboard.py` contains the `Scoreboard` class.

It manages:

* Left player's score
* Right player's score
* Displaying scores
* Updating scores
* Game Over message

### Score variables

```python
self.l_score = 0
self.r_score = 0
```

---

## Left Player Scores

```python
def l_point(self):
    self.l_score += 1
    self.updated_score()
```

Flow:

```text
Left player scores
       ↓
l_score + 1
       ↓
Update screen
```

---

## Right Player Scores

```python
def r_point(self):
    self.r_score += 1
    self.updated_score()
```

Flow:

```text
Right player scores
       ↓
r_score + 1
       ↓
Update screen
```

---

## Game Over

The game has a winning score:

```python
WINNING_SCORE = 5
```

When a player's score reaches the winning score:

```text
Winning score reached
        ↓
Display GAME OVER
        ↓
is_game_on = False
        ↓
Game loop stops
```

---

# 🏆 Complete Game Flow

When you return to this repository after some time, this is the most important diagram to remember:

```text
                    START
                      │
                      ↓
              Create Game Objects
                      │
        ┌─────────────┼─────────────┐
        ↓             ↓             ↓
     Paddle          Ball       Scoreboard
        │             │             │
        └─────────────┼─────────────┘
                      ↓
                 GAME LOOP
                      │
                      ↓
                 Move Ball
                      │
                      ↓
              Wall Collision?
                 /         \
               YES          NO
                │            │
                ↓            │
             Bounce Y        │
                │            │
                └─────┬──────┘
                      ↓
             Paddle Collision?
                 /         \
               YES          NO
                │            │
                ↓            │
        Bounce X + Speed     │
                │            │
                └─────┬──────┘
                      ↓
                Ball Missed?
                 /         \
               YES          NO
                │            │
                ↓            │
            Give Point       │
            Reset Ball       │
                │            │
                └─────┬──────┘
                      ↓
             Winning Score?
                 /         \
               YES          NO
                │            │
                ↓            ↓
            GAME OVER     Repeat Loop
```

---

# 🔗 How the Files Communicate

```text
main.py
   │
   ├── calls Paddle methods
   │       ├── go_up()
   │       └── go_down()
   │
   ├── calls Ball methods
   │       ├── move()
   │       ├── bounce_x()
   │       ├── bounce_y()
   │       ├── increase_speed()
   │       └── reset_position()
   │
   └── calls Scoreboard methods
           ├── l_point()
           ├── r_point()
           └── game_over()
```

---

# 🧩 Python Concepts Practiced

## Object-Oriented Programming

* Classes
* Objects
* Constructors (`__init__`)
* Instance attributes
* Instance methods
* Inheritance
* `super()`

Example:

```python
class Paddle(Turtle):
```

The `Paddle` class inherits functionality from Python's `Turtle` class.

---

## Python Concepts

* Variables
* Constants
* Functions
* Methods
* `if` conditions
* `while` loops
* Boolean expressions
* Logical operators
* Arithmetic operators
* Importing modules
* Multiple Python files
* Method calls
* State management

---

## Game Development Concepts

* Game loop
* Coordinates
* Collision detection
* Object interaction
* Keyboard event handling
* Game boundaries
* Score tracking
* Game state
* Difficulty progression
* Winning conditions

---

# 📌 Important Values

These are the main values used in the game:

```text
Screen
800 × 600

Left Paddle
(-350, 0)

Right Paddle
(350, 0)

Paddle Boundary
+235 / -235

Ball Starting Movement
X = 10
Y = 10

Initial Ball Delay
0.1 seconds

Winning Score
5
```

---

# 🧠 Quick Revision

If you only have **30 seconds**, remember this:

```text
main.py
→ Controls the entire game

paddle.py
→ Paddle movement + screen boundaries

ball.py
→ Ball movement + collision + speed + reset

scoreboard.py
→ Scores + Game Over

Game Loop
→ Move → Detect → React → Score → Reset → Check Winner → Repeat
```

### The core idea

> **The ****`main.py`**** game loop continuously observes what is happening and tells the appropriate object what to do.**

---

# 👨‍💻 Author

**Mahroof Shaikh**

Built as part of my journey to improve my **Python, Object-Oriented Programming, and problem-solving skills**.

---

# 🚀 Future Improvements

* [ ] Restart game after Game Over
* [ ] Add start screen
* [ ] Add pause functionality
* [ ] Add sound effects
* [ ] Add difficulty levels
* [ ] Add maximum ball-speed limit
* [ ] Display the winning player's name
* [ ] Improve game visuals
