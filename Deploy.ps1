param(
    [string]$Environment="INT",
    [string]$Region = "westeurope",
    [string]$ClusterId = "0920-081811-lamps471",
    [string]$TargetDBFSFolderCode = "/DatabricksConnectDemo/Code",
    [string]$BearerToken = ""
)
Set-Location $PSScriptRoot

if ($BearerToken -eq ""){
    $BearerToken = Get-Content -Path ./MyBearerToken.txt -Raw # Create this file in the root of your project with just your bearer token in
}

if (!(Get-Module azure.databricks.cicd.tools -ListAvailable)){
    Install-Module azure.databricks.cicd.tools -Force -SkipPublisherCheck
}

Import-Module azure.databricks.cicd.tools -MinimumVersion 1.1.12 -Force


##### DEPLOY TO DATABRICKS DBFS #####

# Blitz current files & upload files from bin directory
Remove-DatabricksDBFSItem -BearerToken $BearerToken -Region $Region -Path $TargetDBFSFolderCode
Add-DatabricksDBFSFile -BearerToken $BearerToken -Region $Region -LocalRootFolder "./bin" -FilePattern "*.*"  -TargetLocation $TargetDBFSFolderCode -Verbose
$WheelFileName = (Get-ChildItem -Path ./bin -Filter *.whl).Name

$Lib = '{"egg":"LOCATION"}'.Replace("LOCATION", "dbfs:$TargetDBFSFolderCode/$WheelFileName")

##### CREATE A SAMPLE JOB TO EXECUTE #####
$j = "planes"
$PythonParameters = "pipelines.jobs.$j", 1980, 10
$MainScript = "dbfs:" + $TargetDBFSFolderCode + "/main.py"
Add-DatabricksPythonJob -BearerToken $BearerToken -Region $Region -JobName $j -ClusterId $ClusterId `
    -PythonPath $MainScript -PythonParameters $PythonParameters -Libraries $Lib

$j = "amazon"
$PythonParameters = "pipelines.jobs.$j"
$MainScript = "dbfs:" + $TargetDBFSFolderCode + "/main.py"
Add-DatabricksPythonJob -BearerToken $BearerToken -Region $Region -JobName $j -ClusterId $ClusterId `
    -PythonPath $MainScript -PythonParameters $PythonParameters -Libraries $Lib

$j = "simple"
$PythonParameters = $null
$MainScript = "dbfs:" + $TargetDBFSFolderCode + "/simpleExecute.py"
Add-DatabricksPythonJob -BearerToken $BearerToken -Region $Region -JobName $j -ClusterId $ClusterId `
    -PythonPath $MainScript -PythonParameters $PythonParameters -Libraries $Lib

