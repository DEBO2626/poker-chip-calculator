import math
import os
import sys
from typing import Dict, Any, Union, List, Optional, Tuple

def validate_input(prompt: str, input_type: type, min_value: Optional[Union[int, float]] = None, 
                  max_value: Optional[Union[int, float]] = None, default: Optional[Any] = None) -> Any:
    """
    Validate user input with type checking and range validation.
    
    Args:
        prompt: The prompt to display to the user
        input_type: The expected type (int, float, etc.)
        min_value: Minimum acceptable value (optional)
        max_value: Maximum acceptable value (optional)
        default: Default value if input is empty (optional)
        
    Returns:
        Validated input of the specified type
    """
    while True:
        try:
            # Add default value to prompt if provided
            display_prompt = prompt
            if default is not None:
                display_prompt += f" (default: {default})"
            display_prompt += ": "
            
            # Get user input
            user_input = input(display_prompt).strip()
            
            # Use default if input is empty and default is provided
            if user_input == "" and default is not None:
                return default
                
            # Convert to the required type
            if input_type == bool:
                # Special handling for boolean input
                if user_input.lower() in ('yes', 'y', 'true', 't', '1'):
                    value = True
                elif user_input.lower() in ('no', 'n', 'false', 'f', '0'):
                    value = False
                else:
                    raise ValueError("Please answer with Yes or No (or Y/N)")
            else:
                value = input_type(user_input)
            
            # Check range if min_value or max_value is specified
            if min_value is not None and value < min_value:
                print(f"Oops! The number must be {min_value} or higher. Please try again.")
                continue
                
            if max_value is not None and value > max_value:
                print(f"Oops! The number must be {max_value} or lower. Please try again.")
                continue
                
            return value
            
        except ValueError as e:
            if input_type == int:
                print(f"Oops! Please enter a whole number (like 5, 10, or 20)")
            elif input_type == float:
                print(f"Oops! Please enter a number (like 1, 2.5, or 3.75)")
            else:
                print(f"Oops! {str(e)}")

def format_denomination(denom: float) -> str:
    """
    Format chip denomination for clean display.
    
    Args:
        denom: The chip denomination value
        
    Returns:
        Formatted string (e.g., "0.01", "0.25", "5", "100")
    """
    # If it's a whole number, display without decimals
    if denom == int(denom):
        return str(int(denom))
    # Otherwise show with minimal decimal places
    else:
        return f"{denom:.2f}".rstrip('0').rstrip('.')

def round_to_stack(count: int, stack_size: int, prefer_round: bool = False) -> int:
    """
    Round a chip count to the nearest multiple of stack_size.
    Prioritizes easy-to-count numbers (multiples of 5 or 10).
    
    Args:
        count: The original chip count
        stack_size: The stack size to round to (e.g., 5 or 10)
        prefer_round: If True, prefer round numbers like 10, 15, 20, 25 for easier counting
        
    Returns:
        Rounded chip count (always a multiple of 5, preferring 10s when close)
    """
    if count == 0:
        return 0
    
    if stack_size <= 1:
        stack_size = 5  # Force minimum stack size of 5 for easy counting
    
    # Always round to at least a multiple of 5
    if stack_size < 5:
        stack_size = 5
    
    # Round to the nearest multiple of stack_size
    rounded = round(count / stack_size) * stack_size
    
    # Ensure we have at least one stack if the original count was > 0
    if count > 0 and rounded == 0:
        rounded = stack_size
    
    # Always prefer round numbers (multiples of 5, but favor 10, 15, 20, 25, etc.)
    if rounded > 0:
        # For any count, try to snap to nice round numbers
        if 3 <= rounded <= 7:
            return 5
        elif 8 <= rounded <= 12:
            return 10
        elif 13 <= rounded <= 17:
            return 15
        elif 18 <= rounded <= 22:
            return 20
        elif 23 <= rounded <= 27:
            return 25
        elif 28 <= rounded <= 32:
            return 30
        elif 33 <= rounded <= 37:
            return 35
        elif 38 <= rounded <= 42:
            return 40
        elif 43 <= rounded <= 47:
            return 45
        elif 48 <= rounded <= 52:
            return 50
        # For larger numbers, just ensure they're multiples of 5
        else:
            rounded = round(rounded / 5) * 5
    
    return rounded

def round_to_stack_with_limit(count: int, stack_size: int, max_count: int, allow_small: bool = False) -> int:
    """
    Round a chip count to nearest nice stack, but don't exceed the maximum.
    Tournament standard: Only use denominations if we can give at least 5 chips per player.
    This prevents awkward 1-4 chip allocations that violate tournament best practices.
    
    Args:
        count: The desired chip count
        stack_size: The stack size to round to (e.g., 5)
        max_count: The maximum allowed count (based on available inventory)
        allow_small: If True, allow 1-4 chip allocations (for special cases like redistribution)
        
    Returns:
        Rounded chip count that doesn't exceed max_count (always 0 or ≥5 unless allow_small=True)
    """
    if count <= 0 or max_count <= 0:
        return 0
    
    # Tournament standard: Skip denominations if we can't give at least 5 chips per player
    # UNLESS allow_small=True (used when redistributing to avoid wasting significant value)
    if max_count < 5 and not allow_small:
        return 0  # Skip this denomination entirely
    
    # First, cap at the maximum
    count = min(count, max_count)
    
    # Try rounding to nice stack
    rounded = round_to_stack(count, stack_size)
    
    # If rounded exceeds max, round DOWN to nearest 5
    if rounded > max_count:
        rounded = (max_count // 5) * 5
    
    # If rounding would give us less than 5 chips
    if rounded < 5:
        if allow_small and max_count >= 1:
            # Allow small allocations if explicitly permitted
            return max(1, min(max_count, count))
        else:
            return 0
    
    return rounded

def load_chip_set() -> Dict[float, int]:
    """
    Load chip set from file or prompt user for input.
    
    Returns:
        Dictionary mapping chip denominations to quantities
    """
    chip_file_path = "poker chip set counts.txt"
    
    # Try to load from file first
    if os.path.exists(chip_file_path):
        try:
            chip_set = {}
            line_num = 0
            with open(chip_file_path, "r") as f:
                for line in f:
                    line_num += 1
                    line = line.strip()
                    
                    # Skip empty lines and comments
                    if not line or line.startswith("#"):
                        continue
                    
                    parts = line.strip().split()
                    if len(parts) >= 2:
                        # Validate count is positive integer
                        count = int(parts[0])
                        if count <= 0:
                            raise ValueError(f"Line {line_num}: Chip count must be positive (got {count})")
                        if count > 100000:
                            raise ValueError(f"Line {line_num}: Chip count too large (got {count}, max 100,000)")
                        
                        # Handle denomination with or without $ sign
                        denom_str = parts[1]
                        if denom_str.startswith("$"):
                            denom_str = denom_str[1:]
                        denom = float(denom_str)
                        
                        # Validate denomination
                        if denom <= 0:
                            raise ValueError(f"Line {line_num}: Denomination must be positive (got {denom})")
                        if denom > 1000000:
                            raise ValueError(f"Line {line_num}: Denomination too large (got {denom}, max 1,000,000)")
                        if math.isnan(denom) or math.isinf(denom):
                            raise ValueError(f"Line {line_num}: Invalid denomination value")
                        
                        chip_set[denom] = count
            
            if chip_set:
                # Validate chip set has reasonable denominations
                if len(chip_set) < 2:
                    print(f"Warning: Chip set file has only {len(chip_set)} denomination(s).")
                    print("You need at least 2 different denominations for a good tournament.")
                    print("Let's set up your chip set manually.\n")
                else:
                    print(f"Loaded chip set from {chip_file_path}")
                    return chip_set
        except ValueError as e:
            print(f"Error in chip set file: {e}")
            print("Let's set up your chip set manually.\n")
        except Exception as e:
            print(f"Warning: Could not load chip set from file: {e}")
            print("Let's set up your chip set manually.\n")
    else:
        print(f"No chip set file found ({chip_file_path})")
        print("Let's set up your chip set!\n")
    
    # Prompt user to input chip set
    chip_set = {}
    print("Enter your chip denominations and quantities.")
    print("(You can use decimals like 0.01, 0.25, or whole numbers like 1, 5, 25, 100)")
    print("Enter 0 for denomination when finished.\n")
    
    last_entry = None  # Track last entry for undo
    
    while True:
        denom = validate_input("Enter chip denomination (or 0 to finish)", float, min_value=0, max_value=1000000)
        
        if denom == 0:
            break
        
        # Additional validation for denomination
        if math.isnan(denom) or math.isinf(denom):
            print("Oops! That's not a valid number. Please try again.")
            continue
        
        if denom in chip_set:
            print(f"You already entered ${format_denomination(denom)}. Let's update it.")
        
        quantity = validate_input(f"How many ${format_denomination(denom)} chips do you have?", int, min_value=1, max_value=100000)
        
        # Store previous value in case of undo
        previous_value = chip_set.get(denom)
        chip_set[denom] = quantity
        last_entry = (denom, previous_value)  # Store for undo (denom, old_value or None)
        
        print(f"Added: {quantity} x ${format_denomination(denom)} chips")
        
        # Show current chip set
        if len(chip_set) > 0:
            print("\nCurrent chip set:")
            for d in sorted(chip_set.keys()):
                print(f"  {chip_set[d]:>4} x ${format_denomination(d)}")
        
        # Ask what to do next
        while True:
            action = input("\nContinue? (yes/undo/restart) [yes]: ").strip().lower()
            if action == "" or action == "yes" or action == "y":
                break
            elif action == "undo" or action == "u":
                if last_entry:
                    undo_denom, old_value = last_entry
                    if old_value is None:
                        # Was a new entry, remove it
                        del chip_set[undo_denom]
                        print(f"Removed ${format_denomination(undo_denom)} chips")
                    else:
                        # Was an update, restore old value
                        chip_set[undo_denom] = old_value
                        print(f"Restored ${format_denomination(undo_denom)} to {old_value} chips")
                    last_entry = None
                else:
                    print("Nothing to undo!")
                break
            elif action == "restart" or action == "r":
                chip_set.clear()
                last_entry = None
                print("Chip set cleared. Starting over...\n")
                break
            else:
                print("Please enter 'yes', 'undo', or 'restart'")
        
        print()  # Extra line for readability
    
    if len(chip_set) < 2:
        print("\nWarning: You need at least 2 different chip denominations for a good tournament.")
        print("Using default chip set instead.\n")
        return {1: 300, 5: 200, 25: 200, 100: 200, 500: 50, 1000: 50}
    
    # Display summary and confirm
    while True:
        print("\n" + "=" * 50)
        print("YOUR CHIP SET SUMMARY")
        print("=" * 50)
        
        # Calculate totals
        total_chips = sum(chip_set.values())
        total_value = sum(denom * count for denom, count in chip_set.items())
        
        for denom in sorted(chip_set.keys()):
            count = chip_set[denom]
            value = denom * count
            print(f"{count:>4} x ${format_denomination(denom):>8} chips = ${value:>10,.2f}".replace(".00", ""))
        
        print("-" * 50)
        print(f"Total: {total_chips} chips worth ${total_value:,.2f}".replace(".00", ""))
        print("=" * 50)
        
        # Confirm
        confirm = input("\nIs this chip set correct? (yes/restart) [yes]: ").strip().lower()
        if confirm == "" or confirm == "yes" or confirm == "y":
            break
        elif confirm == "restart" or confirm == "r":
            print("\nRestarting chip set entry...")
            print("Unfortunately, you'll need to re-enter the chip set from scratch.")
            restart_confirm = input("Are you sure? (yes/no) [no]: ").strip().lower()
            if restart_confirm in ("yes", "y"):
                # Use recursion one time only for restart
                return load_chip_set()
            else:
                continue
        else:
            print("Please enter 'yes' or 'restart'")
    
    # Ask to save
    save = validate_input("\nSave this chip set to file for future use? (yes/no)", bool, default=True)
    if save:
        try:
            with open(chip_file_path, "w") as f:
                for denom in sorted(chip_set.keys()):
                    f.write(f"{chip_set[denom]} ${format_denomination(denom)}\n")
            print(f"Chip set saved to {chip_file_path}")
        except Exception as e:
            print(f"Warning: Could not save chip set to file: {e}")
    
    print()
    return chip_set

def calculate_chip_distribution_custom(num_players: int, small_blind: float, big_blind: float, 
                                      target_stack: float, stack_size: int = 5) -> Dict[str, Any]:
    """
    Calculate optimal chip distribution for a custom stack size.
    
    Args:
        num_players: Number of players in the tournament
        small_blind: Starting small blind value
        big_blind: Starting big blind value
        target_stack: Desired stack value per player
        stack_size: Size of chip stacks to round to (e.g., 5 or 10)
        
    Returns:
        Dictionary with chip distribution per player and total stack value
    """
    # Input validation
    if num_players <= 0:
        raise ValueError("You need at least 1 player for a tournament")
    if num_players > 100:
        raise ValueError("Too many players! Maximum is 100 players")
    if small_blind <= 0:
        raise ValueError("Small blind must be at least 1")
    if big_blind <= 0:
        raise ValueError("Big blind must be at least 1")
    if small_blind > big_blind:
        raise ValueError("Small blind can't be bigger than big blind (that wouldn't make sense)")
    
    # Validate numeric values aren't infinity or NaN
    for val, name in [(num_players, "players"), (small_blind, "small blind"), 
                       (big_blind, "big blind"), (target_stack, "target stack")]:
        if math.isnan(val) or math.isinf(val):
            raise ValueError(f"Invalid {name} value - must be a normal number")
    
    if target_stack < big_blind * 100:
        raise ValueError("Stack size should be at least 100 big blinds")
    if target_stack > 10000000:
        raise ValueError("Stack size too large - must be under 10,000,000")
    
    # Available chip set
    available_chips = load_chip_set()
    
    # Validate chip inventory can support the players
    total_chip_value = sum(denom * count for denom, count in available_chips.items())
    max_stack_per_player = total_chip_value / num_players
    
    if target_stack > max_stack_per_player * 1.2:
        raise ValueError(f"Target stack ${target_stack:,.0f} is too large! With {num_players} players, "
                        f"maximum achievable is about ${max_stack_per_player:,.0f} per player")
    
    # Check minimum chip inventory
    if num_players > 1 and total_chip_value / num_players < big_blind * 50:
        raise ValueError(f"Not enough chips in your set for {num_players} players! "
                        f"Each player would get less than 50 big blinds")
    
    # Round target stack to nearest 100 for practical distribution
    target_stack = round(target_stack / 100) * 100
    
    # Now design chip distribution
    # Get all available denominations
    all_denoms = sorted(available_chips.keys())
    
    # Determine starting denomination
    if small_blind <= 2:
        # For very small blinds, we can use all denominations
        usable_denoms = all_denoms
    else:
        # Find the closest denomination that's at least the small blind
        usable_denoms = [d for d in all_denoms if d >= small_blind]
    
    if len(usable_denoms) == 0:
        return {'distribution': {}, 'stack_value': 0, 'big_blinds': 0, 
                'error': "No usable chip denominations found for the given blinds"}
    
    # Calculate maximum chips per player for each denomination based on available inventory
    max_per_player = {}
    for denom in usable_denoms:
        max_available = available_chips[denom] // num_players
        max_per_player[denom] = max_available
    
    desired_distribution = {}
    remaining_value = target_stack
    
    # Dynamic distribution strategy that scales with target_stack
    # Distribute chips from smallest to largest, using percentages
    
    # Step 1: Small denomination ($1) - 2% of stack, only for small blind ≤ 2
    if 1 in usable_denoms and small_blind <= 2 and max_per_player.get(1, 0) > 0:
        chip_count = int(remaining_value * 0.02 / 1)  # 2% of target stack
        chip_count = max(10, chip_count)  # At least 10 chips
        chip_count = round_to_stack_with_limit(chip_count, stack_size, max_per_player[1])
        if chip_count > 0:
            desired_distribution[1] = chip_count
            remaining_value -= 1 * chip_count
    
    # Step 2: $5 chips - 10% of remaining value
    if 5 in usable_denoms and remaining_value >= 5 and max_per_player.get(5, 0) > 0:
        chip_count = int(remaining_value * 0.10 / 5)
        chip_count = round_to_stack_with_limit(chip_count, stack_size, max_per_player[5])
        if chip_count > 0:
            desired_distribution[5] = chip_count
            remaining_value -= 5 * chip_count
    
    # Step 3: $25 chips - 15% of remaining value
    if 25 in usable_denoms and remaining_value >= 25 and max_per_player.get(25, 0) > 0:
        chip_count = int(remaining_value * 0.15 / 25)
        chip_count = round_to_stack_with_limit(chip_count, stack_size, max_per_player[25])
        if chip_count > 0:
            desired_distribution[25] = chip_count
            remaining_value -= 25 * chip_count
    
    # Step 4: $100 chips - 25% of remaining value
    if 100 in usable_denoms and remaining_value >= 100 and max_per_player.get(100, 0) > 0:
        chip_count = int(remaining_value * 0.25 / 100)
        chip_count = round_to_stack_with_limit(chip_count, stack_size, max_per_player[100])
        if chip_count > 0:
            desired_distribution[100] = chip_count
            remaining_value -= 100 * chip_count
    
    # Step 5: $500 chips - 20% of remaining value
    if 500 in usable_denoms and remaining_value >= 500 and max_per_player.get(500, 0) > 0:
        chip_count = int(remaining_value * 0.20 / 500)
        chip_count = round_to_stack_with_limit(chip_count, stack_size, max_per_player[500])
        if chip_count > 0:
            desired_distribution[500] = chip_count
            remaining_value -= 500 * chip_count
    
    # Step 6: $1000 chips - Use remaining value, trying to reach target
    if 1000 in usable_denoms and remaining_value >= 1000 and max_per_player.get(1000, 0) > 0:
        chip_count = int(remaining_value / 1000)
        chip_count = round_to_stack_with_limit(chip_count, stack_size, max_per_player[1000])
        if chip_count > 0:
            desired_distribution[1000] = chip_count
            remaining_value -= 1000 * chip_count
    
    # Step 7: Fill remaining gap with highest denomination available
    # Try to get as close as possible to target stack
    if remaining_value > 0:
        for denom in reversed(sorted(usable_denoms)):
            if remaining_value >= denom and max_per_player.get(denom, 0) > 0:
                current_count = desired_distribution.get(denom, 0)
                additional = int(remaining_value / denom)
                max_additional = max_per_player[denom] - current_count
                additional = min(additional, max_additional)
                
                if additional > 0:
                    # Round to stack size
                    new_count = current_count + additional
                    rounded_count = round_to_stack(new_count, stack_size)
                    if rounded_count > current_count:
                        desired_distribution[denom] = rounded_count
                        remaining_value -= denom * (rounded_count - current_count)
                        break
    
    # Calculate final stack value
    actual_stack_value = sum(denom * count for denom, count in desired_distribution.items())
    
    # Check if we have all chips available and ADJUST if needed
    chips_available = True
    shortage_info = []
    adjusted_distribution = desired_distribution.copy()
    
    for denom in adjusted_distribution:
        needed = adjusted_distribution[denom] * num_players
        available = available_chips[denom]
        
        if needed > available:
            chips_available = False
            shortage = needed - available
            # ACTUALLY ADJUST: reduce to maximum available chips per player
            max_per_player_actual = available // num_players
            old_count = adjusted_distribution[denom]
            
            # Try to round down to nearest stack size, but allow ANY amount if rounding gives 0
            adjusted_count = (max_per_player_actual // stack_size) * stack_size
            if adjusted_count == 0 and max_per_player_actual > 0:
                # Use whatever we can fit (even if not a full stack)
                adjusted_count = max_per_player_actual
            
            adjusted_distribution[denom] = adjusted_count
            shortage_info.append(f"Reduced ${denom} chips from {old_count} to {adjusted_count} per player (inventory limit)")
    
    # Recalculate actual stack value with adjusted distribution
    actual_stack_value = sum(denom * count for denom, count in adjusted_distribution.items())
    
    result = {
        'distribution': adjusted_distribution,
        'stack_value': actual_stack_value,
        'big_blinds': actual_stack_value / big_blind,
        'available_chips': available_chips
    }
    
    if not chips_available:
        result['warning'] = "Adjusted distribution to fit available chip inventory"
        result['shortage_info'] = shortage_info
    
    return result

def calculate_chip_distribution(num_players: int, small_blind: float, big_blind: float, 
                               duration_hours: float, minutes_per_level: int, 
                               stack_size: int = 1) -> Dict[str, Any]:
    """
    Calculate optimal poker chip distribution for tournament play.
    
    Args:
        num_players: Number of players in the tournament
        small_blind: Starting small blind value
        big_blind: Starting big blind value
        duration_hours: Expected tournament duration in hours
        minutes_per_level: Minutes between blind level increases
        stack_size: Size of chip stacks to round to (e.g., 5 or 10)
        
    Returns:
        Dictionary with chip distribution per player and total stack value
    """
    # Input validation
    if num_players <= 0:
        raise ValueError("You need at least 1 player for a tournament")
    if num_players > 100:
        raise ValueError("Too many players! Maximum is 100 players")
    if small_blind <= 0:
        raise ValueError("Small blind must be at least 1")
    if big_blind <= 0:
        raise ValueError("Big blind must be at least 1")
    if small_blind > big_blind:
        raise ValueError("Small blind can't be bigger than big blind (that wouldn't make sense)")
    if duration_hours <= 0:
        raise ValueError("Tournament duration must be longer than 0 hours")
    if duration_hours > 24:
        raise ValueError("Tournament duration too long! Maximum is 24 hours")
    if minutes_per_level <= 0:
        raise ValueError("Blind levels must be at least 1 minute long")
    if minutes_per_level > 240:
        raise ValueError("Blind levels too long! Maximum is 240 minutes (4 hours)")
    
    # Validate numeric values aren't infinity or NaN
    for val, name in [(num_players, "players"), (small_blind, "small blind"), 
                       (big_blind, "big blind"), (duration_hours, "duration"), 
                       (minutes_per_level, "minutes per level")]:
        if math.isnan(val) or math.isinf(val):
            raise ValueError(f"Invalid {name} value - must be a normal number")
    
    # Validate tournament duration vs blind intervals makes sense
    total_minutes = duration_hours * 60
    num_levels = int(total_minutes / minutes_per_level)
    if num_levels < 3:
        raise ValueError(f"Tournament too short! With {duration_hours} hours and {minutes_per_level} min/level, "
                        f"you only get {num_levels} blind levels. Try shorter blind intervals or longer duration")
    if num_levels > 100:
        raise ValueError(f"Too many blind levels! With {duration_hours} hours and {minutes_per_level} min/level, "
                        f"you get {num_levels} levels. Try longer blind intervals or shorter duration")
    
    # Available chip set
    available_chips = load_chip_set()
    
    # Validate chip inventory can support the players
    total_chip_value = sum(denom * count for denom, count in available_chips.items())
    max_stack_per_player = total_chip_value / num_players
    
    if num_players > 1 and total_chip_value / num_players < big_blind * 50:
        raise ValueError(f"Not enough chips in your set for {num_players} players! "
                        f"Each player would get less than 50 big blinds")
    
    # Calculate number of blind levels based on tournament duration
    total_minutes = duration_hours * 60
    num_levels = max(1, int(total_minutes / minutes_per_level))
    
    # Calculate blind structure progression
    # Use consistent 1.5x multiplier for all levels
    # This provides steady, predictable blind increases
    
    # Target finish: Level 14 with average stack of 12 BB
    # This balances tournament duration with available chip inventory
    target_end_level = 14
    target_end_bb = 12
    
    # Calculate what the big blind will be at the target end level
    current_bb = big_blind
    for level in range(1, target_end_level):
        # Multiply by 1.5 every level
        current_bb *= 1.5
    
    # Calculate starting stack needed to have target_end_bb at the end level
    target_stack = current_bb * target_end_bb
    
    # AUTO-ADJUSTMENT: If calculated stack exceeds available chips, adjust to maximum
    # This makes Mode 1 "dummy proof" - it always gives the best possible result
    stack_was_adjusted = False
    if target_stack > max_stack_per_player:
        stack_was_adjusted = True
        original_target = target_stack
        # Cap to 90% of maximum to leave safety margin for rounding
        target_stack = max_stack_per_player * 0.9
        target_stack = round(target_stack / 100) * 100
    else:
        # Round to nearest 100 for practical distribution
        target_stack = round(target_stack / 100) * 100
    
    # SMART SCALING: If we have significantly more chips available, scale up the stack
    # This ensures we use available chip inventory instead of leaving chips unused
    # Only scale up if we have at least 2x what the tournament mathematically needs
    if max_stack_per_player > target_stack * 2:
        # Scale up to use more chips, but cap at 70% of maximum to leave safety margin
        # This gives bigger stacks for better poker while staying within inventory
        scaled_target = min(target_stack * 2.5, max_stack_per_player * 0.7)
        scaled_target = round(scaled_target / 100) * 100
        target_stack = scaled_target
    
    # Ensure minimum reasonable stack (at least 100 BB to start)
    min_stack = big_blind * 100
    if target_stack < min_stack:
        target_stack = round(min_stack / 100) * 100
    
    # Now design chip distribution
    # Priority: Focus on middle denominations ($5, $25, $100)
    # Reduce $1 chips (don't last long) and limit high-value chips (come into play too late)
    
    # Find which denominations are usable
    # Modified rule: Prefer starting with $5 chips when possible
    # Only use $1 chips if small blind is $1 or $2
    # For higher blinds, start with the denomination closest to the small blind
    
    # Get all available denominations
    all_denoms = sorted(available_chips.keys())
    
    # Determine starting denomination
    if small_blind <= 2:
        # For very small blinds, we can use all denominations
        usable_denoms = all_denoms
    else:
        # Find the closest denomination that's at least the small blind
        usable_denoms = [d for d in all_denoms if d >= small_blind]
    
    if len(usable_denoms) == 0:
        return {'distribution': {}, 'stack_value': 0, 'big_blinds': 0, 
                'target_level': 0, 'total_levels': num_levels,
                'minutes_per_level': minutes_per_level,
                'error': "No usable chip denominations found for the given blinds"}
    
    # Calculate maximum chips per player for each denomination based on available inventory
    # This prevents us from allocating more than we have
    # Note: We DON'T round here - we'll round when actually allocating chips
    max_per_player = {}
    for denom in usable_denoms:
        max_available = available_chips[denom] // num_players
        max_per_player[denom] = max_available
    
    desired_distribution = {}
    remaining_value = target_stack
    
    # Dynamic distribution strategy that scales with target_stack
    # Distribute chips from smallest to largest, using percentages
    
    # Step 1: Small denomination ($1) - 2% of stack, only for small blind ≤ 2
    if 1 in usable_denoms and small_blind <= 2 and max_per_player.get(1, 0) > 0:
        chip_count = int(remaining_value * 0.02 / 1)  # 2% of target stack
        chip_count = max(10, chip_count)  # At least 10 chips
        chip_count = round_to_stack_with_limit(chip_count, stack_size, max_per_player[1])
        if chip_count > 0:
            desired_distribution[1] = chip_count
            remaining_value -= 1 * chip_count
    
    # Step 2: $5 chips - 10% of remaining value
    if 5 in usable_denoms and remaining_value >= 5 and max_per_player.get(5, 0) > 0:
        chip_count = int(remaining_value * 0.10 / 5)
        chip_count = round_to_stack_with_limit(chip_count, stack_size, max_per_player[5])
        if chip_count > 0:
            desired_distribution[5] = chip_count
            remaining_value -= 5 * chip_count
    
    # Step 3: $25 chips - 15% of remaining value
    if 25 in usable_denoms and remaining_value >= 25 and max_per_player.get(25, 0) > 0:
        chip_count = int(remaining_value * 0.15 / 25)
        chip_count = round_to_stack_with_limit(chip_count, stack_size, max_per_player[25])
        if chip_count > 0:
            desired_distribution[25] = chip_count
            remaining_value -= 25 * chip_count
    
    # Step 4: $100 chips - 25% of remaining value
    if 100 in usable_denoms and remaining_value >= 100 and max_per_player.get(100, 0) > 0:
        chip_count = int(remaining_value * 0.25 / 100)
        chip_count = round_to_stack_with_limit(chip_count, stack_size, max_per_player[100])
        if chip_count > 0:
            desired_distribution[100] = chip_count
            remaining_value -= 100 * chip_count
    
    # Step 5: $500 chips - 20% of remaining value
    if 500 in usable_denoms and remaining_value >= 500 and max_per_player.get(500, 0) > 0:
        chip_count = int(remaining_value * 0.20 / 500)
        chip_count = round_to_stack_with_limit(chip_count, stack_size, max_per_player[500])
        if chip_count > 0:
            desired_distribution[500] = chip_count
            remaining_value -= 500 * chip_count
    
    # Step 6: $1000 chips - Use ALL remaining value
    if 1000 in usable_denoms and remaining_value >= 1000 and max_per_player.get(1000, 0) > 0:
        chip_count = int(remaining_value / 1000)
        chip_count = round_to_stack_with_limit(chip_count, stack_size, max_per_player[1000])
        if chip_count > 0:
            desired_distribution[1000] = chip_count
            remaining_value -= 1000 * chip_count
    
    # Step 7: If we still have significant value left, distribute it to middle denominations
    # CRITICAL FIX: Round the TOTAL count, not just the additional amount!
    if remaining_value >= 500 and 100 in usable_denoms and max_per_player.get(100, 0) > 0:
        # Add more $100 chips with remaining value
        current = desired_distribution.get(100, 0)
        additional = int(remaining_value / 100)
        # Calculate the new total and round it properly
        new_total = current + additional
        max_allowed = max_per_player[100]
        # Round the TOTAL to maintain multiples of 5
        new_total = round_to_stack_with_limit(new_total, stack_size, max_allowed)
        if new_total > current:
            actual_additional = new_total - current
            desired_distribution[100] = new_total
            remaining_value -= 100 * actual_additional
    
    if remaining_value >= 100 and 25 in usable_denoms and max_per_player.get(25, 0) > 0:
        # Add more $25 chips with remaining value
        current = desired_distribution.get(25, 0)
        additional = int(remaining_value / 25)
        # Calculate the new total and round it properly
        new_total = current + additional
        max_allowed = max_per_player[25]
        # Round the TOTAL to maintain multiples of 5
        new_total = round_to_stack_with_limit(new_total, stack_size, max_allowed)
        if new_total > current:
            actual_additional = new_total - current
            desired_distribution[25] = new_total
            remaining_value -= 25 * actual_additional
    
    # Step 8: If still have remaining value, prioritize WORKHORSES over storage chips
    # Priority order: $100 (best), $25 (good), $5 (okay), then higher denoms if needed
    # CRITICAL FIX: Round the TOTAL count, not just the additional amount!
    if remaining_value > 0:
        # Try $100 first (the main workhorse)
        if 100 in usable_denoms and remaining_value >= 100 and max_per_player.get(100, 0) > 0:
            current = desired_distribution.get(100, 0)
            additional = int(remaining_value / 100)
            new_total = current + additional
            max_allowed = max_per_player[100]
            # Round the TOTAL to maintain multiples of 5
            new_total = round_to_stack_with_limit(new_total, stack_size, max_allowed)
            if new_total > current:
                actual_additional = new_total - current
                desired_distribution[100] = new_total
                remaining_value -= 100 * actual_additional
        
        # If still remaining, try $500/$1000 as last resort (allow small amounts to avoid waste)
        # Use allow_small=True to permit 1-4 chip allocations when it prevents waste
        if remaining_value >= 500:
            if 500 in usable_denoms and max_per_player.get(500, 0) > 0:
                current = desired_distribution.get(500, 0)
                max_allowed = max_per_player[500]
                additional = int(remaining_value / 500)
                if additional > 0:
                    # Allow small allocations (1-4 chips) when redistributing to avoid waste
                    new_total = round_to_stack_with_limit(current + additional, stack_size, max_allowed, allow_small=True)
                    if new_total > current:
                        actual_additional = new_total - current
                        desired_distribution[500] = new_total
                        remaining_value -= 500 * actual_additional
        
        if remaining_value >= 1000:
            if 1000 in usable_denoms and max_per_player.get(1000, 0) > 0:
                current = desired_distribution.get(1000, 0)
                max_allowed = max_per_player[1000]
                additional = int(remaining_value / 1000)
                if additional > 0:
                    # Allow small allocations (1-4 chips) when redistributing to avoid waste
                    new_total = round_to_stack_with_limit(current + additional, stack_size, max_allowed, allow_small=True)
                    if new_total > current:
                        actual_additional = new_total - current
                        desired_distribution[1000] = new_total
                        remaining_value -= 1000 * actual_additional
    
    # Note: Stack value may not be exactly at target since we prioritize
    # easy-to-count chip stacks (multiples of 5) over precise values
    
    # Step 5: Check if we have enough chips in the set
    final_distribution = {}
    chips_available = True
    shortage_info = []
    
    for denom, count_per_player in desired_distribution.items():
        total_needed = count_per_player * num_players
        if total_needed > available_chips[denom]:
            chips_available = False
            shortage_info.append(f"${format_denomination(denom)} chips: need {total_needed}, have {available_chips[denom]}")
    
    # If not enough chips, adjust the distribution
    if not chips_available:
        # Reduce chip counts to fit available inventory
        attempts = 0
        max_attempts = 20
        
        while not chips_available and attempts < max_attempts:
            attempts += 1
            
            # Find which denomination is over limit
            for denom in sorted(desired_distribution.keys(), reverse=True):  # Start with highest denominations
                total_needed = desired_distribution[denom] * num_players
                if total_needed > available_chips[denom]:
                    # Calculate max chips per player that fits inventory
                    max_per_player = available_chips[denom] // num_players
                    
                    # Round DOWN to nearest stack of 5, ensuring we don't exceed available chips
                    max_per_player = (max_per_player // 5) * 5
                    
                    # Double-check this doesn't exceed available inventory
                    while max_per_player > 0 and (max_per_player * num_players) > available_chips[denom]:
                        max_per_player -= 5
                    
                    # Make sure we don't go negative
                    max_per_player = max(0, max_per_player)
                    
                    # Calculate value lost by reducing this denomination
                    value_lost = denom * (desired_distribution[denom] - max_per_player)
                    desired_distribution[denom] = max_per_player
                    
                    # Try to compensate with lower denominations if value was lost
                    if value_lost > 0:
                        for lower_denom in sorted([d for d in desired_distribution.keys() if d < denom]):
                            if lower_denom in available_chips:
                                # How many chips of this lower denom would replace the value?
                                additional_chips = int(value_lost / lower_denom)
                                additional_chips = (additional_chips // 5) * 5  # Keep stacks of 5
                                
                                # Check if we have room for these additional chips
                                current_total = (desired_distribution.get(lower_denom, 0) + additional_chips) * num_players
                                if current_total <= available_chips[lower_denom]:
                                    desired_distribution[lower_denom] = desired_distribution.get(lower_denom, 0) + additional_chips
                                    value_lost -= lower_denom * additional_chips
                                    if value_lost <= 0:
                                        break
            
            # Check if all denominations now fit
            chips_available = True
            shortage_info = []
            for denom, count_per_player in desired_distribution.items():
                total_needed = count_per_player * num_players
                if total_needed > available_chips[denom]:
                    chips_available = False
                    shortage_info.append(f"${format_denomination(denom)} chips: need {total_needed}, have {available_chips[denom]}")
    
    # FINAL ENFORCEMENT: If still short after all attempts, force fit to inventory
    if not chips_available:
        for denom in desired_distribution:
            total_needed = desired_distribution[denom] * num_players
            if total_needed > available_chips[denom]:
                # Force reduction to maximum available
                max_per_player = available_chips[denom] // num_players
                # Try to round down to nearest multiple of 5, but allow any amount if rounding gives 0
                rounded = (max_per_player // 5) * 5
                if rounded == 0 and max_per_player > 0:
                    # Use whatever we can fit (even if not a full stack of 5)
                    rounded = max_per_player
                desired_distribution[denom] = max(0, rounded)
    
    final_distribution = desired_distribution
    
    # Calculate actual starting stack
    actual_stack = sum(denom * count for denom, count in final_distribution.items())
    
    # Calculate big blinds
    starting_big_blinds = actual_stack / big_blind if big_blind > 0 else 0
    
    result = {
        'distribution': final_distribution,
        'stack_value': actual_stack,
        'big_blinds': starting_big_blinds,
        'target_level': target_end_level,
        'total_levels': num_levels,
        'minutes_per_level': minutes_per_level,
        'available_chips': available_chips,
        'stack_size': stack_size,
        'stack_was_adjusted': stack_was_adjusted,
        'max_stack_per_player': max_stack_per_player
    }
    
    # Note: We've enforced chip availability, so warning/shortage_info are for informational purposes only
    # The actual distribution will always fit within available inventory
    
    return result


def clear_screen():
    """Clear the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    """Main program function."""
    try:
        while True:
            clear_screen()
            print("=" * 50)
            print("POKER TOURNAMENT CHIP CALCULATOR")
            print("=" * 50)
            print("\nLet's set up your poker tournament!")
            
            # Get inputs with validation
            try:
                num_players = validate_input("\nHow many players will be at the table?", int, 2, 50)
                small_blind = validate_input("What's the starting small blind amount?", float, 0.01, 10000, default=1)
                
                # Ensure big blind is properly validated against small blind
                while True:
                    big_blind = validate_input("What's the starting big blind amount?", float, small_blind, 20000, default=2)
                    if big_blind < small_blind:
                        print(f"Oops! Big blind (${big_blind}) must be equal to or larger than small blind (${small_blind})")
                        continue
                    break
                
                # Ask user which mode they want
                print("\nHow would you like to determine stack size?")
                print("  1. Auto-calculate based on tournament duration")
                print("  2. I'll specify the exact stack amount")
                mode_choice = validate_input("Enter your choice (1 or 2)", int, 1, 2, default=1)
                
                # Use a fixed stack size of 5 with preference for round numbers
                stack_size = 5
                
                if mode_choice == 1:
                    # Auto-calculate mode (current behavior)
                    duration = validate_input("How long should the tournament last? (hours)", float, 0.5, 12)
                    blind_interval = validate_input("How often should blinds increase? (minutes)", int, 5, 240, 20)
                    
                    # Validate duration vs blind interval relationship
                    num_blind_levels = int((duration * 60) / blind_interval)
                    if num_blind_levels < 3:
                        print(f"\nOops! With {duration} hours and {blind_interval} min/level, you only get {num_blind_levels} blind levels.")
                        print("That's too short for a good tournament!")
                        input("\nPress Enter to try again...")
                        continue
                    if num_blind_levels > 100:
                        print(f"\nOops! With {duration} hours and {blind_interval} min/level, you get {num_blind_levels} blind levels.")
                        print("That's way too many levels!")
                        input("\nPress Enter to try again...")
                        continue
                    
                    print("\nCalculating the perfect chip distribution...")
                    
                    # Calculate distribution
                    result = calculate_chip_distribution(num_players, small_blind, big_blind, duration, blind_interval, stack_size)
                else:
                    # Custom stack mode
                    custom_stack = validate_input("What stack size do you want per player? (e.g., 8500)", float, big_blind * 100, 100000)
                    
                    print("\nCalculating chip distribution for your custom stack...")
                    
                    # Calculate distribution with custom stack
                    result = calculate_chip_distribution_custom(num_players, small_blind, big_blind, custom_stack, stack_size)
                
                # Check for errors
                if 'error' in result:
                    print(f"\nOops! {result['error']}")
                    input("\nPress Enter to try again...")
                    continue
                
                # Display results
                print("\n" + "=" * 50)
                print("RECOMMENDED CHIPS FOR EACH PLAYER")
                print("=" * 50)
                
                if not result['distribution']:
                    print("Sorry! We couldn't calculate a good chip distribution with these settings.")
                else:
                    for denom in sorted(result['distribution'].keys()):
                        count = result['distribution'][denom]
                        value = denom * count
                        denom_str = format_denomination(denom)
                        value_str = format_denomination(value)
                        print(f"${denom_str:>6} chips: {count:>2} chips = ${value_str:>8}")
                    
                    print("-" * 50)
                    print(f"Total Stack Value: ${format_denomination(result['stack_value'])}")
                    print(f"Starting Big Blinds: {result['big_blinds']:.1f} BB")
                    print(f"Total Chips per Player: {sum(result['distribution'].values())} chips")
                    print("All chips in stacks of 5 or 10 for easy counting and distribution")
                    
                    # Display warnings if any
                    if 'warning' in result:
                        print("\n" + "!" * 50)
                        print(f"HEADS UP: {result['warning']}")
                        if 'shortage_info' in result:
                            for info in result['shortage_info']:
                                print(f"  - {info}")
                        print("!" * 50)
                    
                    # Only show tournament details if auto-calculated (mode 1)
                    if mode_choice == 1:
                        print("\n" + "=" * 50)
                        print("TOURNAMENT DETAILS")
                        print("=" * 50)
                        print(f"Tournament Length: {duration} hours")
                        print(f"Total Blind Levels: {result['total_levels']} levels")
                        print(f"Time Between Levels: {result['minutes_per_level']} minutes")
                        print(f"Stack designed to last: {result['target_level']} levels comfortably")
                        
                        # Show adjustment message if stack was auto-adjusted to fit chip inventory
                        if result.get('stack_was_adjusted', False):
                            print("\n📊 AUTO-ADJUSTED:")
                            print(f"   Stack size optimized to fit your chip set for {num_players} players")
                            print(f"   (Maximum available: ${result.get('max_stack_per_player', 0):,.0f} per player)")
                    
                    # Show total chips needed from set
                    print("\n" + "=" * 50)
                    print("CHIPS NEEDED FROM YOUR SET")
                    print("=" * 50)
                    
                    for denom in sorted(result['distribution'].keys()):
                        total_needed = result['distribution'][denom] * num_players
                        available = result['available_chips'].get(denom, 0)
                        denom_str = format_denomination(denom)
                        if total_needed <= available:
                            status = "You have enough"
                        else:
                            status = f"Need {total_needed - available} more"
                        print(f"{total_needed:>3} x ${denom_str:<6} chips (you have: {available:>3}) {status}")
                
                # Ask to run again or exit
                print("\n" + "=" * 50)
                run_again = validate_input("Want to calculate another tournament? (yes/no)", bool, default=True)
                if not run_again:
                    print("\nThanks for using the Poker Tournament Chip Calculator!")
                    break
                    
            except ValueError as e:
                print(f"\nOops! {str(e)}")
                input("\nPress Enter to try again...")
                
            except Exception as e:
                print(f"\nSomething went wrong: {str(e)}")
                input("\nPress Enter to try again...")
                
    except KeyboardInterrupt:
        print("\n\nCalculator closed.")
    except Exception as e:
        print(f"\nSorry, we hit a problem: {str(e)}")
        input("\nPress Enter to exit...")
    
    print("\nSee you at the poker table!")


if __name__ == "__main__":
    main()