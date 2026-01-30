"""
AI/ML Job Hunter System
Cold Email Generator + Recruiter Finder + Application Tracker

This system helps you:
1. Find top AI/ML recruiters on LinkedIn
2. Generate personalized cold emails
3. Track applications and follow-ups
4. Position yourself perfectly for roles
"""

import json
from datetime import datetime, timedelta
from typing import List, Dict, Optional


class RecruiterFinder:
    """
    System to find and track AI/ML recruiters
    """
    
    def __init__(self):
        self.recruiter_profiles = []
        self.companies_hiring = self._load_top_companies()
    
    def _load_top_companies(self) -> Dict:
        """
        Top companies hiring for AI/ML roles in India and globally
        """
        return {
            "tier_1_global": [
                "Google", "Microsoft", "Amazon", "Meta", "Apple",
                "OpenAI", "Anthropic", "DeepMind", "NVIDIA"
            ],
            "tier_1_india": [
                "Flipkart", "Swiggy", "PhonePe", "Razorpay", "CRED",
                "Ola", "Paytm", "Zomato", "Dream11"
            ],
            "tier_2_ai_focused": [
                "Hugging Face", "Cohere", "Stability AI", "Midjourney",
                "Character.AI", "Perplexity", "Weights & Biases"
            ],
            "tier_2_india_consulting": [
                "Fractal Analytics", "LatentView", "Tiger Analytics",
                "Mu Sigma", "Artivatic", "Sigmoid"
            ],
            "startups_ai": [
                "Sarvam AI", "Krutrim", "Ola Krutrim", "Juspay",
                "Vernacular.ai", "Haptik", "Yellow.ai"
            ]
        }
    
    def get_linkedin_search_queries(self) -> List[str]:
        """
        Optimized LinkedIn search queries to find AI/ML recruiters
        """
        return [
            # By title
            '"AI Recruiter" OR "ML Recruiter" OR "Data Science Recruiter"',
            '"Technical Recruiter" "Machine Learning"',
            '"Talent Acquisition" "Artificial Intelligence"',
            
            # By company + role
            '"Google" "Technical Recruiter" "AI"',
            '"Microsoft" "Recruiter" "Machine Learning"',
            '"Amazon" "Talent Acquisition" "ML"',
            
            # India specific
            '"Bangalore" "AI Recruiter"',
            '"Pune" "Machine Learning Recruiter"',
            '"Hyderabad" "Data Science Recruiter"',
            
            # Hiring managers
            '"Hiring Manager" "Machine Learning"',
            '"Engineering Manager" "AI Team"',
            '"Head of AI" OR "VP of AI"'
        ]
    
    def create_recruiter_tracking_template(self) -> str:
        """
        Template to track recruiters you've contacted
        """
        template = """
=== RECRUITER TRACKING SHEET ===

Date: {date}

RECRUITER INFORMATION:
Name: 
Company: 
Title: 
LinkedIn URL: 
Email: (if found)
Location: 

OUTREACH DETAILS:
Connection Request Sent: [Date]
Connection Accepted: [Date]
First Email Sent: [Date]
Email Subject: 
Response Received: [Yes/No]
Response Date: 
Follow-up Dates: 

JOB DETAILS:
Role Applied For: 
Job Post URL: 
Application Date: 
Status: [Applied / In Review / Interview Scheduled / Rejected / Offer]

NOTES:
- Recruiter's interests/posts: 
- Common connections: 
- Best approach: 
- Follow-up strategy: 

NEXT STEPS:
[ ] Send connection request
[ ] Send personalized message
[ ] Send email
[ ] Follow up (1 week)
[ ] Follow up (2 weeks)
[ ] Apply to job
[ ] Thank you note

---
""".format(date=datetime.now().strftime("%Y-%m-%d"))
        
        return template


class ColdEmailGenerator:
    """
    Generate personalized cold emails for recruiters
    """
    
    def __init__(self):
        self.email_templates = self._load_templates()
    
    def _load_templates(self) -> Dict:
        """
        Different email templates for different scenarios
        """
        return {
            "connection_request_message": """
Hi {recruiter_name},

I noticed you recruit for {specialty} roles at {company}. I recently completed my AI/ML certification from GUVI and I'm actively sharing my learning journey on LinkedIn.

I'd love to connect and learn more about opportunities in this space!

Best regards,
{your_name}
            """,
            
            "cold_email_with_job_post": """
Subject: Application for {job_title} - {your_name}

Hi {recruiter_name},

I hope this email finds you well. I came across the {job_title} position at {company} and I'm excited about the opportunity to contribute to {specific_company_initiative}.

**Why I'm a great fit:**

• Recently completed AI/ML certification from GUVI with hands-on projects in {relevant_skills}
• Built {specific_project} that achieved {specific_result}
• Actively contributing to the AI/ML community through technical content on LinkedIn ({followers_count}+ followers)
• Strong foundation in {key_requirements_from_jd}

**What caught my attention:**
{specific_detail_from_job_post}

This aligns perfectly with my project experience in {your_relevant_experience}.

**My approach:**
I believe in learning by doing. My portfolio includes:
- {Project_1}: {brief_description}
- {Project_2}: {brief_description}
- {Project_3}: {brief_description}

I've attached my resume and would love to discuss how I can contribute to {team_name} at {company}.

Would you be available for a brief chat this week?

Best regards,
{your_name}
{phone_number}
{linkedin_profile}
{portfolio_link}
            """,
            
            "cold_email_no_specific_job": """
Subject: Exploring AI/ML Opportunities at {company}

Hi {recruiter_name},

I'm {your_name}, a freshly certified AI/ML professional from GUVI, and I'm reaching out to explore opportunities at {company}.

**Why {company}?**
{specific_reason_you_admire_company}

**What I bring:**
• Completed comprehensive AI/ML certification with focus on {specialization}
• Built production-ready models for {use_case}
• Growing presence in the AI/ML community (sharing insights with {followers_count}+ professionals on LinkedIn)

**My edge:**
While I'm early in my career, I combine technical skills with the ability to communicate complex concepts clearly - something I've honed by creating technical content.

I'm particularly interested in roles involving {specific_technology_or_domain}. Would love to connect and learn about current or upcoming opportunities in your team.

Best regards,
{your_name}
{contact_info}
            """,
            
            "follow_up_email_1_week": """
Subject: Following up - {job_title} Application

Hi {recruiter_name},

I wanted to follow up on my application for the {job_title} position I sent last week.

Since then, I've:
• {recent_achievement_or_learning}
• {relevant_content_you_posted}

I remain very interested in the role and would be happy to provide any additional information needed.

Looking forward to hearing from you!

Best regards,
{your_name}
            """,
            
            "follow_up_email_2_weeks": """
Subject: Still interested - {job_title} at {company}

Hi {recruiter_name},

I hope you're doing well! I'm following up on my application for the {job_title} position.

I understand you're likely reviewing many applications. I wanted to share that I recently:
{recent_relevant_achievement}

This experience has strengthened my conviction that I'd be a great addition to the {team_name} team.

Is there any update on the hiring timeline?

Best regards,
{your_name}
            """,
            
            "value_first_email": """
Subject: {insight_or_resource} for {company}'s {specific_project}

Hi {recruiter_name},

I recently came across {company}'s work on {specific_project} and wanted to share {something_valuable}:

{brief_insight_or_resource}

I'm {your_name}, an AI/ML professional actively working on similar challenges. I recently completed my certification from GUVI and have been building projects in {domain}.

If {company} is hiring for roles in this space, I'd love to explore how I can contribute!

Best regards,
{your_name}
            """
        }
    
    def generate_personalized_email(self, 
                                   template_type: str,
                                   job_details: Dict,
                                   your_profile: Dict) -> str:
        """
        Generate a fully personalized email
        
        Args:
            template_type: Type of email to generate
            job_details: Company, role, job description details
            your_profile: Your information, projects, achievements
        
        Returns:
            Personalized email ready to send
        """
        
        template = self.email_templates.get(template_type, "")
        
        # Merge and handle missing keys gracefully
        all_params = {**job_details, **your_profile}
        
        # Replace placeholders, keep {} for missing keys
        try:
            email = template.format(**all_params)
        except KeyError as e:
            # If key is missing, replace with placeholder
            import re
            email = template
            for match in re.findall(r'\{([^}]+)\}', template):
                if match not in all_params:
                    email = email.replace(f'{{{match}}}', f'[{match.replace("_", " ").title()}]')
        
        return email
    
    def analyze_job_description(self, job_description: str) -> Dict:
        """
        Extract key requirements from job description for personalization
        
        Args:
            job_description: Full text of job posting
        
        Returns:
            Dict with extracted key points
        """
        
        # Keywords to look for
        skills_keywords = [
            "Python", "TensorFlow", "PyTorch", "Keras", "Scikit-learn",
            "NLP", "Computer Vision", "Deep Learning", "ML Ops",
            "AWS", "GCP", "Azure", "Docker", "Kubernetes",
            "SQL", "NoSQL", "Spark", "Hadoop"
        ]
        
        requirements_keywords = [
            "Bachelor", "Master", "PhD", "years of experience",
            "certification", "portfolio", "projects"
        ]
        
        # Extract (simplified - in real implementation, use NLP)
        extracted = {
            "key_skills": [],
            "requirements": [],
            "nice_to_have": [],
            "company_values": []
        }
        
        # Simple keyword matching
        jd_lower = job_description.lower()
        
        for skill in skills_keywords:
            if skill.lower() in jd_lower:
                extracted["key_skills"].append(skill)
        
        return extracted
    
    def create_email_customization_guide(self) -> str:
        """
        Guide for customizing emails effectively
        """
        
        guide = """
=== EMAIL CUSTOMIZATION GUIDE ===

CRITICAL PERSONALIZATION POINTS:

1. SUBJECT LINE:
   ❌ Generic: "Application for ML Engineer role"
   ✅ Specific: "Application for ML Engineer - Built similar recommendation system"
   
2. OPENING:
   ❌ Generic: "I'm writing to apply for..."
   ✅ Specific: "I noticed your team recently launched [X]. As someone who built [similar Y]..."

3. WHY THIS COMPANY:
   Research and mention:
   - Recent product launch
   - Company blog post you read
   - Their AI/ML tech stack
   - Their mission/values
   
   ❌ "I admire your company"
   ✅ "Your recent work on [specific project] using [specific tech] aligns with my experience in..."

4. WHY YOU:
   Link your projects to their needs:
   ❌ "I built a chatbot"
   ✅ "I built a customer service chatbot that reduced response time by 60% - similar to the challenge mentioned in your job post"

5. CALL TO ACTION:
   ❌ "I look forward to hearing from you"
   ✅ "Would you have 15 minutes this week to discuss how I can contribute to [specific team/project]?"

6. PROOF POINTS:
   Always include:
   - Specific numbers (accuracy %, time saved, users impacted)
   - Technologies used
   - Link to live demo or GitHub
   - LinkedIn post with engagement metrics

RESEARCH CHECKLIST (5 minutes per company):
[ ] Company's latest AI/ML project
[ ] Recent LinkedIn posts from the company
[ ] Recruiter's recent posts/interests
[ ] Job posting specific requirements
[ ] Common connections
[ ] Company's tech blog posts
[ ] Recent news about the company

EMAIL SENDING STRATEGY:

BEST TIMES TO SEND (IST):
- Tuesday-Thursday: 9-11 AM (they check morning emails)
- Tuesday-Thursday: 2-4 PM (after lunch)
- Avoid: Monday (too busy), Friday (weekend mode), Weekends

SUBJECT LINE FORMULAS:
1. "Application for [Role] - [Your Unique Value]"
2. "[Specific Skill] Engineer with [X] Projects - Applying for [Role]"
3. "Re: [Job Post ID/Title] - [Your Name]"
4. "[Recruiter Name] - [Your Unique Hook] for [Role]"

FOLLOW-UP TIMELINE:
Day 0: Send initial email
Day 3: Connection request on LinkedIn (if not connected)
Day 7: First follow-up email
Day 14: Second follow-up email
Day 21: Final follow-up or move on

LENGTH:
- Connection message: 50-75 words
- Cold email: 150-250 words (recruiters are busy!)
- Follow-up: 75-100 words

TONE:
✅ Professional but conversational
✅ Enthusiastic but not desperate
✅ Confident but humble
✅ Direct but polite

AVOID:
❌ Spelling/grammar errors (use Grammarly)
❌ Generic templates that look copy-pasted
❌ Mentioning salary in first email
❌ Being too casual or too formal
❌ Long paragraphs (use bullet points)
❌ Attachments in cold emails (mention "resume available on request")

POWER WORDS TO USE:
• "Built" (not "worked on")
• "Achieved" (not "responsible for")
• "Contributed" (not "participated in")
• "Optimized" (not "improved")
• "Launched" (not "completed")
        """
        
        return guide


class JobApplicationTracker:
    """
    Track all your applications, interviews, and follow-ups
    """
    
    def __init__(self):
        self.applications = []
    
    def create_tracking_spreadsheet_template(self) -> Dict:
        """
        Template for tracking all applications
        """
        
        template = {
            "columns": [
                "Application Date",
                "Company",
                "Role Title",
                "Job Post URL",
                "Recruiter Name",
                "Recruiter LinkedIn",
                "Recruiter Email",
                "Application Method",  # LinkedIn / Email / Portal
                "Status",  # Applied / In Review / Interview / Offer / Rejected
                "Response Date",
                "Interview Date",
                "Follow-up Dates",
                "Notes",
                "Next Action",
                "Priority"  # High / Medium / Low
            ],
            
            "sample_entries": [
                {
                    "Application Date": "2026-01-28",
                    "Company": "Google",
                    "Role Title": "ML Engineer - Early Career",
                    "Job Post URL": "https://careers.google.com/...",
                    "Recruiter Name": "Jane Smith",
                    "Recruiter LinkedIn": "linkedin.com/in/janesmith",
                    "Recruiter Email": "jane@google.com",
                    "Application Method": "Email + LinkedIn",
                    "Status": "Applied",
                    "Response Date": "",
                    "Interview Date": "",
                    "Follow-up Dates": "2026-02-04 (1 week)",
                    "Notes": "Mentioned my NLP project. They use TensorFlow.",
                    "Next Action": "Follow up on Feb 4 if no response",
                    "Priority": "High"
                }
            ]
        }
        
        return template
    
    def calculate_follow_up_dates(self, application_date: str) -> List[str]:
        """
        Calculate when to follow up
        """
        base_date = datetime.strptime(application_date, "%Y-%m-%d")
        
        follow_ups = {
            "first_follow_up": base_date + timedelta(days=7),
            "second_follow_up": base_date + timedelta(days=14),
            "final_follow_up": base_date + timedelta(days=21)
        }
        
        return follow_ups


class YourProfileBuilder:
    """
    Build and maintain your professional profile for emails
    """
    
    def __init__(self):
        self.profile = self._create_profile_template()
    
    def _create_profile_template(self) -> Dict:
        """
        Template for your professional profile
        Fill this out once, use everywhere
        """
        
        return {
            "basic_info": {
                "your_name": "Your Full Name",
                "phone_number": "+91-XXXXXXXXXX",
                "email": "your.email@gmail.com",
                "linkedin_profile": "linkedin.com/in/yourprofile",
                "github_profile": "github.com/yourhandle",
                "location": "Pune, Maharashtra, India"
            },
            
            "elevator_pitch": {
                "short_version": "AI/ML Engineer | GUVI Certified | Building intelligent systems",
                
                "medium_version": """
                AI/ML professional with hands-on experience in [X, Y, Z]. 
                Recently completed comprehensive certification from GUVI. 
                Passionate about [specific area] and actively contributing 
                to the AI/ML community through technical content.
                """,
                
                "long_version": """
                AI/ML Engineer with practical experience in building end-to-end 
                machine learning solutions. Recently completed intensive AI/ML 
                certification from GUVI with focus on [specialization]. 
                
                Built [X] projects including [notable project] that [achieved Y]. 
                Strong foundation in Python, TensorFlow, and cloud deployment. 
                
                Actively sharing learnings with [X]+ professionals on LinkedIn 
                and looking to bring this combination of technical skills and 
                communication ability to a fast-paced AI team.
                """
            },
            
            "key_projects": [
                {
                    "name": "Project 1 Name",
                    "description": "One-line description",
                    "technologies": ["Python", "TensorFlow", "etc"],
                    "impact": "Achieved X% accuracy / Saved Y hours / etc",
                    "link": "github.com/yourproject"
                },
                # Add 2-3 more
            ],
            
            "technical_skills": {
                "programming": ["Python", "SQL", "etc"],
                "ml_frameworks": ["TensorFlow", "PyTorch", "Scikit-learn"],
                "tools": ["Git", "Docker", "Jupyter"],
                "cloud": ["AWS", "GCP", "Azure"],
                "specializations": ["NLP", "Computer Vision", "etc"]
            },
            
            "achievements": [
                "Completed GUVI AI/ML Certification",
                "Built [X] production-ready ML models",
                "Growing technical content following on LinkedIn ([X]+ followers)",
                # Add more
            ],
            
            "content_proof": {
                "linkedin_followers": "500+",
                "avg_post_engagement": "50+",
                "best_performing_post": "Link to post with 100+ engagements",
                "expertise_demonstrated": "Regularly share insights on [topics]"
            }
        }
    
    def generate_resume_bullet_points(self) -> List[str]:
        """
        Generate strong bullet points for your resume
        """
        
        bullets = [
            # GUVI Certification
            "Completed comprehensive AI/ML certification from GUVI covering neural networks, deep learning, NLP, and computer vision with 5+ hands-on projects",
            
            # Projects (customize with your actuals)
            "Built [Project Name] using [Technologies] that achieved [Metric]% accuracy in [Task]",
            
            "Developed end-to-end ML pipeline for [Use Case] resulting in [Impact/Result]",
            
            "Implemented [Algorithm/Model] for [Problem] using [Tech Stack], reducing [Metric] by X%",
            
            # Skills demonstration
            "Proficient in Python, TensorFlow, PyTorch with experience deploying models to [Cloud Platform]",
            
            # Soft skills
            "Growing technical content following on LinkedIn ([X]+ professionals) through clear communication of complex AI/ML concepts",
            
            # Learning mindset
            "Actively learning and implementing cutting-edge techniques from latest research papers and industry best practices"
        ]
        
        return bullets


def create_complete_job_hunting_system():
    """
    Set up the complete job hunting system
    """
    
    print("\n" + "="*70)
    print("AI/ML JOB HUNTING SYSTEM - COMPLETE SETUP")
    print("="*70)
    
    # 1. Recruiter Finder
    print("\n📱 STEP 1: Setting up recruiter finder...")
    finder = RecruiterFinder()
    
    # Save LinkedIn search queries
    queries = finder.get_linkedin_search_queries()
    with open('linkedin_recruiter_searches.txt', 'w', encoding='utf-8') as f:
        f.write("=== LINKEDIN SEARCH QUERIES FOR AI/ML RECRUITERS ===\n\n")
        f.write("Copy-paste these into LinkedIn search bar:\n\n")
        for i, query in enumerate(queries, 1):
            f.write(f"{i}. {query}\n\n")
    
    print("✅ LinkedIn search queries: linkedin_recruiter_searches.txt")
    
    # Save company list
    companies = finder.companies_hiring
    with open('target_companies.json', 'w', encoding='utf-8') as f:
        json.dump(companies, f, indent=2)
    
    print("✅ Target companies list: target_companies.json")
    
    # Save recruiter tracking template
    with open('recruiter_tracking_template.txt', 'w', encoding='utf-8') as f:
        f.write(finder.create_recruiter_tracking_template())
    
    print("✅ Recruiter tracking template: recruiter_tracking_template.txt")
    
    # 2. Email Generator
    print("\n📧 STEP 2: Setting up email generator...")
    email_gen = ColdEmailGenerator()
    
    # Save all email templates
    with open('email_templates.json', 'w', encoding='utf-8') as f:
        json.dump(email_gen.email_templates, f, indent=2)
    
    print("✅ Email templates: email_templates.json")
    
    # Save customization guide
    with open('email_customization_guide.txt', 'w', encoding='utf-8') as f:
        f.write(email_gen.create_email_customization_guide())
    
    print("✅ Email customization guide: email_customization_guide.txt")
    
    # 3. Application Tracker
    print("\n📊 STEP 3: Setting up application tracker...")
    tracker = JobApplicationTracker()
    
    tracking_template = tracker.create_tracking_spreadsheet_template()
    with open('application_tracker_template.json', 'w', encoding='utf-8') as f:
        json.dump(tracking_template, f, indent=2)
    
    print("✅ Application tracker template: application_tracker_template.json")
    
    # 4. Profile Builder
    print("\n👤 STEP 4: Setting up your profile builder...")
    profile = YourProfileBuilder()
    
    with open('your_profile_template.json', 'w', encoding='utf-8') as f:
        json.dump(profile.profile, f, indent=2)
    
    print("✅ Your profile template: your_profile_template.json")
    
    # Sample resume bullets
    with open('resume_bullet_points.txt', 'w', encoding='utf-8') as f:
        f.write("=== STRONG RESUME BULLET POINTS ===\n\n")
        bullets = profile.generate_resume_bullet_points()
        for bullet in bullets:
            f.write(f"• {bullet}\n\n")
    
    print("✅ Resume bullet points: resume_bullet_points.txt")
    
    # 5. Daily Workflow Guide
    print("\n" + "="*70)
    print("YOUR DAILY JOB HUNTING WORKFLOW")
    print("="*70)
    
    workflow = """
MORNING ROUTINE (30 minutes):
1. Check LinkedIn for new job posts (use saved searches)
2. Review application tracker
3. Send follow-up emails if needed
4. Update recruiter tracking sheet

RESEARCH TIME (1 hour):
For each interesting job:
1. Research company (5 min)
   - Recent news
   - AI/ML projects
   - Company blog
   - Tech stack

2. Find recruiter (10 min)
   - Use LinkedIn search queries
   - Check job post for contact
   - Look for hiring manager
   
3. Customize email (15 min)
   - Pull from templates
   - Personalize heavily
   - Add specific company details
   - Mention relevant project
   
4. Send & track (5 min)
   - Send email
   - Connection request
   - Update tracker
   - Set follow-up reminder

DAILY TARGET:
- Research: 3-5 companies
- Applications: 2-3 personalized emails
- Follow-ups: 2-3 from previous applications
- LinkedIn engagement: 30 min

WEEKLY TARGET:
- Applications sent: 10-15
- Follow-ups: 5-7
- Interview practices: 2-3 sessions
- LinkedIn posts: 2-3 (to show activity)

SUCCESS METRICS:
Week 1-2: 15-20 applications, 2-3 responses
Week 3-4: 20-25 applications, 5-7 responses, 1-2 interviews
Month 2: First offer negotiations
    """
    
    print(workflow)
    
    # 6. Sample Email Examples
    print("\n" + "="*70)
    print("SAMPLE EMAIL EXAMPLES")
    print("="*70)
    
    sample_profile = {
        "your_name": "Rahul Sharma",
        "recruiter_name": "Priya Patel",
        "company": "Swiggy",
        "job_title": "ML Engineer - Recommendation Systems",
        "relevant_skills": "recommendation engines, collaborative filtering",
        "specific_project": "food recommendation system",
        "specific_result": "improved click-through rate by 35%",
        "followers_count": "500",
        "phone_number": "+91-9876543210",
        "linkedin_profile": "linkedin.com/in/rahulsharma-ml",
        "portfolio_link": "github.com/rahulsharma",
        "specific_company_initiative": "your personalized food discovery engine",
        "specific_detail_from_job_post": "building scalable recommendation models for millions of users",
        "your_relevant_experience": "building a similar recommendation system for my capstone project",
        "key_requirements_from_jd": "Python, TensorFlow, and A/B testing",
        "Project_1": "Food Recommendation Engine",
        "Project_2": "Sentiment Analysis for Reviews",
        "Project_3": "Demand Forecasting Model",
        "team_name": "ML Platform",
        "specialty": "AI/ML",
        "recent_achievement_or_learning": "published a detailed post on collaborative filtering that got 100+ engagements",
        "relevant_content_you_posted": "analyzed Swiggy's personalization strategy in a LinkedIn post"
    }
    
    print("\nEXAMPLE 1: Cold Email with Job Post\n")
    example1 = email_gen.generate_personalized_email(
        "cold_email_with_job_post",
        sample_profile,
        sample_profile
    )
    print(example1)
    
    print("\n" + "-"*70)
    print("\nEXAMPLE 2: Connection Request Message\n")
    example2 = email_gen.generate_personalized_email(
        "connection_request_message",
        sample_profile,
        sample_profile
    )
    print(example2)
    
    print("\n✅ Complete job hunting system ready!")
    print("\n🎯 NEXT STEPS:")
    print("   1. Fill out your_profile_template.json with YOUR details")
    print("   2. Use linkedin_recruiter_searches.txt to find recruiters")
    print("   3. Customize email_templates.json for each application")
    print("   4. Track everything in application_tracker_template.json")
    print("   5. Send 2-3 personalized emails daily")
    print("   6. Follow up every 7 days")
    print("\n💼 TARGET: First interview within 2 weeks, offer within 6 weeks!")


if __name__ == "__main__":
    create_complete_job_hunting_system()
