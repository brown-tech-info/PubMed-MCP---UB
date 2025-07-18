# PubMed MCP Server

A Model Context Protocol (MCP) server that provides access to PubMed scientific publications. Search research papers, retrieve abstracts, and get publication details directly within your Claude Desktop application.

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![MCP Compatible](https://img.shields.io/badge/MCP-Compatible-green.svg)](https://modelcontextprotocol.io/)

## ✨ Features

- 🔍 **Smart PubMed Search** - Search scientific publications with advanced filtering
- 📄 **Detailed Article Info** - Get comprehensive publication details by PMID
- 🔗 **Related Articles** - Discover similar research papers
- 🌐 **Clickable Links** - Direct access to PubMed, DOI, and full-text sources
- 🔒 **Secure API Management** - Environment-based API key storage
- ⚡ **Fast & Reliable** - Optimized API calls with proper error handling

## 🚀 Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/pubmed-mcp-server.git
cd pubmed-mcp-server
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure Environment
```bash
# Copy the example environment file
cp .env.example .env

# Edit .env with your details
PUBMED_API_KEY=your_api_key_here
PUBMED_EMAIL=your_email@example.com
PUBMED_TOOL_NAME=PubMedMCPServer
```

> **💡 Getting an API Key**: Visit [NCBI Account Settings](https://www.ncbi.nlm.nih.gov/account/settings/) to generate a free API key for better rate limits.

### 4. Test the Server
```bash
python test_server.py
```

## 🔧 Claude Desktop Integration

### 1. Locate Your Claude Desktop Config
- **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`
- **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`

### 2. Add Server Configuration
```json
{
  "mcpServers": {
    "pubmed": {
      "command": "python",
      "args": ["/path/to/your/pubmed-mcp-server/server.py"],
      "env": {
        "PYTHONPATH": "/path/to/your/pubmed-mcp-server"
      }
    }
  }
}
```

### 3. Restart Claude Desktop

You should now see PubMed tools available in Claude Desktop! 🎉

## 🛠️ Available Tools

### `search_pubmed`
Search PubMed for scientific publications with advanced filtering.

**Parameters:**
- `query` (required): Search terms (e.g., "machine learning healthcare", "CRISPR gene editing")
- `max_results` (optional): Results to return (1-50, default: 10)
- `sort` (optional): Sort by "relevance", "pub_date", "author", or "journal"
- `date_range` (optional): Filter by date ("2020:2024", "last_5_years", "2023")

### `get_publication_details`
Get comprehensive information about a specific publication.

**Parameters:**
- `pmid` (required): PubMed ID of the publication

### `get_similar_articles`
Find articles similar to a given publication.

**Parameters:**
- `pmid` (required): Reference publication PMID
- `max_results` (optional): Number of similar articles (1-20, default: 10)

## 💬 Usage Examples

Once connected to Claude Desktop, try these natural language queries:

```
🔍 "Search PubMed for recent papers on COVID-19 vaccines published in 2024"
📄 "Get detailed information for PMID 33301246"
🔗 "Find articles similar to PMID 34567890"
📊 "Look up machine learning applications in radiology from the last 3 years"
🧬 "Search for CRISPR gene editing papers, show me 20 results sorted by date"
```

## ⚡ API Rate Limits

- **Without API key**: 3 requests/second
- **With API key**: 10 requests/second

The server automatically handles rate limiting and includes retry logic.

## 🐛 Troubleshooting

### Server Won't Start
```bash
# Check dependencies
python diagnose.py

# Verify Python version
python --version  # Should be 3.8+
```

### Claude Desktop Not Connecting
1. Verify file paths in Claude config
2. Restart Claude Desktop completely
3. Check server logs for errors
4. Ensure .env file is properly configured

### No Search Results
- Check internet connection
- Verify PubMed API accessibility
- Try simpler search terms
- Check if API key is valid

## 🔗 API Reference

This server uses the [NCBI E-utilities API](https://www.ncbi.nlm.nih.gov/books/NBK25497/):
- **E-search**: Find publication PMIDs
- **E-fetch**: Retrieve detailed article information  
- **E-link**: Discover related articles

## 🧪 Development

### Project Structure
```
pubmed-mcp-server/
├── server.py              # Main MCP server
├── test_server.py         # Test suite
├── diagnose.py           # Diagnostic tool
├── requirements.txt      # Dependencies
├── .env.example         # Environment template
└── README.md           # Documentation
```

### Adding New Features
1. **New Tools**: Extend `_setup_handlers()` in `server.py`
2. **API Endpoints**: Add methods following PubMed E-utilities
3. **Data Sources**: Integrate other NCBI databases (PMC, Taxonomy, etc.)

### Running Tests
```bash
python test_server.py
python diagnose.py
```

## 📋 Requirements

- **Python**: 3.8 or higher
- **Claude Desktop**: Latest version
- **Dependencies**: See `requirements.txt`
- **Optional**: NCBI API key for better performance

## 🤝 Contributing

Contributions welcome! Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Model Context Protocol](https://modelcontextprotocol.io/) team
- [NCBI](https://www.ncbi.nlm.nih.gov/) for the excellent E-utilities API
- [Claude Desktop](https://claude.ai/) for MCP integration

## 📞 Support

- 🐛 **Bug Reports**: [GitHub Issues](https://github.com/yourusername/pubmed-mcp-server/issues)
- 💡 **Feature Requests**: [GitHub Discussions](https://github.com/yourusername/pubmed-mcp-server/discussions)
- 📧 **Contact**: your.email@example.com

---

⭐ **Star this repo if it helps your research!** ⭐