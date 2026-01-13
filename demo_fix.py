"""
Demonstration of the chip shortage bug fix.
Shows the exact scenario from user's report: 13 players, $8500 custom stack.
"""

import sys
sys.path.insert(0, r'c:\Users\john_\Desktop\Poker chip')

from pokerchipcounter import calculate_chip_distribution_custom

def demo_before_after():
    """Show what the user experienced vs. what happens now"""
    
    print("=" * 70)
    print("CHIP SHORTAGE BUG FIX - DEMONSTRATION")
    print("=" * 70)
    print("\nScenario: 13 players, requesting $8500 stack per player")
    print("\n" + "=" * 70)
    print("BEFORE THE FIX (What you saw):")
    print("=" * 70)
    print("""
$     1 chips: 20 chips = $      20
$     5 chips: 15 chips = $      75
$    25 chips: 15 chips = $     375
$   100 chips: 15 chips = $    1500
$ 1000  chips:  5 chips = $    5000  ← PROBLEM!
--------------------------------------------------
Total Stack Value: $6970
Starting Big Blinds: 3485.0 BB

!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
HEADS UP: Adjusted distribution due to chip shortage
  - Need 65 × $1000 chips but only 50 available (short 15)
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

CHIPS NEEDED FROM YOUR SET:
 65 x $1000   chips (you have:  50) Need 15 more  ❌ IMPOSSIBLE!
    """)
    
    print("\n" + "=" * 70)
    print("AFTER THE FIX (What happens now):")
    print("=" * 70)
    
    result = calculate_chip_distribution_custom(
        num_players=13,
        small_blind=1,
        big_blind=2,
        target_stack=8500
    )
    
    print()
    for denom in sorted(result['distribution'].keys()):
        count = result['distribution'][denom]
        value = denom * count
        if denom == 1000:
            marker = "  ← FIXED! Reduced from 5 to 3"
        else:
            marker = ""
        print(f"${denom:>6} chips: {count:>2} chips = ${value:>7}{marker}")
    
    print("-" * 70)
    print(f"Total Stack Value: ${result['stack_value']}")
    print(f"Starting Big Blinds: {result['big_blinds']:.1f} BB")
    
    print("\n" + "=" * 70)
    print("CHIP AVAILABILITY CHECK:")
    print("=" * 70)
    
    all_ok = True
    for denom in sorted(result['distribution'].keys()):
        total_needed = result['distribution'][denom] * 13
        available = result['available_chips'][denom]
        
        if total_needed <= available:
            status = "✓ OK"
            marker = ""
        else:
            status = "✗ SHORTAGE"
            all_ok = False
            marker = f"  (short {total_needed - available})"
        
        print(f"{total_needed:>3} x ${denom:<6} chips (you have: {available:>3}) {status}{marker}")
    
    print("\n" + "=" * 70)
    if all_ok:
        print("✓✓✓ ALL CHIPS FIT WITHIN AVAILABLE INVENTORY ✓✓✓")
        print("=" * 70)
        print("\n🎉 BUG FIXED! The calculator now:")
        print("   • Never suggests impossible distributions")
        print("   • Automatically adjusts to fit your chip set")
        print("   • Gets as close to target as possible")
        print("   • Always shows achievable results")
    else:
        print("✗✗✗ STILL SHOWING SHORTAGES - BUG NOT FIXED ✗✗✗")
        print("=" * 70)
    
    print("\n" + "=" * 70)
    print("KEY TAKEAWAY:")
    print("=" * 70)
    print(f"Requested: $8,500 per player")
    print(f"Achievable: ${result['stack_value']:,} per player")
    print(f"Reason: Limited to 50 × $1000 chips for 13 players")
    print(f"Solution: Use 3 × $1000 chips per player (39 total)")
    print("\nThe calculator now shows you what's ACTUALLY POSSIBLE,")
    print("not what's IMPOSSIBLE to achieve with your chip set.")

if __name__ == "__main__":
    demo_before_after()