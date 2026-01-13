---
description: Repository Information Overview
alwaysApply: true
---

# Poker Chip Calculator Information

## Summary
A Python application that calculates optimal poker chip distribution for tournament play based on player count, blind structure, and tournament duration. The calculator helps determine the right number of chips per player and ensures the distribution works with the available chip set.

## Structure
- **build/**: Contains PyInstaller build files and artifacts
- **dist/**: Contains the compiled executable (PokerChipCalculator.exe)
- **pokerchipcounter.py**: Main Python source code file
- **PokerChipCalculator.spec**: PyInstaller specification file
- **poker chip set counts.txt**: Reference file with available chip counts

## Language & Runtime
**Language**: Python
**Build System**: PyInstaller
**Main File**: pokerchipcounter.py

## Dependencies
**Standard Library Dependencies**:
- math

## Build & Installation
The application is built using PyInstaller to create a standalone executable:

```bash
pyinstaller --name="PokerChipCalculator" --onefile pokerchipcounter.py
```

## Application Logic

### Two Operating Modes

**Mode 1 - Auto-calculate (Duration-based)**:
- Calculates optimal stack size based on tournament parameters
- Uses constant 1.5× blind progression for all levels
- Targets level 14 finish with 12 BB ending stack
- Automatically scales to produce realistic stacks (~2,335 BB starting)
- Input parameters:
  - Number of players
  - Starting small blind / big blind values
  - Tournament duration (hours)
  - Minutes between blind level increases

**Mode 2 - Custom Stack**:
- User specifies exact desired stack amount (e.g., $8,500)
- Calculator distributes chips optimally to get as close as possible
- Respects chip inventory limits and stack size rounding
- Minimum requirement: 100 BB starting stack

### Core Functions

**`calculate_chip_distribution()`**:
- Auto-calculates stack based on duration and blind structure
- Uses 1.5× constant blind progression (previously was 2× → 1.5× mixed)
- Targets level 14 finish (previously level 19)
- Returns distribution that fits within available chip set

**`calculate_chip_distribution_custom()`**:
- Takes custom target stack amount as input
- Uses same percentage-based distribution strategy
- Returns actual achievable stack (may be less than target due to constraints)

### Chip Distribution Strategy
Both modes use identical allocation percentages:
- 2% in $1 chips
- 10% in $5 chips  
- 15% in $25 chips
- 25% in $100 chips
- 20% in $500 chips
- Remainder in $1000 chips

**Key Features**:
- Percentage-based allocation scales across wide range of stack sizes
- Rounds chip counts to standard stack sizes (typically 20-chip stacks)
- Verifies distribution against available chip inventory
- Handles 8-16 players with realistic stack sizes
- Validates minimum BB requirements (100 BB for custom, proper scaling for auto)

## Usage
The application runs as a command-line interface that:
1. Prompts for mode selection (Auto-calculate or Custom stack)
2. Collects appropriate parameters based on mode
3. Calculates optimal chip distribution
4. Displays per-player chip counts
5. Shows total chips needed and validates against available set
6. For Mode 1: Shows tournament blind structure and timing details

## Available Chip Set
The default chip set contains:
- 300 × $1 chips
- 200 × $5 chips
- 200 × $25 chips
- 200 × $100 chips
- 50 × $500 chips
- 50 × $1000 chips

**Per-Player Maximum** (based on chip set total / players):
- The calculator automatically determines max available chips per player
- Ensures distributions don't exceed physical inventory
- Typical range: $8,105 per player for 8 players down to ~$5,753 for 14 players

## Recent Changes & Design Decisions

### Blind Progression Fix (v2.0)
**Problem**: Original 2× → 1.5× mixed progression caused unrealistic stack requirements
- Level 19 blinds reached $39,366/$78,733
- Required stacks of $472,400+ (impossible with $8,105 available per player)

**Solution**: Changed to constant 1.5× progression for ALL levels
- Level 14 blinds: $195/$389
- Required stacks: ~$4,671 (2,335 BB) - fits comfortably within chip set
- More practical for home games with limited chips

### Custom Stack Mode Addition
**Rationale**: Experienced tournament directors often know exact stack size they want
- Mode 2 allows manual stack specification
- Calculator optimizes chip distribution to get as close as possible
- Example: Request $8,500 → Get $6,975 actual (limited by inventory/rounding)

### Key Design Principles
1. **Realistic over theoretical**: Calculations must work with physical chip constraints
2. **Percentage-based distribution**: Scales better than fixed chip counts
3. **Conservative blind progression**: 1.5× allows longer, more strategic play
4. **Stack size rounding**: Maintains neat stacks (typically 20 chips) for easier counting
5. **Dual-mode flexibility**: Serves both casual users (auto) and experts (custom)

## Recent Bug Fixes

### Chip Shortage Enforcement (Current Session)
**Problem**: Calculator could return distributions requiring more chips than available
- Both modes could show "Need 15 more chips" despite claiming to adjust
- Warning message was displayed but distribution wasn't actually fixed

**Solution**: Added automatic enforcement in both modes
- Detects any denomination shortage
- Reduces chip counts to maximum available per player
- Allows partial stacks (1-4 chips) when needed to maximize value
- **GUARANTEE**: Never returns impossible distributions

**Example**: 13 players requesting $8500 stack
- Before: Showed shortage of 15 × $1000 chips ❌
- After: Adjusted to 3 × $1000 chips per player (39 total) ✓
- Result: $4970 achievable stack instead of impossible $6970

## Known Limitations & Considerations
- **Custom mode may not reach target**: Physical chip limits and rounding prevent exact matches
- **Lower denominations get exhausted first**: With many players, $1/$5 chips run out quickly
- **Stack rounding reduces precision**: Neat stacks prioritized over exact values (but allows partial stacks when needed)
- **Fixed chip set**: Currently hardcoded to specific inventory (300/200/200/200/50/50)
- **Minimum viable players**: Calculations work best with 8-16 players
- **No rebuy support**: Designed for freezeout tournament structure only
- **Automatic adjustment**: High player counts or large stacks may be reduced to fit inventory