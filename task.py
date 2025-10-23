from crewai import Task
from agents import blog_researcher, blog_writer
from tools import youtube_search

# Simple research task
research_task = Task(
    description="Search for videos about '{topic}' and summarize the content.",
    expected_output="A 2-3 paragraph summary of video content about {topic}",
    agent=blog_researcher,
    tools=[youtube_search]
)

# Simple writing task
writing_task = Task(
    description="Write a blog post about '{topic}' using the research findings.",
    expected_output="A well-structured blog post about {topic}",
    agent=blog_writer,
    context=[research_task],
    output_file='blog_post.md'
)