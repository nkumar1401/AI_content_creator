"""
COMPLETE AI/ML CAREER LAUNCH SYSTEM - MASTER SETUP
Run this ONE script to set up everything

Author: AI/ML Career System
Version: 2.0
"""

import os
import json
import subprocess
import sys
from datetime import datetime


def print_header(text):
    """Print formatted header"""
    print("\n" + "="*70)
    print(f"  {text}")
    print("="*70)


def print_step(step_num, total_steps, description):
    """Print step progress"""
    print(f"\n[{step_num}/{total_steps}] {description}")


def check_python_version():
    """Ensure Python 3.7+"""
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 7):
        print("❌ ERROR: Python 3.7+ required")
        print(f"   Your version: {version.major}.{version.minor}")
        sys.exit(1)
    print(f"✅ Python {version.major}.{version.minor} detected")


def install_dependencies():
    """Install required packages"""
    print("📦 Installing dependencies...")
    
    packages = [
        'feedparser==6.0.10',
        'requests==2.31.0',
        'python-dateutil==2.8.2'
    ]
    
    try:
        for package in packages:
            print(f"   Installing {package}...")
            subprocess.check_call([
                sys.executable, '-m', 'pip', 'install', 
                package, '--quiet', '--break-system-packages'
            ], stderr=subprocess.DEVNULL)
        print("✅ All dependencies installed")
        return True
    except Exception as e:
        print(f"⚠️  Warning: Some packages may not have installed: {e}")
        print("   This is OK - the system will still work for most features")
        return False


def create_directory_structure():
    """Create necessary directories"""
    print("📁 Creating directory structure...")
    
    dirs = [
        'generated_posts',
        'logs',
        'drafts',
        'data'
    ]
    
    for directory in dirs:
        os.makedirs(directory, exist_ok=True)
        print(f"   ✅ {directory}/")
    
    print("✅ Directory structure created")


def create_configuration_files():
    """Create all configuration and data files"""
    print("⚙️  Creating configuration files...")
    
    # Content sources
    sources = {
        "youtube": {
            "Two Minute Papers": "https://www.youtube.com/feeds/videos.xml?channel_id=UCbfYPyITQ-7l4upoX8nvctg",
            "Yannic Kilcher": "https://www.youtube.com/feeds/videos.xml?channel_id=UCZHmQk67mSJgfCCTn7xBfew",
            "AI Explained": "https://www.youtube.com/feeds/videos.xml?channel_id=UCNJ1Ymd5yFuUPtn21xtRbbw",
            "Sentdex": "https://www.youtube.com/feeds/videos.xml?channel_id=UCfzlCWGWYyIQ0aLC5w48gBQ"
        },
        "reddit": {
            "r/MachineLearning": "https://www.reddit.com/r/MachineLearning/.rss",
            "r/artificial": "https://www.reddit.com/r/artificial/.rss",
            "r/LocalLLaMA": "https://www.reddit.com/r/LocalLLaMA/.rss"
        },
        "blogs": {
            "OpenAI Blog": "https://openai.com/blog/rss.xml",
            "Google AI Blog": "https://blog.research.google/feeds/posts/default",
            "Hugging Face": "https://huggingface.co/blog/feed.xml",
            "NVIDIA Blog": "https://blogs.nvidia.com/feed/"
        },
        "news": {
            "VentureBeat AI": "https://venturebeat.com/category/ai/feed/",
            "TechCrunch AI": "https://techcrunch.com/category/artificial-intelligence/feed/"
        }
    }
    
    with open('data/content_sources.json', 'w', encoding='utf-8') as f:
        json.dump(sources, f, indent=2)
    print("   ✅ content_sources.json")
    
    # Content calendar
    calendar = {
        "Monday": {
            "type": "personal_learning",
            "time": "8:30 AM IST",
            "focus": "Weekend learning or project progress"
        },
        "Tuesday": {
            "type": "news_update",
            "time": "5:30 PM IST",
            "focus": "Major announcement or breakthrough"
        },
        "Wednesday": {
            "type": "tool_review",
            "time": "9:00 AM IST",
            "focus": "New tools or interesting finds"
        },
        "Thursday": {
            "type": "personal_learning",
            "time": "8:30 AM IST",
            "focus": "Deep dive or concept breakdown"
        },
        "Friday": {
            "type": "news_roundup",
            "time": "5:00 PM IST",
            "focus": "Week's highlights or trends"
        },
        "Saturday": {
            "type": "optional",
            "time": "10:00 AM IST",
            "focus": "Optional reflection or project"
        },
        "Sunday": {
            "type": "rest",
            "time": "N/A",
            "focus": "Engage with others, no posting"
        }
    }
    
    with open('data/content_calendar.json', 'w', encoding='utf-8') as f:
        json.dump(calendar, f, indent=2)
    print("   ✅ content_calendar.json")
    
    # Target companies
    companies = {
        "tier_1_global": [
            "Google", "Microsoft", "Amazon", "Meta", "Apple",
            "OpenAI", "Anthropic", "NVIDIA"
        ],
        "tier_1_india": [
            "Flipkart", "Swiggy", "PhonePe", "Razorpay", "CRED",
            "Ola", "Paytm", "Zomato"
        ],
        "ai_startups": [
            "Hugging Face", "Cohere", "Stability AI",
            "Sarvam AI", "Krutrim", "Yellow.ai"
        ],
        "consulting_india": [
            "Fractal Analytics", "LatentView", "Tiger Analytics",
            "Mu Sigma"
        ]
    }
    
    with open('data/target_companies.json', 'w', encoding='utf-8') as f:
        json.dump(companies, f, indent=2)
    print("   ✅ target_companies.json")
    
    # Email templates
    email_templates = {
        "cold_email_with_job": """Subject: Application for {job_title} - {your_name}

Hi {recruiter_name},

I came across the {job_title} position at {company} and I'm excited about the opportunity.

Why I'm a great fit:
• Recently completed AI/ML certification from GUVI
• Built {project_name} that achieved {result}
• Strong foundation in {key_skills}

What caught my attention: {specific_detail}

I've attached my resume and would love to discuss how I can contribute to {team_name}.

Best regards,
{your_name}
{contact_info}""",
        
        "connection_request": """Hi {recruiter_name},

Noticed you recruit for AI/ML roles at {company}. I recently completed my AI/ML certification from GUVI and I'm actively sharing my journey on LinkedIn.

Would love to connect!

Best,
{your_name}""",
        
        "follow_up_1_week": """Subject: Following up - {job_title} Application

Hi {recruiter_name},

Following up on my application from last week.

Since then, I've {recent_achievement}.

Still very interested! Any update on the timeline?

Best,
{your_name}"""
    }
    
    with open('data/email_templates.json', 'w', encoding='utf-8') as f:
        json.dump(email_templates, f, indent=2)
    print("   ✅ email_templates.json")
    
    # Your profile template
    profile = {
        "basic_info": {
            "your_name": "YOUR_NAME_HERE",
            "phone": "+91-XXXXXXXXXX",
            "email": "your.email@gmail.com",
            "linkedin": "linkedin.com/in/yourprofile",
            "github": "github.com/yourhandle",
            "location": "Pune, Maharashtra, India"
        },
        "education": {
            "certification": "GUVI AI/ML Certification",
            "status": "Completed"
        },
        "key_projects": [
            {
                "name": "Project Name",
                "description": "What it does",
                "tech": ["Python", "TensorFlow"],
                "result": "Achieved X% accuracy",
                "link": "github.com/yourproject"
            }
        ],
        "skills": {
            "programming": ["Python", "SQL"],
            "ml_frameworks": ["TensorFlow", "Scikit-learn"],
            "tools": ["Git", "Jupyter"],
            "specializations": ["NLP", "Computer Vision"]
        }
    }
    
    with open('data/your_profile.json', 'w', encoding='utf-8') as f:
        json.dump(profile, f, indent=2)
    print("   ✅ your_profile.json")
    
    # Application tracker
    tracker = {
        "applications": [],
        "template": {
            "date": "YYYY-MM-DD",
            "company": "",
            "role": "",
            "recruiter": "",
            "status": "Applied",
            "next_action": ""
        }
    }
    
    with open('data/application_tracker.json', 'w', encoding='utf-8') as f:
        json.dump(tracker, f, indent=2)
    print("   ✅ application_tracker.json")
    
    print("✅ All configuration files created")


def create_text_templates():
    """Create text file templates"""
    print("📝 Creating text templates...")
    
    # LinkedIn recruiter searches
    searches = """=== LINKEDIN RECRUITER SEARCH QUERIES ===

Copy these into LinkedIn search bar:

1. "AI Recruiter" OR "ML Recruiter"
2. "Technical Recruiter" "Machine Learning" "Bangalore"
3. "Google" "Technical Recruiter" "AI"
4. "Microsoft" "Recruiter" "Machine Learning"
5. "Hiring Manager" "Machine Learning"
6. "AI Recruiter" "Pune"
7. "Data Science Recruiter" "India"

Use these to find recruiters, then send connection requests!
"""
    
    with open('linkedin_recruiter_searches.txt', 'w', encoding='utf-8') as f:
        f.write(searches)
    print("   ✅ linkedin_recruiter_searches.txt")
    
    # Study notes template
    notes = f"""=== STUDY NOTES TEMPLATE ===
Date: {datetime.now().strftime('%Y-%m-%d')}

TOPIC: [What you studied]

KEY LEARNINGS:
1. 
2. 
3. 

BREAKTHROUGH MOMENT:
[What finally clicked?]

PRACTICAL APPLICATION:
[How can this be used?]

POST POTENTIAL: [Yes/No]

NEXT STEPS:
[What to learn next?]
"""
    
    with open('study_notes_template.txt', 'w', encoding='utf-8') as f:
        f.write(notes)
    print("   ✅ study_notes_template.txt")
    
    # Daily search log
    search_log = f"""=== AI SEARCH/CHAT LOG ===
Date: {datetime.now().strftime('%Y-%m-%d')}

PLATFORM: [ChatGPT / Gemini / Claude / Perplexity]

TOPIC:


KEY INSIGHTS:
1. 
2. 
3. 

BREAKTHROUGH:


POST POTENTIAL: [Yes/No]
"""
    
    with open('daily_search_log_template.txt', 'w', encoding='utf-8') as f:
        f.write(search_log)
    print("   ✅ daily_search_log_template.txt")
    
    print("✅ All text templates created")


def create_quick_start_guide():
    """Create a quick start guide"""
    guide = """# QUICK START GUIDE

## Your System is Ready!

### Daily Workflow:

**Morning (7:00 AM):**
```bash
python run_daily.py
```
This fetches latest AI/ML news and tells you what to post today.

**Morning (8:30 AM):**
1. Open: content_creator_dashboard.html
2. Create post based on daily suggestions
3. Copy and post to LinkedIn manually
4. Engage with comments

**Evening (5:00 PM):**
1. Check: data/target_companies.json
2. Use: linkedin_recruiter_searches.txt to find recruiters
3. Customize: data/email_templates.json
4. Send: 2-3 personalized emails
5. Update: data/application_tracker.json

### Important Files:

**Must Fill Out:**
- `data/your_profile.json` - Add YOUR details!

**Use Daily:**
- `run_daily.py` - Your automation
- `content_creator_dashboard.html` - Create posts
- `data/application_tracker.json` - Track jobs

**Reference:**
- `linkedin_recruiter_searches.txt` - Find recruiters
- `data/email_templates.json` - Email templates
- `data/target_companies.json` - Where to apply

### Weekly Review:

```bash
python run_daily.py --review
```

### Need Help?

Read: COMPLETE_GUIDE.md

## Next Steps:

1. ✅ Fill out: data/your_profile.json
2. ✅ Run: python run_daily.py
3. ✅ Open: content_creator_dashboard.html
4. ✅ Create your first post!

**Let's build your AI/ML career!** 🚀
"""
    
    with open('QUICK_START.md', 'w', encoding='utf-8') as f:
        f.write(guide)
    print("   ✅ QUICK_START.md")


def setup_complete_message():
    """Display completion message"""
    print_header("🎉 SETUP COMPLETE!")
    
    print("""
Your AI/ML Career Launch System is ready!

📁 Directory Structure:
   ├── data/                      (All your data files)
   ├── generated_posts/           (Auto-generated posts)
   ├── logs/                      (Activity logs)
   ├── drafts/                    (Post drafts)
   ├── run_daily.py              (Daily automation)
   ├── content_creator_dashboard.html
   └── QUICK_START.md            (Read this next!)

🎯 Next Steps:

1. FILL YOUR PROFILE:
   nano data/your_profile.json
   (Add YOUR name, projects, skills, contact info)

2. RUN DAILY AUTOMATION:
   python run_daily.py
   (Fetches news, tells you what to post)

3. CREATE FIRST POST:
   open content_creator_dashboard.html
   (Generate your first LinkedIn post)

4. START JOB HUNTING:
   cat linkedin_recruiter_searches.txt
   (Find recruiters on LinkedIn)

📚 Full Documentation:
   - QUICK_START.md (Start here!)
   - COMPLETE_GUIDE.md (Complete strategy)

💡 Pro Tips:
   - Run 'python run_daily.py' every morning
   - Fill out data/your_profile.json TODAY
   - Post to LinkedIn manually (never auto-post!)
   - Track all applications in data/application_tracker.json

⏰ Set Up Automation:
   Windows: Task Scheduler → Run run_daily.py at 7 AM
   Mac/Linux: crontab -e → 0 7 * * * python3 run_daily.py

🎊 You're ready to launch your AI/ML career!

Questions? Check QUICK_START.md or COMPLETE_GUIDE.md

Good luck! 🚀
""")


def main():
    """Main setup function"""
    print_header("AI/ML CAREER LAUNCH SYSTEM - MASTER SETUP")
    print("\nThis will set up everything you need to:")
    print("  ✅ Create LinkedIn content automatically")
    print("  ✅ Find and email recruiters")
    print("  ✅ Track job applications")
    print("  ✅ Build your personal brand")
    print("\nStarting setup...\n")
    
    total_steps = 6
    
    # Step 1: Check Python
    print_step(1, total_steps, "Checking Python version")
    check_python_version()
    
    # Step 2: Install dependencies
    print_step(2, total_steps, "Installing dependencies")
    install_dependencies()
    
    # Step 3: Create directories
    print_step(3, total_steps, "Creating directory structure")
    create_directory_structure()
    
    # Step 4: Create config files
    print_step(4, total_steps, "Creating configuration files")
    create_configuration_files()
    
    # Step 5: Create templates
    print_step(5, total_steps, "Creating text templates")
    create_text_templates()
    
    # Step 6: Create guides
    print_step(6, total_steps, "Creating quick start guide")
    create_quick_start_guide()
    
    # Completion message
    setup_complete_message()


if __name__ == "__main__":
    main()