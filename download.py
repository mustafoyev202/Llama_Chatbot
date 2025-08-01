"""
Model download script for Llama 4 Chat Interface
"""

import os
import sys
from pathlib import Path
from huggingface_hub import snapshot_download
import logging

from config import MODEL_CONFIG, setup_environment, get_model_path

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def download_model():
    """Download the Llama 4 model from Hugging Face Hub"""
    
    # Setup environment
    setup_environment()
    
    logger.info("🚀 Starting model download...")
    logger.info(f"Model: {MODEL_CONFIG['name']}")
    logger.info(f"Repository: {MODEL_CONFIG['repo_id']}")
    logger.info(f"File pattern: {MODEL_CONFIG['file_pattern']}")
    
    try:
        # Create models directory
        model_dir = Path(MODEL_CONFIG['path']).parent
        model_dir.mkdir(parents=True, exist_ok=True)
        logger.info(f"📁 Created directory: {model_dir}")
        
        # Download the model
        logger.info("📥 Downloading model files...")
        snapshot_download(
            repo_id=MODEL_CONFIG['repo_id'],
            local_dir=str(model_dir),
            allow_patterns=[MODEL_CONFIG['file_pattern']],
            resume_download=True,
            local_dir_use_symlinks=False
        )
        
        # Verify download
        model_path = get_model_path()
        if model_path.exists():
            size_gb = model_path.stat().st_size / (1024**3)
            logger.info(f"✅ Model downloaded successfully!")
            logger.info(f"📊 Model size: {size_gb:.2f} GB")
            logger.info(f"📍 Location: {model_path}")
        else:
            logger.error("❌ Model file not found after download")
            return False
            
    except Exception as e:
        logger.error(f"❌ Download failed: {e}")
        return False
    
    return True

def check_disk_space():
    """Check if there's enough disk space for the model"""
    import shutil
    
    # Model is approximately 2.5GB
    required_space_gb = 3.0
    model_dir = Path(MODEL_CONFIG['path']).parent
    
    try:
        total, used, free = shutil.disk_usage(str(model_dir))
        free_gb = free / (1024**3)
        
        logger.info(f"💾 Available disk space: {free_gb:.2f} GB")
        
        if free_gb < required_space_gb:
            logger.warning(f"⚠️ Low disk space: {free_gb:.2f} GB available, {required_space_gb} GB recommended")
            return False
        return True
    except Exception as e:
        logger.warning(f"⚠️ Could not check disk space: {e}")
        return True

def main():
    """Main download function"""
    print("🦙 Llama 4 Model Downloader")
    print("=" * 40)
    
    # Check disk space
    if not check_disk_space():
        response = input("Continue anyway? (y/N): ")
        if response.lower() != 'y':
            print("Download cancelled.")
            return
    
    # Download model
    if download_model():
        print("\n🎉 Model download completed successfully!")
        print("You can now run the chat interface with: streamlit run app.py")
    else:
        print("\n❌ Model download failed!")
        print("Please check your internet connection and try again.")
        sys.exit(1)

if __name__ == "__main__":
    main()
