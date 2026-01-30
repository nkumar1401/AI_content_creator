#!/usr/bin/env python3
"""
AI/ML Career Launch System - Daily Runner
Run this script every morning to prepare your content and job hunting tasks

Usage:
    python run_daily.py          # Daily content prep
    python run_daily.py --review # Weekly review
"""

import json
import os
import sys
from datetime import datetime
import argparse


def load_json(filepath, default=None):
    """Load JSON file safely"""
    try:
        with open(filepath, 'r') as f:
            return json.load(f)
    except:
        return default or {}


def print_header(text, char="="):
    """Print formatted header"""
    print(f"\n{char * 70}")
    print(f"  {text}")
    print(f"{char * 70}")


def fetch_rss_feeds():
    """Fetch latest RSS feeds"""
    print("\n📡 Fetching latest AI/ML news...")
    
    try:
        # Try to import feedparser
        import feedparser
        from datetime import timedelta
        
        sources = load_json('data/content_sources.json', {})
        all_content = {}
        count = 0
        
        for category, feeds in sources.items():
            all_content[category] = {}
            for name, url in list(feeds.items())[:2]:  # Limit to 2 per category for speed
                try:
                    print(f"   Fetching {name}...", end=" ")
                    feed = feedparser.parse(url)
                    
                    items = []
                    for entry in feed.entries[:3]:  # Get top 3 items
                        items.append({
                            'title': entry.get('title', 'No title'),
                            'link': entry.get('link', ''),
                            'summary': entry.get('summary', '')[:150]
                        })
                    
                    all_content[category][name] = items
                    count += len(items)
                    print("✅")
                except Exception as e:
                    print(f"⚠️ ({str(e)[:30]})")
                    all_content[category][name] = []
        
        # Save aggregated content
        with open('data/aggregated_content.json', 'w', encoding='utf-8') as f:
            json.dump(all_content, f, indent=2)
        
        print(f"✅ Fetched {count} news items")
        return all_content
        
    except ImportError:
        print("⚠️  feedparser not installed")
        print("   Run: pip install feedparser --break-system-packages")
        print("   For now, using cached content...")
        return load_json('data/aggregated_content.json', {})


def check_content_calendar():
    """Check today's content plan"""
    today = datetime.now()
    day_name = today.strftime("%A")
    
    calendar = load_json('data/content_calendar.json', {})
    today_plan = calendar.get(day_name, {})
    
    print_header(f"📅 TODAY'S PLAN - {day_name}, {today.strftime('%B %d, %Y')}")
    
    content_type = today_plan.get('type', 'flexible')
    focus = today_plan.get('focus', 'Your choice')
    time = today_plan.get('time', 'Flexible')
    
    print(f"\n📝 Content Type: {content_type}")
    print(f"🎯 Focus: {focus}")
    print(f"⏰ Best Time: {time}")
    
    # Give specific instructions
    print("\n💡 What to do:")
    
    if 'learning' in content_type.lower():
        print("""
   1. Think about what you learned recently
   2. Open: content_creator_dashboard.html
   3. Choose: "Personal Learning" tab
   4. Fill in: Topic + 3-5 key insights
   5. Generate, customize, post!
        """)
    elif 'news' in content_type.lower():
        print("""
   1. Check: data/aggregated_content.json (see below)
   2. Pick: Most interesting news item
   3. Open: content_creator_dashboard.html
   4. Choose: "News Update" tab
   5. Add YOUR perspective (critical!)
        """)
    elif 'tool' in content_type.lower():
        print("""
   1. Think of a tool you've used recently
   2. Open: content_creator_dashboard.html
   3. Choose: "App Launch" tab
   4. Share honest review with examples
        """)
    elif 'rest' in content_type.lower():
        print("""
   📌 NO POSTING TODAY!
   
   Instead:
   - Comment on 10+ others' posts
   - Respond to your comments
   - Build relationships
   - Rest and recharge
        """)
    else:
        print("""
   Flexible day! Choose based on:
   - What you learned this week
   - Interesting news (check aggregated_content.json)
   - Tools you've tried
        """)
    
    return today_plan


def show_top_news():
    """Display top news items"""
    print_header("🔥 TOP NEWS ITEMS")
    
    content = load_json('data/aggregated_content.json', {})
    
    if not content:
        print("\n⚠️  No news items yet. Run 'python setup.py' first!")
        return
    
    count = 0
    for category, sources in content.items():
        if count >= 5:
            break
        for source, items in sources.items():
            if count >= 5:
                break
            for item in items[:1]:  # One per source
                print(f"\n📰 {source}:")
                print(f"   {item.get('title', 'No title')}")
                print(f"   🔗 {item.get('link', 'No link')[:60]}...")
                count += 1
                if count >= 5:
                    break
    
    if count == 0:
        print("\n⚠️  No news items found. RSS feeds may be unavailable.")
        print("   You can still create posts from your own learning!")


def show_job_hunting_tasks():
    """Show job hunting tasks"""
    print_header("💼 TODAY'S JOB HUNTING TASKS")
    
    print("""
MORNING (30 min):
  [ ] Check data/application_tracker.json
  [ ] Send follow-up emails (Day 7/14/21)
  [ ] Find 3 new job postings

EVENING (60 min):
  [ ] Research 2-3 companies
      → Check data/target_companies.json
  
  [ ] Find recruiters
      → Use linkedin_recruiter_searches.txt
      → Connect with 3-5 recruiters
  
  [ ] Send 2-3 personalized emails
      → Use data/email_templates.json
      → Customize with data/your_profile.json
  
  [ ] Apply to 2-3 jobs on LinkedIn/Naukri
  
  [ ] Update data/application_tracker.json

📊 WEEKLY TARGET:
   - 10-15 applications sent
   - 5-7 recruiter connections
   - 2-3 follow-ups sent
    """)


def show_posting_checklist():
    """Show pre-posting checklist"""
    print_header("✅ POSTING CHECKLIST")
    
    print("""
BEFORE YOU POST:
  [ ] Content is ready (generated & customized)
  [ ] Added YOUR unique perspective
  [ ] Checked for typos and grammar
  [ ] Added relevant hashtags (3-5)
  [ ] Included a question (boosts engagement)
  [ ] Links are working (if any)

OPTIMAL POSTING TIMES (IST):
  ⭐ Best: 8:00-10:00 AM (weekdays)
  ⭐ Best: 5:00-6:00 PM (weekdays)
  ⚠️  Avoid: Before 7 AM, after 10 PM, weekends

AFTER YOU POST:
  [ ] Reply to EVERY comment within first hour (crucial!)
  [ ] Like and respond thoughtfully
  [ ] Engage with others' posts too
  [ ] Save post analytics for review

⚠️  CRITICAL: Post MANUALLY to LinkedIn!
    Never use auto-posting tools (risks account ban)
    """)


def log_activity():
    """Log today's activity"""
    today = datetime.now()
    
    log_entry = {
        "date": today.strftime("%Y-%m-%d"),
        "day": today.strftime("%A"),
        "status": "prep_completed",
        "timestamp": today.isoformat()
    }
    
    # Load existing logs
    try:
        with open('logs/activity_log.json', 'r') as f:
            logs = json.load(f)
    except:
        logs = []
    
    logs.append(log_entry)
    
    # Save logs
    os.makedirs('logs', exist_ok=True)
    with open('logs/activity_log.json', 'w', encoding='utf-8') as f:
        json.dump(logs, f, indent=2)


def weekly_review():
    """Show weekly review"""
    print_header("📊 WEEKLY REVIEW")
    
    try:
        with open('logs/activity_log.json', 'r') as f:
            logs = json.load(f)
        
        # Get last 7 days
        recent = logs[-7:] if len(logs) >= 7 else logs
        
        print(f"\n📈 Activity Summary:")
        print(f"   Days active: {len(recent)}")
        
        # Check content tracker
        tracker = load_json('data/application_tracker.json', {})
        apps = tracker.get('applications', [])
        
        print(f"   Job applications: {len(apps)}")
        
        # Status breakdown
        if apps:
            statuses = {}
            for app in apps:
                status = app.get('status', 'Unknown')
                statuses[status] = statuses.get(status, 0) + 1
            
            print(f"\n📋 Application Status:")
            for status, count in statuses.items():
                print(f"   {status}: {count}")
        
        print(f"\n💡 INSIGHTS:")
        print(f"   - Are you posting 2-3x per week?")
        print(f"   - Are you sending 10-15 applications?")
        print(f"   - Are you following up consistently?")
        
        print(f"\n🎯 NEXT WEEK GOALS:")
        print(f"   [ ] Plan 3 content topics")
        print(f"   [ ] Target 5 new companies")
        print(f"   [ ] Follow up on pending applications")
        
    except:
        print("\n⚠️  No activity logs yet. Keep using the system!")


def main():
    """Main function"""
    parser = argparse.ArgumentParser(description='AI/ML Career Daily Runner')
    parser.add_argument('--review', action='store_true', help='Show weekly review')
    args = parser.parse_args()
    
    if args.review:
        weekly_review()
        return
    
    # Daily workflow
    print_header("🚀 AI/ML CAREER LAUNCH SYSTEM")
    print(f"Good morning! Let's prepare today's content and tasks.")
    
    # Fetch RSS feeds
    fetch_rss_feeds()
    
    # Check calendar
    check_content_calendar()
    
    # Show top news
    show_top_news()
    
    # Job hunting tasks
    show_job_hunting_tasks()
    
    # Posting checklist
    show_posting_checklist()
    
    # Log activity
    log_activity()
    
    # Final message
    print_header("✅ DAILY PREP COMPLETE!")
    print("""
🎯 YOUR ACTION ITEMS:

1. Open: content_creator_dashboard.html
2. Create today's post (10 min)
3. Post to LinkedIn manually
4. Evening: Send 2-3 job applications

📝 Need help?
   - QUICK_START.md (quick reference)
   - COMPLETE_GUIDE.md (full strategy)

💪 You've got this! Build your AI/ML career today!
    """)


if __name__ == "__main__":
    main()
