import os
import time
from dotenv import load_dotenv
from crewai import Crew, Process
from agents import blog_researcher, blog_writer
from task import research_task, writing_task


def main():
    print("Starting YouTube research crew...")
    
    # Create crew with minimal configuration
    crew = Crew(
        agents=[blog_researcher, blog_writer],
        tasks=[research_task, writing_task],
        process=Process.sequential,
        verbose=True,
        memory=False,
        cache=False,
        max_rpm=10,  
        share_crew=False
    )
    
    try:
        print("Executing crew...")
        result = crew.kickoff(inputs={'topic': 'AI vs ML vs Data Science'})
        
        print("\n" + "="*50)
        print("SUCCESS! Result:")
        print("="*50)
        print(result)
        
        # Check if output file was created
        if os.path.exists('blog_post.md'):
            print("\nBlog post saved to: blog_post.md")
        
    except Exception as e:
        print(f"\nError occurred: {str(e)}")
        print("\nTroubleshooting steps:")
        print("1. Check your GROQ_API_KEY in .env file")
        print("2. Verify you have credits in your Groq account")
        print("3. Try reducing max_rpm or adding delays")
        print("4. Check internet connection")

if __name__ == "__main__":
    main()