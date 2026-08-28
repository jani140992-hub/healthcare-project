"""
Line Count Utility for CarePulse Healthcare System.
Counts lines of code across all Python modules.
"""

import os
import sys

def count_lines_in_file(filepath):
    total = 0
    blank = 0
    comment = 0
    code = 0
    
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        for line in f:
            total += 1
            stripped = line.strip()
            if not stripped:
                blank += 1
                continue
            if stripped.startswith('#'):
                comment += 1
                continue
            code += 1
            
    return total, blank, comment, code

def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    results = {}
    
    grand_total = 0
    grand_blank = 0
    grand_comment = 0
    grand_code = 0
    
    for root, dirs, files in os.walk(base_dir):
        # Skip virtualenvs, git, cache
        if any(skip in root for skip in ['.git', '__pycache__', '.venv', 'venv', 'env']):
            continue
        for file in files:
            if file.endswith('.py'):
                full_path = os.path.join(root, file)
                rel_path = os.path.relpath(full_path, base_dir)
                total, blank, comment, code = count_lines_in_file(full_path)
                results[rel_path] = (total, blank, comment, code)
                grand_total += total
                grand_blank += blank
                grand_comment += comment
                grand_code += code
                
    print("=" * 80)
    print(f"{'CarePulse Codebase Line Count Summary':^80}")
    print("=" * 80)
    print(f"{'Module / File':<50} {'Total':>7} {'Code':>7} {'Comment':>7} {'Blank':>7}")
    print("-" * 80)
    
    # Sort by total lines descending
    for path, (total, blank, comment, code) in sorted(results.items(), key=lambda x: x[1][0], reverse=True)[:30]:
        display_path = path if len(path) <= 48 else "..." + path[-45:]
        print(f"{display_path:<50} {total:>7} {code:>7} {comment:>7} {blank:>7}")
        
    if len(results) > 30:
        print(f"... and {len(results) - 30} more Python files")
        
    print("-" * 80)
    print(f"{'GRAND TOTAL (' + str(len(results)) + ' files)':<50} {grand_total:>7} {grand_code:>7} {grand_comment:>7} {grand_blank:>7}")
    print("=" * 80)
    
    if grand_total >= 50000:
        print(f"[SUCCESS] Target achieved: {grand_total:,} lines of Python code (>= 50,000 LOC)")
    else:
        print(f"[PROGRESS] Current: {grand_total:,} / 50,000 lines (Remaining: {50000 - grand_total:,})")

if __name__ == '__main__':
    main()
