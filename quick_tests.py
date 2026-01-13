"""Quick test scenarios for poker chip calculator"""
import math

def simulate_blinds_constant(starting_bb, target_level, multiplier=1.5):
    """Simulate blind progression with constant multiplier"""
    current_bb = starting_bb
    print(f"\nBlind Progression (starting BB = ${starting_bb}, {multiplier}× every level):")
    print(f"Level 1:  SB ${starting_bb/2:.0f} / BB ${starting_bb:.0f}")
    
    for level in range(1, target_level):
        current_bb *= multiplier
        print(f"Level {level+1:2d}: SB ${current_bb/2:,.0f} / BB ${current_bb:,.0f}")
    
    return current_bb

def test_scenario(players, sb, bb, hours, min_per_level, target_level=19):
    """Test a specific tournament scenario"""
    print("\n" + "="*70)
    print(f"SCENARIO: {players} players, ${sb}/${bb} blinds, {hours}h, {min_per_level} min/level")
    print("="*70)
    
    total_levels = int((hours * 60) / min_per_level)
    print(f"Total possible levels: {total_levels}")
    
    # Calculate what BB will be at target level with 1.5× constant
    final_bb = simulate_blinds_constant(bb, target_level, 1.5)
    
    required_stack = final_bb * 12  # Target 12 BB at target level
    print(f"\n>>> BB at level {target_level}: ${final_bb:,.2f}")
    print(f">>> Required starting stack (12 BB): ${required_stack:,.2f}")
    
    # Available chips per player
    available_per_player = {
        1: 300 // players,
        5: 200 // players,
        25: 200 // players,
        100: 200 // players,
        500: 50 // players,
        1000: 50 // players
    }
    
    max_value = sum(denom * count for denom, count in available_per_player.items())
    print(f">>> Max available per player from chip set: ${max_value:,.0f}")
    print(f">>> Starting big blinds with ${max_value}: {max_value/bb:.0f} BB")
    
    if required_stack > max_value:
        print(f"\n⚠️  PROBLEM: Need ${required_stack:,.0f} but only ${max_value:,.0f} available!")
        print(f"   Short by: ${required_stack - max_value:,.0f}")
    else:
        print(f"\n✓ Achievable with available chips")
        print(f"   Actual starting stack: ${required_stack:,.0f} ({required_stack/bb:.0f} BB)")

# Run tests
print("TESTING POKER CHIP CALCULATOR")
print("Blind structure: 1.5× CONSTANT for ALL levels")

# User's typical game
test_scenario(12, 1, 2, 4.5, 12, target_level=19)

# Try different target levels
print("\n\n" + "="*70)
print("TESTING DIFFERENT TARGET LEVELS (12 players, 1/2 blinds, 4.5h)")
print("="*70)

for target in [14, 16, 18, 20]:
    test_scenario(12, 1, 2, 4.5, 12, target_level=target)