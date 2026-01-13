# Input Validation Quick Reference

## Valid Input Ranges

| Input | Minimum | Maximum | Notes |
|-------|---------|---------|-------|
| Players | 2 | 50 | Also validates against chip inventory |
| Small Blind | 0.01 | 10,000 | Must be <= big blind |
| Big Blind | small_blind | 20,000 | Must be >= small blind |
| Duration | 0.5 hours | 12 hours | Max 24h in validation |
| Blind Interval | 5 min | 240 min | Validated against duration |
| Custom Stack | 100 BB | 10,000,000 | Also validates against inventory |
| Chip Count | 1 | 100,000 | Per denomination in file |
| Denomination | 0.01 | 1,000,000 | In chip set file |

## Calculated Limits

| Check | Limit | Error Message |
|-------|-------|---------------|
| Blind Levels | 3-100 | "Tournament too short/long!" |
| Chips per Player | >= 50 BB | "Not enough chips in your set" |
| Stack vs Inventory | <= 120% available | "Target stack too large!" |

## Special Validations

### Blocked Values
- ❌ Negative numbers (all inputs)
- ❌ Zero (players, blinds, duration, intervals)
- ❌ Infinity (all numeric inputs)
- ❌ NaN (all numeric inputs)
- ❌ Small blind > big blind

### Relationship Checks
- Duration vs Blind Intervals → Must produce 3-100 levels
- Players vs Chip Inventory → Must allow 50+ BB per player
- Custom Stack vs Inventory → Must fit within available chips
- Calculated Stack vs Inventory → Prevents impossible tournaments

## Error Message Examples

### Good Error Messages (User-Friendly)
```
✅ "Too many players! Maximum is 50 players"

✅ "Tournament too short! With 0.5 hours and 60 min/level, 
   you only get 0 blind levels. Try shorter blind intervals 
   or longer duration"

✅ "Target stack $1,000,000 is too large! With 12 players, 
   maximum achievable is about $8,442 per player"

✅ "Not enough chips in your set for 12 players! 
   Each player would get less than 50 big blinds"
```

### File Error Messages
```
✅ "Error in chip set file: Line 3: Chip count must be positive (got -50)"

✅ "Error in chip set file: Line 1: Denomination too large (got 10000000.0, max 1,000,000)"
```

## File Format

### Valid Format
```
# My chip set (comments supported)
300 $1
200 $5
200 $25
200 $100
50 $500
50 $1000
```

### Invalid Formats
```
❌ -50 $1          (negative count)
❌ 300 $0          (zero denomination)
❌ 300 $-5         (negative denomination)
❌ 1000000 $1      (count too large)
❌ 300 $10000000   (denomination too large)
❌ abc $1          (invalid format)
```

## Common User Mistakes - All Handled

| Mistake | Caught? | Message |
|---------|---------|---------|
| 100 players | ✅ | "Too many players! Maximum is 50 players" |
| SB $10, BB $5 | ✅ | "Small blind can't be bigger than big blind" |
| 12h with 1min levels | ✅ | "Too many blind levels! ...you get 720 levels" |
| 0.5h with 60min levels | ✅ | "Tournament too short! ...you only get 0 blind levels" |
| 50 players, 8 tables | ✅ | "Not enough chips in your set for 50 players!" |
| $1M stack request | ✅ | "Target stack $1,000,000 is too large!" |
| Blank input fields | ✅ | Uses defaults or requests valid input |
| Copy-paste garbage | ✅ | "Please enter a number (like 1, 2.5, or 3.75)" |

## Testing Your Implementation

### Test These Scenarios:
1. **Valid inputs** → Should work perfectly
2. **Extreme values** → Should give helpful error
3. **Wrong order** (SB > BB) → Should catch it
4. **Too many players** → Should validate inventory
5. **Corrupted file** → Should fall back gracefully
6. **Cancel/back** → Should allow retry
7. **Empty inputs** → Should use defaults or request input

### Expected Behavior:
- ✅ Never crashes
- ✅ Always gives helpful error message
- ✅ Suggests fix when possible
- ✅ Allows user to try again
- ✅ Falls back to defaults when appropriate

## Integration Checklist

When integrating into your app:

1. **Input Fields**
   - [ ] Add min/max attributes matching these ranges
   - [ ] Show valid ranges in placeholders/hints
   - [ ] Validate on change (real-time feedback)
   - [ ] Validate on submit (final check)

2. **Error Display**
   - [ ] Show errors near relevant field
   - [ ] Use friendly error messages from validation
   - [ ] Allow user to correct and resubmit
   - [ ] Clear errors when user corrects input

3. **Edge Cases**
   - [ ] Test with min/max values
   - [ ] Test with invalid relationships (SB > BB)
   - [ ] Test with extreme player counts
   - [ ] Test with corrupted chip set files
   - [ ] Test with copy-paste garbage

4. **User Guidance**
   - [ ] Show examples of valid input
   - [ ] Provide defaults for common scenarios
   - [ ] Show chip inventory status
   - [ ] Calculate and show available range

## Production Deployment

### Pre-launch Testing:
```bash
# Run all validation tests
python test_validation.py

# Verify 20/20 tests pass
# Verify all errors are user-friendly
# Verify no crashes occur
```

### Monitoring:
- Log any ValueError exceptions (these are validation failures)
- Track which validation errors are most common
- Improve UI hints based on common mistakes

### Success Criteria:
- ✅ Zero crashes from invalid input
- ✅ All errors caught and explained
- ✅ Users can recover from any mistake
- ✅ Clear path to valid input

---

**Status: PRODUCTION READY**

All inputs validated, all edge cases handled, all errors user-friendly.