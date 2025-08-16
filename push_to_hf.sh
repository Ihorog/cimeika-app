#!/bin/bash

# === Clone GitHub \u2192 Push to Hugging Face Space ===
# Requires: huggingface-cli, git

# Load environment variables
source .env || exit 1

# 1. Clone the GitHub repo
rm -rf cimeika && git clone "$GITHUB_REPO_URL"
cd cimeika || exit 1

# 2. Login to Hugging Face
echo "$HUGGINGFACE_TOKEN" | huggingface-cli login --token

# 3. Add HF as remote if not already added
if ! git remote | grep -q hf; then
  git remote add hf "$HF_SPACE_URL"
fi

# 4. Push to Hugging Face Space
# Try pushing to main; if not available, push to master
git push hf main || git push hf master

# 5. Done
echo "\ud83d\ude0a Repo successfully cloned from GitHub and pushed to Hugging Face."

