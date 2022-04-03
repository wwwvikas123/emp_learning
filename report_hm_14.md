## Задача 1

### 1.

```
 cd git-lesson/

 git init
```

### 2.

```
 touch README.md
 git add README.md && git commit -m "first file - readme"
```

### 3.

```
 git checkout -B feat1-add-readme
 echo "nemnogo texta" > README.md 
 git add README.md && git commit -m "first file - readme"
 git checkout master 
```

### 4.

```
 echo "takze dobavila text na mastere" README.md 
 git add README.md && git commit -m "izmenenia v master"
```

### 5.

```
 git merge feat1-add-readme 
```

### 6.

 git checkout feat1-add-readme 
 touch temp_file
 git add temp_file && git commit -m "added temp_file"
 
### 7. 

```
 git status 
 git log
 git revert a71c76b49ccafbb489b4a96f391939889ddb945c
```

## Задача 2

git remote add origin git@github.com:wwwvikas123/git-lesson.git
git branch -M main
git push -u origin main
git push origin --all
git checkout feat1-add-readme 
echo "Hello Github" > README.md 
git add README.md && git commit -m "changed README"
git push
