"""Test smart scaling - uses more chips when significantly more available"""

import sys
sys.path.insert(0, r"c:\Users\john_\Desktop\Poker chip")

from pokerchipcounter import calculate_chip_distribution, load_chip_set

chip_set = load_chip_set()

print("=" * 70)
print("SMART SCALING TEST: 12 players, 4 hours, 12 min intervals")
print("=" * 70)

result = calculate_chip_distribution(
    num_players=12,
    small_blind=1,
    big_blind=2,
    duration_hours=4.0,
    minutes_per_level=12,
    stack_size=5
)

total_available = sum(denom * count for denom, count in chip_set.items())
max_per_player = total_available / 12

print(f"\nChip Set Analysis:")
print(f"  Total chip value: ${total_available:,}")
print(f"  Max per player: ${max_per_player:,.0f}")
print(f"  Tournament math needs: ~$2,000 (for level 14 finish)")
print(f"  Available / Needed ratio: {max_per_player / 2000:.1f}x")

print(f"\nResult:")
print(f"  Stack given: ${result['stack_value']:,}")
print(f"  Starting BB: {result['big_blinds']:.1f} BB")
print(f"  Chip utilization: {(result['stack_value'] / max_per_player) * 100:.1f}%")

print(f"\nChip Distribution:")
for denom in sorted(result['distribution'].keys()):
    count = result['distribution'][denom]
    value = count * denom
    print(f"  ${denom:>6} chips: {count:>2} chips = ${value:>8,}")

print(f"\nTotal chips per player: {sum(result['distribution'].values())} chips")

print("\n" + "=" * 70)
if result['stack_value'] > 3000:
    print("✅ SMART SCALING WORKING: Using more available chips!")
    print(f"   Scaled from ~$2,000 → ${result['stack_value']:,}")
else:
    print("❌ Still giving minimal stack")
print("=" * 70)