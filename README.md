# github_readme
A beginners guide to github
name:Opeyemi Adeyemi
slack handle:@Dayvvo

Definition
- Git is a version control system. It is used to track changes in code and for collaboration in projects. Version control can be done locally with git or remotely using an online version control system e.g github, bitbucket, etc

Terms:
Repository: the file in which you want to track file changes with git
Commit: a sort of save point in code. can help to create multiple versions of project
Branch: a sort of an offshoot of your project. Can help to safely implement new features without risk of damaging existing code.By default the user is on the Master branch

git setup: download  and install git bash for windows

Commands:
git init: initialize git in your project folder
git add: add files to the staging area(prepare them for commiting) can be used to add a single file(git add filename) or the entire folder(git add .)
git commmit -m message: create a commit with -m to add a commit message for reference purposes
git push: used to push the contents of a repository to an online repository:
git clone: used to clone(copy) an online repository to your local computer


key features(assuming you have installed and opened git bash in your desired folder path): 
1 creating a repo and adding a commit:
  git init
  git add . (add all files to the staging area)
  git commit -m message

2 pushing a repository to github
  repeat the steps above
  login to github/create account if you have none and create a new repository and select all options i.e private/public repository, set repo name, initialize readme file etc and create.
  open the repository click clone or download and copy the repo path
  add the repo path to your local repository remote by using git add remote origin (git repo file path)
  push your local repo with the commant git push origin master to push it to the master branch of your newly created git repo

3 cloning a repo
  repeat the steps in number 1 and copy the repo path you created
  in git bash type git clone file path




