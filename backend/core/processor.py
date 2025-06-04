# backend/core/processor.py
class RepoProcessor:
    def __init__(self):
        self.client = chromadb.Client()

    def clone_repo(self, repo_url: str) -> str:
        """Returns local path to cloned repo"""
        repo_name = repo_url.split("/")[-1].replace(".git", "")
        repo_path = f"./repos/{repo_name}"

        if not os.path.exists(repo_path):
            Repo.clone_from(repo_url, repo_path)

        return repo_path
