import sys
sys.path.insert(0, r'c:\Users\john_\Desktop\Poker chip')

from pokerchipcounter import calculate_chip_distribution

print("=" * 60)
print("TEST 1: 12 players, 1/2 blinds, 4.5 hours, 12 min/level")
print("=" * 60)
result1 = calculate_chip_distribution(
    num_players=12,
    small_blind=1,
    big_blind=2,
    duration_hours=4.5,
    minutes_per_level=12,
    stack_size=5
)

if 'error' not in result1:
    print(f"Stack per player: ${result1['stack_value']:,.0f}")
    print(f"Starting big blinds: {result1['big_blinds']:.1f} BB")
    print(f"Total levels: {result1['total_levels']}")
    print(f"Chip distribution:")
    for denom, count in sorted(result1['distribution'].items()):
        print(f"  {count:>3} x ${denom}")
else:
    print(f"ERROR: {result1['error']}")

print("\n" + "=" * 60)
print("TEST 2: 7 players, 1/2 blinds, 4.5 hours, 12 min/level")
print("=" * 60)
result2 = calculate_chip_distribution(
    num_players=7,
    small_blind=1,
    big_blind=2,
    duration_hours=4.5,
    minutes_per_level=12,
    stack_size=5
)

if 'error' not in result2:
    print(f"Stack per player: ${result2['stack_value']:,.0f}")
    print(f"Starting big blinds: {result2['big_blinds']:.1f} BB")
    print(f"Total levels: {result2['total_levels']}")
    print(f"Chip distribution:")
    for denom, count in sorted(result2['distribution'].items()):
        print(f"  {count:>3} x ${denom}")
else:
    print(f"ERROR: {result2['error']}")

print("\n" + "=" * 60)
print("TEST 3: 12 players, 1/2 blinds, 5 hours, 15 min/level")
print("=" * 60)
result3 = calculate_chip_distribution(
    num_players=12,
    small_blind=1,
    big_blind=2,
    duration_hours=5,
    minutes_per_level=15,
    stack_size=5
)

if 'error' not in result3:
    print(f"Stack per player: ${result3['stack_value']:,.0f}")
    print(f"Starting big blinds: {result3['big_blinds']:.1f} BB")
    print(f"Total levels: {result3['total_levels']}")
    print(f"Chip distribution:")
    for denom, count in sorted(result3['distribution'].items()):
        print(f"  {count:>3} x ${denom}")
else:
    print(f"ERROR: {result3['error']}")

print("\n" + "=" * 60)
print("TEST 4: 12 players, 1/2 blinds, 3 hours, 10 min/level")
print("=" * 60)
result4 = calculate_chip_distribution(
    num_players=12,
    small_blind=1,
    big_blind=2,
    duration_hours=3,
    minutes_per_level=10,
    stack_size=5
)

if 'error' not in result4:
    print(f"Stack per player: ${result4['stack_value']:,.0f}")
    print(f"Starting big blinds: {result4['big_blinds']:.1f} BB")
    print(f"Total levels: {result4['total_levels']}")
    print(f"Chip distribution:")
    for denom, count in sorted(result4['distribution'].items()):
        print(f"  {count:>3} x ${denom}")
else:
    print(f"ERROR: {result4['error']}")