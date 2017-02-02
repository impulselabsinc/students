# students

## Pull down latest changes

Change into the folder where all your files are stored
```sh
cd ~/impulselabs/students/2017/coop/
cd ~/impulselabs/students/2017/ps11/
```

Pull down the latest changes. 
_Always do this before you do anything else_
```sh
git pull
```

Add files that you have created or changed to github.
_Adding a dot (.) will add all the files in that directory to github_
```sh
git add /path/to/file.py
git add /path/to/all/files/in/folder/.
```

Commit your changes to git
```sh
git commit -m "first commit or some other reason"
```

Push your changes to github
enter the username and password you were given
```sh
git push
```

Check the status of all your files
This will show you which files have been added but not pushed and files that have not yet been committed
```sh
git status
```

This is what I would do to create a directory calld toot where I can also save code Minecraft
```sh
cd ~/impulselabsinc/students/2017/ps11/
git pull
mkdir toot
cd toot
ln -s ../../../mcpi mcpi
git add .
git commit -m "created a new folder calld toot"
git push

```

This is what I would do to push a file called myPythonFile.py up to Github
```sh
cd ~/impulselabsinc/students/2017/ps11/toot/
git add myPythonFile.py
git commit -m "added my python file that does something cool"
git push

```

If you experience the following error, it is because there is a missing name configuration
```sh
fatal: empty ident name (for <pi@raspberrypi.(none)>) not allowed
```

You can fix this error by using the following command to add a name
```sh
git config user.name "imp2"
```

If you experience the following error, it is because there is a missing e-mail configuration
```sh
fatal: empty ident name (for <pi@raspberrypi.(none)>) not allowed
```

You can fix this error by using the following command to add an e-mail address
```sh
git config user.email "imp2@impulselabs.io"
```
