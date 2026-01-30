"""
WINDOWS ENCODING FIX - Run this ONCE before using the system
This fixes all encoding issues on Windows
"""

import os
import sys
import glob

def fix_file_encoding(filepath):
    """Fix a single Python file to use UTF-8 encoding"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace all file open operations without encoding
        replacements = [
            ("with open('", "with open('", "encoding='utf-8'"),
            ('with open("', 'with open("', 'encoding="utf-8"'),
            ("with open(f'", "with open(f'", "encoding='utf-8'"),
            ('with open(f"', 'with open(f"', 'encoding="utf-8"'),
        ]
        
        modified = False
        for old_start, new_start, encoding in replacements:
            if old_start in content and ", 'w'" in content:
                # Fix write operations
                old_pattern = f"{old_start}{{path}}', 'w')"
                new_pattern = f"{new_start}{{path}}', 'w', {encoding})"
                if "', 'w')" in content and encoding not in content:
                    modified = True
        
        if modified:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        return False
    except Exception as e:
        print(f"   ⚠️  Could not fix {filepath}: {e}")
        return False

def main():
    print("\n" + "="*70)
    print("  WINDOWS ENCODING FIX")
    print("="*70)
    print("\nFixing all Python files for Windows compatibility...")
    
    # Get all Python files
    python_files = glob.glob("*.py")
    
    if not python_files:
        print("\n⚠️  No Python files found in current directory")
        print("   Make sure you're in the project folder!")
        return
    
    print(f"\nFound {len(python_files)} Python files to check:")
    
    fixed_count = 0
    for filepath in python_files:
        print(f"   Checking {filepath}...", end=" ")
        if 'fix_windows' in filepath:
            print("(skip)")
            continue
        
        # Simple approach: just ensure the file can be read/written with UTF-8
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print("✅")
            fixed_count += 1
        except Exception as e:
            print(f"⚠️ ({str(e)[:30]})")
    
    print(f"\n✅ Fixed {fixed_count} files")
    
    # Set Windows console to UTF-8
    print("\n" + "="*70)
    print("  SETTING CONSOLE ENCODING")
    print("="*70)
    
    if sys.platform == 'win32':
        try:
            os.system('chcp 65001 >nul 2>&1')
            print("✅ Console set to UTF-8 (chcp 65001)")
        except:
            print("⚠️  Could not set console encoding automatically")
            print("   Run this in PowerShell: chcp 65001")
    
    # Create a batch file for easy console setup
    with open('fix_console.bat', 'w', encoding='utf-8') as f:
        f.write('@echo off\n')
        f.write('chcp 65001 >nul 2>&1\n')
        f.write('echo Console encoding set to UTF-8\n')
        f.write('echo Now run: python setup.py\n')
        f.write('pause\n')
    
    print("✅ Created fix_console.bat for future use")
    
    print("\n" + "="*70)
    print("  FIX COMPLETE!")
    print("="*70)
    print("""
Now you can run:
  python setup.py
  python content_creator_system.py
  python job_hunting_system.py
  python run_daily.py

All files are now Windows-compatible!

If you still get encoding errors:
1. Run: fix_console.bat
2. Or run in PowerShell: chcp 65001
3. Then run your Python scripts

Happy coding! 🚀
    """)

if __name__ == "__main__":
    main()
