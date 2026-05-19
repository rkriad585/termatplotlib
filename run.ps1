<#
.SYNOPSIS
    termatplotlib launcher for PowerShell
.DESCRIPTION
    Launches termatplotlib with the given arguments.
    Usage: .\run.ps1 --type bar --labels "A B C" --data "10 20 30"
#>

python -m termatplotlib @args
