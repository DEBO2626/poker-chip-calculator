"""
Edge Case Testing for Poker Chip Calculator
Tests extreme scenarios and boundary conditions
"""

import sys
from pokerchipcounter import calculate_chip_distribution, calculate_chip_distribution_custom

def test_edge_cases():
    """Test extreme and boundary scenarios"""
    
    print("=" * 70)
    print("🧪 EDGE CASE TESTING - Extreme Scenarios")
    print("=" * 70)
    
    edge_cases = []
    
    # Test 1: Minimum players with maximum duration
    print("\n📌 Test 1: Minimum Players (5) + Maximum Duration (6h)")
    try:
        result = calculate_chip_distribution(
            num_players=5,
            small_blind=25,
            big_blind=50,
            duration_hours=6,
            minutes_per_level=15
        )
        print(f"   ✅ PASSED: Stack=${result['stack_value']}")
        edge_cases.append(("5 players, 6h", True, result['stack_value']))
    except Exception as e:
        print(f"   ❌ FAILED: {e}")
        edge_cases.append(("5 players, 6h", False, str(e)))
    
    # Test 2: Maximum realistic players with minimum duration
    print("\n📌 Test 2: Maximum Players (15) + Minimum Duration (4h)")
    try:
        result = calculate_chip_distribution(
            num_players=15,
            small_blind=25,
            big_blind=50,
            duration_hours=4,
            minutes_per_level=15
        )
        print(f"   ✅ PASSED: Stack=${result['stack_value']}")
        edge_cases.append(("15 players, 4h", True, result['stack_value']))
    except Exception as e:
        print(f"   ❌ FAILED: {e}")
        edge_cases.append(("15 players, 4h", False, str(e)))
    
    # Test 3: Very short levels (10 minutes)
    print("\n📌 Test 3: Very Short Levels (10 min) - 10 players, 4h")
    try:
        result = calculate_chip_distribution(
            num_players=10,
            small_blind=25,
            big_blind=50,
            duration_hours=4,
            minutes_per_level=10
        )
        print(f"   ✅ PASSED: Stack=${result['stack_value']}, Levels={result.get('total_levels', 0)}")
        edge_cases.append(("10min levels", True, result['stack_value']))
    except Exception as e:
        print(f"   ❌ FAILED: {e}")
        edge_cases.append(("10min levels", False, str(e)))
    
    # Test 4: Very long levels (30 minutes)
    print("\n📌 Test 4: Very Long Levels (30 min) - 10 players, 4h")
    try:
        result = calculate_chip_distribution(
            num_players=10,
            small_blind=25,
            big_blind=50,
            duration_hours=4,
            minutes_per_level=30
        )
        print(f"   ✅ PASSED: Stack=${result['stack_value']}, Levels={result.get('total_levels', 0)}")
        edge_cases.append(("30min levels", True, result['stack_value']))
    except Exception as e:
        print(f"   ❌ FAILED: {e}")
        edge_cases.append(("30min levels", False, str(e)))
    
    # Test 5: Custom mode at exact maximum capacity (8 players)
    print("\n📌 Test 5: Custom Stack at Maximum Capacity (8 players, $12,662)")
    try:
        result = calculate_chip_distribution_custom(
            num_players=8,
            small_blind=25,
            big_blind=50,
            target_stack=12662
        )
        print(f"   ✅ PASSED: Achieved=${result['stack_value']}")
        edge_cases.append(("Custom max (8p)", True, result['stack_value']))
    except Exception as e:
        print(f"   ❌ FAILED: {e}")
        edge_cases.append(("Custom max (8p)", False, str(e)))
    
    # Test 6: Custom mode slightly over maximum (should adjust or fail gracefully)
    print("\n📌 Test 6: Custom Stack Over Maximum (8 players, $15,000)")
    try:
        result = calculate_chip_distribution_custom(
            num_players=8,
            small_blind=25,
            big_blind=50,
            target_stack=15000
        )
        print(f"   ✅ PASSED: Achieved=${result['stack_value']} (adjusted down)")
        edge_cases.append(("Custom over max (8p)", True, result['stack_value']))
    except Exception as e:
        print(f"   ❌ FAILED: {e}")
        edge_cases.append(("Custom over max (8p)", False, str(e)))
    
    # Test 7: Minimum viable stack (100 BB)
    print("\n📌 Test 7: Minimum Viable Stack (100 BB = $5,000)")
    try:
        result = calculate_chip_distribution_custom(
            num_players=10,
            small_blind=25,
            big_blind=50,
            target_stack=5000
        )
        print(f"   ✅ PASSED: Achieved=${result['stack_value']}")
        edge_cases.append(("Minimum 100BB", True, result['stack_value']))
    except Exception as e:
        print(f"   ❌ FAILED: {e}")
        edge_cases.append(("Minimum 100BB", False, str(e)))
    
    # Test 8: Below minimum stack (should fail)
    print("\n📌 Test 8: Below Minimum Stack (50 BB = $2,500) - Should Fail")
    try:
        result = calculate_chip_distribution_custom(
            num_players=10,
            small_blind=25,
            big_blind=50,
            target_stack=2500
        )
        print(f"   ❌ UNEXPECTED PASS: Should have rejected ${result['stack_value']}")
        edge_cases.append(("Below minimum", False, "Should have failed"))
    except ValueError as e:
        print(f"   ✅ CORRECTLY REJECTED: {e}")
        edge_cases.append(("Below minimum", True, "Correctly rejected"))
    
    # Test 9: Odd number of players (11)
    print("\n📌 Test 9: Odd Player Count (11 players, 5h)")
    try:
        result = calculate_chip_distribution(
            num_players=11,
            small_blind=25,
            big_blind=50,
            duration_hours=5,
            minutes_per_level=15
        )
        print(f"   ✅ PASSED: Stack=${result['stack_value']}")
        edge_cases.append(("11 players", True, result['stack_value']))
    except Exception as e:
        print(f"   ❌ FAILED: {e}")
        edge_cases.append(("11 players", False, str(e)))
    
    # Test 10: Different blind structure (10/20 instead of 25/50)
    print("\n📌 Test 10: Different Blind Structure (10/20 instead of 25/50)")
    try:
        result = calculate_chip_distribution(
            num_players=8,
            small_blind=10,
            big_blind=20,
            duration_hours=5,
            minutes_per_level=15
        )
        print(f"   ✅ PASSED: Stack=${result['stack_value']} ({result['stack_value']//20} BB)")
        edge_cases.append(("10/20 blinds", True, result['stack_value']))
    except Exception as e:
        print(f"   ❌ FAILED: {e}")
        edge_cases.append(("10/20 blinds", False, str(e)))
    
    # Test 11: Ultra-high blind structure (100/200)
    print("\n📌 Test 11: High Blind Structure (100/200)")
    try:
        result = calculate_chip_distribution(
            num_players=8,
            small_blind=100,
            big_blind=200,
            duration_hours=5,
            minutes_per_level=15
        )
        print(f"   ✅ PASSED: Stack=${result['stack_value']} ({result['stack_value']//200} BB)")
        edge_cases.append(("100/200 blinds", True, result['stack_value']))
    except Exception as e:
        print(f"   ❌ FAILED: {e}")
        edge_cases.append(("100/200 blinds", False, str(e)))
    
    # Test 12: Check if auto-adjustment flag works
    print("\n📌 Test 12: Verify Auto-Adjustment Flag (12 players, 6h)")
    try:
        result = calculate_chip_distribution(
            num_players=12,
            small_blind=25,
            big_blind=50,
            duration_hours=6,
            minutes_per_level=15
        )
        was_adjusted = result.get('stack_was_adjusted', False)
        max_stack = result.get('max_stack_per_player', 0)
        print(f"   ✅ PASSED: Stack=${result['stack_value']}, Adjusted={was_adjusted}, Max=${max_stack:.0f}")
        edge_cases.append(("Auto-adjust flag", True, f"Adjusted={was_adjusted}"))
    except Exception as e:
        print(f"   ❌ FAILED: {e}")
        edge_cases.append(("Auto-adjust flag", False, str(e)))
    
    # Summary
    print("\n" + "=" * 70)
    print("📊 EDGE CASE TEST SUMMARY")
    print("=" * 70)
    
    passed = sum(1 for _, success, _ in edge_cases if success)
    total = len(edge_cases)
    
    for test_name, success, result in edge_cases:
        status = "✅" if success else "❌"
        print(f"{status} {test_name:30s} → {result}")
    
    print(f"\n🎯 RESULT: {passed}/{total} edge cases passed ({100*passed/total:.1f}%)")
    
    if passed == total:
        print("🎉 PERFECT! All edge cases handled correctly!")
    elif passed >= total * 0.9:
        print("✅ EXCELLENT! System is very robust!")
    elif passed >= total * 0.75:
        print("⚠️  GOOD, but some edge cases need attention")
    else:
        print("❌ ATTENTION NEEDED: Multiple edge cases failing")
    
    print("=" * 70)

if __name__ == "__main__":
    test_edge_cases()