"""
Comprehensive System Test
Tests all combinations of:
- Players: 5-15
- Tournament durations: 4-6 hours
- Custom stacks: $5,000 - $10,000
"""

import sys
from pokerchipcounter import calculate_chip_distribution, calculate_chip_distribution_custom

# Available chip set
CHIP_SET = {
    1: 300,
    5: 200,
    25: 200,
    100: 200,
    500: 50,
    1000: 50
}

def check_shortage(distribution, num_players, chip_set):
    """Check if distribution causes any chip shortage"""
    shortages = []
    for denom, count_per_player in distribution.items():
        total_needed = count_per_player * num_players
        available = chip_set[denom]
        if total_needed > available:
            shortages.append({
                'denom': denom,
                'needed': total_needed,
                'available': available,
                'short': total_needed - available
            })
    return shortages

def calculate_stack_value(distribution):
    """Calculate total stack value from distribution"""
    return sum(denom * count for denom, count in distribution.items())

def test_mode1_auto_calculate():
    """Test Mode 1: Auto-calculate with varying players and duration"""
    print("=" * 80)
    print("MODE 1: AUTO-CALCULATE (Duration-Based)")
    print("=" * 80)
    
    results = []
    total_tests = 0
    passed_tests = 0
    failed_tests = 0
    
    for num_players in range(5, 16):  # 5-15 players
        for duration_hours in [4, 5, 6]:  # 4-6 hours
            total_tests += 1
            
            # Test parameters
            small_blind = 5
            big_blind = 10
            minutes_per_level = 20
            
            try:
                result = calculate_chip_distribution(
                    num_players, 
                    small_blind, 
                    big_blind, 
                    duration_hours, 
                    minutes_per_level
                )
                
                distribution = result['distribution']
                stack = result['stack_value']
                
                # Check for shortages
                shortages = check_shortage(distribution, num_players, CHIP_SET)
                
                if shortages:
                    status = "❌ FAIL"
                    failed_tests += 1
                else:
                    status = "✓ PASS"
                    passed_tests += 1
                
                results.append({
                    'players': num_players,
                    'duration': duration_hours,
                    'stack': stack,
                    'shortages': shortages,
                    'status': status,
                    'distribution': distribution
                })
                
            except Exception as e:
                failed_tests += 1
                results.append({
                    'players': num_players,
                    'duration': duration_hours,
                    'error': str(e),
                    'status': "❌ ERROR"
                })
    
    # Print summary
    print(f"\nTotal Tests: {total_tests}")
    print(f"Passed: {passed_tests}")
    print(f"Failed: {failed_tests}")
    print(f"Success Rate: {(passed_tests/total_tests)*100:.1f}%\n")
    
    # Print detailed results
    print(f"{'Players':<10}{'Duration':<12}{'Stack':<12}{'Status':<10}{'Issues'}")
    print("-" * 80)
    
    for r in results:
        players = r['players']
        duration = f"{r['duration']}h" if 'duration' in r else 'N/A'
        stack = f"${r['stack']:,}" if 'stack' in r else 'N/A'
        status = r['status']
        
        if 'error' in r:
            issues = f"ERROR: {r['error']}"
        elif r.get('shortages'):
            issues = f"Shortages: {len(r['shortages'])} denominations"
        else:
            issues = "None"
        
        print(f"{players:<10}{duration:<12}{stack:<12}{status:<10}{issues}")
    
    # Print failures in detail
    if failed_tests > 0:
        print("\n" + "=" * 80)
        print("DETAILED FAILURE ANALYSIS")
        print("=" * 80)
        for r in results:
            if r['status'] != "✓ PASS":
                print(f"\n{r['players']} players, {r.get('duration', 'N/A')}h:")
                if 'shortages' in r and r['shortages']:
                    for s in r['shortages']:
                        print(f"  - ${s['denom']}: Need {s['needed']}, Have {s['available']}, Short {s['short']}")
                if 'error' in r:
                    print(f"  - Error: {r['error']}")
    
    return results, passed_tests, failed_tests

def test_mode2_custom_stack():
    """Test Mode 2: Custom stack with varying players and stack sizes"""
    print("\n" + "=" * 80)
    print("MODE 2: CUSTOM STACK")
    print("=" * 80)
    
    results = []
    total_tests = 0
    passed_tests = 0
    failed_tests = 0
    
    for num_players in range(5, 16):  # 5-15 players
        for target_stack in range(5000, 11000, 1000):  # $5k-$10k in $1k increments
            total_tests += 1
            
            # Test parameters
            small_blind = 5
            big_blind = 10
            
            try:
                result = calculate_chip_distribution_custom(
                    num_players,
                    small_blind,
                    big_blind,
                    target_stack
                )
                
                distribution = result['distribution']
                actual_stack = result['stack_value']
                
                # Check for shortages
                shortages = check_shortage(distribution, num_players, CHIP_SET)
                
                # Calculate achievement rate
                achievement_rate = (actual_stack / target_stack) * 100
                
                if shortages:
                    status = "❌ FAIL"
                    failed_tests += 1
                else:
                    status = "✓ PASS"
                    passed_tests += 1
                
                results.append({
                    'players': num_players,
                    'target': target_stack,
                    'actual': actual_stack,
                    'achievement': achievement_rate,
                    'shortages': shortages,
                    'status': status,
                    'distribution': distribution
                })
                
            except Exception as e:
                failed_tests += 1
                results.append({
                    'players': num_players,
                    'target': target_stack,
                    'error': str(e),
                    'status': "❌ ERROR"
                })
    
    # Print summary
    print(f"\nTotal Tests: {total_tests}")
    print(f"Passed: {passed_tests}")
    print(f"Failed: {failed_tests}")
    print(f"Success Rate: {(passed_tests/total_tests)*100:.1f}%\n")
    
    # Print detailed results
    print(f"{'Players':<10}{'Target':<12}{'Actual':<12}{'Achievement':<14}{'Status':<10}{'Issues'}")
    print("-" * 90)
    
    for r in results:
        players = r['players']
        target = f"${r['target']:,}" if 'target' in r else 'N/A'
        actual = f"${r['actual']:,}" if 'actual' in r else 'N/A'
        achievement = f"{r['achievement']:.1f}%" if 'achievement' in r else 'N/A'
        status = r['status']
        
        if 'error' in r:
            issues = f"ERROR: {r['error']}"
        elif r.get('shortages'):
            issues = f"Shortages: {len(r['shortages'])} denoms"
        else:
            issues = "None"
        
        print(f"{players:<10}{target:<12}{actual:<12}{achievement:<14}{status:<10}{issues}")
    
    # Print failures in detail
    if failed_tests > 0:
        print("\n" + "=" * 80)
        print("DETAILED FAILURE ANALYSIS")
        print("=" * 80)
        for r in results:
            if r['status'] != "✓ PASS":
                print(f"\n{r['players']} players, ${r.get('target', 0):,} target:")
                if 'shortages' in r and r['shortages']:
                    for s in r['shortages']:
                        print(f"  - ${s['denom']}: Need {s['needed']}, Have {s['available']}, Short {s['short']}")
                if 'error' in r:
                    print(f"  - Error: {r['error']}")
    
    # Achievement statistics
    if passed_tests > 0:
        achievements = [r['achievement'] for r in results if 'achievement' in r]
        print("\n" + "=" * 80)
        print("ACHIEVEMENT STATISTICS (Target vs Actual)")
        print("=" * 80)
        print(f"Average Achievement: {sum(achievements)/len(achievements):.1f}%")
        print(f"Minimum Achievement: {min(achievements):.1f}%")
        print(f"Maximum Achievement: {max(achievements):.1f}%")
        
        # Show which scenarios had low achievement (<80%)
        low_achievement = [r for r in results if 'achievement' in r and r['achievement'] < 80]
        if low_achievement:
            print(f"\nLow Achievement Scenarios (<80%):")
            for r in low_achievement:
                print(f"  - {r['players']} players, ${r['target']:,} target: {r['achievement']:.1f}% (${r['actual']:,})")
    
    return results, passed_tests, failed_tests

def generate_summary_report(mode1_results, mode1_pass, mode1_fail, mode2_results, mode2_pass, mode2_fail):
    """Generate final summary report"""
    print("\n" + "=" * 80)
    print("COMPREHENSIVE TEST SUMMARY REPORT")
    print("=" * 80)
    
    mode1_total = mode1_pass + mode1_fail
    mode2_total = mode2_pass + mode2_fail
    total_tests = mode1_total + mode2_total
    total_pass = mode1_pass + mode2_pass
    total_fail = mode1_fail + mode2_fail
    
    print(f"\n{'Category':<30}{'Passed':<12}{'Failed':<12}{'Total':<12}{'Rate'}")
    print("-" * 80)
    print(f"{'Mode 1 (Auto-Calculate)':<30}{mode1_pass:<12}{mode1_fail:<12}{mode1_total:<12}{(mode1_pass/mode1_total)*100:.1f}%")
    print(f"{'Mode 2 (Custom Stack)':<30}{mode2_pass:<12}{mode2_fail:<12}{mode2_total:<12}{(mode2_pass/mode2_total)*100:.1f}%")
    print("-" * 80)
    print(f"{'TOTAL':<30}{total_pass:<12}{total_fail:<12}{total_tests:<12}{(total_pass/total_tests)*100:.1f}%")
    
    # Coverage information
    print("\n" + "=" * 80)
    print("TEST COVERAGE")
    print("=" * 80)
    print(f"Players tested: 5-15 (11 different counts)")
    print(f"Mode 1 durations: 4-6 hours (3 different durations)")
    print(f"Mode 2 stacks: $5,000-$10,000 (6 different amounts)")
    print(f"Mode 1 scenarios: 11 players × 3 durations = 33 tests")
    print(f"Mode 2 scenarios: 11 players × 6 stacks = 66 tests")
    print(f"Total scenarios: 99 tests")
    
    # System health assessment
    print("\n" + "=" * 80)
    print("SYSTEM HEALTH ASSESSMENT")
    print("=" * 80)
    
    if total_fail == 0:
        print("✓ EXCELLENT: All tests passed! No chip shortages detected.")
        print("✓ The calculator correctly handles all player counts and scenarios.")
        print("✓ Chip shortage enforcement is working perfectly.")
    elif total_fail < 5:
        print("⚠ GOOD: Minor issues detected in edge cases.")
        print(f"  {total_fail} failures out of {total_tests} tests.")
    elif total_fail < 20:
        print("⚠ WARNING: Multiple failures detected.")
        print(f"  {total_fail} failures out of {total_tests} tests need investigation.")
    else:
        print("❌ CRITICAL: System has significant issues.")
        print(f"  {total_fail} failures out of {total_tests} tests.")
        print("  Review chip shortage enforcement logic.")
    
    # Recommendations
    print("\n" + "=" * 80)
    print("RECOMMENDATIONS")
    print("=" * 80)
    
    if total_fail == 0:
        print("✓ System is production-ready")
        print("✓ Safe to rebuild executable with: pyinstaller --name=\"PokerChipCalculator\" --onefile pokerchipcounter.py")
        print("✓ No additional fixes required")
    else:
        print("⚠ Review failed test cases before production deployment")
        print("⚠ Investigate chip shortage enforcement for failing scenarios")
        print("⚠ Consider adjusting distribution percentages or stack rounding")

if __name__ == "__main__":
    print("\n")
    print("╔" + "═" * 78 + "╗")
    print("║" + " " * 20 + "COMPREHENSIVE SYSTEM TEST" + " " * 33 + "║")
    print("║" + " " * 78 + "║")
    print("║" + "  Testing: 5-15 players, 4-6 hour tournaments, $5k-$10k stacks" + " " * 13 + "║")
    print("║" + "  Total Tests: 99 (33 Mode 1 + 66 Mode 2)" + " " * 37 + "║")
    print("╚" + "═" * 78 + "╝")
    print("\n")
    
    # Run tests
    mode1_results, mode1_pass, mode1_fail = test_mode1_auto_calculate()
    mode2_results, mode2_pass, mode2_fail = test_mode2_custom_stack()
    
    # Generate final report
    generate_summary_report(mode1_results, mode1_pass, mode1_fail, mode2_results, mode2_pass, mode2_fail)
    
    print("\n" + "=" * 80)
    print("Test completed. Report generated above.")
    print("=" * 80)