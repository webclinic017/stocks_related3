def git_clone():
    import git
    import os
    import subprocess

###############################
    bg='git@github.com:dk-code93/StockScanner.git'

    
    os.system('rm -rf /home/az2/Downloads/ff3/ff4')
    os.system('mkdir /home/az2/Downloads/ff3/ff4')
    p=os.listdir('/home/az2/Downloads/ff3/ff4')
    print(p)
    for x in p:
        print(os.remove('/home/az2/Downloads/ff3/ff4/'+str(x)))
        if '.' not in x:
    ##        print(x)
            print(os.remove('/home/az2/Downloads/ff3/ff4/'+str(x)))


    remoteurl=str(bg)
    localfolder='/home/az2/Downloads/ff3/ff4'
    myrepo=git.Repo.clone_from(remoteurl,localfolder)
    print('\n\n\n')
    i=0
    for x in os.listdir(localfolder):
    ##    if '.' not in x:
        print(i,'  ',x)
        i=i+1
    print('\n\n')
    print('cloned from : ',bg)
    print('cloned to local drive at : ,/home/az2/Downloads/ff3/ff4')




def git_upload():
    import random
    import os
    import subprocess
    import time

##    git fetch # synchronize with the server
##git branch --remote # list remote branches
##git branch -D -r origin/test

    cmd=[
        'aws ec2 describe-instances --query 'Reservations[*].Instances[*].[InstanceId]' --filters Name=instance-state-name,Values=running --output text',\

##        'git push git@github.com:azhar145/test52_in_sky.git --delete  vv_remote',
        'git init',\
        'git status',\
        'git branch -l'\
        'git branch bv_local_test',\
        'git checkout bv_local_test',\
        
        
        'git branch -d bv_local',\
        'git branch  bv_local',\
        'git checkout bv_local',
        'git branch -d bv_local_test',\
        'git add S.txt',\
        'git commit -m "mm"'
        'git status',\
        
        'git fetch',\
        'git fetch --all --prune',\
        'git branch --remote'

        
##        'git branch -D -r ($git branch --remote)'
        
####        
##        'git remote add vv_remote git@github.com:azhar145/test52_in_sky.git',\
##        'git remote set-url --add vv_remote git@github.com:azhar145/test52_in_sky.git',\
##        'git push --set-upstream  vv_remote bv_local'
#        git push --set-upstream finger jf

##

        ]
    
    



##    cmd=[

##        'git config /home/az2/Downloads/ff3/ff4',\
##        'git push git@github.com:azhar145/test52_in_sky.git --delete day4',\
##        'git push git@github.com:azhar145/test52_in_sky.git --delete day5'
##        'git init',\
##        'git branch -l'
####        'systemctl start ssh',\
####         'git push git@github.com:azhar145/test52_in_sky.git --delete nd',\
##         'cd /home/az2/Downloads/ff3/ff4',\
##         'git init /home/az2/Downloads/ff3/ff4',\
##        'git config --list',\
##         'git branch -d bv',\
##         'git branch  bv',\
##         'git checkout bv', 'git branch -l',\
##        'git add S.txt','git commit -m "fff"','git status',\
##
##         'git remote set-url --push azhar git@github.com:azhar145/test52_in_sky.git',\
##         'git push git@github.com:azhar145/test52_in_sky.git bv:day5'
##



        

##        'git stash','git checkout -b pasha','git stash apply','git status','git init -b pasha',\
##        'git branch -m pasha','git branch -a','git branch -l','git branch -r',\
##         'git fetch','git checkout vrr','git branch -r',\
##        'git remote -v','git remote set-url pasha git@github.com:azhar145/test52_in_sky.git','git remote -v'

         
##        'git config --list','git branch -r' ,'git branch -l','pwd','cd /home/az2/Downloads/ff3/ff4',\
##         'rm -rf /home/az2/Downloads/ff3/ff4','mkdir /home/az2/Downloads/ff3/ff4/','ls -l /home/az2/Downloads/ff3/ff4',\
##         'cp /home/az2/Downloads/x12input_1.txt /home/az2/Downloads/ff3/ff4',\
##         'ls -ltr /home/az2/Downloads/ff3/ff4',\
##         'git init -b pasha',\
##         'git init .',\
##         'git log',\
##         'git remote -v',\
##         'git add /home/az2/Downloads/ff3/ff4/.','git commit -m "1947"',\
##         'git remote add hh git@github.com:azhar145/test52_in_sky.git',\
##         'git push git@github.com:azhar145/test52_in_sky.git hh'
##         ]
    
##    cmd=['who','pwd','cd /home/az2/Downloads/ff3/ff4','ls -ltr /home/az2/Downloads/ff3/ff4', 'git config','git branch -r' ,'git branch -l','git remote -v',]
    print('\n\n\n')
    for x in cmd:
        print('\n')
        print('=========================================================================')
        print('command ---> ',x)
        print('-------------------------------------------------------------------------')
        print('output --> ')
        print(os.popen(x).read())
        print('-------------------------------------------------------------------------')
        print('=========================================================================')
    print('end')
##git_clone()         
git_upload()

##import os
##print(os. system('ls -l'))

##def x():
##    
##    import git
##    my_repo = git.Repo.init('/home/az2/Downloads/.git/')
##    repo_fetch = len(my_repo.remotes.origin.fetch())
##    for x in range(0,len(my_repo.remotes.origin.fetch())):
##        print(my_repo.remotes.origin.fetch()[x])
##    print ('Total no ',repo_fetch)
##


##git.Repo.clone_from(gitlab_ssh_URL, local_path)
##my_repo = git.Repo(local_path)
##tag_id = choose_tag() # Return the position of an existing tag in my_repo.tags
##my_repo.head.reference = my_repo.tags[tag_id]
##my_repo.head.reset(index=True, working_tree=True)
##fetch_info = my_repo.remotes.origin.fetch('master:master')
##for info in fetch_info:
##    print('{} {} {}'.format(info.ref, info.old_commit, info.flags))



##    print(x,'   ',str(x),'  ')

##print(os.system('git remote -v'))
##repo_dir = os.path.join(rw_dir, 'my-new-repo')
##file_name = os.path.join(repo_dir, os.system('touch new-file.txt'))
##
##r = git.Repo.init(repo_dir)
### This function just creates an empty file ...
##open(file_name, 'wb').close()
##r.index.add([file_name])
##r.index.commit("initial commit")

##def print_repository_info(repo):
##    print('Repository description: {}'.format(repo.description))
##    print('Repository active branch is {}'.format(repo.active_branch))
##
##    for remote in repo.remotes:
##        print('Remote named "{}" with URL "{}"'.format(remote, remote.url))
##
##    print('Last commit for repository is {}.'.format(str(repo.head.commit.hexsha)))

##import git
##import os
##
##rw_dir='/home/az2/Downloads/ff3/.git/'
##empty_repo = git.Repo.init(os.path.join(rw_dir, 'empty'))
##bare_repo = git.Repo.init(os.path.join(rw_dir, 'bare-repo'), bare=True)
##cloned_repo = git.repo.clone(os.path.join(rw_dir, 'git@github.com:azhar145/88.git'))
##print(bare_repo)
##print('\n\n\n')
##print(repo.untracked_files)
####origin = empty_repo.create_remote('origin', repo.remotes.origin.url)
##
####test_remote = repo.create_remote('test97', 'git@github.com:azhar145')
####print(test_remote)
####g=git.Repo('https://github.com/azhar145/88.git')
####os.system('rm /home/az2/Downloads/ff3/.git/gg.txt')
##repo = git.Repo.init('/home/az2/Downloads/ff3/.git/')
##print('[1] ',repo.git.status())
##os.system('cp /home/az2/Downloads/gg.txt /home/az2/Downloads/ff3/.git/gg.txt')
##
##print('[2] ',repo.git.add('/home/az2/Downloads/ff3/.git/gg.txt'))
####repo.git.add(all=True)   # git add --all
##repo.index.commit('my commit description')
##
##print('[4] ',repo.git.status())
##origin = repo.remote('origin')

##bare_repo=repo
##assert bare_repo.bare
      
##print(repo.git.add('/home/az2/Downloads/gg.txt'))
##print (repo.git.status())



##import os
##import subprocess
##
##def gitAdd(fileName, repoDir):
##    cmd = ['git', 'add', fileName]
##    p = subprocess.Popen(cmd, cwd=repoDir)
##    p.wait()
##
##gitAdd('test33.txt', '/home/az2/Downloads/')
##

##
##repo = git.Repo.init('.')
##origin = repo.create_remote('origin', 'git@github.com:azhar145/88.git')
##origin.fetch()
### the HEAD ref usually points to master, which is 'yet to be born'            
##repo.head.ref.set_tracking_branch(origin.refs.master)
##origin.pull()

##
##
##print(git.FetchInfo.list_items())
##repo_clone_url = "git@github.com:mygithubuser/myrepo.git"
##local_repo = "mytestproject"
##test_branch = "test-branch"
##repo = git.Repo.clone_from(repo_clone_url, local_repo)
### Check out branch test_branch somehow
### write to file in working directory
##repo.index.add(["test.txt"])
##commit = repo.index.commit("Commit test")

##import git
####repo = git.Repo( 'git@github.com:azhar145/88.git' )
##repo = git.Repo( '/home/me/repodir' )
##print (repo.git.status())
### checkout and track a remote branch
##print (repo.git.checkout( 'origin/somebranch', b='somebranch' ))
### add a file
##print (repo.git.add( 'somefile' ))
### commit
##print (repo.git.commit( m='my commit message' ))
### now we are one commit ahead
##print (repo.git.status())

                                                                        ##import sh
##git = sh.git.bake(_cwd='/home/az2/Downloads')
##print (git.status())
##### checkout and track a remote branch
##print git.checkout('-b', 'somebranch')
### add a file
##print git.add('somefile')
### commit
##print git.commit(m='my commit message')
### now we are one commit ahead
##print git.status()
        
                                                                                                                                                                            
