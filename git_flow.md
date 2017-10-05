Git Flow
http://nvie.com/posts/a-successful-git-branching-model/

* Create a release branch from develop - release/version-number

Release Branch
* Update version number and tag number in project.podspec.json
* pod install
* Build the project
* git add -A
* git commit 
* git push origin release/version-number
* git checkout develop

Develop Branch
* git merge --no-ff release/version-number
* git push -u origin develop
* git checkout master

Master Branch
* git merge --no-ff release/version-number
* git tag version-number
* git tag --list [To check if the version-number tag is added]
* git push -u origin master version-number
* cd to root repository
* pod repo push --verbose mnet-pod-specs ./MNALApplink.podspec.json --allow-warnings
	Refer https://github.com/gnithin/Notes/blob/master/Notes/iOS/privatePods.md
