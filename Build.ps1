param(
    [string]$Environment='int'
)
Set-Location $PSScriptRoot

New-Item ./bin -ItemType Directory -Force | Out-Null

$egg = Get-ChildItem -Path './src/dist/pipelines-*-py3.5.egg' | Where-Object { -not $_.PsIsContainer } | Sort-Object LastWriteTime -Descending | Select-Object -first 1

if ($null -eq $egg)
{
    Throw "Egg for Python 3.5 not found in src/dist (run python setup.py bdist_egg)"
}
Copy-Item $egg.FullName "./bin/pipelines.egg"

# Copy the root py file that will be executed by jobs
Copy-Item "./src/main.py" ./bin
Copy-Item "./src/simpleExecute.py" ./bin
Copy-Item "./src/configs/$Environment.config.json" "./bin/config.json"