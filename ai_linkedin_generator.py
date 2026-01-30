"""
AI-Powered LinkedIn Post Generator
Uses Claude API to create highly personalized, natural posts from study notes
"""

import json
from datetime import datetime
from typing import List, Dict, Optional
import os


class AILinkedInPostGenerator:
    """
    Advanced post generator using AI for natural, personalized content
    
    Note: This version shows the structure. To actually use Claude API:
    - No API key needed when running in Claude environment
    - For standalone use, get API key from console.anthropic.com
    """
    
    def __init__(self, user_profile: Dict[str, str] = None):
        """
        Initialize with optional user profile for personalization
        
        Args:
            user_profile: Dict with keys like 'name', 'background', 'goal', 'tone'
        """
        self.user_profile = user_profile or {
            "background": "AI/ML learner completing certification",
            "goal": "Breaking into AI/ML career",
            "tone": "enthusiastic and educational"
        }
    
    def generate_ai_post(self, study_notes: str, style: str = "story") -> str:
        """
        Generate a LinkedIn post using AI based on your study notes
        
        Args:
            study_notes: Your raw notes or learnings (can be messy!)
            style: 'story', 'tips', 'breakdown', 'achievement', or 'question'
        
        Returns:
            Polished LinkedIn post ready to review and publish
        """
        
        prompt = self._create_prompt(study_notes, style)
        
        # This is a template - shows what would be sent to Claude API
        # In a real implementation, you'd call the API here
        
        post = self._generate_post_template(study_notes, style)
        return post
    
    def _create_prompt(self, study_notes: str, style: str) -> str:
        """Create the prompt for AI generation"""
        
        style_instructions = {
            "story": """
            Create a personal, engaging story about learning this topic.
            - Start with a hook about a breakthrough moment
            - Include 3-4 key insights in a natural flow
            - End with a question to engage audience
            - Keep it authentic and humble
            """,
            "tips": """
            Format as actionable takeaways:
            - Lead with value proposition
            - 3-5 numbered insights
            - Make each tip practical and clear
            - End with a call to save/share
            """,
            "breakdown": """
            Explain the concept simply:
            - Use an analogy or metaphor to start
            - Break down into digestible parts
            - Show practical application
            - Invite questions/discussion
            """,
            "achievement": """
            Celebrate the milestone professionally:
            - Mention the achievement (certification/project)
            - Share 2-3 biggest learnings
            - Express gratitude where appropriate
            - Look forward to next steps
            """,
            "question": """
            Pose a thought-provoking question:
            - Share brief context/insight
            - Ask specific, answerable question
            - Encourage diverse perspectives
            - Show genuine curiosity
            """
        }
        
        prompt = f"""You are helping create a LinkedIn post for someone with this background:
{json.dumps(self.user_profile, indent=2)}

Their study notes:
{study_notes}

Create a LinkedIn post in '{style}' style following these guidelines:
{style_instructions.get(style, style_instructions['story'])}

Requirements:
- 150-200 words (LinkedIn sweet spot)
- Professional but conversational tone
- Include 3-4 relevant hashtags at the end
- Use emojis sparingly (1-2 max)
- Make it authentic - avoid corporate jargon
- Focus on value for readers

Return only the post text, ready to copy-paste."""
        
        return prompt
    
    def _generate_post_template(self, study_notes: str, style: str) -> str:
        """
        Generate template post (simulated - replace with actual AI call)
        This shows the structure while you integrate real AI
        """
        
        # Extract topic from notes (simple approach)
        topic = study_notes.split('\n')[0][:50] if study_notes else "AI/ML concepts"
        
        templates = {
            "story": f"""🎯 Just had a breakthrough with {topic}!

While working through my GUVI AI/ML certification, something finally clicked. 

Here's what I learned:
→ [Key insight 1 from your notes]
→ [Key insight 2 from your notes]
→ [Key insight 3 from your notes]

The real game-changer was seeing how theory translates to real-world problems. That's when everything made sense.

For anyone else on this learning journey - what's been your biggest "aha" moment?

#MachineLearning #AI #LearningInPublic #TechCareer""",
            
            "tips": f"""💡 5 things I wish I knew earlier about {topic}:

1. [First key learning]
2. [Second key learning]
3. [Third key learning]
4. [Fourth key learning]
5. [Fifth key learning]

These fundamentals are game-changers. Bookmark this if you're learning AI/ML!

What would you add to this list?

#AI #MachineLearning #DataScience #TechTips""",
            
            "achievement": f"""🎓 Excited to share: Just completed my AI/ML certification from GUVI!

The journey taught me way more than I expected:

→ {topic} isn't just theory - it's solving real problems
→ Hands-on projects beat passive learning every time
→ The AI/ML community is incredibly supportive

Now actively looking for opportunities to apply these skills in a professional setting. If your team needs someone passionate about AI/ML with fresh perspectives, let's connect!

#AIMLCertification #CareerTransition #MachineLearning #OpenToWork"""
        }
        
        return templates.get(style, templates["story"])
    
    def create_from_notes(self, notes_file: str, output_dir: str = "generated_posts") -> List[str]:
        """
        Read study notes from file and generate multiple post options
        
        Args:
            notes_file: Path to your notes (txt, md, etc.)
            output_dir: Where to save generated posts
        
        Returns:
            List of generated post filenames
        """
        
        # Read notes
        with open(notes_file, 'r', encoding='utf-8') as f:
            notes = f.read()
        
        # Generate posts in different styles
        styles = ["story", "tips", "breakdown"]
        generated_files = []
        
        os.makedirs(output_dir, exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        for style in styles:
            post = self.generate_ai_post(notes, style)
            
            filename = f"{output_dir}/linkedin_{style}_{timestamp}.txt"
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(f"=== LinkedIn Post - {style.upper()} Style ===\n")
                f.write(f"Generated: {datetime.now()}\n")
                f.write(f"{'='*60}\n\n")
                f.write(post)
                f.write("\n\n" + "="*60)
                f.write("\n\n📝 REVIEW CHECKLIST:")
                f.write("\n[ ] Does it sound like me?")
                f.write("\n[ ] Is it valuable to readers?")
                f.write("\n[ ] Are hashtags relevant?")
                f.write("\n[ ] Proofread for typos?")
                f.write("\n[ ] Ready to engage with comments?")
            
            generated_files.append(filename)
            print(f"✅ Generated {style} post: {filename}")
        
        return generated_files
    
    def analyze_post_quality(self, post_text: str) -> Dict[str, any]:
        """
        Analyze a post and provide improvement suggestions
        
        Returns dict with:
        - word_count
        - has_question
        - hashtag_count
        - engagement_score (estimated)
        - suggestions
        """
        
        words = len(post_text.split())
        has_question = '?' in post_text
        hashtags = post_text.count('#')
        
        suggestions = []
        
        if words < 100:
            suggestions.append("Consider adding more context - posts 150-200 words perform best")
        elif words > 300:
            suggestions.append("Might be too long - consider breaking into two posts")
        
        if not has_question:
            suggestions.append("Add a question at the end to boost engagement")
        
        if hashtags < 3:
            suggestions.append("Add 3-5 relevant hashtags for better discoverability")
        elif hashtags > 7:
            suggestions.append("Too many hashtags can look spammy - stick to 3-5")
        
        if '!' in post_text[:50]:
            suggestions.append("Great hook! Exclamation in first line grabs attention")
        
        # Simple engagement score (0-100)
        score = 50  # baseline
        score += 10 if 150 <= words <= 200 else -10
        score += 15 if has_question else 0
        score += 10 if 3 <= hashtags <= 5 else -5
        score += 10 if any(emoji in post_text for emoji in ['🎯', '💡', '🚀', '✨']) else 0
        
        return {
            "word_count": words,
            "has_question": has_question,
            "hashtag_count": hashtags,
            "engagement_score": max(0, min(100, score)),
            "suggestions": suggestions
        }


def create_study_notes_template():
    """Create a template for capturing study notes effectively"""
    
    template = """
=== Study Notes Template for LinkedIn Posts ===

TOPIC: [What you studied today]

DATE: [When you learned this]

KEY LEARNINGS (3-5 points):
1. 
2. 
3. 
4. 
5. 

BREAKTHROUGH MOMENT:
[What finally clicked? What was confusing before?]

PRACTICAL APPLICATION:
[How can this be used in real projects?]

QUESTIONS REMAINING:
[What are you still curious about?]

RESOURCES USED:
- 
- 

NEXT STEPS:
[What will you learn next related to this?]

---
💡 TIP: Be honest about what was hard. Vulnerability makes great LinkedIn content!
"""
    
    with open('/home/claude/study_notes_template.txt', 'w', encoding='utf-8') as f:
        f.write(template)
    
    print("✅ Study notes template created: study_notes_template.txt")
    return template


def demo_workflow():
    """Demonstrate the complete workflow"""
    
    print("\n" + "="*70)
    print("LINKEDIN POST GENERATOR - COMPLETE WORKFLOW")
    print("="*70)
    
    # Step 1: Create template
    print("\n📝 STEP 1: Creating study notes template...")
    create_study_notes_template()
    
    # Step 2: Example notes
    print("\n📝 STEP 2: Example study notes...")
    example_notes = """
TOPIC: Convolutional Neural Networks (CNNs)

KEY LEARNINGS:
1. CNNs automatically learn spatial hierarchies - no manual feature engineering
2. Convolution layers detect patterns (edges, textures, objects)
3. Pooling reduces dimensions while preserving important features
4. Transfer learning with pre-trained models saves massive training time

BREAKTHROUGH MOMENT:
Finally understood why CNNs work better than regular neural nets for images - 
it's about preserving spatial relationships! Regular NNs flatten images and 
lose this crucial information.

PRACTICAL APPLICATION:
Used VGG16 for image classification project - achieved 94% accuracy on 
custom dataset with just 1000 images thanks to transfer learning.
"""
    
    # Save example notes
    with open('/home/claude/example_notes.txt', 'w', encoding='utf-8') as f:
        f.write(example_notes)
    
    print("Example notes saved to: example_notes.txt")
    
    # Step 3: Generate posts
    print("\n🤖 STEP 3: Generating LinkedIn posts...")
    
    generator = AILinkedInPostGenerator(user_profile={
        "background": "Completed GUVI AI/ML certification",
        "goal": "Starting career in AI/ML",
        "tone": "enthusiastic learner, humble, technical but accessible"
    })
    
    generated_files = generator.create_from_notes('/home/claude/example_notes.txt')
    
    # Step 4: Analyze quality
    print("\n📊 STEP 4: Quality analysis...")
    
    with open(generated_files[0], 'r') as f:
        content = f.read()
        # Extract just the post part
        post_text = content.split('='*60)[2].strip()
    
    analysis = generator.analyze_post_quality(post_text)
    
    print(f"\nPost Quality Analysis:")
    print(f"  • Word count: {analysis['word_count']}")
    print(f"  • Has question: {'✅' if analysis['has_question'] else '❌'}")
    print(f"  • Hashtags: {analysis['hashtag_count']}")
    print(f"  • Engagement score: {analysis['engagement_score']}/100")
    
    if analysis['suggestions']:
        print(f"\n  Suggestions:")
        for suggestion in analysis['suggestions']:
            print(f"    - {suggestion}")
    
    # Step 5: Best practices
    print("\n" + "="*70)
    print("📱 BEST PRACTICES FOR POSTING")
    print("="*70)
    print("""
1. TIMING (IST):
   - Best: Tuesday-Thursday, 8-10 AM or 5-6 PM
   - Good: Monday, Wednesday morning
   - Avoid: Weekends, late nights

2. ENGAGEMENT:
   - Reply to ALL comments within first hour
   - Ask ONE clear question per post
   - Tag relevant people/companies (sparingly)

3. CONSISTENCY:
   - Post 2-3 times per week
   - Same days/times builds habit
   - Quality > Quantity always

4. AUTHENTICITY:
   - Share struggles, not just wins
   - Use your voice, not corporate speak
   - Be helpful, not promotional

5. REVIEW BEFORE POSTING:
   ✓ Read aloud - does it sound like you?
   ✓ Value check - would YOU engage with this?
   ✓ Proofread - typos hurt credibility
   ✓ Mobile preview - most people read on phone
    """)
    
    print("\n✅ All posts ready in 'generated_posts/' folder!")
    print("🎯 Next: Review, personalize, and schedule your posts!")


if __name__ == "__main__":
    demo_workflow()
