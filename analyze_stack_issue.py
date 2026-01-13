"""Analyze why stacks are so low after tournament standard fix"""

import sys
sys.path.insert(0, r"c:\Users\john_\Desktop\Poker chip")

from pokerchipcounter import load_chip_set

chip_set = load_chip_set()

print("=" * 60)
print("CHIP SET ANALYSIS")
print("=" * 60)

total_value = 0
for denom, count in sorted(chip_set.items()):
    value = denom * count
    total_value += value
    print(f"{count:>3} × ${denom:>6} = ${value:>9,}")

print("-" * 60)
print(f"Total chip set value: ${total_value:,}")
print()

for players in [12, 13]:
    max_per_player = total_value / players
    print(f"{players} players: ${max_per_player:,.0f} per player available")
    print(f"  $500 chips: {chip_set[500]} ÷ {players} = {chip_set[500] / players:.1f} per player", 
          "✅ ≥5" if chip_set[500] / players >= 5 else "❌ <5 (SKIPPED)")
    print(f"  $1000 chips: {chip_set[1000]} ÷ {players} = {chip_set[1000] / players:.1f} per player",
          "✅ ≥5" if chip_set[1000] / players >= 5 else "❌ <5 (SKIPPED)")
    print()

print("=" * 60)
print("THE PROBLEM")
print("=" * 60)
print("With tournament standard fix (skip if <5 chips):")
print("  12 players: Skip $500 and $1000 → Only use $1/$5/$25/$100")
print("  13 players: Skip $500 and $1000 → Only use $1/$5/$25/$100")
print()
print("This limits stacks to ~$2,000 when we have $8,000+ available!")
print()
print("SOLUTION OPTIONS:")
print("  1. Relax the 5+ rule for when it wastes significant value")
print("  2. Better redistribute to mid-range chips when high chips skipped")
print("  3. Make it configurable (tournament standard vs maximize stack)")