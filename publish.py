#!/usr/bin/env python3
"""
Publishing script for portfoliogen package.
"""

import subprocess
import sys
import os
from pathlib import Path

def run_command(command, description):
    """Run a command and handle errors."""
    print(f"\n🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully")
        if result.stdout:
            print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed:")
        print(f"Error: {e.stderr}")
        return False

def main():
    """Main publishing workflow."""
    print("🚀 PortfolioGen Publishing Script")
    print("=" * 50)
    
    # Check if we're in the right directory
    if not Path("setup.py").exists() or not Path("portfoliogen").exists():
        print("❌ Error: Run this script from the portfoliogen package root directory")
        sys.exit(1)
    
    # Step 1: Clean previous builds
    print("\n1️⃣ Cleaning previous builds...")
    for dir_name in ["build", "dist", "*.egg-info"]:
        if Path(dir_name).exists():
            run_command(f"rmdir /s /q {dir_name}", f"Removing {dir_name}")
    
    # Step 2: Install build dependencies
    if not run_command("pip install build twine", "Installing build dependencies"):
        sys.exit(1)
    
    # Step 3: Build the package
    if not run_command("python -m build", "Building package"):
        sys.exit(1)
    
    # Step 4: Check the built package
    if not run_command("python -m twine check dist/*", "Checking package"):
        sys.exit(1)
    
    print("\n" + "=" * 50)
    print("✅ Package built successfully!")
    print("\n📦 Built files:")
    
    dist_path = Path("dist")
    if dist_path.exists():
        for file in dist_path.iterdir():
            print(f"   - {file.name}")
    
    print("\n🚀 Ready to publish!")
    print("\nNext steps:")
    print("1. Test upload to TestPyPI (optional):")
    print("   python -m twine upload --repository testpypi dist/*")
    print("\n2. Upload to PyPI:")
    print("   python -m twine upload dist/*")
    print("\n3. Install from PyPI:")
    print("   pip install portfoliogen")
    
    # Ask if user wants to upload
    response = input("\nDo you want to upload to PyPI now? (y/N): ").strip().lower()
    if response == 'y':
        print("\n🚀 Uploading to PyPI...")
        if run_command("python -m twine upload dist/*", "Uploading to PyPI"):
            print("\n🎉 Package published successfully!")
            print("📦 Install with: pip install portfoliogen")
        else:
            print("\n❌ Upload failed. You can try manually with:")
            print("   python -m twine upload dist/*")

if __name__ == "__main__":
    main()