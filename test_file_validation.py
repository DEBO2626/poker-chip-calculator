"""Test file validation for corrupted chip set files"""
import os
import sys
sys.path.insert(0, r'c:\Users\john_\Desktop\Poker chip')

from pokerchipcounter import load_chip_set

# Backup original file
original_file = "poker chip set counts.txt"
backup_file = "poker chip set counts.backup"

if os.path.exists(original_file):
    with open(original_file, 'r') as f:
        original_content = f.read()
    with open(backup_file, 'w') as f:
        f.write(original_content)
    print("Backed up original chip set file")

def test_corrupted_file(name, content):
    """Test a corrupted file"""
    print(f"\n{'='*60}")
    print(f"TEST: {name}")
    print('='*60)
    print(f"File content:\n{content}")
    print('-'*60)
    
    # Write corrupted file
    with open(original_file, 'w') as f:
        f.write(content)
    
    # Try to load
    try:
        result = load_chip_set()
        print(f"Result: {result}")
    except Exception as e:
        print(f"Exception: {e}")

# Test 1: Negative chip count
test_corrupted_file("Negative chip count",
    "-50 $1\n200 $5\n200 $25\n")

# Test 2: Zero denomination
test_corrupted_file("Zero denomination",
    "300 $0\n200 $5\n200 $25\n")

# Test 3: Negative denomination
test_corrupted_file("Negative denomination",
    "300 $-5\n200 $5\n200 $25\n")

# Test 4: Excessive count
test_corrupted_file("Excessive count (1 million)",
    "1000000 $1\n200 $5\n200 $25\n")

# Test 5: Excessive denomination
test_corrupted_file("Excessive denomination (10 million)",
    "300 $10000000\n200 $5\n200 $25\n")

# Test 6: Invalid format
test_corrupted_file("Invalid format (text instead of number)",
    "abc $1\n200 $5\n200 $25\n")

# Test 7: Only one denomination
test_corrupted_file("Only one denomination",
    "300 $1\n")

# Test 8: Empty file
test_corrupted_file("Empty file",
    "")

# Test 9: Comments only
test_corrupted_file("Comments only",
    "# This is a comment\n# Another comment\n")

# Test 10: Valid file with comments
test_corrupted_file("Valid file with comments",
    "# My chip set\n300 $1\n200 $5\n# Middle chips\n200 $25\n200 $100\n")

# Restore original file
print(f"\n{'='*60}")
print("RESTORING ORIGINAL FILE")
print('='*60)
if os.path.exists(backup_file):
    with open(backup_file, 'r') as f:
        original_content = f.read()
    with open(original_file, 'w') as f:
        f.write(original_content)
    os.remove(backup_file)
    print("Original chip set file restored")

print("\nFile validation tests completed!")