#!/bin/bash
#
# Install Git hooks for Triple-Z/LeetCode repo in local dir.
#

hooks=(pre-commit)

# set -o errexit
set -o xtrace
set -o nounset
set -o pipefail

UTILS_DIR=$(dirname "${BASH_SOURCE[@]}")
# go to root dir
cd $UTILS_DIR/..

if [ "$1"x = "-r"x ]; then
    for hook in ${hooks[@]}; do
        rm -f .git/hook/$hook
    done
fi

for hook in ${hooks[@]}; do
    if [ -r .git/hooks/$hook ]; then
        cnt=$(cat .git/hooks/$hook | tail -n 5)
        isInstalled=$(grep -c "\"$cnt\"" .git/hooks/$hook)
        if [ $isInstalled -eq 0 ]; then
            echo "The $hook hook exists, appending..."
            cat utils/hooks/$hook | tail -n 5 >> .git/hooks/$hook
        fi
    else
        cp utils/hooks/$hook .git/hooks/$hook
    fi
    chmod +x .git/hooks/$hook

    if [ $? -eq 0 ]; then
        echo "Git hooks are installed in \`.git/hooks\`."
    else
        echo "[ERROR] Hooks installed failed."
    fi
done

exit 0
