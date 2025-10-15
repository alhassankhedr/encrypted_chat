#!/bin/bash

# OpenWebUI + Lorica.ai Integration Setup Script
# This script automates the installation and setup process

set -e  # Exit on any error

echo "🚀 Setting up OpenWebUI + Lorica.ai Integration..."

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Check if Python 3.12 is available
check_python() {
    print_status "Checking Python version..."
    
    if command -v python3.12 &> /dev/null; then
        PYTHON_CMD="python3.12"
        print_success "Python 3.12 found"
    elif command -v python3 &> /dev/null; then
        PYTHON_VERSION=$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')
        if [[ "$PYTHON_VERSION" == "3.12" ]]; then
            PYTHON_CMD="python3"
            print_success "Python 3.12 found"
        else
            print_error "Python 3.12 is required, but found version $PYTHON_VERSION"
            print_status "Please install Python 3.12 and try again"
            exit 1
        fi
    else
        print_error "Python 3.12 is not installed"
        print_status "Please install Python 3.12 and try again"
        exit 1
    fi
}

# Create virtual environment
create_venv() {
    print_status "Creating virtual environment..."
    
    if [ -d "venv" ]; then
        print_warning "Virtual environment already exists. Removing it..."
        rm -rf venv
    fi
    
    $PYTHON_CMD -m venv venv
    print_success "Virtual environment created"
}

# Activate virtual environment
activate_venv() {
    print_status "Activating virtual environment..."
    
    if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
        source venv/Scripts/activate
    else
        source venv/bin/activate
    fi
    
    print_success "Virtual environment activated"
}

# Install dependencies
install_deps() {
    print_status "Installing dependencies..."
    
    # Upgrade pip first
    pip install --upgrade pip
    
    # Install requirements
    pip install -r requirements.txt
    
    print_success "Dependencies installed successfully"
}

# Create necessary directories
create_dirs() {
    print_status "Creating necessary directories..."
    
    mkdir -p logs
    mkdir -p config
    
    print_success "Directories created"
}

# Display next steps
show_next_steps() {
    echo ""
    echo "🎉 Setup completed successfully!"
    echo ""
    echo "📋 Next steps:"
    echo "1. Activate the virtual environment:"
    if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
        echo "   source venv/Scripts/activate"
    else
        echo "   source venv/bin/activate"
    fi
    echo ""
    echo "2. Start OpenWebUI:"
    echo "   open-webui serve"
    echo ""
    echo "3. Open your browser and go to: http://localhost:8080"
    echo ""
    echo "4. Follow the configuration steps in the README.md to:"
    echo "   - Add the Lorica function"
    echo "   - Configure your API credentials"
    echo "   - Enable the function"
    echo ""
    echo "📖 For detailed instructions, see README.md"
    echo ""
    echo "🔒 Your data will be protected with end-to-end encryption!"
}

# Main execution
main() {
    echo "=========================================="
    echo "OpenWebUI + Lorica.ai Integration Setup"
    echo "=========================================="
    echo ""
    
    check_python
    create_venv
    activate_venv
    install_deps
    create_dirs
    show_next_steps
}

# Run main function
main "$@"

