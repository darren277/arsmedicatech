#!/usr/bin/env python3
"""
Test runner script for the arsmedicatech project.

This script provides convenient commands to run different types of tests
with various options and configurations.
"""

import sys
import subprocess
import argparse
import os
from pathlib import Path


def run_command(cmd, description=""):
    """Run a command and handle errors."""
    if description:
        print(f"\n{'='*60}")
        print(f"Running: {description}")
        print(f"{'='*60}")
    
    print(f"Command: {' '.join(cmd)}")
    print("-" * 60)
    
    try:
        result = subprocess.run(cmd, check=True, capture_output=False)
        print(f"\n✅ {description} completed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"\n❌ {description} failed with exit code {e.returncode}")
        return False


def main():
    parser = argparse.ArgumentParser(description="Test runner for arsmedicatech project")
    parser.add_argument(
        "test_type",
        choices=["unit", "integration", "all", "coverage", "quick"],
        help="Type of tests to run"
    )
    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Run tests in verbose mode"
    )
    parser.add_argument(
        "--markers", "-m",
        help="Run tests with specific markers (e.g., 'db' or 'slow')"
    )
    parser.add_argument(
        "--file", "-f",
        help="Run tests from a specific file"
    )
    parser.add_argument(
        "--function", "-k",
        help="Run tests matching a specific function name pattern"
    )
    parser.add_argument(
        "--parallel", "-n",
        type=int,
        help="Run tests in parallel with specified number of workers"
    )
    
    args = parser.parse_args()
    
    # Base pytest command - use sys.executable to ensure we use the current Python environment
    cmd = [sys.executable, "-m", "pytest"]
    
    # Add test type specific options
    if args.test_type == "unit":
        cmd.extend(["-m", "unit"])
        description = "Unit Tests"
    elif args.test_type == "integration":
        cmd.extend(["-m", "integration"])
        description = "Integration Tests"
    elif args.test_type == "coverage":
        cmd.extend(["--cov=lib", "--cov-report=html", "--cov-report=term"])
        description = "Tests with Coverage Report"
    elif args.test_type == "quick":
        cmd.extend(["-m", "not slow"])
        description = "Quick Tests (excluding slow tests)"
    else:  # all
        description = "All Tests"
    
    # Add additional options
    if args.verbose:
        cmd.append("-v")
    
    if args.markers:
        cmd.extend(["-m", args.markers])
    
    if args.file:
        cmd.append(args.file)
    
    if args.function:
        cmd.extend(["-k", args.function])
    
    if args.parallel:
        cmd.extend(["-n", str(args.parallel)])
    
    # Run the tests
    success = run_command(cmd, description)
    
    if success:
        print("\n🎉 All tests passed!")
        sys.exit(0)
    else:
        print("\n💥 Some tests failed!")
        sys.exit(1)


if __name__ == "__main__":
    main()
