# # !/bin/bash
source "setup/dictionary.sh"

envup() {
  local file=$([ -z "$1" ] && echo ".env" || echo ".env$1")

  if [ -f $file ]; then
    set -a
    source $file
    set +a
  else
    echo "No $file file found" 1>&2
    return 1
  fi
}

envup 

EXTGLOB="$(shopt |grep extglob)"

if [[ $EXTGLOB =~ "extglob off" ]]; then
    shopt -s extglob || echo "Enabled extglob"
else
    echo "extglob already enabled"
fi


for repos in "${!clones[*]}" ; do 
    for repo in ${repos} ; do
        OLD_REPO=$SOURCE$repo
        NEW_REPO=${clones[$repo]}

        cd $OLD_REPO
        echo "Accessing ${OLD_REPO}"

        PREFIX="sed '1 s/^/[${repo}] /'"
        echo "Prefixing all commits as follows: '[${repo}] commit message ... '"

        git filter-branch -f --msg-filter "$(echo $PREFIX)" -- --branches master


        cd $DESTINATION

        echo "Adding remote tracking for ${repo}"
        git remote add $repo $OLD_REPO
        git fetch $repo


        echo "Merging ${repo}"
        git merge -s ours --no-commit --allow-unrelated-histories $repo/master

        echo "Adding ${repo} files to curriculum"
        git read-tree --prefix=$NEW_REPO -u $repo/master

        COMMIT_MSG="[${repo}] moved files into their own subdirectory"
        echo "Commiting changes as follows: '${COMMIT_MSG}'"
        git commit -m "$(echo $COMMIT_MSG)"

        echo "Removing remote tracking for ${repo}"
        git remote remove $repo
    done
done