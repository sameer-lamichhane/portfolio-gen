#!/usr/bin/env python3
"""
Script to commit and push changes to GitHub
"""

import subprocess
import sys

def run_command(cmd, description):
    """Run a command and print the result"""
    print(f"\n🔧 {description}")
    print(f"Command: {cmd}")
    print("-" * 50)
    
    try:
        result = subprocess.run(cmd, shell=True, text=True)
        return result.returncode == 0
    except Exception as e:
        print(f"Error: {e}")
        return False

def main():
    """Commit and push changes"""
    print("🚀 Pushing PortfolioGen Changes")
    print("=" * 50)
    
    # Add all changes
    if not run_command("git add .", "Adding all changes"):
        print("❌ Failed to add changes")
        return
    
    # Commit changes
    commit_message = "feat: Add photographer template and enhanced CLI features\n\n- Added professional photography portfolio template\n- Enhanced developer template with better responsive design\n- Added --list command to show available templates\n- Improved CLI with template validation and help\n- Mobile-optimized designs for both templates\n- Fixed testimonial slider and navigation issues\n- Updated README with comprehensive documentation\n- Version bump to 1.2.0"
    
    if not run_command(f'git commit -m "{commit_message}"', "Committing changes"):
        print("❌ Failed to commit changes")
        return
    
    # Push to origin
    if not run_command("git push origin main", "Pushing to GitHub"):
        print("❌ Failed to push changes")
        return
    
    print("\n✅ Successfully pushed changes to GitHub!")
    print("\n📋 Next steps:")
    print("1. Test the CLI commands:")
    print("   python test_commands.py")
    print("\n2. Test package installation:")
    print("   pip install -e .")
    print("   portfoliogen --list")
    print("   portfoliogen -t photographer MyTest")
    print("\n3. Create a new release on GitHub")
    print("4. Publish to PyPI if needed")

if __name__ == "__main__":
    main()