#!/bin/bash

# Назва гілки для пушу
BRANCH_NAME="main"

# Повідомлення коміту
COMMIT_MESSAGE="Added user authorization and recommendation features"

# Додаємо всі зміни до staging area
git add .

# Робимо коміт із повідомленням
git commit -m "$COMMIT_MESSAGE"

# Пушимо коміт до віддаленого репозиторію
git push origin $BRANCH_NAME

echo "Changes have been committed and pushed to branch $BRANCH_NAME."
