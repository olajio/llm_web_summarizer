# Website Summarizer

An intelligent office assistant that analyzes website contents and provides concise, accurate summaries using AI models. Supports multiple AI providers including Ollama (local), OpenAI, Google Gemini, Anthropic Claude, and more.

## Features

- **Automated Web Scraping**: Fetches and extracts meaningful content from any website
- **AI-Powered Summarization**: Uses state-of-the-art language models to generate intelligent summaries
- **Multiple AI Provider Support**: Choose from local (Ollama) or cloud-based AI services
- **News Detection**: Automatically identifies and summarizes news or announcements
- **Clean Output**: Presents summaries in beautifully formatted Markdown
- **Flexible Configuration**: Easy switching between different AI providers and models

## Prerequisites

- Python 3.7 or higher
- An AI provider (choose one):
  - **Ollama** (local, free) - Recommended for privacy and offline use
  - **OpenAI** (cloud, paid) - GPT-4 and GPT-3.5 models
  - **Google Gemini** (cloud, free tier available)
  - **Claude** (via OpenRouter or similar)
  - **Other providers** (OpenRouter, Together AI, Groq, etc.)

## Installation

1. **Clone or download this project**

2. **Install required Python packages:**
   ```bash
   pip install openai python-dotenv ipython
   ```

3. **Choose and configure your AI provider** (see Configuration section below)

## AI Provider Configuration

The script supports multiple AI providers. Choose one and follow its setup instructions:

### Option 1: Ollama (Local AI - Default) ⭐ Recommended

**Pros:** Free, private, works offline, no API key needed
**Cons:** Requires local installation and decent hardware

1. **Install Ollama:**
   - Visit [ollama.ai](https://ollama.ai) and download for your OS
   
2. **Pull a model:**
   ```bash
   ollama pull llama3.2
   ```
   
3. **Start Ollama:**
   ```bash
   ollama serve
   ```

4. **Configure in code:**
   - Already configured by default!
   - Change `MODEL_NAME` if using different model

**Available Models:**
- `llama3.2` (default)
- `llama3.1`
- `mistral`
- `phi3`
- `codellama`

---

### Option 2: OpenAI (Official API)

**Pros:** Highest quality models (GPT-4), excellent performance
**Cons:** Paid service (charges per token)

1. **Get API key:**
   - Visit [platform.openai.com/api-keys](https://platform.openai.com/api-keys)
   - Create account and generate API key
   
2. **Add to `.env` file:**
   ```
   OPENAI_API_KEY=sk-your_api_key_here
   ```

3. **Configure in code:**
   ```python
   # Uncomment these lines in the script:
   openai_api_key = os.getenv("OPENAI_API_KEY")
   openai_client = OpenAI(api_key=openai_api_key)
   client = openai_client
   MODEL_NAME = "gpt-4o-mini"  # Or: gpt-4, gpt-4-turbo, gpt-3.5-turbo
   
   # Comment out the Ollama section
   ```

**Available Models:**
- `gpt-4o-mini` (fast, affordable)
- `gpt-4` (most capable)
- `gpt-4-turbo` (balance of speed and quality)
- `gpt-3.5-turbo` (fastest, cheapest)

---

### Option 3: Google Gemini

**Pros:** Free tier available, good performance, Google ecosystem integration
**Cons:** Requires Google account and API setup

1. **Get API key:**
   - Visit [ai.google.dev](https://ai.google.dev/)
   - Create project and generate API key
   
2. **Add to `.env` file:**
   ```
   GOOGLE_API_KEY=AIz_your_api_key_here
   ```

3. **Configure in code:**
   ```python
   # Uncomment these lines in the script:
   GEMINI_BASE_URL = "https://generativelanguage.googleapis.com/v1beta/openai/"
   google_api_key = os.getenv("GOOGLE_API_KEY")
   gemini = OpenAI(base_url=GEMINI_BASE_URL, api_key=google_api_key)
   client = gemini
   MODEL_NAME = "gemini-1.5-flash"
   
   # Comment out the Ollama section
   ```

**Available Models:**
- `gemini-1.5-flash` (fast, free tier)
- `gemini-1.5-pro` (more capable)
- `gemini-1.0-pro` (original version)

---

### Option 4: Anthropic Claude (via OpenRouter)

**Pros:** Excellent reasoning, longer context windows
**Cons:** Requires third-party service (OpenRouter), costs money

1. **Get API key:**
   - Visit [openrouter.ai](https://openrouter.ai)
   - Create account and generate API key
   
2. **Add to `.env` file:**
   ```
   CLAUDE_API_KEY=your_openrouter_api_key_here
   ```

3. **Configure in code:**
   ```python
   # Uncomment these lines in the script:
   CLAUDE_BASE_URL = "https://openrouter.ai/api/v1"
   claude_api_key = os.getenv("CLAUDE_API_KEY")
   claude = OpenAI(base_url=CLAUDE_BASE_URL, api_key=claude_api_key)
   client = claude
   MODEL_NAME = "anthropic/claude-3-haiku"
   
   # Comment out the Ollama section
   ```

**Available Models:**
- `anthropic/claude-3-haiku` (fast, affordable)
- `anthropic/claude-3-sonnet` (balanced)
- `anthropic/claude-3-opus` (most capable)

---

### Option 5: Other Providers

The script works with any OpenAI-compatible API. Popular options:

**OpenRouter** ([openrouter.ai](https://openrouter.ai))
- Access to 100+ models from various providers
- Pay per use, competitive pricing

**Together AI** ([together.ai](https://together.ai))
- Open source models
- Good performance and pricing

**Groq** ([groq.com](https://groq.com))
- Extremely fast inference
- Free tier available

**Replicate** ([replicate.com](https://replicate.com))
- Wide variety of models
- Pay per second of compute

**Configuration template:**
```python
CUSTOM_BASE_URL = "https://api.your-provider.com/v1"
custom_api_key = os.getenv("YOUR_PROVIDER_API_KEY")
custom_client = OpenAI(base_url=CUSTOM_BASE_URL, api_key=custom_api_key)
client = custom_client
MODEL_NAME = "provider-specific-model-name"
```

## Usage

1. **Run the script:**
   ```bash
   python main_script.py
   ```

2. **Enter a website URL when prompted:**
   ```
   Enter url or website address. The address must be in the format https://url.domain :
   ```
   
   You can enter the URL in either format:
   - `example.com` (the script will automatically add `https://`)
   - `https://example.com`

3. **View the summary:**
   The script will display a formatted Markdown summary in your terminal/Jupyter notebook.

## How It Works

1. **User Input**: You provide a website URL
2. **Web Scraping**: The `scraper.py` module fetches and extracts meaningful text content
3. **Content Processing**: Extracted content is formatted with system and user prompts
4. **AI Analysis**: The configured AI model analyzes the content and filters out navigation elements
5. **Summary Generation**: AI generates a concise summary including any news or announcements
6. **Display**: Summary is rendered in beautiful Markdown format

## Project Structure

```
project/
├── main_script.py      # Main application (this file)
├── scraper.py          # Web scraping module
├── .env                # Environment variables (API keys)
├── README.md           # This file
└── requirements.txt    # Python dependencies (optional)
```

## Customization

### Modify the System Prompt

Change how the AI behaves by editing the `system_prompt` variable:

```python
system_prompt = """
You are a [YOUR ROLE] that analyzes website contents and provides [YOUR OUTPUT].
Focus on [YOUR PRIORITIES].
Respond in [YOUR FORMAT].
"""
```

### Adjust Summary Detail

Modify the `user_prompt_prefix` to change output detail:

```python
user_prompt_prefix = """
Provide a [detailed/brief] summary.
Focus on [specific aspects].
Include [specific elements].
"""
```

### Change Output Format

Request different formats in the system prompt:
- `Respond in markdown` (default)
- `Respond in JSON format`
- `Respond as bullet points`
- `Respond as a single paragraph`

## 🔍 Comparison of AI Providers

| Provider | Cost | Speed | Quality | Privacy | Best For |
|----------|------|-------|---------|---------|----------|
| **Ollama** | Free | Medium | Good | 100% Private | Privacy, offline use, experimentation |
| **OpenAI** | $$$ | Fast | Excellent | Cloud-based | Production, highest quality needed |
| **Gemini** | Free tier | Fast | Very Good | Cloud-based | Free tier usage, good balance |
| **Claude** | $$ | Medium | Excellent | Cloud-based | Long documents, reasoning tasks |
| **OpenRouter** | $ | Varies | Varies | Cloud-based | Trying multiple models, flexibility |

## Troubleshooting

### General Issues

**Error: "Module 'scraper' not found"**
- Solution: Ensure `scraper.py` is in the same directory
- Verify `scraper.py` contains `fetch_website_contents()` function

**Error: "No module named 'openai'"**
- Solution: Install dependencies with `pip install openai python-dotenv ipython`

### Ollama Issues

**Error: "Connection refused"**
- Solution: Start Ollama server with `ollama serve`
- Verify it's running on `http://localhost:11434`

**Error: "Model 'llama3.2' not found"**
- Solution: Pull the model with `ollama pull llama3.2`

**Slow performance**
- Ensure adequate RAM (8GB minimum)
- Try smaller models like `phi3`
- Close other resource-intensive applications

### OpenAI Issues

**Error: "Incorrect API key"**
- Verify key starts with `sk-`
- Check `.env` file is in the same directory
- Ensure no extra spaces in the API key

**Error: "Rate limit exceeded"**
- You've hit your usage limit
- Wait a few minutes or upgrade your OpenAI plan

### Gemini Issues

**Error: "API key not valid"**
- Verify key starts with `AIz`
- Ensure API is enabled in Google Cloud Console
- Check billing is set up (even for free tier)

### Claude/OpenRouter Issues

**Error: "Model not found"**
- Verify the exact model name from provider's documentation
- Check your account has access to that model

**Error: "Insufficient credits"**
- Add credits to your OpenRouter/provider account

## Privacy & Security

### Ollama (Local)
- ✅ 100% private - all processing on your machine
- ✅ No data leaves your computer
- ✅ Works offline
- ✅ No API keys needed

### Cloud Providers (OpenAI, Gemini, Claude)
- ⚠️ Website content sent to provider's servers
- ⚠️ Subject to provider's privacy policy
- ⚠️ Requires internet connection
- ⚠️ API keys must be kept secure

**Security Tips:**
- Never commit `.env` file to version control
- Add `.env` to your `.gitignore`
- Rotate API keys periodically
- Use environment variables, never hardcode keys

## Dependencies

```
openai>=1.0.0          # OpenAI-compatible API client
python-dotenv>=1.0.0   # Environment variable management
ipython>=8.0.0         # Rich display capabilities
```

Create `requirements.txt`:
```bash
pip freeze > requirements.txt
```

Install from `requirements.txt`:
```bash
pip install -r requirements.txt
```

## Contributing

Contributions are welcome! Areas for improvement:
- Support for PDF and document summarization
- Batch processing of multiple URLs
- Export summaries to files (PDF, TXT, MD)
- Web interface using Streamlit or Gradio
- Comparison mode for multiple website versions
- Custom prompt templates
- Summary caching to avoid re-processing

## Example Output

**Input:** `https://anthropic.com`

**Output:**
```markdown
### Website Summary

Anthropic is an AI safety company focused on building reliable, 
interpretable, and steerable AI systems. The company develops Claude, 
a family of large language models designed with safety in mind.

**Recent Announcements:**
- Claude 3.5 Sonnet released with improved performance
- New partnership with Amazon Web Services announced
- Research paper published on Constitutional AI approach
```

## License

This project is provided as-is for educational and personal use.

## Acknowledgments

- Built with [OpenAI API](https://openai.com) compatibility
- Local AI powered by [Ollama](https://ollama.ai)
- Cloud options: [Google Gemini](https://ai.google.dev/), [Anthropic Claude](https://anthropic.com)
- Multi-model support via [OpenRouter](https://openrouter.ai)

---

**Made with ❤️ for efficient web content analysis**

*Choose your AI provider based on your needs: Ollama for privacy, OpenAI for quality, Gemini for free tier, Claude for reasoning!*
