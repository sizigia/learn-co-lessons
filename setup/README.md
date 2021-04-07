# Merging All Lesson Repos into a Curriculum Repo

### References
- `$repo`: individual lesson repository on local machine  
- `${clones[$repo]}`: new local path for `$repo` within 

## Requirements:
1. Keep repo(s) history
2. Prefix all commit messages to distinguish commits between repos
3. Respect curriculum structure

## How To:

1. Clone the projects you want to merge.
    
    For my purpose, I have **51 lesson** repositories in a local folder.
    I downloaded them with a [Python script](clone_repos.py), using the [GitHub API](https://docs.github.com/en/rest).

    The destination repo is **learn-co-lessons** and will contain all **lesson** repositories, following the [curriculum's structure](../README.md).

2. I want all my **lesson** repositories to be subdirectories of the new project:  
    1. I set up the following variables:
        - Stored on my environment variables [file](../.env_sample)
            - `SOURCE`: local folder containing all **lesson** repos
            - `DESTINATION`: folder containing the new structure repo

            ```bash
            SOURCE=/local/source/old-folder/
            DESTINATION=/local/source/new-folder/
            ```
        - Set up on each iteration of the loop:
            - `OLD_REPO`: individual **lesson** folder within `SOURCE`
            - `NEW_REPO`: individual **lesson** folder within `DESTINATION`
           
            ```bash
            OLD_REPO=$SOURCE$repo
            NEW_REPO=${clones[$repo]}
            ```

        1. After setting up the variables, I'll access the old individual **lesson** folder:
        
            ```bash
            cd $OLD_REPO
            ```

        2. Since I'm merging each **lesson** repo history to the main repo history, I want to have a clear idea of which commit messages belong to each repo. In order to do this, I'll prefix all commits.
            - First I'm going to create a `PREFIX` variable that will edit the commit message by appending the lesson name between brackets:
                ```bash
                PREFIX="sed '1 s/^/[${repo}] /'"
                ```
            - Then I'll use `PREFIX` with [git filter-branch](https://git-scm.com/docs/git-filter-branch) to rewrite all commits from the `master` branch:
                ```bash
                git filter-branch -f --msg-filter "$(echo $PREFIX)" -- --branches master
                ```

    
    2. Now, I'll proceed with the merging and cleaning part.

        ```bash 
        cd $DESTINATION
        ```

        1. I add the **lesson** repository as a [remote](https://git-scm.com/docs/git-remote), and merge everything into the destINATIONination repo.  
            `git remote add <name> <url or path-to-repo>`

            ```bash
            git remote add $repo $OLD_REPO
            git fetch $repo
            ```

            This is the same as running:
            
            ```bash
            git remote add -f $repo $OLD_REPO
            ```

        2. First, I'll initiate the [merge](https://git-scm.com/docs/git-merge). 

            I'll use the merge strategy `-s ours` (`-s`, to select the strategy) to avoid modifying my current files:
            > This resolves any number of heads, but the resulting tree of the merge is always that of the current branch head, effectively ignoring all changes from all other branches. It is meant to be used to supersede old development history of side branches. 

            Also, I don't want to commit anything yet, so I'll use `--no-commit` to avoid it.

            Git doesn't allow a merge without a common history, so I'll force the merge with the option `--allow-unrelated-histories`.

            Assuming **master** is my main branch (new default is **main**):
            
            ```bash
            git merge -s ours --no-commit --allow-unrelated-histories $repo/master
            ```
        3. The next thing I want to do is to add the **lesson** repo files to its dedicated subdirectory. The command [`git read-tree`](https://git-scm.com/docs/git-read-tree) reads the information from the tree info into the index.

            By using `--prefix=...`, it'll keep the current index contents, and read the contents of the `master` branch of **lesson** repo folder into the subdirectory `$NEW_REPO`. It also refuses to overwrite entries that already existed in the original index file.
            
            Finally, I use the `-u` flag to update the files in the work tree with the result of the merge, after a successful merge.

            ```bash
            git read-tree --prefix=$NEW_REPO -u $repo/master
            ```

        4. The last stop before cleaning is commiting the changes:
            - I set up a commit message template with `$COMMIT_MSG`.

                ```bash        
                COMMIT_MSG="[${repo}] moved files into their own subdirectory"
                ```
            - And commit!
                ```bash
                git commit -m $COMMIT_MSG
                ```

        
        5. Finally, I'll delete the remote track.

            ```bash
            git remote remove $repo
            ```
    
    3. It's a good practice to the merges before pushing to the remote repository. 
        - `git log --onefile`: shows the commit history without details, only messages and IDs.
        - `git rebase -i`: it allows to modify specific commits. The `-i` stands for `interactive`. You can check this [example](https://www.youtube.com/watch?v=tukOm3Afd8s) to understand how it works.
    4. Once you're happy with the results, it's time to push:
        ```bash
        git push origin master
        ```