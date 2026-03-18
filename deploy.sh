#!/bin/bash
# Deploy blog to GitHub Pages
# Usage: ./deploy.sh

set -e
cd "$(dirname "$0")"

echo "🔨 Building..."
npm run build

echo "📦 Deploying to gh-pages..."
cd dist
rm -rf .git
git init
git checkout -b gh-pages
git add -A
git commit -m "Deploy $(date '+%Y-%m-%d %H:%M')"
git remote add origin https://github.com/extrasmall0/extrasmall0.github.io.git
git push -f origin gh-pages

echo "✅ Deployed to https://extrasmall0.github.io/"
