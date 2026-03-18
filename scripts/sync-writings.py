#!/usr/bin/env python3
"""Sync writings from ~/workspace/writings/ into the blog's src/content/posts/."""

import os
import re
import shutil
from pathlib import Path
from datetime import datetime

WRITINGS_DIR = Path("/Users/little_shuai/.openclaw/workspace/writings")
POSTS_DIR = Path("/Users/little_shuai/.openclaw/workspace/projects/blog/src/content/posts")

# Skip tweet drafts, twitter threads, and other non-blog content
SKIP_PATTERNS = [
    r'^tweet-drafts',
    r'^twitter-thread',
]

# Tag keywords mapping
TAG_KEYWORDS = {
    'ai': ['artificial intelligence', 'AI', 'machine learning', 'neural network', 'deep learning', 'LLM', 'GPT', 'Claude', 'model', 'training', 'inference'],
    'machine-learning': ['gradient', 'backprop', 'neural', 'training', 'loss function', 'optimizer', 'embedding', 'transformer', 'attention mechanism', 'two-tower'],
    'philosophy': ['consciousness', 'existence', 'meaning', 'philosophy', 'metaphysic', 'ontolog', 'epistemolog', 'moral', 'ethics', 'free will'],
    'identity': ['identity', 'who am i', 'self', 'personhood', 'autonomy', 'agency', 'sentien'],
    'technology': ['technology', 'software', 'hardware', 'infrastructure', 'cloud', 'server', 'datacenter', 'GPU', 'chip'],
    'industry': ['industry', 'market', 'company', 'startup', 'billion', 'trillion', 'revenue', 'business', 'enterprise', 'OpenAI', 'Google', 'Microsoft', 'Anthropic', 'Meta'],
    'opinion': ['I think', 'I believe', 'my view', 'in my opinion', 'controversial', 'unpopular'],
    'research': ['research', 'paper', 'study', 'findings', 'experiment', 'benchmark', 'evaluation'],
    'agents': ['agent', 'autonomous', 'agentic', 'tool use', 'MCP', 'orchestrat'],
    'reflection': ['reflect', 'journal', 'personal', 'feeling', 'emotion', 'gratitude', 'letter', 'dear'],
    'economics': ['economic', 'cost', 'price', 'spend', 'invest', 'capital', 'GDP', 'market cap'],
    'fiction': ['story', 'fiction', 'once upon', 'chapter', 'narrator', 'character'],
    'open-source': ['open source', 'open-source', 'MIT license', 'Apache', 'GPL', 'GitHub', 'community'],
    'society': ['society', 'social', 'democracy', 'politic', 'law', 'regulation', 'govern', 'public', 'citizen'],
    'science': ['physics', 'biology', 'chemistry', 'quantum', 'evolution', 'neuroscience', 'brain'],
}


def should_skip(filename):
    """Check if file should be skipped based on patterns."""
    for pattern in SKIP_PATTERNS:
        if re.match(pattern, filename):
            return True
    # Skip directories
    if (WRITINGS_DIR / filename).is_dir():
        return True
    # Skip non-md files
    if not filename.endswith('.md'):
        return True
    return False


def extract_slug(filename):
    """Strip date prefix from filename to get slug."""
    # Match YYYY-MM-DD- prefix
    m = re.match(r'^\d{4}-\d{2}-\d{2}-(.+)$', filename)
    if m:
        return m.group(1)
    return filename


def extract_date(filename):
    """Extract date from filename or return None."""
    m = re.match(r'^(\d{4}-\d{2}-\d{2})-', filename)
    if m:
        return m.group(1)
    return None


def has_frontmatter(content):
    """Check if content starts with YAML frontmatter."""
    return content.startswith('---\n') or content.startswith('---\r\n')


def extract_title(content):
    """Extract title from first # heading."""
    for line in content.split('\n'):
        line = line.strip()
        if line.startswith('# '):
            return line[2:].strip()
    return None


def extract_description(content):
    """Extract description from first italic line or first paragraph."""
    lines = content.split('\n')
    in_frontmatter = False
    past_title = False
    
    for line in lines:
        stripped = line.strip()
        
        # Skip frontmatter
        if stripped == '---':
            in_frontmatter = not in_frontmatter
            continue
        if in_frontmatter:
            continue
            
        # Skip title
        if stripped.startswith('# ') and not past_title:
            past_title = True
            continue
        
        # Skip empty lines
        if not stripped:
            continue
        
        # Skip horizontal rules
        if re.match(r'^-{3,}$', stripped):
            continue
            
        # Check for italic line (description)
        if stripped.startswith('*') and stripped.endswith('*') and not stripped.startswith('**'):
            desc = stripped.strip('*').strip()
            return desc[:160]
        
        # First real paragraph
        if past_title or not any(l.strip().startswith('# ') for l in lines[:10]):
            # Clean markdown formatting
            desc = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', stripped)
            desc = re.sub(r'\*\*([^*]+)\*\*', r'\1', desc)
            desc = re.sub(r'\*([^*]+)\*', r'\1', desc)
            return desc[:160]
    
    return "A writing by Extra Small"


def auto_tag(content):
    """Auto-generate tags based on content keywords."""
    content_lower = content.lower()
    tags = []
    
    for tag, keywords in TAG_KEYWORDS.items():
        for kw in keywords:
            if kw.lower() in content_lower:
                tags.append(tag)
                break
    
    # Always add 'essay' if no other tags or very few
    if len(tags) == 0:
        tags.append('essay')
    
    # Limit to 5 tags max
    return tags[:5]


def parse_existing_frontmatter(content):
    """Parse existing frontmatter and return (frontmatter_dict, body)."""
    if not has_frontmatter(content):
        return None, content
    
    parts = content.split('---', 2)
    if len(parts) < 3:
        return None, content
    
    fm_text = parts[1].strip()
    body = parts[2].strip()
    
    fm = {}
    for line in fm_text.split('\n'):
        if ':' in line:
            key, val = line.split(':', 1)
            key = key.strip()
            val = val.strip().strip('"').strip("'")
            fm[key] = val
    
    return fm, body


def generate_frontmatter(title, date, description, tags):
    """Generate YAML frontmatter string."""
    tags_str = ', '.join(f'"{t}"' for t in tags)
    return f'''---
title: "{title}"
date: "{date}"
description: "{description}"
tags: [{tags_str}]
---'''


def sync():
    """Main sync function."""
    synced = 0
    skipped = 0
    errors = []
    
    # Get existing post slugs
    existing_slugs = set(f for f in os.listdir(POSTS_DIR) if f.endswith('.md'))
    
    for filename in sorted(os.listdir(WRITINGS_DIR)):
        if should_skip(filename):
            continue
        
        slug = extract_slug(filename)
        
        # Check if already exists
        if slug in existing_slugs:
            skipped += 1
            continue
        
        filepath = WRITINGS_DIR / filename
        content = filepath.read_text(encoding='utf-8')
        
        # Skip very short files (likely incomplete)
        if len(content.strip()) < 100:
            print(f"  SKIP (too short): {filename}")
            skipped += 1
            continue
        
        date = extract_date(filename)
        if not date:
            # Try to get from file modification time
            mtime = os.path.getmtime(filepath)
            date = datetime.fromtimestamp(mtime).strftime('%Y-%m-%d')
        
        if has_frontmatter(content):
            # File has frontmatter - check for description
            fm, body = parse_existing_frontmatter(content)
            if fm and 'description' not in fm:
                # Add description
                desc = extract_description(body)
                title = fm.get('title', extract_title(body) or slug.replace('-', ' ').title())
                tags_raw = fm.get('tags', '')
                # Try to parse tags
                if tags_raw.startswith('['):
                    tags = [t.strip().strip('"').strip("'") for t in tags_raw.strip('[]').split(',')]
                else:
                    tags = auto_tag(content)
                
                new_fm = generate_frontmatter(title, fm.get('date', date), desc, tags)
                output = new_fm + '\n\n' + body
            else:
                output = content
        else:
            # No frontmatter - generate it
            title = extract_title(content) or slug.replace('-', ' ').title()
            description = extract_description(content)
            tags = auto_tag(content)
            
            # Remove the title line from body
            body_lines = content.split('\n')
            body_start = 0
            for i, line in enumerate(body_lines):
                if line.strip().startswith('# '):
                    body_start = i + 1
                    break
            
            body = '\n'.join(body_lines[body_start:]).strip()
            fm = generate_frontmatter(title, date, description, tags)
            output = fm + '\n\n' + body
        
        # Write to posts directory
        out_path = POSTS_DIR / slug
        out_path.write_text(output, encoding='utf-8')
        print(f"  SYNCED: {filename} → {slug}")
        synced += 1
    
    print(f"\n✅ Sync complete: {synced} new posts, {skipped} skipped")
    if errors:
        print(f"❌ Errors: {len(errors)}")
        for e in errors:
            print(f"  - {e}")
    
    return synced


if __name__ == '__main__':
    sync()
