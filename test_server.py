#!/usr/bin/env python3
"""
Test script for PubMed MCP Server

This script tests the basic functionality of the PubMed MCP server
without requiring Claude Desktop integration.
"""

import asyncio
import json
from server import PubMedMCPServer

async def test_pubmed_server():
    """Test the PubMed MCP server functionality"""
    print("Testing PubMed MCP Server...")
    print("=" * 50)
    
    server = PubMedMCPServer()
    
    # Test 1: Search PubMed
    print("\n1. Testing PubMed search...")
    try:
        search_args = {
            "query": "COVID-19 vaccine",
            "max_results": 3,
            "sort": "date"
        }
        results = await server._search_pubmed(search_args)
        print("✅ Search successful!")
        print(f"Result preview: {results[0].text[:200]}...")
    except Exception as e:
        print(f"❌ Search failed: {e}")
    
    # Test 2: Get publication details (using a known PMID)
    print("\n2. Testing publication details...")
    try:
        detail_args = {"pmid": "33301246"}  # A COVID-19 vaccine paper
        results = await server._get_publication_details(detail_args)
        print("✅ Publication details successful!")
        print(f"Result preview: {results[0].text[:200]}...")
    except Exception as e:
        print(f"❌ Publication details failed: {e}")
    
    # Test 3: Get similar articles
    print("\n3. Testing similar articles...")
    try:
        similar_args = {
            "pmid": "33301246",
            "max_results": 3
        }
        results = await server._get_similar_articles(similar_args)
        print("✅ Similar articles successful!")
        print(f"Result preview: {results[0].text[:200]}...")
    except Exception as e:
        print(f"❌ Similar articles failed: {e}")
    
    print("\n" + "=" * 50)
    print("Testing complete!")
    print("\nIf all tests passed, your server is ready to use with Claude Desktop.")
    print("If any tests failed, check your internet connection and API configuration.")

if __name__ == "__main__":
    asyncio.run(test_pubmed_server())