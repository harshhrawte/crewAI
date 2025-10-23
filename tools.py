# tools.py - COMPLETELY REWRITTEN
from crewai.tools import tool

@tool("youtube_search")
def youtube_search(query: str) -> str:
    """
    Search YouTube videos on a specific channel for a given query.
    Use this tool to search for videos about any topic.
    
    Args:
        query: The search query as a simple string
    """
    youtube_channel_handle = '@krishnaik06'
    
    # Convert to string if somehow it's not
    if not isinstance(query, str):
        if isinstance(query, dict) and 'description' in query:
            query = query['description']
        else:
            query = str(query)
    
    print(f"Searching for: {query}")
    
    # Mock response - replace with actual YouTube API call
    if any(term in query.upper() for term in ["AI", "ML", "DATA SCIENCE", "MACHINE LEARNING", "ARTIFICIAL"]):
        return f"""Found video about '{query}' on channel {youtube_channel_handle}:

Title: "AI vs ML vs DL vs Data Science - Complete Guide"
Duration: 25:30
Views: 1.2M

Video Summary:
This comprehensive video explains the key differences between:

1. **Artificial Intelligence (AI)**: The broader concept of machines performing tasks that typically require human intelligence. AI includes everything from simple rule-based systems to complex machine learning models.

2. **Machine Learning (ML)**: A subset of AI that focuses on algorithms that can learn and make decisions from data without being explicitly programmed for every scenario.

3. **Deep Learning (DL)**: A specialized subset of ML that uses neural networks with multiple layers (deep neural networks) to process and large amounts of data.

4. **Data Science**: An interdisciplinary field that combines domain expertise, programming skills, mathematics, and statistics to extract insights from data.

The video covers real-world applications, career paths, and how these fields interconnect in modern technology."""
    else:
        return f"Searched for '{query}' on {youtube_channel_handle} but no relevant videos found."
