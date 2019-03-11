param(
    [string]$Environment="INT",
    [string]$Region = "westeurope",
    [string]$ClusterId = "0307-093126-gaps139",
    [string]$TargetDBFSFolderCode = "/DatabricksConnectDemo/Code",
    [string]$BearerToken = ""
)
Set-Location $PSScriptRoot

if ($BearerToken -eq ""){
    $BearerToken = Get-Content -Path ./MyBearerToken.txt -Raw # Create this file in the root of your project with just your bearer token in
}

Import-Module azure.databricks.cicd.tools -MinimumVersion 1.1.12 -Force


##### DEPLOY TO DATABRICKS DBFS #####

# Blitz current files & upload files from bin directory
Remove-DatabricksDBFSItem -BearerToken $BearerToken -Region $Region -Path $TargetDBFSFolderCode
Add-DatabricksDBFSFile -BearerToken $BearerToken -Region $Region -LocalRootFolder "./bin" -FilePattern "*.*"  -TargetLocation $TargetDBFSFolderCode -Verbose

##### CREATE A SAMPLE JOB TO EXECUTE #####
$j = "planes"
$PythonParameters = "pipelines.jobs.$j", 1980, 10
$MainScript = "dbfs:" + $TargetDBFSFolderCode + "/main.py"
Add-DatabricksPythonJob -BearerToken $BearerToken -Region $Region -JobName $j -ClusterId $ClusterId `
    -PythonPath $MainScript -PythonParameters $PythonParameters -Verbose 

$j = "amazon"
$PythonParameters = "pipelines.jobs.$j"
$MainScript = "dbfs:" + $TargetDBFSFolderCode + "/main.py"
Add-DatabricksPythonJob -BearerToken $BearerToken -Region $Region -JobName $j -ClusterId $ClusterId `
    -PythonPath $MainScript -PythonParameters $PythonParameters -Verbose 

$j = "simple"
$PythonParameters = $null
$MainScript = "dbfs:" + $TargetDBFSFolderCode + "/simpleExecute.py"
Add-DatabricksPythonJob -BearerToken $BearerToken -Region $Region -JobName $j -ClusterId $ClusterId `
    -PythonPath $MainScript -PythonParameters $PythonParameters -Verbose 


Set-DatabricksSecret -BearerToken $BearerToken -Region $Region -ScopeName "DataThirst1" -SecretName "Secret1" -SecretValue "This is a secret!"