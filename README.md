# 🦙 Llama 4 Local Chat Interface

A modern, user-friendly web interface for running Llama 4 Scout 17B locally using Streamlit and llama.cpp.

## ✨ Features

- **Local AI Chat**: Run Llama 4 Scout 17B completely offline
- **Modern Web Interface**: Clean, responsive UI built with Streamlit
- **High Performance**: Optimized with llama.cpp for efficient inference
- **Easy Setup**: Simple installation and model download process
- **Customizable**: Adjustable generation parameters for different use cases

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- At least 16GB RAM (32GB recommended)
- NVIDIA GPU with CUDA support (optional, for faster inference)

### Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd Llama
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Download llama.cpp**
   ```bash
   git clone https://github.com/ggerganov/llama.cpp.git
   cd llama.cpp
   make
   cd ..
   ```

4. **Download the model**
   ```bash
   python download.py
   ```

5. **Run the application**
   ```bash
   streamlit run app.py
   ```

The app will be available at `http://localhost:8501`

## 📁 Project Structure

```
Llama/
├── app.py              # Main Streamlit application
├── download.py         # Model download script
├── requirements.txt    # Python dependencies
├── README.md          # This file
├── .gitignore         # Git ignore rules
├── config.py          # Configuration settings
├── utils.py           # Utility functions
└── llama_models/      # Downloaded models (created after download)
    └── Llama-4-Scout-17B/
        └── Llama-4-Scout-17B-16E-Instruct-UD-IQ2_XXS.gguf
```

## 🎛️ Configuration

You can customize the model behavior by modifying parameters in `app.py`:

- **Temperature**: Controls randomness (0.0-1.0)
- **Top-p**: Nucleus sampling parameter
- **Context size**: Maximum input length
- **Threads**: CPU threads for inference
- **GPU layers**: Number of layers to run on GPU

## 🔧 Advanced Usage

### Custom Model Path

Edit the `MODEL_PATH` variable in `app.py` to use a different model:

```python
MODEL_PATH = "path/to/your/model.gguf"
```

### Batch Processing

For processing multiple prompts, you can modify the script to handle file inputs or batch operations.

## 🐛 Troubleshooting

### Common Issues

1. **Out of Memory**: Reduce `--ctx-size` or use a smaller model
2. **Slow Performance**: Enable GPU acceleration or increase `--threads`
3. **Model Download Fails**: Check internet connection and disk space

### Performance Tips

- Use an SSD for faster model loading
- Enable GPU acceleration if available
- Adjust thread count based on your CPU cores

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [llama.cpp](https://github.com/ggerganov/llama.cpp) for efficient inference
- [Streamlit](https://streamlit.io/) for the web interface
- [Hugging Face](https://huggingface.co/) for model hosting
- [Unsloth](https://github.com/unslothai) for the optimized model

## 📞 Support

If you encounter any issues or have questions, please open an issue on GitHub. 