git fetch origin

$branches = git branch | ForEach-Object { $_.Trim().TrimStart('* ') }

foreach ($branch in $branches) {
  Write-Host "`n=== $branch ===" -ForegroundColor Cyan
  git diff --stat "origin/$branch" "$branch"
}