# PowerShell script to upload .env variables as GitHub secrets

# Path to your .env file
$envFile = ".env"

# Check if .env exists
if (!(Test-Path $envFile)) {
    Write-Host ".env file not found in current directory."
    exit 1
}

# Read each line, skip comments and empty lines
Get-Content $envFile | ForEach-Object {
    if ($_ -match "^\s*#") { return }         # Skip comments
    if ($_ -match "^\s*$") { return }         # Skip empty lines
    if ($_ -match "^\s*([^=]+)=(.*)$") {
        $key = $matches[1].Trim()
        $value = $matches[2].Trim()
        Write-Host "Setting secret: $key"
        gh secret set $key -b"$value"
    }
}
