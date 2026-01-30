"""
LinkedIn Post Generator
Transforms study notes into engaging LinkedIn posts about AI/ML learning
"""

import json
from datetime import datetime
from typing import List, Dict
import os

class LinkedInPostGenerator:
    def __init__(self):
        self.post_styles = {
            "story": "Share a learning journey with personal insights",
            "tips": "Present key takeaways as actionable tips",
            "breakdown": "Explain a complex concept simply",
            "achievement": "Celebrate a milestone or certification",
            "question": "Engage audience with a thought-provoking question"
        }
        
    def generate_post_variations(self, topic: str, key_points: List[str], 
                                 learning_context: str = "") -> Dict[str, str]:
        """
        Generate 3 different post variations from study notes
        
        Args:
            topic: Main subject (e.g., "Neural Networks", "Random Forest")
            key_points: List of 3-5 key learnings
            learning_context: Where you learned it (e.g., "GUVI AI/ML certification")
        """
        
        posts = {}
        
        # Style 1: Personal Learning Story
        posts["story"] = self._generate_story_post(topic, key_points, learning_context)
        
        # Style 2: Quick Tips Format
        posts["tips"] = self._generate_tips_post(topic, key_points)
        
        # Style 3: Concept Breakdown
        posts["breakdown"] = self._generate_breakdown_post(topic, key_points)
        
        return posts
    
    def _generate_story_post(self, topic: str, key_points: List[str], 
                            learning_context: str) -> str:
        """Generate a personal learning journey post"""
        
        context_line = f"while working through my {learning_context}" if learning_context else "in my AI/ML journey"
        
        post = f"""Just had a breakthrough moment with {topic} {context_line}! 🚀

Here's what clicked for me:

{self._format_points(key_points)}

The real 'aha!' moment was understanding how all these pieces connect. It's amazing how {topic.lower()} bridges theory and practical implementation.

What's been your biggest learning moment recently in AI/ML?

#MachineLearning #AI #DataScience #Learning #TechCareer"""
        
        return post
    
    def _generate_tips_post(self, topic: str, key_points: List[str]) -> str:
        """Generate a tips/takeaways format post"""
        
        post = f"""📚 Key insights from studying {topic}:

{self._format_points(key_points, numbered=True)}

These fundamentals are crucial for anyone diving into AI/ML. Save this for later reference!

What would you add to this list?

#ArtificialIntelligence #MachineLearning #DataScience #TechTips #AIMLCommunity"""
        
        return post
    
    def _generate_breakdown_post(self, topic: str, key_points: List[str]) -> str:
        """Generate a concept explanation post"""
        
        post = f"""🧠 Breaking down {topic} - simplified:

Think of it this way: {key_points[0] if key_points else 'complex concepts become simple with the right mental model'}

Key components:
{self._format_points(key_points[1:] if len(key_points) > 1 else key_points)}

The beauty of {topic} is how it transforms raw data into actionable insights. That's the power of modern AI/ML.

Questions? Drop them in the comments - happy to discuss!

#MachineLearning #AI #TechExplained #DataScience #LearningInPublic"""
        
        return post
    
    def _format_points(self, points: List[str], numbered: bool = False) -> str:
        """Format bullet points for LinkedIn"""
        formatted = []
        for i, point in enumerate(points, 1):
            if numbered:
                formatted.append(f"{i}. {point}")
            else:
                formatted.append(f"→ {point}")
        return "\n".join(formatted)
    
    def save_posts(self, posts: Dict[str, str], topic: str, output_dir: str = "generated_posts"):
        """Save generated posts to files"""
        os.makedirs(output_dir, exist_ok=True)
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{output_dir}/linkedin_posts_{topic.replace(' ', '_')}_{timestamp}.txt"
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(f"=== LinkedIn Posts for: {topic} ===\n")
            f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            
            for style, content in posts.items():
                f.write(f"\n{'='*60}\n")
                f.write(f"STYLE: {style.upper()}\n")
                f.write(f"{'='*60}\n\n")
                f.write(content)
                f.write(f"\n\n{'='*60}\n")
        
        print(f"✅ Posts saved to: {filename}")
        return filename
    
    def create_posting_schedule(self, topics: List[str], posts_per_week: int = 3) -> List[Dict]:
        """Create a content calendar"""
        schedule = []
        days = ["Monday", "Wednesday", "Friday", "Tuesday", "Thursday"]
        
        for i, topic in enumerate(topics):
            day_index = i % len(days)
            schedule.append({
                "topic": topic,
                "suggested_day": days[day_index],
                "suggested_time": "9:00 AM or 5:00 PM IST",
                "status": "pending"
            })
        
        return schedule[:posts_per_week]


def main():
    """Example usage"""
    generator = LinkedInPostGenerator()
    
    # Example 1: Post about Neural Networks
    print("\n" + "="*70)
    print("EXAMPLE 1: Neural Networks Learning")
    print("="*70)
    
    topic1 = "Neural Networks"
    key_points1 = [
        "Forward propagation flows data through layers to make predictions",
        "Backpropagation calculates gradients to update weights efficiently",
        "Activation functions introduce non-linearity - crucial for complex patterns",
        "Learning rate impacts convergence speed and model stability"
    ]
    
    posts1 = generator.generate_post_variations(
        topic=topic1,
        key_points=key_points1,
        learning_context="GUVI AI/ML certification"
    )
    
    # Display all variations
    for style, content in posts1.items():
        print(f"\n--- {style.upper()} STYLE ---\n")
        print(content)
        print("\n" + "-"*70)
    
    # Save to file
    saved_file = generator.save_posts(posts1, topic1)
    
    # Example 2: Quick demonstration with another topic
    print("\n\n" + "="*70)
    print("EXAMPLE 2: Random Forest")
    print("="*70)
    
    topic2 = "Random Forest"
    key_points2 = [
        "Ensemble of decision trees working together for better predictions",
        "Each tree votes, majority wins - wisdom of crowds in action",
        "Reduces overfitting compared to single decision trees",
        "Great for both classification and regression problems"
    ]
    
    posts2 = generator.generate_post_variations(
        topic=topic2,
        key_points=key_points2,
        learning_context="GUVI AI/ML certification"
    )
    
    print("\n--- STORY STYLE (Preview) ---\n")
    print(posts2["story"])
    
    # Create content schedule
    print("\n\n" + "="*70)
    print("CONTENT SCHEDULE SUGGESTION")
    print("="*70)
    
    topics = ["Neural Networks", "Random Forest", "Gradient Descent", "CNNs", "NLP Basics"]
    schedule = generator.create_posting_schedule(topics, posts_per_week=3)
    
    print("\nWeek 1 Schedule:")
    for item in schedule:
        print(f"  • {item['suggested_day']}: {item['topic']} ({item['suggested_time']})")
    
    print("\n💡 TIP: Best posting times on LinkedIn (IST):")
    print("   - Morning: 8-10 AM (professionals checking before work)")
    print("   - Evening: 5-6 PM (post-work engagement)")
    print("   - Avoid: Late nights and weekends")
    
    print("\n✅ All posts saved and ready for review!")


if __name__ == "__main__":
    main()
