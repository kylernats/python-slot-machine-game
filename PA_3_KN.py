# This program prints out a slot machine game, where the user has the ability to win tokens
# if they land on a fruit combination where all 3 fruits are the same.
# If not all 3 are the same, the user loses a token.
# The user can keep spinning as long as they have 1 or more tokens left

#Created by Kyler Nats


#This imports random, os, and drawing panel
import random
import os
from DrawingPanel import *

def main():
    """
    Main function that runs a slot machine game.
    Special winning pictures are 1, 14, and 25 - landing on any of these adds one token.
    """
    # Get the current directory where your Python script is located
    current_dir = os.getcwd()
    image_dir = os.path.join(current_dir, "Programming Assignment 3 Pictures")
    
    # Verify all required images exist
    if not os.path.exists(image_dir):
        print(f"Error: Could not find the images directory: {image_dir}")
        return
    
    # Initialize panel
    PANEL_WIDTH = 600
    PANEL_HEIGHT = 500
    WHITE_AREA_WIDTH = 580
    WHITE_AREA_HEIGHT = 300
    
    panel = DrawingPanel(PANEL_WIDTH, PANEL_HEIGHT, background="red")
    panel.set_title("Slot Machine Game")
    
    # Create display areas with proper margins
    panel.fill_rect(10, 10, WHITE_AREA_WIDTH, WHITE_AREA_HEIGHT, color="white")  # Display area
    panel.fill_rect(10, 350, WHITE_AREA_WIDTH, 100, color="blue")  # Message area
    
    # Define winning pictures
    winning_pictures = [1, 14, 25]
    
    # Calculate center position for single image
    x_position = 80  # Centered position for single image
    y_position = 80   # Vertical position
    
    # Initial token count
    tokens = 5
    
    # Display welcome message and rules
    if not panel.message_yes_no(
        'Welcome to the Slot Machine!\n\n' +
        'Rules:\n' +
        '- You start with 5 tokens\n' +
        '- Each spin costs 1 token\n' +
        '- Each winning spin adds 1 token\n' +
        '- Run out of tokens and you lose\n\n' +
        'Would you like to play?',
        title='Play?'
    ):
        panel.draw_string("Thanks for playing!", 160, 400, color="white", font=("Helvetica", 24, "bold"))
        panel.sleep(2000)
        return

    # Main game loop
    while tokens > 0:
        # Display current tokens
        panel.fill_rect(10, 350, WHITE_AREA_WIDTH, 100, color="blue")
        panel.draw_string(f"Current tokens: {tokens}", 125, 400, color="white", font=("Helvetica", 24, "bold"))
        
        # Ask if they want to spin or cash out
        if not panel.message_yes_no(
            f'You have {tokens} tokens.\nWould you like to spin? (Cost: 1 token)\nSelect No to cash out.',
            title='Spin or Cash Out?'
        ):
            break
        
        # Deduct token for spin
        tokens -= 1
        
        # Clear display areas and show spinning message
        panel.fill_rect(10, 10, WHITE_AREA_WIDTH, WHITE_AREA_HEIGHT, color="white")
        panel.fill_rect(10, 350, WHITE_AREA_WIDTH, 100, color="blue")
        panel.draw_string("Spinning...", 165, 400, color="white", font=("Helvetica", 24, "bold"))
        
        # Spin animation
        for _ in range(15):
            panel.fill_rect(10, 10, WHITE_AREA_WIDTH, WHITE_AREA_HEIGHT, color="white")  # Clear previous image
            temp_picture = random.randint(1, 27)
            image_path = os.path.join(image_dir, f"picture{temp_picture}.png")
            panel.draw_image(image_path, x_position, y_position)
            panel.sleep(100)
        
        # Final result
        final_picture = random.randint(1, 27)
        
        # Display final picture
        panel.fill_rect(10, 10, WHITE_AREA_WIDTH, WHITE_AREA_HEIGHT, color="white")
        image_path = os.path.join(image_dir, f"picture{final_picture}.png")
        panel.draw_image(image_path, x_position, y_position)
        
        # Check if winning picture
        won_this_spin = final_picture in winning_pictures
        if won_this_spin:
            tokens += 1
        
        # Display result
        panel.fill_rect(10, 350, WHITE_AREA_WIDTH, 100, color="blue")
        if won_this_spin:
            panel.draw_string("CONGRATULATIONS! You won a token!", 75, 400, 
                            color="white", font=("Helvetica", 24, "bold"))
        else:
            if tokens > 0:
                panel.draw_string(f"Keep trying! Tokens left: {tokens}", 125, 400, 
                                color="white", font=("Helvetica", 24, "bold"))
            else:
                panel.draw_string("Out of tokens! Game Over!", 125, 400, 
                                color="white", font=("Helvetica", 24, "bold"))
        
        panel.sleep(2000)
    
    # End game message 
    panel.fill_rect(10, 350, WHITE_AREA_WIDTH, 100, color="blue")
    if tokens <= 0:
        panel.draw_string("Game Over! You ran out of tokens!", 100, 400, 
                         color="white", font=("Helvetica", 24, "bold"))
        panel.message_box("Game Over!", "You ran out of tokens!")
    else:
        panel.draw_string(f"Thanks for playing! Final tokens: {tokens}", 100, 400, 
                         color="white", font=("Helvetica", 24, "bold"))
        panel.message_box("Thanks for Playing!", f"Final token count: {tokens}")
    
    panel.sleep(3000)

#This starts the program
main()
