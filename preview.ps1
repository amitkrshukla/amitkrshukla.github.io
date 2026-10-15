# Preview Script for Windows PowerShell
# Starts a local HTTP server to preview your static files and assets locally
# Usage: Open PowerShell in this folder and run: .\preview.ps1

$port = 4000
$listener = New-Object System.Net.HttpListener
$listener.Prefixes.Add("http://localhost:$port/")

try {
    $listener.Start()
    Write-Host "`n===========================================================" -ForegroundColor Green
    Write-Host " Site Preview Server running at: http://localhost:$port/ " -ForegroundColor Cyan
    Write-Host " Press Ctrl+C in this terminal to stop the server." -ForegroundColor Yellow
    Write-Host "===========================================================`n" -ForegroundColor Green

    # Launch default web browser
    Start-Process "http://localhost:$port/resume/"

    while ($listener.IsListening) {
        $context = $listener.GetContext()
        $request = $context.Request
        $response = $context.Response

        $rawUrl = $request.Url.LocalPath.TrimStart('/')
        if ([string]::IsNullOrEmpty($rawUrl)) {
            $rawUrl = "index.html"
        }

        # Handle directory paths
        $localPath = Join-Path $PSScriptRoot $rawUrl
        if (Test-Path $localPath -PathType Container) {
            $localPath = Join-Path $localPath "index.html"
        }

        if (Test-Path $localPath -PathType Leaf) {
            $ext = [System.IO.Path]::GetExtension($localPath).ToLower()
            $contentType = switch ($ext) {
                ".html" { "text/html; charset=utf-8" }
                ".css"  { "text/css; charset=utf-8" }
                ".js"   { "application/javascript; charset=utf-8" }
                ".json" { "application/json; charset=utf-8" }
                ".svg"  { "image/svg+xml" }
                ".png"  { "image/png" }
                ".jpg"  { "image/jpeg" }
                ".pdf"  { "application/pdf" }
                ".xml"  { "application/xml" }
                default { "application/octet-stream" }
            }

            $bytes = [System.IO.File]::ReadAllBytes($localPath)
            $response.ContentType = $contentType
            $response.ContentLength64 = $bytes.Length
            $response.OutputStream.Write($bytes, 0, $bytes.Length)
        } else {
            $response.StatusCode = 404
            $errBytes = [System.Text.Encoding]::UTF8.GetBytes("<h1>404 Not Found</h1><p>File not found: $rawUrl</p>")
            $response.OutputStream.Write($errBytes, 0, $errBytes.Length)
        }

        $response.Close()
    }
}
catch {
    Write-Host "Server stopped or error occurred: $_" -ForegroundColor Red
}
finally {
    $listener.Stop()
    $listener.Close()
}
