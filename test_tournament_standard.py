"""Test tournament-standard chip distribution (no 1-4 chip allocations)"""

import sys
sys.path.insert(0, r"c:\Users\john_\Desktop\Poker chip")

from pokerchipcounter import calculate_chip_distribution, load_chip_set

def test_13_players():
    """Test the exact scenario user reported: 13 players, 4.5 hours, 12 min intervals"""
    print("=" * 60)
    print("TEST: 13 Players (Tournament Standard)")
    print("=" * 60)
    
    chip_set = load_chip_set()
    
    result = calculate_chip_distribution(
        num_players=13,
        small_blind=1,
        big_blind=2,
        duration_hours=4.5,
        minutes_per_level=12,
        stack_size=5
    )
    
    print(f"\nStack Value: ${result['stack_value']:,.0f}")
    print(f"Starting BB: {result['big_blinds']:.1f} BB")
    print("\nChip Distribution per Player:")
    
    # Check for violations
    violations = []
    
    for denom in sorted(result['distribution'].keys()):
        count = result['distribution'][denom]
        value = count * denom
        print(f"  ${denom:>6} chips: {count:>2} chips = ${value:>8,}")
        
        # Flag any 1-4 chip allocations
        if 1 <= count <= 4:
            violations.append(f"  ❌ VIOLATION: ${denom} chips has {count} chips (should be 0 or ≥5)")
    
    print(f"\nTotal Chips per Player: {sum(result['distribution'].values())} chips")
    
    # Report violations
    if violations:
        print("\n" + "=" * 60)
        print("⚠️  TOURNAMENT STANDARD VIOLATIONS:")
        print("=" * 60)
        for v in violations:
            print(v)
        return False
    else:
        print("\n" + "=" * 60)
        print("✅ TOURNAMENT STANDARD: All denominations in stacks of 5+")
        print("=" * 60)
        return True

def test_multiple_player_counts():
    """Test various player counts to ensure no violations"""
    chip_set = load_chip_set()
    
    print("\n" + "=" * 60)
    print("TEST: Various Player Counts (8-16 players)")
    print("=" * 60)
    
    all_passed = True
    
    for players in range(8, 17):
        result = calculate_chip_distribution(
            num_players=players,
            small_blind=1,
            big_blind=2,
            duration_hours=4.0,
            minutes_per_level=15,
            stack_size=5
        )
        
        # Check for violations
        violations = []
        for denom, count in result['distribution'].items():
            if 1 <= count <= 4:
                violations.append(f"${denom}: {count} chips")
        
        status = "✅ PASS" if not violations else f"❌ FAIL: {', '.join(violations)}"
        print(f"{players:2} players: {status}")
        
        if violations:
            all_passed = False
    
    return all_passed

if __name__ == "__main__":
    print("\n🎯 Testing Tournament-Standard Chip Distribution")
    print("=" * 60)
    print("Rule: All denominations must be 0 or ≥5 chips per player")
    print("=" * 60)
    
    test1 = test_13_players()
    test2 = test_multiple_player_counts()
    
    print("\n" + "=" * 60)
    print("FINAL RESULT")
    print("=" * 60)
    
    if test1 and test2:
        print("✅ ALL TESTS PASSED - Tournament standard enforced!")
    else:
        print("❌ SOME TESTS FAILED - Still have 1-4 chip allocations")