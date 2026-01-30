"""
AI/ML Content Creator Hub
Aggregates news, monitors sources, and generates LinkedIn posts for content creators

This system helps you become a thought leader by:
1. Tracking AI/ML news from top sources
2. Monitoring new app launches
3. Following major developments
4. Mixing with your personal learning
"""

import json
from datetime import datetime, timedelta
from typing import List, Dict, Optional
import os


class ContentAggregator:
    """
    Aggregates content from multiple sources for AI/ML content creation
    """
    
    def __init__(self):
        self.sources = self._initialize_sources()
        self.content_queue = []
        
    def _initialize_sources(self) -> Dict:
        """
        Initialize all content sources to monitor
        """
        return {
            # YouTube Channels (RSS feeds available)
            "youtube": {
                "Two Minute Papers": "https://www.youtube.com/feeds/videos.xml?channel_id=UCbfYPyITQ-7l4upoX8nvctg",
                "Yannic Kilcher": "https://www.youtube.com/feeds/videos.xml?channel_id=UCZHmQk67mSJgfCCTn7xBfew",
                "AI Explained": "https://www.youtube.com/feeds/videos.xml?channel_id=UCNJ1Ymd5yFuUPtn21xtRbbw",
                "Sentdex": "https://www.youtube.com/feeds/videos.xml?channel_id=UCfzlCWGWYyIQ0aLC5w48gBQ",
                "3Blue1Brown": "https://www.youtube.com/feeds/videos.xml?channel_id=UCYO_jab_esuFRV4b17AJtAw",
                "Andrej Karpathy": "https://www.youtube.com/@AndrejKarpathy"
            },
            
            # Reddit Communities
            "reddit": {
                "r/MachineLearning": "https://www.reddit.com/r/MachineLearning/.rss",
                "r/artificial": "https://www.reddit.com/r/artificial/.rss",
                "r/LocalLLaMA": "https://www.reddit.com/r/LocalLLaMA/.rss",
                "r/MLQuestions": "https://www.reddit.com/r/MLQuestions/.rss",
                "r/learnmachinelearning": "https://www.reddit.com/r/learnmachinelearning/.rss"
            },
            
            # Official Blogs (RSS available)
            "blogs": {
                "OpenAI Blog": "https://openai.com/blog/rss.xml",
                "Google AI Blog": "https://blog.research.google/feeds/posts/default",
                "DeepMind Blog": "https://deepmind.google/blog/rss.xml",
                "Meta AI": "https://ai.meta.com/blog/rss/",
                "Anthropic": "https://www.anthropic.com/index/rss.xml",
                "NVIDIA Blog": "https://blogs.nvidia.com/feed/",
                "Hugging Face": "https://huggingface.co/blog/feed.xml",
                "Papers with Code": "https://paperswithcode.com/feeds/latest.xml"
            },
            
            # News Sites
            "news": {
                "VentureBeat AI": "https://venturebeat.com/category/ai/feed/",
                "TechCrunch AI": "https://techcrunch.com/category/artificial-intelligence/feed/",
                "The Verge AI": "https://www.theverge.com/ai-artificial-intelligence/rss/index.xml",
                "Ars Technica AI": "https://arstechnica.com/ai/feed/"
            },
            
            # Research Aggregators
            "research": {
                "arXiv CS.AI": "http://export.arxiv.org/rss/cs.AI",
                "arXiv CS.LG": "http://export.arxiv.org/rss/cs.LG",
                "arXiv CS.CV": "http://export.arxiv.org/rss/cs.CV",
                "arXiv CS.CL": "http://export.arxiv.org/rss/cs.CL"
            }
        }
    
    def get_all_sources_list(self) -> List[Dict[str, str]]:
        """
        Get formatted list of all sources for easy setup
        """
        all_sources = []
        for category, sources in self.sources.items():
            for name, url in sources.items():
                all_sources.append({
                    "category": category,
                    "name": name,
                    "url": url,
                    "type": "rss"
                })
        return all_sources
    
    def create_rss_reader_script(self, output_file: str = "rss_reader.py"):
        """
        Generate a Python script to read RSS feeds
        """
        script = '''"""
RSS Feed Reader for AI/ML Content Aggregation
Reads RSS feeds and extracts latest content
"""

import feedparser
from datetime import datetime, timedelta
import json

def fetch_feed(url, hours_back=24):
    """Fetch and parse RSS feed"""
    try:
        feed = feedparser.parse(url)
        cutoff_time = datetime.now() - timedelta(hours=hours_back)
        
        items = []
        for entry in feed.entries[:10]:  # Get last 10 items
            pub_date = None
            if hasattr(entry, 'published_parsed'):
                pub_date = datetime(*entry.published_parsed[:6])
            
            # Only include recent items
            if pub_date and pub_date > cutoff_time:
                items.append({
                    'title': entry.title,
                    'link': entry.link,
                    'summary': entry.get('summary', '')[:200],
                    'published': pub_date.isoformat()
                })
        
        return items
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return []

def aggregate_all_feeds(sources_json='sources.json', hours_back=24):
    """Aggregate content from all configured sources"""
    
    with open(sources_json, 'r') as f:
        sources = json.load(f)
    
    all_content = {}
    
    for source in sources:
        category = source['category']
        name = source['name']
        url = source['url']
        
        print(f"Fetching {name}...")
        items = fetch_feed(url, hours_back)
        
        if category not in all_content:
            all_content[category] = {}
        
        all_content[category][name] = items
    
    return all_content

if __name__ == "__main__":
    # Fetch last 24 hours of content
    content = aggregate_all_feeds(hours_back=24)
    
    # Save to file
    with open('aggregated_content.json', 'w', encoding='utf-8') as f:
        json.dump(content, f, indent=2)
    
    print(f"\\nAggregated content saved to aggregated_content.json")
    
    # Print summary
    total_items = sum(len(items) for cat in content.values() for items in cat.values())
    print(f"Total new items found: {total_items}")
'''
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(script)
        
        print(f"✅ RSS reader script created: {output_file}")
        return output_file


class ContentTypeGenerator:
    """
    Generate LinkedIn posts for different content types
    """
    
    def __init__(self):
        self.post_templates = self._load_templates()
    
    def _load_templates(self) -> Dict:
        """Load post templates for different content types"""
        return {
            "personal_learning": {
                "hook_options": [
                    "Just learned something mind-blowing about",
                    "Today's breakthrough:",
                    "Finally understood why",
                    "Deep dive into"
                ],
                "structure": "hook + insights + question + hashtags"
            },
            
            "news_update": {
                "hook_options": [
                    "Breaking in AI:",
                    "Major update:",
                    "Just dropped:",
                    "This changes everything:"
                ],
                "structure": "hook + summary + implications + link + hashtags"
            },
            
            "app_launch": {
                "hook_options": [
                    "New tool alert:",
                    "Just discovered:",
                    "Game-changer just launched:",
                    "Worth checking out:"
                ],
                "structure": "hook + features + use_cases + call_to_action + hashtags"
            },
            
            "research_paper": {
                "hook_options": [
                    "Fascinating new research:",
                    "Paper breakdown:",
                    "Latest from [Lab]:",
                    "This paper is wild:"
                ],
                "structure": "hook + key_findings + implications + link + hashtags"
            },
            
            "company_announcement": {
                "hook_options": [
                    "Big news from [Company]:",
                    "[Company] just announced:",
                    "Major development:",
                    "Industry shift:"
                ],
                "structure": "hook + announcement + analysis + implications + hashtags"
            },
            
            "tutorial_share": {
                "hook_options": [
                    "Here's how to",
                    "Quick tutorial:",
                    "Step-by-step:",
                    "Learn this in 5 minutes:"
                ],
                "structure": "hook + steps + example + resources + hashtags"
            }
        }
    
    def generate_news_post(self, title: str, summary: str, source: str, 
                          link: str, post_style: str = "informative") -> str:
        """
        Generate a LinkedIn post from news content
        
        Args:
            title: Article/video title
            summary: Brief summary
            source: Source name (e.g., "OpenAI Blog")
            link: URL to original content
            post_style: 'informative', 'excited', 'analytical'
        """
        
        if post_style == "excited":
            post = f"""🚀 Just saw this - {title}

{summary}

This is HUGE because:
→ [Your insight 1]
→ [Your insight 2]
→ [Your insight 3]

What are your thoughts on this development?

Source: {source}
Read more: {link}

#AI #MachineLearning #TechNews #Innovation"""

        elif post_style == "analytical":
            post = f"""📊 Analysis: {title}

Key points:
• {summary[:100]}...

My take:
This signals [your analysis]. The implications for AI/ML are significant because [your reasoning].

Worth watching: [what to watch next]

Full details: {link}

#ArtificialIntelligence #AITrends #TechAnalysis"""

        else:  # informative
            post = f"""📰 Update from {source}:

{title}

{summary}

Why this matters:
→ [Implication 1]
→ [Implication 2]

Link in comments 👇

#AI #MachineLearning #TechUpdate #{source.replace(' ', '')}"""
        
        return post
    
    def generate_app_launch_post(self, app_name: str, description: str, 
                                 features: List[str], link: str) -> str:
        """Generate post for new app/tool launch"""
        
        features_text = "\n".join([f"✓ {feature}" for feature in features[:4]])
        
        post = f"""🔥 New tool alert: {app_name}

{description}

Key features:
{features_text}

Perfect for: [your use case]

I'm particularly excited about [specific feature] because [reason].

Who's planning to try this?

Check it out: {link}

#AITools #MachineLearning #ProductLaunch #TechTools"""
        
        return post
    
    def generate_learning_news_mix(self, learning_content: str, 
                                   news_content: str) -> str:
        """
        Mix personal learning with news - shows you're both learning and informed
        """
        
        post = f"""🎯 Connecting the dots...

While studying {learning_content}, I came across this news:

{news_content}

Interesting timing! This real-world development validates exactly what I've been learning about. 

The practical implications are clear: [your insight]

Anyone else seeing this pattern?

#MachineLearning #AI #ContinuousLearning #TechNews"""
        
        return post


class ContentCalendar:
    """
    Manage content posting schedule
    """
    
    def __init__(self):
        self.schedule = []
    
    def create_weekly_mix(self, personal_learning_days: List[str] = None,
                         news_days: List[str] = None) -> Dict:
        """
        Create a balanced content calendar
        
        Default strategy:
        - 2x personal learning posts (Monday, Thursday)
        - 3x news/updates (Tuesday, Wednesday, Friday)
        - Weekend optional
        """
        
        if personal_learning_days is None:
            personal_learning_days = ["Monday", "Thursday"]
        
        if news_days is None:
            news_days = ["Tuesday", "Wednesday", "Friday"]
        
        calendar = {
            "Monday": {
                "type": "personal_learning",
                "time": "8:30 AM IST",
                "content_focus": "Weekend learning or project progress"
            },
            "Tuesday": {
                "type": "news_update",
                "time": "5:30 PM IST",
                "content_focus": "Major announcement or breakthrough"
            },
            "Wednesday": {
                "type": "app_launch / tool_review",
                "time": "9:00 AM IST",
                "content_focus": "New tools or interesting finds"
            },
            "Thursday": {
                "type": "personal_learning",
                "time": "8:30 AM IST",
                "content_focus": "Deep dive or concept breakdown"
            },
            "Friday": {
                "type": "news_roundup / trend_analysis",
                "time": "5:00 PM IST",
                "content_focus": "Week's highlights or trends"
            },
            "Saturday": {
                "type": "optional_reflection",
                "time": "10:00 AM IST",
                "content_focus": "Week recap or weekend project"
            },
            "Sunday": {
                "type": "rest / engage_only",
                "time": "N/A",
                "content_focus": "Comment on others' posts, no posting"
            }
        }
        
        return calendar
    
    def generate_daily_suggestions(self, day: str, 
                                   aggregated_content: Dict) -> List[str]:
        """
        Suggest content for today based on calendar and available content
        """
        
        calendar = self.create_weekly_mix()
        today_plan = calendar.get(day, {})
        content_type = today_plan.get("type", "news_update")
        
        suggestions = []
        
        if content_type == "news_update":
            suggestions.append("Pick top 1-2 news items from today's aggregated content")
            suggestions.append("Focus on high-impact developments")
            suggestions.append("Add your unique perspective")
        
        elif content_type == "personal_learning":
            suggestions.append("Share what you learned this week")
            suggestions.append("Use your study notes template")
            suggestions.append("Include practical examples")
        
        elif content_type == "app_launch / tool_review":
            suggestions.append("Check new tool launches from aggregated content")
            suggestions.append("Try the tool if possible and share experience")
            suggestions.append("Compare with existing solutions")
        
        return suggestions


class SearchHistoryIntegrator:
    """
    Connect with your search history from different AI platforms
    """
    
    def __init__(self):
        self.platforms = ["ChatGPT", "Gemini", "Perplexity", "Claude"]
    
    def create_search_log_template(self) -> str:
        """
        Template for manually logging your searches/conversations
        """
        
        template = f"""
=== AI Search/Chat Log ===
Date: {datetime.now().strftime('%Y-%m-%d')}

Platform Used: [ChatGPT / Gemini / Perplexity / Claude]

SEARCH TOPIC:


KEY INSIGHTS:
1. 
2. 
3. 

BREAKTHROUGH MOMENT:


INTERESTING FOLLOW-UP:


POST POTENTIAL: [Yes/No]
- If yes, what angle?

RELATED NEWS: [Any related news you saw?]

---
💡 TIP: Log this right after interesting conversations!
"""
        return template
    
    def suggest_post_from_search(self, search_topic: str, 
                                 insights: List[str]) -> str:
        """
        Generate post suggestion from your search activity
        """
        
        post = f"""💭 Down the rabbit hole of {search_topic}...

Used multiple AI assistants today (ChatGPT, Gemini, Claude) to understand this better. 

Here's what I learned:

{chr(10).join([f"→ {insight}" for insight in insights])}

The fascinating part? Each AI explained it differently, which actually helped me grasp the full picture.

What's your experience using multiple AI tools for learning?

#AI #MachineLearning #AITools #LearningInPublic"""
        
        return post


def create_complete_system():
    """
    Set up the complete content creation system
    """
    
    print("\n" + "="*70)
    print("AI/ML CONTENT CREATOR SYSTEM SETUP")
    print("="*70)
    
    # 1. Content Aggregator
    print("\n📡 STEP 1: Setting up content sources...")
    aggregator = ContentAggregator()
    
    # Save sources to JSON
    sources = aggregator.get_all_sources_list()
    with open('content_sources.json', 'w', encoding='utf-8') as f:
        json.dump(sources, f, indent=2)
    print(f"✅ Saved {len(sources)} content sources to content_sources.json")
    
    # Create RSS reader
    aggregator.create_rss_reader_script()
    
    # 2. Content Calendar
    print("\n📅 STEP 2: Creating content calendar...")
    calendar = ContentCalendar()
    weekly_plan = calendar.create_weekly_mix()
    
    with open('content_calendar.json', 'w', encoding='utf-8') as f:
        json.dump(weekly_plan, f, indent=2)
    print("✅ Content calendar created: content_calendar.json")
    
    print("\nYour Weekly Schedule:")
    for day, plan in weekly_plan.items():
        print(f"  {day:10} | {plan['type']:30} | {plan['time']}")
    
    # 3. Post Templates
    print("\n📝 STEP 3: Setting up post generators...")
    generator = ContentTypeGenerator()
    
    # Example posts
    examples = {
        "news": generator.generate_news_post(
            title="GPT-5 Training Begins",
            summary="OpenAI announces start of GPT-5 training with new architecture",
            source="OpenAI Blog",
            link="https://example.com",
            post_style="excited"
        ),
        
        "app_launch": generator.generate_app_launch_post(
            app_name="Claude Code",
            description="AI coding assistant that works in your terminal",
            features=[
                "Works with any codebase",
                "Integrated with Git",
                "Smart context management",
                "Terminal-native workflow"
            ],
            link="https://example.com"
        )
    }
    
    with open('example_posts.json', 'w', encoding='utf-8') as f:
        json.dump(examples, f, indent=2)
    print("✅ Example posts generated: example_posts.json")
    
    # 4. Search History Integration
    print("\n🔍 STEP 4: Search history integration...")
    search_integrator = SearchHistoryIntegrator()
    
    template = search_integrator.create_search_log_template()
    with open('daily_search_log_template.txt', 'w', encoding='utf-8') as f:
        f.write(template)
    print("✅ Search log template: daily_search_log_template.txt")
    
    # 5. Workflow Guide
    print("\n" + "="*70)
    print("YOUR DAILY WORKFLOW")
    print("="*70)
    
    workflow = """
MORNING ROUTINE (15 minutes):
1. Run RSS aggregator: python rss_reader.py
2. Review aggregated_content.json
3. Pick 2-3 interesting items
4. Check today's calendar (content_calendar.json)

LEARNING TIME (Throughout Day):
1. Study your AI/ML topics
2. Use ChatGPT/Gemini/Claude for questions
3. Fill out daily_search_log_template.txt
4. Note interesting searches for posts

EVENING ROUTINE (20 minutes):
1. Decide: Personal learning or News post?
2. Use appropriate generator
3. Customize the generated post
4. Schedule or post immediately
5. Engage with responses

WEEKLY REVIEW (Sunday):
1. Check what performed well
2. Adjust next week's calendar
3. Plan topics based on trends
4. Update sources if needed
    """
    
    print(workflow)
    
    # 6. Installation requirements
    print("\n" + "="*70)
    print("REQUIRED PYTHON PACKAGES")
    print("="*70)
    
    requirements = """
feedparser==6.0.10
requests==2.31.0
python-dateutil==2.8.2
    """
    
    with open('requirements.txt', 'w', encoding='utf-8') as f:
        f.write(requirements.strip())
    
    print("\nInstall with: pip install -r requirements.txt")
    
    print("\n✅ Complete system setup finished!")
    print("\n🎯 Next Steps:")
    print("   1. Install requirements: pip install -r requirements.txt")
    print("   2. Run aggregator: python rss_reader.py")
    print("   3. Check content_calendar.json for today's focus")
    print("   4. Start creating content!")


if __name__ == "__main__":
    create_complete_system()
