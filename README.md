# InteractiveRebase
This repository contains a branch, `main`, which is meant to be used for practise with interactive rebases. Instructions are provided below.

## Why use interactive rebase?

Interactive rebase allows you to modify Git's commit history. It's useful for cleaning up PRs so they're easier to review, among other things. For example:

1. You might have the wrong Jira number in your commit messages.
2. You might find a mistake in one of your commits. You could fix it in a separate commit, but this could confuse reviewers if they review the commit with the mistake and leave comments, only for the comments to no longer make sense when the mistake is fixed.
3. You might accidentally include a password or secret key in a commit, which must **not** be pushed to the remote repository (this is a security problem).

## Instructions
To practise your interactive rebasing skills:

1. Clone a copy of this repo to your local environment.
2. Imagine the commits in this repo are for a pull request (PR) which will be reviewed.
3. See there are some problems with the commits (described in brackets on the commit messages).
4. Create a new branch with the latest commits from the _main_ branch. We will do the interactive rebase using this branch. This way, if we mess up the rebase, we don't lose all our work.
5. In the terminal, show a log of the last 10 commits or so (this will show the commit hashes).
   ```
   git log --oneline -n 10
   ```
6. Begin the rebase by modifying the commits after the initial commit, 2eff783.
   ```
   git rebase --interactive 2eff783
   ```
7. The [VI editor](https://ryanstutorials.net/linuxtutorial/vi.php) launches, showing the commands for the rebase. We will modify these as follows:
   1. Navigate the cursor using the arrow keys to highlight the first letter of the command
      
      `pick 1dfafe6 Fix mistake in earlier commit`.
   2. Press `d` and then `d` again to delete the command and store it in the clipboard.
   3. Navigate the cursor to highlight the first letter of the command
      
      `pick b29e6a4 LG-0000: Update function (this commit contains a mistake)`.
   4. Press `p` to paste the deleted line below the current line (`shift` + `p` to paste above). The commands should now be:
      ```
      pick b29e6a4 LG-0000: Update function (this commit contains a mistake)
      pick 1dfafe6 Fix mistake in earlier commit
      pick 7a9ad26 LG-0000: Add new function
      pick dedcc65 LG-0000: Add tests
      pick eed8c49 LG-0000: Update README (but oh no, I accidentally committed the password for my personal email)
      pick 9e443de Add test (but I forgot to include a Jira ticket number in the commit message)
      ```
   5. Press `i` to enter INSERT mode, to edit the commands.
   6. Using the arrow keys to move the cursor, edit the commands so they look like this:
       ```
       pick b29e6a4 LG-0000: Update function (this commit contains a mistake)
       squash 1dfafe6 Fix mistake in earlier commit
       pick 7a9ad26 LG-0000: Add new function
       pick dedcc65 LG-0000: Add tests
       edit eed8c49 LG-0000: Update README (but oh no, I accidentally committed the password for my personal email)
       reword 9e443de Add test (but I forgot to include a Jira ticket number in the commit message)
       ```
   7. The rebase has now been updated to:
      1. Fix the mistake in b29e6a4 using `squash` to combine it with 1dfafe6.
      2. `reword` 9e443de to include the missing Jira reference.
      3. `edit` eed8c49 to remove the password which must not be pushed to the remote repo for security reasons.
   8. Press `ESC` to leave INSERT mode.
   9. Type `:wq` to save the commands and exit, which will begin the rebase.
8. The attempt to combine 1dfafe6 and b29e6a4 (fixing the mistake) will result in a conflict, which we can fix in our IDE. We're trying to merge b29e6a4, which includes a mistake, with 1dfafe6, which fixes it. This is a bit confusing, because 1dfafe6 includes changes from other commits. Since it's only meant to be fixing the mistake, we will remove the other changes when we resolve our conflicts. The result should look like [6ca08ab](https://github.com/BenLambell-Plexus/InteractiveRebase/commit/6ca08ab7d1abb3a5014e41c3dcf933e87d05e228).
9. Stage the changes and continue the rebase.
   ```
   git add .
   git rebase --continue
   ```
10. Git will prompt us to provide a commit message for the squashed commits, using the VI editor again. In this case, we will delete the message _Fix mistake in earlier commit_ (by typing `d` and then `d` again, like before), and then exit the editor with `:wq`, which will continue the rebase.
11. Next, the rebase will allow us to edit eed8c49. Remove the email and password, which should not have been committed, using your IDE.
12. Stage the changes and continue the rebase. We don't need to modify the commit message this time.
    ```
    git add .
    git rebase --continue
    :wq
    ```
13. Next, we have another conflict when 7a9ad26 is applied, because it includes the mistake from b29e6a4 (which has now been fixed). We can fix this using our IDE (the result should look like [ec615c6](https://github.com/BenLambell-Plexus/InteractiveRebase/commit/ec615c6bfbe479f3ab22edda6931f16452897c0d)).
14. Stage the changes and continue the rebase. Again, we don't need to modify the commit message this time.
    ```
    git add .
    git rebase --continue
    :wq
    ```
15. Finally, the rebase will prompt us to reword 9e443de in the VI editor. We press `i` to enter INSERT mode, add the missing Jira number (LG-0000) to the commit message, and press `ESC` to exit INSERT mode and continue.
16. The rebase has now been completed. The result should look like [this](https://github.com/BenLambell-Plexus/InteractiveRebase/commits/expected-result).

## Notes

If you mess something up during an interactive rebase, you can cancel it with `git rebase --abort`.

I recommend always creating a new branch before starting an interactive rebase, so if you make a mistake you still have a copy of the original commits (in the original branch).

## Setup
Not essential, but you should be able to run the tests with the commands:
```
poetry install
poetry shell
pytest
```
