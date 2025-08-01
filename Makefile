# Makefile for Llama 4 Chat Interface

.PHONY: help install setup download check run clean test

# Default target
help:
	@echo "🦙 Llama 4 Chat Interface - Available Commands"
	@echo "=============================================="
	@echo "make install    - Install Python dependencies"
	@echo "make setup      - Full setup (install + llama.cpp + model)"
	@echo "make download   - Download the model"
	@echo "make check      - Check system requirements"
	@echo "make run        - Start the chat interface"
	@echo "make clean      - Clean temporary files"
	@echo "make test       - Run system checks"

# Install Python dependencies
install:
	@echo "📦 Installing Python dependencies..."
	pip install -r requirements.txt

# Full setup
setup:
	@echo "🚀 Setting up Llama 4 Chat Interface..."
	@echo "📦 Installing dependencies..."
	pip install -r requirements.txt
	@echo "🔧 Setting up llama.cpp..."
	@if [ ! -d "llama.cpp" ]; then \
		git clone https://github.com/ggerganov/llama.cpp.git; \
	fi
	@cd llama.cpp && make
	@echo "📥 Downloading model..."
	python download.py
	@echo "✅ Setup completed!"

# Download model
download:
	@echo "📥 Downloading model..."
	python download.py

# Check system
check:
	@echo "🔍 Checking system requirements..."
	python scripts/check_system.py

# Run the application
run:
	@echo "🚀 Starting Llama 4 Chat Interface..."
	streamlit run app.py

# Clean temporary files
clean:
	@echo "🧹 Cleaning temporary files..."
	@find . -type f -name "*.pyc" -delete
	@find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	@find . -type f -name "*.log" -delete
	@echo "✅ Clean completed!"

# Run tests/checks
test:
	@echo "🧪 Running system checks..."
	python scripts/check_system.py

# Development helpers
dev-install:
	@echo "🔧 Installing development dependencies..."
	pip install -r requirements.txt
	pip install pytest black flake8 mypy

format:
	@echo "🎨 Formatting code..."
	black *.py scripts/*.py

lint:
	@echo "🔍 Linting code..."
	flake8 *.py scripts/*.py

# Platform-specific commands
setup-windows:
	@echo "🪟 Windows setup..."
	@if [ ! -d "llama.cpp" ]; then \
		git clone https://github.com/ggerganov/llama.cpp.git; \
	fi
	@cd llama.cpp && cmake -B build -S . && cmake --build build --config Release

setup-linux:
	@echo "🐧 Linux setup..."
	@if [ ! -d "llama.cpp" ]; then \
		git clone https://github.com/ggerganov/llama.cpp.git; \
	fi
	@cd llama.cpp && make

setup-mac:
	@echo "🍎 macOS setup..."
	@if [ ! -d "llama.cpp" ]; then \
		git clone https://github.com/ggerganov/llama.cpp.git; \
	fi
	@cd llama.cpp && make 