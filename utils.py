"""
Utility functions for the Llama 4 Chat Interface
"""

import tempfile
import os
import subprocess
import logging
from pathlib import Path
from typing import Optional, Dict, Any
import time

from config import INFERENCE_CONFIG, get_model_path, get_llama_cpp_path

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def format_prompt(user_input: str, system_prompt: Optional[str] = None) -> str:
    """
    Format user input into the expected prompt format for Llama 4.
    
    Args:
        user_input: The user's input text
        system_prompt: Optional system prompt to prepend
    
    Returns:
        Formatted prompt string
    """
    if system_prompt:
        formatted = f"<|header_start|>system<|header_end|>\n\n{system_prompt}<|eot|>"
    else:
        formatted = ""
    
    formatted += f"<|header_start|>user<|header_end|>\n\n{user_input}<|eot|><|header_start|>assistant<|header_end|>\n\n"
    return formatted

def run_llama_inference(prompt: str, custom_config: Optional[Dict[str, Any]] = None) -> str:
    """
    Run Llama inference using llama.cpp.
    
    Args:
        prompt: The formatted prompt to send to the model
        custom_config: Optional custom configuration parameters
    
    Returns:
        Model response as string
    """
    config = INFERENCE_CONFIG.copy()
    if custom_config:
        config.update(custom_config)
    
    # Create temporary file for prompt
    with tempfile.NamedTemporaryFile(delete=False, mode="w", suffix=".txt", encoding="utf-8") as tmp_prompt:
        tmp_prompt.write(prompt)
        tmp_prompt_path = tmp_prompt.name

    try:
        # Build command
        cmd = [
            str(get_llama_cpp_path()),
            "--model", str(get_model_path()),
            "--threads", str(config["threads"]),
            "--ctx-size", str(config["ctx_size"]),
            "--n-gpu-layers", str(config["n_gpu_layers"]),
            "-ot", config["gpu_layers_filter"],
            "--seed", str(config["seed"]),
            "--prio", str(config["priority"]),
            "--temp", str(config["temperature"]),
            "--min-p", str(config["min_p"]),
            "--top-p", str(config["top_p"]),
            "--repeat-penalty", str(config["repeat_penalty"]),
            "--file", tmp_prompt_path
        ]
        
        logger.info(f"Running inference with config: {config}")
        start_time = time.time()
        
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=300  # 5 minute timeout
        )
        
        inference_time = time.time() - start_time
        logger.info(f"Inference completed in {inference_time:.2f} seconds")
        
        if result.returncode != 0:
            logger.error(f"llama.cpp error: {result.stderr}")
            return f"Error: {result.stderr}"
        
        return result.stdout.strip()
        
    except subprocess.TimeoutExpired:
        logger.error("Inference timed out")
        return "Error: Inference timed out after 5 minutes"
    except Exception as e:
        logger.error(f"Inference error: {e}")
        return f"Error: {e}"
    finally:
        # Clean up temporary file
        try:
            os.remove(tmp_prompt_path)
        except OSError:
            pass

def validate_model_exists() -> bool:
    """
    Check if the model file exists.
    
    Returns:
        True if model exists, False otherwise
    """
    model_path = get_model_path()
    exists = model_path.exists()
    if not exists:
        logger.warning(f"Model not found at {model_path}")
    return exists

def validate_llama_cpp_exists() -> bool:
    """
    Check if llama.cpp executable exists.
    
    Returns:
        True if executable exists, False otherwise
    """
    llama_path = get_llama_cpp_path()
    exists = llama_path.exists()
    if not exists:
        logger.warning(f"llama.cpp not found at {llama_path}")
    return exists

def get_system_info() -> Dict[str, Any]:
    """
    Get system information for debugging.
    
    Returns:
        Dictionary with system information
    """
    import psutil
    import sys
    
    return {
        "python_version": sys.version,
        "platform": sys.platform,
        "cpu_count": psutil.cpu_count(),
        "memory_total_gb": psutil.virtual_memory().total / (1024**3),
        "memory_available_gb": psutil.virtual_memory().available / (1024**3),
        "disk_usage": psutil.disk_usage('/').percent if os.name != 'nt' else psutil.disk_usage('C:\\').percent
    }

def sanitize_input(text: str) -> str:
    """
    Sanitize user input to prevent injection attacks.
    
    Args:
        text: Input text to sanitize
    
    Returns:
        Sanitized text
    """
    # Remove potentially dangerous characters
    dangerous_chars = ['<script>', '</script>', 'javascript:', 'data:', 'vbscript:']
    sanitized = text
    for char in dangerous_chars:
        sanitized = sanitized.replace(char, '')
    
    # Limit length
    if len(sanitized) > 10000:
        sanitized = sanitized[:10000] + "..."
    
    return sanitized

def estimate_tokens(text: str) -> int:
    """
    Rough estimate of token count (approximate).
    
    Args:
        text: Text to estimate tokens for
    
    Returns:
        Estimated token count
    """
    # Rough approximation: 1 token ≈ 4 characters for English text
    return len(text) // 4

def format_response_time(seconds: float) -> str:
    """
    Format response time in a human-readable format.
    
    Args:
        seconds: Time in seconds
    
    Returns:
        Formatted time string
    """
    if seconds < 1:
        return f"{seconds*1000:.0f}ms"
    elif seconds < 60:
        return f"{seconds:.1f}s"
    else:
        minutes = int(seconds // 60)
        remaining_seconds = seconds % 60
        return f"{minutes}m {remaining_seconds:.0f}s" 