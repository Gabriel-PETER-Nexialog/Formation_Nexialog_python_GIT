$branches = @(
  "main",
  "module/00-introduction",
  "module/01-git-basics",
  "module/02-solid",
  "module/03-dry-yagni",
  "module/04-patterns",
  "module/05-tests-tdd_bdd",
  "module/06-git-advanced",
  "module/07-coding-with-ia"
)

for ($i = 1; $i -lt $branches.Length; $i++) {
  $parent = $branches[$i - 1]
  $current = $branches[$i]

  Write-Host "Rebasing $current onto $parent..."
  git switch $current
  git rebase $parent

  if ($LASTEXITCODE -ne 0) {
    Write-Host "Conflict on $current -- stopping. Resolve then run git rebase --continue"
    exit 1
  }
}

Write-Host "All branches updated!"