"""
Configuration settings for the Llama 4 Chat Interface
"""

import os
from pathlib import Path

# Project paths
PROJECT_ROOT = Path(__file__).parent
MODELS_DIR = PROJECT_ROOT / "llama_models"
LLAMA_CPP_DIR = PROJECT_ROOT / "llama.cpp"

# Model configuration
MODEL_CONFIG = {
    "name": "Llama-4-Scout-17B",
    "repo_id": "unsloth/Llama-4-Scout-17B-16E-Instruct-GGUF",
    "file_pattern": "*IQ2_XXS*",
    "path": MODELS_DIR / "Llama-4-Scout-17B" / "Llama-4-Scout-17B-16E-Instruct-UD-IQ2_XXS.gguf"
}

# Llama.cpp inference parameters
INFERENCE_CONFIG = {
    "threads": 16,
    "ctx_size": 16384,
    "n_gpu_layers": 99,
    "gpu_layers_filter": ".ffn_.*_exps.=CPU",
    "seed": 42,
    "priority": 3,
    "temperature": 0.6,
    "min_p": 0.01,
    "top_p": 0.9,
    "repeat_penalty": 1.1,
    "max_tokens": 2048
}

# Streamlit UI configuration
UI_CONFIG = {
    "page_title": "🦙 Llama 4 Chat",
    "page_icon": "🦙",
    "layout": "wide",
    "initial_sidebar_state": "expanded",
    "text_area_height": 200,
    "placeholder_text": "Ask me anything...",
    "theme": {
        "primaryColor": "#FF6B6B",
        "backgroundColor": "#FFFFFF",
        "secondaryBackgroundColor": "#F0F2F6",
        "textColor": "#262730"
    }
}

# Environment variables
ENV_VARS = {
    "HF_HUB_ENABLE_HF_TRANSFER": "1",
    "TOKENIZERS_PARALLELISM": "false"
}

# System requirements
SYSTEM_REQUIREMENTS = {
    "min_ram_gb": 16,
    "recommended_ram_gb": 32,
    "min_python_version": "3.8",
    "supported_platforms": ["linux", "darwin", "win32"]
}

# Logging configuration
LOGGING_CONFIG = {
    "level": "INFO",
    "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    "file": "llama_chat.log"
}

def setup_environment():
    """Set up environment variables"""
    for key, value in ENV_VARS.items():
        os.environ[key] = value

def validate_system_requirements():
    """Validate system requirements"""
    import sys
    import psutil
    
    # Check Python version
    if sys.version_info < (3, 8):
        raise RuntimeError(f"Python 3.8+ required, got {sys.version}")
    
    # Check available RAM
    ram_gb = psutil.virtual_memory().total / (1024**3)
    if ram_gb < SYSTEM_REQUIREMENTS["min_ram_gb"]:
        raise RuntimeError(f"At least {SYSTEM_REQUIREMENTS['min_ram_gb']}GB RAM required, got {ram_gb:.1f}GB")
    
    # Check platform
    if sys.platform not in SYSTEM_REQUIREMENTS["supported_platforms"]:
        print(f"Warning: Platform {sys.platform} may not be fully supported")

def get_model_path():
    """Get the model path, creating directories if needed"""
    model_path = MODEL_CONFIG["path"]
    model_path.parent.mkdir(parents=True, exist_ok=True)
    return model_path

def get_llama_cpp_path():
    """Get the llama.cpp executable path"""
    if os.name == 'nt':  # Windows
        return LLAMA_CPP_DIR / "llama-cli.exe"
    else:  # Unix-like
        return LLAMA_CPP_DIR / "llama-cli" 