"""
Llama 4 Chat Interface - Main Application
"""

import streamlit as st
import time
from typing import Optional

from config import UI_CONFIG, setup_environment, validate_system_requirements
from utils import (
    format_prompt, 
    run_llama_inference, 
    validate_model_exists, 
    validate_llama_cpp_exists,
    get_system_info,
    sanitize_input,
    estimate_tokens,
    format_response_time
)

def main():
    """Main application function"""
    # Setup environment
    setup_environment()
    
    # Configure Streamlit page
    st.set_page_config(
        page_title=UI_CONFIG["page_title"],
        page_icon=UI_CONFIG["page_icon"],
        layout=UI_CONFIG["layout"],
        initial_sidebar_state=UI_CONFIG["initial_sidebar_state"]
    )
    
    # Custom CSS for better styling
    st.markdown("""
    <style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        color: #FF6B6B;
        text-align: center;
        margin-bottom: 2rem;
    }
    .stTextArea textarea {
        border-radius: 10px;
        border: 2px solid #e0e0e0;
    }
    .stButton button {
        border-radius: 10px;
        background-color: #FF6B6B;
        color: white;
        font-weight: bold;
        padding: 0.5rem 2rem;
    }
    .stButton button:hover {
        background-color: #FF5252;
    }
    .info-box {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 10px;
        border-left: 4px solid #FF6B6B;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Header
    st.markdown('<h1 class="main-header">🦙 Llama 4 Chat Interface</h1>', unsafe_allow_html=True)
    st.markdown("### Local AI Chat with Llama 4 Scout 17B")
    
    # Sidebar
    with st.sidebar:
        st.header("⚙️ Settings")
        
        # System validation
        st.subheader("🔍 System Check")
        try:
            validate_system_requirements()
            st.success("✅ System requirements met")
        except Exception as e:
            st.error(f"❌ System check failed: {e}")
            return
        
        # Model validation
        model_exists = validate_model_exists()
        llama_exists = validate_llama_cpp_exists()
        
        if model_exists:
            st.success("✅ Model found")
        else:
            st.error("❌ Model not found")
            st.info("Run `python download.py` to download the model")
        
        if llama_exists:
            st.success("✅ llama.cpp found")
        else:
            st.error("❌ llama.cpp not found")
            st.info("Clone and build llama.cpp in the project directory")
        
        # System info
        if st.checkbox("Show system information"):
            sys_info = get_system_info()
            st.json(sys_info)
        
        # Generation parameters
        st.subheader("🎛️ Generation Parameters")
        temperature = st.slider("Temperature", 0.0, 1.0, 0.6, 0.1, 
                              help="Controls randomness in generation")
        top_p = st.slider("Top-p", 0.0, 1.0, 0.9, 0.05,
                         help="Nucleus sampling parameter")
        max_tokens = st.slider("Max tokens", 100, 4096, 2048, 100,
                              help="Maximum number of tokens to generate")
        
        # Custom config
        custom_config = {
            "temperature": temperature,
            "top_p": top_p,
            "max_tokens": max_tokens
        }
    
    # Main chat interface
    if not model_exists or not llama_exists:
        st.error("⚠️ Please ensure both the model and llama.cpp are properly set up before using the chat interface.")
        return
    
    # Chat history
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []
    
    # Display chat history
    for i, (user_msg, assistant_msg, response_time) in enumerate(st.session_state.chat_history):
        with st.chat_message("user"):
            st.write(user_msg)
        with st.chat_message("assistant"):
            st.write(assistant_msg)
            st.caption(f"Response time: {response_time}")
    
    # Input area
    user_input = st.text_area(
        "Your message:",
        height=UI_CONFIG["text_area_height"],
        placeholder=UI_CONFIG["placeholder_text"],
        key="user_input"
    )
    
    # Generate button
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        generate_button = st.button("🚀 Generate Response", use_container_width=True)
    
    # Processing
    if generate_button:
        if not user_input.strip():
            st.warning("⚠️ Please enter a message.")
        else:
            # Sanitize input
            sanitized_input = sanitize_input(user_input)
            
            # Estimate tokens
            estimated_tokens = estimate_tokens(sanitized_input)
            st.info(f"📊 Estimated input tokens: {estimated_tokens}")
            
            # Generate response
            with st.spinner("🤔 Thinking..."):
                start_time = time.time()
                
                # Format prompt
                prompt = format_prompt(sanitized_input)
                
                # Run inference
                response = run_llama_inference(prompt, custom_config)
                
                response_time = time.time() - start_time
                formatted_time = format_response_time(response_time)
                
                # Add to chat history
                st.session_state.chat_history.append((sanitized_input, response, formatted_time))
                
                # Display response
                st.markdown("### ✨ Response:")
                st.markdown(response)
                st.success(f"⏱️ Generated in {formatted_time}")
    
    # Clear chat button
    if st.session_state.chat_history:
        if st.button("🗑️ Clear Chat History"):
            st.session_state.chat_history = []
            st.rerun()
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; color: #666;'>
        <p>Built with ❤️ using Streamlit and llama.cpp</p>
        <p>Model: Llama 4 Scout 17B (IQ2_XXS quantized)</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
