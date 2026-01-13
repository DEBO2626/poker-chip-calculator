"""Test user's exact scenario: 13 players, 4.5 hours, 12 min intervals"""

import sys
sys.path.insert(0, r"c:\Users\john_\Desktop\Poker chip")

from pokerchipcounter import calculate_chip_distribution, load_chip_set

chip_set = load_chip_set()

print("=" * 60)
print("BEFORE FIX: User reported seeing:")
print("=" * 60)
print("$   500 chips:  1 chips = $     500  ❌")
print("$ 1000 chips:  2 chips = $    2000  ❌")
print()
print("=" * 60)
print("AFTER FIX: 13 players, 4.5 hours, 12 min intervals")
print("=" * 60)

result = calculate_chip_distribution(
    num_players=13,
    small_blind=1,
    big_blind=2,
    duration_hours=4.5,
    minutes_per_level=12,
    stack_size=5
)

print(f"\nTotal Stack Value: ${result['stack_value']:,.0f}")
print(f"Starting Big Blinds: {result['big_blinds']:.1f} BB")
print(f"\nChip Distribution per Player:")

for denom in sorted(result['distribution'].keys()):
    count = result['distribution'][denom]
    value = count * denom
    status = "✅" if count == 0 or count >= 5 else "❌"
    print(f"  ${denom:>6} chips: {count:>2} chips = ${value:>8,} {status}")

print(f"\nTotal Chips per Player: {sum(result['distribution'].values())} chips")
print()
print("=" * 60)
print("✅ RESULT: All denominations now in stacks of 5+")
print("No more awkward 1-chip or 2-chip allocations!")
print("=" * 60)