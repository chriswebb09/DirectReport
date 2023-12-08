import re
import requests

class GithubClient:
    # Define a function to parse the git shortlog
    def parse_git_shortlog(self, shortlog):
        """
        Parses a git shortlog and returns a dictionary with the author and their commits.

        Args:
          shortlog: The git shortlog string.

        Returns:
          A dictionary with the author and their commits.
        """
        authors = {}
        for line in shortlog.splitlines():
            match = re.match(r"^(.*?)\s+\((.*?)\):", line)
            if match:
                author, commits = match.groups()
                authors[author] = int(commits)
        return authors

    # def get_pull_request_comments_count(repo_owner, repo_name, pull_request_number):
    def get_pull_request_comments(self):
        """
        Gets the number of comments on a pull request.

        Args:
          repo_owner: The owner of the GitHub repository.
          repo_name: The name of the GitHub repository.
          pull_request_number: The number of the pull request.

        Returns:
          The number of comments on the pull request.
        """

        url = f"https://api.github.com/repos/chriswebb09/DirectReport/pulls/comments"
        headers = {"Authorization": "token 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"}

        response = requests.get(url, headers=headers)
        response.raise_for_status()
        print(response.content)
        print(response)

    def get_pull_requests(self):
        """
        Gets the number of comments on a pull request.

        Args:
          repo_owner: The owner of the GitHub repository.
          repo_name: The name of the GitHub repository.
          pull_request_number: The number of the pull request.

        Returns:
          The number of comments on the pull request.
        """

        url = f"https://api.github.com/repos/chriswebb09/DirectReport/pulls"
        headers = {"Authorization": "token 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"}

        response = requests.get(url, headers=headers)
        response.raise_for_status()
        print(response.content)
        print(response)
        return len(response.json())








# # Parse the git shortlog
# shortlog = """Adrian Prantl (67):\n add mangling testcase\n Debug Info: Represent private discriminators in DWARF.\n Revert \"Debug Info: Represent private discriminators in DWARF.\"\n Debug Info: Represent private discriminators in DWARF.\n Un-XFAIL and update test.\n Move the logic for ignoring the debug locations for closure setup code into SILGen. NFC-ish.\n Debug Info: Associate a function call with the beginning of the expression.\n Debug Info / SILGen: fix the source location of variable assignments\n typo\n Fix the debug locations of inserted operations in AvailableValueAggregator.\n Don't emit shadow copies for anonymous variables.\n Remove dead API IRGenDebugInfo::setArtificialTrapLocation().\n Use compiler-generated location for func.-sig.-spec. thunks\n whitespace\n Fix the missing inlined-at field of function-level SILDebugScopes.\n Add debug info support for inlined and specialized generic variables.\n Revert \"Add debug info support for inlined and specialized generic variables.\"\n Add debug info support for inlined and specialized generic variables.\n Update mangling prefix in Mangling.rst\n Add initial support for debug info for coroutine allocas.\n Temporarily disable failing test case, rdar://problem/43340064\n Add build-script support for the Swift LLDB backwards-compatibility tests.\n Remove accidentally committed debugging code\n Deserialize Swift compatibility version in CompilerInvocation::loadFromSerializedAST()\n SILGen: Preserve function argument debug info for arguments needing alloc_stack\n Use as the filename for SILLocation-less functions to avoid misleading source locatio\nns in backtraces.\n Add a -verify-linetable LLVM option.\n Enable debug info for inlined generics by default. It works now.\n Fix nonasserts compilation\n\nAhmad Alhashemi (5):\n [Parser] Detect nonbreaking space U+00A0 and fixit\n Move non-breaking space handling to lexUnknown\n Add more non-breaking space test cases\n Minor style edits\n Add tests for non-breaking space detect and fix-it\n\nAkshay Shrimali (1):\n Update README.md\n\nAlan Zeino (1):\n Fix typo in code example in libSyntax README\n\nAlbin \"albinek\" Sadowski (1):\n Fix syntax highlighting in CHANGELOG (#15107)\n\nAlejandro (3):\n Remove a warning, some doc fixes (#16863)\n [SR-8178] Fix BinaryFloatingPoint.random(in:) open range returning upperBound (#17794)\n [Docs] Fix minor code typo in SILPro..Man..md\n\nAlex Blewitt (5):\n [SR-7032] Fix compare for lhs and rhs\n [SR-7036] Use || instead of && for kind comparison\n [SR-7041] Remove duplicate conditional check\n Remove duplicate verb\n [SR-7043] Remove duplicate if statement"""
#
# # Get the authors and their commits
# authors = parse_git_shortlog(shortlog)
#
# # Print the team report
# print("Team Report")
# print("-----------")
# for author, commits in authors.items():
#   print(f"{author}: {commits} commits")
