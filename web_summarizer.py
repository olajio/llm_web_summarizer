# ============================================================================
# Website Summarizer with AI
# ============================================================================
# This script fetches website content and generates intelligent summaries
# using AI models. Supports multiple AI providers with simple configuration.
# ============================================================================

# ----------------------------------------------------------------------------
# IMPORTS
# ----------------------------------------------------------------------------
import os
from dotenv import load_dotenv
from scraper import fetch_website_contents  # Custom module for web scraping
from IPython.display import Markdown, display
from openai import OpenAI  # OpenAI-compatible client for multiple providers

# Load environment variables from .env file
load_dotenv()

# ============================================================================
# AI PROVIDER CONFIGURATION
# ============================================================================
# Configure which AI provider you want to use by uncommenting the appropriate
# section below. Only one provider should be active at a time.
# ============================================================================

# ----------------------------------------------------------------------------
# OPTION 1: OLLAMA (Local AI - Default)
# ----------------------------------------------------------------------------
# Ollama runs AI models locally on your machine. No API keys needed!
# Requirements: Install Ollama from https://ollama.ai
# Pull model: ollama pull llama3.2
# Start server: ollama serve
# ----------------------------------------------------------------------------
OLLAMA_BASE_URL = "http://localhost:11434/v1"
ollama_api_key = "ollama"  # Dummy key for local use
ollama = OpenAI(base_url=OLLAMA_BASE_URL, api_key=ollama_api_key)
client = ollama  # Set active client
MODEL_NAME = "llama3.2"  # Change to: llama3.1, mistral, phi3, codellama, etc.

# ----------------------------------------------------------------------------
# OPTION 2: GOOGLE GEMINI (Commented out by default)
# ----------------------------------------------------------------------------
# Gemini is Google's AI model with generous free tier
# Requirements: Get API key from https://ai.google.dev/
# Add to .env file: GOOGLE_API_KEY=your_api_key_here
# ----------------------------------------------------------------------------
# GEMINI_BASE_URL = "https://generativelanguage.googleapis.com/v1beta/openai/"
# google_api_key = os.getenv("GOOGLE_API_KEY")
# gemini = OpenAI(base_url=GEMINI_BASE_URL, api_key=google_api_key)
# client = gemini  # Set active client
# MODEL_NAME = "gemini-1.5-flash"  # Or: gemini-1.5-pro, gemini-1.0-pro

# # API Key Validation for Gemini
# if not google_api_key:
#     print("No API key found - check your .env file or troubleshooting notebook!")
# elif not google_api_key.startswith("AIz"):
#     print("API key found but doesn't start with 'AIz' - please verify it's correct")
# else:
#     print("API key found and looks good!")

# ----------------------------------------------------------------------------
# OPTION 3: OPENAI (Official OpenAI API)
# ----------------------------------------------------------------------------
# Use official OpenAI models like GPT-4 or GPT-3.5
# Requirements: Get API key from https://platform.openai.com/api-keys
# Add to .env file: OPENAI_API_KEY=your_api_key_here
# Note: OpenAI is a paid service, charges per token
# ----------------------------------------------------------------------------
# openai_api_key = os.getenv("OPENAI_API_KEY")
# openai_client = OpenAI(api_key=openai_api_key)  # No base_url needed
# client = openai_client  # Set active client
# MODEL_NAME = "gpt-4o-mini"  # Or: gpt-4, gpt-4-turbo, gpt-3.5-turbo

# # API Key Validation for OpenAI
# if not openai_api_key:
#     print("No OpenAI API key found - check your .env file!")
# elif not openai_api_key.startswith("sk-"):
#     print("API key found but doesn't start with 'sk-' - please verify it's correct")
# else:
#     print("OpenAI API key found and looks good!")

# ----------------------------------------------------------------------------
# OPTION 4: ANTHROPIC CLAUDE (Via OpenAI-compatible wrapper)
# ----------------------------------------------------------------------------
# Use Claude models via third-party OpenAI-compatible endpoints
# Note: Direct Claude API requires different client library (anthropic)
# For OpenAI-compatible endpoint, check providers like OpenRouter
# Add to .env file: CLAUDE_API_KEY=your_api_key_here
# ----------------------------------------------------------------------------
# CLAUDE_BASE_URL = "https://openrouter.ai/api/v1"  # Example: OpenRouter
# claude_api_key = os.getenv("CLAUDE_API_KEY")
# claude = OpenAI(base_url=CLAUDE_BASE_URL, api_key=claude_api_key)
# client = claude  # Set active client
# MODEL_NAME = "anthropic/claude-3-haiku"  # Or: claude-3-sonnet, claude-3-opus

# ----------------------------------------------------------------------------
# OPTION 5: OTHER PROVIDERS (OpenRouter, Together AI, etc.)
# ----------------------------------------------------------------------------
# Many providers offer OpenAI-compatible APIs:
# - OpenRouter: https://openrouter.ai (access to multiple models)
# - Together AI: https://together.ai (open source models)
# - Groq: https://groq.com (fast inference)
# - Replicate: https://replicate.com (various models)
# Add to .env file: YOUR_PROVIDER_API_KEY=your_api_key_here
# ----------------------------------------------------------------------------
# CUSTOM_BASE_URL = "https://api.your-provider.com/v1"
# custom_api_key = os.getenv("YOUR_PROVIDER_API_KEY")
# custom_client = OpenAI(base_url=CUSTOM_BASE_URL, api_key=custom_api_key)
# client = custom_client  # Set active client
# MODEL_NAME = "your-model-name"  # Check provider's documentation

# ============================================================================
# AI PROMPT CONFIGURATION
# ============================================================================
# These prompts guide the AI's behavior and output format
# ============================================================================

# System prompt: Defines the AI's role and behavior
system_prompt = """
You are a office assistant that analyzes the contents of a website,
and provides a short, accurate summary, ignoring text that might be navigation related.
Respond in markdown. Do not wrap the markdown in a code block - respond just with the markdown.
"""

# User prompt prefix: Specific instructions for each request
user_prompt_prefix = """
Here are the contents of a website.
Provide a short summary of this website.
If it includes news or announcements, then summarize these too.
"""

# ============================================================================
# FUNCTION DEFINITIONS
# ============================================================================

# Constructs message array for AI API with system and user prompts
def messages_for(url_content):
    return [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt_prefix + url_content}
    ]

# Fetches website content and generates AI-powered summary
def summarize(url):
    url_content = fetch_website_contents(url)
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=messages_for(url_content)
    )
    return response.choices[0].message.content

# Generates and displays website summary in formatted Markdown
def display_summary(url):
    summary = summarize(url)
    display(Markdown(summary))

# ============================================================================
# MAIN EXECUTION
# ============================================================================
if __name__ == "__main__":
    # Get URL input from user
    url = input("Enter url or website address. The address you be in the format url.doman. For example, cnn.com :")
    
    # Add https:// prefix if not already present
    url = f"https://{url}"
    
    # Display confirmation to user
    print("")
    print(f"You entered {url}")
    print("")
    
    # Generate and display the summary
    display_summary(url)
