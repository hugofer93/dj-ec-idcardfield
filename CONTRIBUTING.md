# Contributing


## Add changes

1. **Create a feature branch from `dev`**:

    ```bash
    git checkout dev
    git pull origin dev
    git checkout -b feature/new-changes
    ```

2. **Develop changes and run the tests**:

    * Make the necessary changes to the feature branch
    * Run the tests

3. **Merge feature branch in `dev`**:

    ```bash
    git checkout dev
    git pull origin dev
    git merge --no-ff feature/new-changes
    git push origin dev
    ```

4. **Create a release branch from `dev`**:

    ```bash
    git checkout dev
    git pull origin dev
    git checkout -b release/0.1.5
    ```

5. **Update version**:

    * `pyproject.toml`:

        ```toml
        [tool.poetry]
        name = "dj-ec-idcardfield"
        version = "0.1.5"
        ```

    * `dj_ec_idcardfield/__init__.py`:

        ```python
        __version__ = '0.1.5'
        ```

    * `CHANGELOG.md`:

        ```markdown
        ## [0.1.5] - YYYY-MM-DD

        ### Added
        - Description of new changes and features.
        ```

6. **Commit changes**:

    ```bash
    git add pyproject.toml
    git add CHANGELOG.md
    git add dj_ec_idcardfield/__init__.py
    git commit -m "Prepare version 0.1.5"
    ```

7. **Merge release branch into `main`**:

    ```bash
    git checkout main
    git pull origin main
    git merge --no-ff release/0.1.5
    git push origin main
    ```

8. **Create a tag for the new release**:

    ```bash
    git tag -a 0.1.5 -m "Release 0.1.5"
    git push origin 0.1.5
    ```

9. **Merge release branch into `dev`**:

    ```bash
    git checkout dev
    git pull origin dev
    git merge --no-ff release/0.1.5
    git push origin dev
    ```

10. **Merge release branch into `stable/0.1.x`**:

    ```bash
    git checkout stable/0.1.x
    git pull origin stable/0.1.x
    git merge --no-ff release/0.1.5
    git push origin stable/0.1.x
    ```

11. **Remove the release branch**:

    ```bash
    git branch -d release/0.1.5
    git push origin --delete release/0.1.5
    ``` 

12. **Build and upload package to TestPyPI and PyPI**:

    ```bash
    # Build Python package
    poetry build

    # Upload package to TestPyPI
    python -m twine upload --repository testpypi dist/*

    # Upload package to PyPI
    python -m twine upload dist/*
    ```

13. **Create compressed source code files**:

    ```bash
    git archive --format zip --output dist/Source\ code.zip 0.1.1
    git archive --format tar.gz --output dist/Source\ code.tar.gz 0.1.1
    ```

14. **Upload the files generated in the `dist/` directory to GitHub Releases**:

    * Go to the Repo's release page on GitHub.
    * Create a new release or edit an existing one.
    * Upload the compressed files from the `dist/` directory.


## Fix errors

1. **Create a hotfix branch from `main` or `stable/0.1.x`**:

    ```bash
    git checkout main
    git pull origin main
    git checkout -b hotfix/bug-name
    ```

2. **Fix the bug and run the tests**:

    * Make the necessary changes to the hotfix branch
    * Run the tests

3. **Update version**:

    * `pyproject.toml`:

        ```toml
        [tool.poetry]
        name = "dj-ec-idcardfield"
        version = "0.1.1"
        ```

    * `dj_ec_idcardfield/__init__.py`:

        ```python
        __version__ = '0.1.1'
        ```

    * `CHANGELOG.md`:

        ```markdown
        ## [0.1.1] - YYYY-MM-DD

        ### Fix
        - Description of the bug fix.
        ```

4. **Commit changes**:

    ```bash
    git add pyproject.toml
    git add CHANGELOG.md
    git add dj_ec_idcardfield/__init__.py
    git commit -m "Prepare version 0.1.1"
    ```

5. **Merge hotfix branch into `main` or `stable/0.1.x`**:

    ```bash
    git checkout main
    git pull origin main
    git merge --no-ff hotfix/bug-name
    git push origin main
    ```

6. **Create a tag for the new release**:

    ```bash
    git tag -a 0.1.1 -m "Release 0.1.1"
    git push origin 0.1.1
    ```

7. **Merge hotfix branch into `dev`**:

    ```bash
    git checkout dev
    git pull origin dev
    git merge --no-ff hotfix/bug-name
    git push origin dev
    ```

8. **Merge hotfix branch into `main` or `stable/0.1.x`**:

    ```bash
    git checkout stable/0.1.x
    git pull origin stable/0.1.x
    git merge --no-ff hotfix/bug-name
    git push origin stable/0.1.x
    ```

9. **Remove the hotfix branch**:

    ```bash
    git branch -d hotfix/bug-name
    git push origin --delete hotfix/bug-name
    ```

10. **Build and upload package to TestPyPI and PyPI**:

    ```bash
    # Build Python package
    poetry build

    # Upload package to TestPyPI
    python -m twine upload --repository testpypi dist/*

    # Upload package to PyPI
    python -m twine upload dist/*
    ```

11. **Create compressed source code files**:

    ```bash
    git archive --format zip --output dist/Source\ code.zip 0.1.1
    git archive --format tar.gz --output dist/Source\ code.tar.gz 0.1.1
    ```

12. **Upload the files generated in the `dist/` directory to GitHub Releases**:

    * Go to the Repo's release page on GitHub.
    * Create a new release or edit an existing one.
    * Upload the compressed files from the `dist/` directory.
