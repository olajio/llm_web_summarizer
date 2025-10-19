# Website Summarizer

An intelligent office assistant that analyzes website contents and provides concise, accurate summaries using local AI models via Ollama.

## Features

- **Automated Web Scraping**: Fetches and extracts meaningful content from any website
- **AI-Powered Summarization**: Uses Llama 3.2 model to generate intelligent summaries
- **News Detection**: Automatically identifies and summarizes news or announcements
- **Clean Output**: Presents summaries in beautifully formatted Markdown
- **Local AI**: Runs entirely on your machine using Ollama - no external API calls or data sharing

## Prerequisites

- Python 3.7 or higher
- Ollama installed and running locally
- Llama 3.2 model pulled in Ollama

## Installation

1. **Clone or download this project**

2. **Install required Python packages:**
   ```bash
   pip install openai python-dotenv ipython
   ```

3. **Install Ollama** (if not already installed):
   - Visit [ollama.ai](https://ollama.ai) for installation instructions
   - Pull the Llama 3.2 model:
     ```bash
     ollama pull llama3.2
     ```

4. **Ensure Ollama is running:**
   ```bash
   ollama serve
   ```
   (This should be running on `http://localhost:11434`)

## Required Files

- `main_script.py` - The main application script (this file)
- `scraper.py` - Web scraping module (must contain `fetch_website_contents()` function)
- `.env` - Environment variables file (optional, for future API key configurations)

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

1. **Web Scraping**: The `scraper.py` module fetches the HTML content from the provided URL and extracts meaningful text
2. **Content Processing**: The extracted content is sent to the AI model with a specialized system prompt
3. **AI Analysis**: Llama 3.2 analyzes the content, filtering out navigation elements and focusing on main content
4. **Summary Generation**: The AI generates a concise summary including any news or announcements found
5. **Display**: The summary is rendered in beautiful Markdown format

## System Prompt

The AI assistant is instructed to:
- Analyze website contents accurately
- Provide short, concise summaries
- Ignore navigation-related text
- Identify and summarize news or announcements
- Respond in clean Markdown format

## Configuration

### Ollama Settings
The script is configured to use:
- **Base URL**: `http://localhost:11434/v1`
- **Model**: `llama3.2`
- **API Key**: `ollama` (dummy key for local use)

### Switching to Other Models

To use a different Ollama model, modify this line:
```python
model = "llama3.2"  # Change to your preferred model
```

Available alternatives:
- `llama3.1`
- `mistral`
- `codellama`
- `phi3`

### Future: Google Gemini Support

The code includes commented-out sections for Google Gemini API integration. To use Gemini:

1. Uncomment the Gemini-related lines
2. Add your Google API key to `.env`:
   ```
   GOOGLE_API_KEY=your_api_key_here
   ```
3. Update the base URL and model name accordingly

## Example Output

```markdown
### Website Summary

This website provides information about...

**Recent Announcements:**
- New product launch scheduled for Q4 2024
- Partnership with XYZ Corporation announced
- Updated pricing structure effective immediately
```

## Troubleshooting

### Ollama Connection Issues
- **Error**: "Connection refused"
- **Solution**: Ensure Ollama is running (`ollama serve`)

### Model Not Found
- **Error**: "Model 'llama3.2' not found"
- **Solution**: Pull the model with `ollama pull llama3.2`

### Scraper Module Issues
- **Error**: "Module 'scraper' not found"
- **Solution**: Ensure `scraper.py` is in the same directory

### Slow Response Times
- **Issue**: Summarization takes too long
- **Solution**:
  - Use a smaller/faster model like `phi3`
  - Ensure you have adequate RAM (8GB minimum recommended)
  - Check if other resource-intensive applications are running

## Privacy & Security

- **100% Local**: All processing happens on your machine
- **No Data Sharing**: Website content and summaries never leave your computer
- **No API Keys Required**: Uses local Ollama instance (no external API calls)

## Dependencies

- `openai` - OpenAI-compatible API client
- `python-dotenv` - Environment variable management
- `IPython` - Rich display capabilities
- `scraper` - Custom web scraping module (included in project)

## Contributing

Contributions are welcome! Areas for improvement:
- Support for PDF and document summarization
- Batch processing of multiple URLs
- Export summaries to file formats (PDF, TXT, MD)
- Web interface using Streamlit or Flask
- Comparison mode for multiple website versions

## License

This project is provided as-is for educational and personal use.

## Acknowledgments

- Built with [Ollama](https://ollama.ai)
- Powered by [Llama 3.2](https://ai.meta.com/llama/)
- Uses OpenAI-compatible API interface
