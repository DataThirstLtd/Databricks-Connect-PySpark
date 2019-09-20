param(
    [string]$Environment='int'
)
Set-Location $PSScriptRoot

New-Item ./bin -ItemType Directory -Force | Out-Null

$egg = Get-ChildItem -Path './dist/pipelines-*.whl' | Where-Object { -not $_.PsIsContainer } | Sort-Object LastWriteTime -Descending | Select-Object -first 1

if ($null -eq $egg)
{
    Throw "Egg for Python 3.5 not found in ./dist (run python setup.py bdist_wheel)"
}
Copy-Item $egg.FullName "./bin/$($egg.Name)"

# Copy the root py file that will be executed by jobs
Copy-Item "./main.py" ./bin
Copy-Item "./simpleExecute.py" ./bin
Copy-Item "./configs/$Environment.config.json" "./bin/config.json"

Remove-Item -Path ./build -Force -Recurse
Remove-Item -Path ./dist -Force -Recurse
Remove-Item -Path ./pipelines.egg-info -Force -Recurse