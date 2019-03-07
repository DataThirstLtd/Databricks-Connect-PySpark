Set-Location $PSScriptRoot
$BearerToken = Get-Content -Path ./MyBearerToken.txt -Raw # Create this file in the root of your project with just your bearer token in

Import-Module azure.databricks.cicd.tools -MinimumVersion 1.1.12 -Force

$Region = "westeurope"
$ClusterId = "0307-093126-gaps139"
$TargetDBFSFolderCode = "/DatabricksConnectDemo/Code"

# Create a bin folder to build into
Remove-Item ./bin -Recurse -Force -ErrorAction:SilentlyContinue
New-Item ./bin -ItemType Directory -Force | Out-Null
$folders = Get-ChildItem -Path ./src -Directory -Exclude "__pycache__"
foreach ($f in $folders){
    Copy-Item "$f/*.py" ./bin
}

# Zip up all modules into a flat zip file
$source = Resolve-Path ./bin/*.py
$ZipFilePath = "./bin/scripts"
Compress-Archive -LiteralPath $source -DestinationPath $ZipFilePath 

# Clean up files that were added to the zip
Remove-Item -Path ./bin/*.py

# Copy the root py file that will be executed by jobsß
Copy-Item "./src/jobs.py" ./bin

##### DEPLOY TO DATABRICKS DBFS #####

# Blitz current files & upload files from bin directory
Remove-DatabricksDBFSItem -BearerToken $BearerToken -Region $Region -Path $TargetDBFSFolderCode
Add-DatabricksDBFSFile -BearerToken $BearerToken -Region $Region -LocalRootFolder "./bin" -FilePattern "*.*"  -TargetLocation $TargetDBFSFolderCode -Verbose


##### CREATE A SMAPLE JOB TO EXECUTE #####
$j = "planes"
$PythonParameters = "$j", 1980, 10
$MainScript = "dbfs:" + $TargetDBFSFolderCode + "/jobs.py"
Add-DatabricksPythonJob -BearerToken $BearerToken -Region $Region -JobName $j -ClusterId $ClusterId `
    -PythonPath $MainScript -PythonParameters $PythonParameters -Verbose

$j = "amazon"
$PythonParameters = $j
$MainScript = "dbfs:" + $TargetDBFSFolderCode + "/jobs.py"
Add-DatabricksPythonJob -BearerToken $BearerToken -Region $Region -JobName $j -ClusterId $ClusterId `
    -PythonPath $MainScript -PythonParameters $PythonParameters -Verbose