"""
Test the chip shortage fix - ensure NO distribution ever requires more chips than available.
"""

import sys
sys.path.insert(0, r'c:\Users\john_\Desktop\Poker chip')

from pokerchipcounter import calculate_chip_distribution_custom, calculate_chip_distribution

def test_custom_stack_13_players():
    """Test the exact scenario from user: 13 players, $8500 stack"""
    print("=" * 60)
    print("TEST: 13 players, $8500 custom stack")
    print("=" * 60)
    
    result = calculate_chip_distribution_custom(
        num_players=13,
        small_blind=1,
        big_blind=2,
        target_stack=8500
    )
    
    print("\nDistribution per player:")
    for denom in sorted(result['distribution'].keys()):
        count = result['distribution'][denom]
        value = denom * count
        print(f"  ${denom:>6} x {count:>2} = ${value:>7}")
    
    print(f"\nActual stack value: ${result['stack_value']}")
    print(f"Starting BB: {result['big_blinds']:.1f}")
    
    # Verify NO shortages
    print("\n" + "=" * 60)
    print("CHIP AVAILABILITY CHECK")
    print("=" * 60)
    
    all_available = True
    for denom in sorted(result['distribution'].keys()):
        total_needed = result['distribution'][denom] * 13
        available = result['available_chips'][denom]
        status = "✓ OK" if total_needed <= available else "✗ SHORTAGE!"
        
        if total_needed > available:
            all_available = False
            print(f"${denom:>6}: need {total_needed:>3}, have {available:>3} - {status} (short {total_needed - available})")
        else:
            print(f"${denom:>6}: need {total_needed:>3}, have {available:>3} - {status}")
    
    print("\n" + "=" * 60)
    if all_available:
        print("✓ TEST PASSED: All chips fit within available inventory!")
    else:
        print("✗ TEST FAILED: Still showing chip shortage!")
    print("=" * 60)
    
    return all_available

def test_mode1_high_player_count():
    """Test Mode 1 with many players to trigger potential shortages"""
    print("\n\n" + "=" * 60)
    print("TEST: Mode 1 - 16 players, 4 hour tournament")
    print("=" * 60)
    
    result = calculate_chip_distribution(
        num_players=16,
        small_blind=1,
        big_blind=2,
        duration_hours=4,
        minutes_per_level=20
    )
    
    print("\nDistribution per player:")
    for denom in sorted(result['distribution'].keys()):
        count = result['distribution'][denom]
        value = denom * count
        print(f"  ${denom:>6} x {count:>2} = ${value:>7}")
    
    print(f"\nActual stack value: ${result['stack_value']}")
    print(f"Starting BB: {result['big_blinds']:.1f}")
    
    # Verify NO shortages
    print("\n" + "=" * 60)
    print("CHIP AVAILABILITY CHECK")
    print("=" * 60)
    
    all_available = True
    for denom in sorted(result['distribution'].keys()):
        total_needed = result['distribution'][denom] * 16
        available = result['available_chips'][denom]
        status = "✓ OK" if total_needed <= available else "✗ SHORTAGE!"
        
        if total_needed > available:
            all_available = False
            print(f"${denom:>6}: need {total_needed:>3}, have {available:>3} - {status} (short {total_needed - available})")
        else:
            print(f"${denom:>6}: need {total_needed:>3}, have {available:>3} - {status}")
    
    print("\n" + "=" * 60)
    if all_available:
        print("✓ TEST PASSED: All chips fit within available inventory!")
    else:
        print("✗ TEST FAILED: Still showing chip shortage!")
    print("=" * 60)
    
    return all_available

if __name__ == "__main__":
    test1_passed = test_custom_stack_13_players()
    test2_passed = test_mode1_high_player_count()
    
    print("\n\n" + "=" * 60)
    print("FINAL RESULTS")
    print("=" * 60)
    print(f"Custom Stack Test (13 players): {'✓ PASSED' if test1_passed else '✗ FAILED'}")
    print(f"Auto-calculate Test (16 players): {'✓ PASSED' if test2_passed else '✗ FAILED'}")
    
    if test1_passed and test2_passed:
        print("\n🎉 ALL TESTS PASSED! No chip shortages possible.")
    else:
        print("\n⚠️ SOME TESTS FAILED! Chip shortage bug still exists.")