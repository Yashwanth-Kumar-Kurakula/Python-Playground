import pygame
import sys

pygame.init()

# Color constants
BACKGROUND_COLOR = (0, 0, 50)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# Screen dimensions constants
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 600

# Player class
class Player:
    def __init__(self, color):
        self.color = color

# Class representing the welcome screen
class WelcomeScreen:
    def __init__(self, screen):
        self.screen = screen  # Surface on which to draw the welcome screen
        self.TEXT_COLOR = WHITE  # Color of the welcome screen text
        self.BUTTON_COLOR = RED  # Color of the "continue" button

    # Method to clear the welcome screen
    def clear(self):
        self.screen.fill(BACKGROUND_COLOR)  # Fill the screen with the background color
        pygame.display.update()  # Update the screen

    # Method to display the game title
    def show_title1(self):
        title_font = pygame.font.SysFont(None, 150)  # Load a font for the title
        title_surface = title_font.render("Connect 4", True, self.TEXT_COLOR)  # Create a surface with the title
        title_rect = title_surface.get_rect(
            center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 5))  # Set the position of the title on the screen
        self.screen.blit(title_surface, title_rect)  # Display the title on the screen

    # Method to display "Rules"
    def show_title2(self):
        title_font = pygame.font.SysFont(None, 70)  # Load a font for the title
        title_surface = title_font.render("Game Rules:", True, self.TEXT_COLOR)  # Create a text surface
        title_rect = title_surface.get_rect(
            center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3 + 50))  # Set the position of the title on the screen
        self.screen.blit(title_surface, title_rect)  # Display the title on the screen

        # Add an underline below the text
        line_y = title_rect.bottom + 5
        pygame.draw.line(self.screen, self.TEXT_COLOR, (title_rect.left, line_y), (title_rect.right, line_y), 2)

    # Method to display the rules
    def show_rules(self):
        # Load a font for the text
        font = pygame.font.SysFont(None, 21)
        line_height = 25  # height of a text line
        line_margin = 5  # margin between lines

        # Definition of the game rules
        rules_text = ["- The game is played by two players, each with a color of pieces.",
                      "- The goal of the game is to place 4 pieces of your color in a row (horizontal, vertical, or diagonal).",
                      "- Turn by turn, players choose a column to place their piece.",
                      "- The piece falls to the bottom of the chosen column or on another piece already present in the column.",
                      "- If no player has aligned 4 pieces at the end of the game, the game is a draw."]

        # Displaying the rules
        y_pos = SCREEN_HEIGHT // 3 + 135  # Vertical position of the first line
        for line in rules_text:
            text_surface = font.render(line, True, self.TEXT_COLOR)  # Create a surface with the text
            text_rect = text_surface.get_rect(left=SCREEN_WIDTH // 40,
                                              top=y_pos)  # Set the position of the text on the screen
            self.screen.blit(text_surface, text_rect)  # Display the text on the screen
            y_pos += line_height + line_margin  # Update the vertical position for the next line

    # Method to display the "continue" button allowing users to start the game
    def show_button(self):
        font = pygame.font.SysFont(None, 40)
        text = font.render('PLAY!', True, self.TEXT_COLOR)
        button_width = text.get_width() + 20
        button_height = text.get_height() + 20
        x_button = (SCREEN_WIDTH - button_width) // 2
        y_button = (SCREEN_HEIGHT - button_height) // 2 + 250
        button_rect = pygame.Rect(x_button, y_button, button_width, button_height)
        pygame.draw.rect(self.screen, self.BUTTON_COLOR, button_rect)
        self.screen.blit(text, (x_button + 10, y_button + 10))
        pygame.display.update(button_rect)
        self.button_area = button_rect  # store the button collision area

    # Main method that calls all secondary methods
    def show(self):
        self.show_title1()
        self.show_title2()
        self.show_rules()
        self.show_button()

        pygame.display.update()  # Update the screen

# Class representing the game grid
class Grid:
    def __init__(self, screen):
        self.screen = screen
        self.board = [[0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0]]

        self.NUM_COLUMNS = 7
        self.NUM_ROWS = 6

        self.width = int(SCREEN_WIDTH / self.NUM_COLUMNS)
        self.height = int(SCREEN_HEIGHT / self.NUM_ROWS)

    # Method to draw the grid and pieces based on the state of the board
    def draw(self):
        for row in range(self.NUM_ROWS):
            for column in range(self.NUM_COLUMNS):
                x = column * self.width
                y = row * self.height
                if self.board[row][column] == 0:
                    pass
                else:
                    if self.board[row][column] == 1:
                        pygame.draw.circle(self.screen, RED, (x + self.width // 2, y + self.height // 2),
                                           self.width // 2 - 2)
                    if self.board[row][column] == 2:
                        pygame.draw.circle(self.screen, YELLOW, (x + self.width // 2, y + self.height // 2),
                                           self.width // 2 - 2)
                pygame.draw.rect(self.screen, WHITE, (x, y, self.width, self.height), 2)

    # Method to check the row where the piece will come based on the already present pieces
    def check_row(self, column):
        if column < 0 or column >= self.NUM_COLUMNS:
            return -1
        row = self.NUM_ROWS - 1
        while row >= 0 and self.board[row][column] != 0:
            row -= 1
        if row >= 0:
            return row
        return -1

    # Method to check if four pieces of the same color are aligned
    def check_alignment(self):
        # Check alignments diagonally (top-left to bottom-right)
        for i in range(self.NUM_ROWS - 3):
            for j in range(self.NUM_COLUMNS - 3):
                if self.board[i][j] == self.board[i + 1][j + 1] == self.board[i + 2][j + 2] == self.board[i + 3][j + 3] and \
                        self.board[i][j] != 0:
                    return self.board[i][j]

        # Check alignments diagonally (bottom-left to top-right)
        for i in range(3, self.NUM_ROWS):
            for j in range(self.NUM_COLUMNS - 3):
                if self.board[i][j] == self.board[i - 1][j + 1] == self.board[i - 2][j + 2] == self.board[i - 3][j + 3] and \
                        self.board[i][j] != 0:
                    return self.board[i][j]

        # Check horizontal alignments
        for i in range(self.NUM_ROWS):
            for j in range(self.NUM_COLUMNS - 3):
                if self.board[i][j] == self.board[i][j + 1] == self.board[i][j + 2] == self.board[i][j + 3] and self.board[i][j] != 0:
                    return self.board[i][j]

        # Check vertical alignments
        for i in range(self.NUM_ROWS - 3):
            for j in range(self.NUM_COLUMNS):
                if self.board[i][j] == self.board[i + 1][j] == self.board[i + 2][j] == self.board[i + 3][j] and self.board[i][j] != 0:
                    return self.board[i][j]

        return 0

    # Method to check if the grid is full
    def is_full(self):
        for row in self.board:
            if 0 in row:
                return False
        return True

    # Method to modify the state of the "board" attribute
    def modify_cell(self, column, current_player):
        if self.board[0][column] == 0:
            if current_player.color == 'red':
                self.board[self.check_row(column)][column] = 1
            else:
                self.board[self.check_row(column)][column] = 2

# Class representing the game logic
class Game:
    def __init__(self, screen, player1, player2, draw_case, interrupt_case):
        self.screen = screen  # Surface on which to play
        self.clock = pygame.time.Clock()  # Create the clock object
        self.UPDATE_SPEED = 60

        # Define the grid and players
        self.game_grid = Grid(self.screen)
        self.player1 = player1
        self.player2 = player2
        self.draw_case = draw_case

        self.turn = 1
        self.current_player = self.player1
        self.result = self.draw_case
        self.interrupt_case = interrupt_case

    # Method to clear all game elements
    def clear(self):
        self.screen.fill(BACKGROUND_COLOR)  # Fill the screen with the background color
        pygame.display.update()  # Update the screen

    # Method to display the game grid
    def display(self):
        self.game_grid.draw()  # Draw the grid
        pygame.display.update()  # Update the screen
        self.clock.tick(self.UPDATE_SPEED)  # Set the window update speed

    # Main game method
    def run(self):
        # Main loop
        game_in_progress = True
        while game_in_progress:
            if self.game_grid.check_alignment() != 0:
                if self.game_grid.check_alignment() == 1:
                    self.result = self.player1
                if self.game_grid.check_alignment() == 2:
                    self.result = self.player2
                game_in_progress = False
            if self.game_grid.is_full():
                self.result = self.draw_case
                game_in_progress = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.result = self.interrupt_case
                    game_in_progress = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        pos = pygame.mouse.get_pos()
                        column = pos[0] // self.game_grid.width
                        if self.game_grid.board[0][column] == 0:
                            self.game_grid.modify_cell(column, self.current_player)
                            if self.turn % 2 == 1:
                                self.current_player = self.player2
                            else:
                                self.current_player = self.player1
                            self.turn += 1
            self.display()
        return self.result

# Class representing the exit screen
class ExitScreen:
    def __init__(self, screen, result):
        self.screen = screen
        self.result = result
        self.TEXT_COLOR = WHITE
        self.BUTTON_COLOR = RED

    # Method to clear the exit screen (optional)
    def clear(self):
        self.screen.fill(BACKGROUND_COLOR)  # Fill the screen with the background color
        pygame.display.update()  # Update the screen

    # Method to display the title
    def show_title1(self):
        pygame.font.init()
        title_font = pygame.font.SysFont(None, 150)  # Load a font for the title
        title_surface = title_font.render("Connect 4", True, self.TEXT_COLOR)  # Create a surface with the title
        title_rect = title_surface.get_rect(
            center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 5))  # Set the position of the title on the screen
        self.screen.blit(title_surface, title_rect)  # Display the title on the screen

    # Method to display the end game message
    def show_message(self):
        pygame.font.init()
        if self.result.color == 'red':
            message = 'The REDs have won!'
        elif self.result.color == 'yellow':
            message = 'The YELLOWS have won!'
        else:
            message = 'DRAW!'
        title_font = pygame.font.SysFont(None, 70)
        title_surface = title_font.render(message, True, self.TEXT_COLOR)  # Create a surface with the message
        title_rect = title_surface.get_rect(
            center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))  # Set the position of the message on the screen
        self.screen.blit(title_surface, title_rect)  # Display the title on the screen

    # Method to display the end game button
    def show_button(self):
        font = pygame.font.SysFont(None, 40)
        text = font.render('EXIT', True, self.TEXT_COLOR)
        button_width = text.get_width() + 20
        button_height = text.get_height() + 20
        x_button = (SCREEN_WIDTH - button_width) // 2
        y_button = (SCREEN_HEIGHT - button_height) // 2 + 250
        button_rect = pygame.Rect(x_button, y_button, button_width, button_height)
        pygame.draw.rect(self.screen, self.BUTTON_COLOR, button_rect)
        self.screen.blit(text, (x_button + 10, y_button + 10))
        pygame.display.update(button_rect)
        self.button_area = button_rect  # store the button collision area

    # Main method that displays all secondary methods
    def show(self):
        self.show_title1()
        self.show_message()
        self.show_button()

        pygame.display.update()  # Update the screen

# Initialize the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.fill(BACKGROUND_COLOR)

# Create instances of the Player class
player1 = Player('red')
player2 = Player('yellow')
draw = Player('none')
interrupted = Player('interrupted')

# Create instances of the WelcomeScreen and Game classes
welcome_screen = WelcomeScreen(screen)
game = Game(screen, player1, player2, draw, interrupted)

welcome_screen.show()  # Display the welcome screen

continue1 = True
while continue1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONUP:
            x, y = event.pos
            if welcome_screen.button_area.collidepoint(x, y):
                welcome_screen.clear()
                del welcome_screen
                winner = game.run()
                game.clear()
                del game
                continue1 = False

# Create an instance of the ExitScreen class based on the game result
if winner.color == 'red':
    exit_screen = ExitScreen(screen, player1)
elif winner.color == 'yellow':
    exit_screen = ExitScreen(screen, player2)
elif winner.color == 'none':
    exit_screen = ExitScreen(screen, draw)
else:
    pygame.quit()
    sys.exit()

exit_screen.show()  # Display the exit screen

continue2 = True
while continue2:
    pygame.init()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONUP:
            x, y = event.pos
            if exit_screen.button_area.collidepoint(x, y):
                del exit_screen
                continue2 = False

pygame.quit()
sys.exit()
