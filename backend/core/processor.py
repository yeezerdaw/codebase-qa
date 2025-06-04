import os
from git import Repo


class RepoProcessor:
    def __init__(self):
        self.repo_dir = "./repos"
        os.makedirs(self.repo_dir, exist_ok=True)

    def clone_repo(self, repo_url: str) -> str:
        repo_name = repo_url.split("/")[-1].replace(".git", "")
        repo_path = f"{self.repo_dir}/{repo_name}"

        if not os.path.exists(repo_path):
            Repo.clone_from(repo_url, repo_path)

        return repo_path
