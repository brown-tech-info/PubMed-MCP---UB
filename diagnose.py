#!/usr/bin/env python3
"""
Diagnostic script to help troubleshoot MCP server issues
"""

import os
import sys
import subprocess
import json
from pathlib import Path

def check_python_environment():
    """Check Python and dependencies"""
    print("🐍 Python Environment Check")
    print(f"Python version: {sys.version}")
    print(f"Python executable: {sys.executable}")
    
    # Check if required packages are installed
    required_packages = ['mcp', 'httpx', 'python-dotenv', 'xmltodict']
    for package in required_packages:
        try:
            __import__(package.replace('-', '_'))
            print(f"✅ {package} is installed")
        except ImportError:
            print(f"❌ {package} is NOT installed")
    print()

def check_file_structure():
    """Check if all required files exist"""
    print("📁 File Structure Check")
    current_dir = Path(__file__).parent
    required_files = [
        'server.py',
        '.env',
        'requirements.txt',
        'README.md'
    ]
    
    for file in required_files:
        file_path = current_dir / file
        if file_path.exists():
            print(f"✅ {file} exists")
        else:
            print(f"❌ {file} is missing")
    print()

def check_env_file():
    """Check environment file"""
    print("🔧 Environment Configuration Check")
    env_path = Path(__file__).parent / '.env'
    
    if env_path.exists():
        print("✅ .env file exists")
        try:
            with open(env_path, 'r') as f:
                content = f.read()
                if 'PUBMED_API_KEY=' in content:
                    print("✅ PUBMED_API_KEY is configured")
                if 'PUBMED_EMAIL=' in content:
                    print("✅ PUBMED_EMAIL is configured")
        except Exception as e:
            print(f"❌ Error reading .env file: {e}")
    else:
        print("❌ .env file is missing")
    print()

def check_server_syntax():
    """Check if server.py has syntax errors"""
    print("🔍 Server Syntax Check")
    try:
        result = subprocess.run([
            sys.executable, '-m', 'py_compile', 'server.py'
        ], cwd=Path(__file__).parent, capture_output=True, text=True)
        
        if result.returncode == 0:
            print("✅ server.py syntax is valid")
        else:
            print("❌ server.py has syntax errors:")
            print(result.stderr)
    except Exception as e:
        print(f"❌ Error checking syntax: {e}")
    print()

def test_server_import():
    """Test if we can import the server module"""
    print("📦 Server Import Test")
    try:
        # Add current directory to path
        current_dir = str(Path(__file__).parent)
        if current_dir not in sys.path:
            sys.path.insert(0, current_dir)
        
        import server
        print("✅ Server module imports successfully")
        
        # Try to create server instance
        server_instance = server.PubMedMCPServer()
        print("✅ PubMedMCPServer instance created successfully")
        
    except Exception as e:
        print(f"❌ Error importing server: {e}")
    print()

def generate_claude_config():
    """Generate Claude Desktop configuration"""
    print("⚙️ Claude Desktop Configuration")
    
    current_dir = Path(__file__).parent
    server_path = current_dir / 'server.py'
    
    config = {
        "mcpServers": {
            "pubmed": {
                "command": "python",
                "args": [str(server_path)],
                "env": {
                    "PYTHONPATH": str(current_dir)
                }
            }
        }
    }
    
    print("Claude Desktop configuration should be:")
    print(json.dumps(config, indent=2))
    
    # Try to find Claude config file
    appdata = os.getenv('APPDATA')
    if appdata:
        claude_config_path = Path(appdata) / 'Claude' / 'claude_desktop_config.json'
        print(f"\nClaude config file should be at: {claude_config_path}")
        
        if claude_config_path.exists():
            print("✅ Claude config file exists")
            try:
                with open(claude_config_path, 'r') as f:
                    existing_config = json.load(f)
                    if 'mcpServers' in existing_config and 'pubmed' in existing_config['mcpServers']:
                        print("✅ PubMed server is configured in Claude")
                    else:
                        print("❌ PubMed server not found in Claude config")
            except Exception as e:
                print(f"❌ Error reading Claude config: {e}")
        else:
            print("❌ Claude config file not found")
    print()

def main():
    """Run all diagnostic checks"""
    print("🔧 PubMed MCP Server Diagnostic Tool")
    print("=" * 50)
    
    check_python_environment()
    check_file_structure()
    check_env_file()
    check_server_syntax()
    test_server_import()
    generate_claude_config()
    
    print("=" * 50)
    print("Diagnostic complete!")
    print("\nIf any checks failed, please fix those issues first.")
    print("If all checks passed, try restarting Claude Desktop.")

if __name__ == "__main__":
    main()