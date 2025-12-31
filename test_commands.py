#!/usr/bin/env python3
"""
Test script for PortfolioGen CLI commands
"""

import subprocess
import sys
import os
from pathlib import Path

def run_command(cmd, description):
    """Run a command and print the result"""
    print(f"\n🔧 {description}")
    print(f"Command: {cmd}")
    print("-" * 50)
    
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        print(result.stdout)
        if result.stderr:
            print("STDERR:", result.stderr)
        return result.returncode == 0
    except Exception as e:
        print(f"Error: {e}")
        return False

def main():
    """Test PortfolioGen commands"""
    print("🚀 Testing PortfolioGen CLI Commands")
    print("=" * 50)
    
    # Test list command
    run_command("python -m portfoliogen --list", "Testing --list command")
    
    # Test version command
    run_command("python -m portfoliogen --version", "Testing --version command")
    
    # Test help command
    run_command("python -m portfoliogen --help", "Testing --help command")
    
    # Test developer template (default)
    run_command("python -m portfoliogen TestDeveloper", "Testing developer template")
    
    # Test photographer template
    run_command("python -m portfoliogen -t photographer TestPhotographer", "Testing photographer template")
    
    # Check if folders were created
    print("\n📁 Checking created folders:")
    for folder in ["TestDeveloper", "TestPhotographer"]:
        if Path(folder).exists():
            print(f"✅ {folder} - Created successfully")
            files = list(Path(folder).glob("*"))
            for file in files:
                print(f"   📄 {file.name}")
        else:
            print(f"❌ {folder} - Not found")
    
    print("\n🎉 Testing completed!")
    print("\nTo clean up test folders, run:")
    print("rm -rf TestDeveloper TestPhotographer")

if __name__ == "__main__":
    main()