import os
import shutil
import requests

branches = []

def getBranches():
    response = requests.get('https://api.github.com/repos/FaithfulTeam/Faithful/branches')
    for branch in response.json():
        if '.' in branch['name']:
            branches.append(branch['name'])

def downloadBranches():
    os.mkdir('branches')
    for branch in branches:
        os.system(f'git clone --branch={branch} -v https://github.com/FaithfulTeam/Faithful ./branches/{branch}')

def makeZip():
    for branch in branches:
        shutil.make_archive(f'deploy/{branch}', 'zip', f'branches/{branch}')

def main():
    os.mkdir('deploy')
    getBranches()
    downloadBranches()
    makeZip()

if __name__ == '__main__':
    main()