# make_zip.ps1
# Skrypt do budowania paczki ZIP dla Blendera
# Wersja z pauzą i diagnostyką błędów

# Wymuś zatrzymanie w przypadku błędu
$ErrorActionPreference = 'Stop'

# 1. Ustalanie ścieżek
$sourceDir = $PSScriptRoot
$addonName = "AttractorBuilder"
$zipName   = "attractor_builder.zip"
$zipPath   = Join-Path $sourceDir $zipName

# Używamy folderu tymczasowego
$tempDir     = [System.IO.Path]::GetTempPath()
$stagingRoot = Join-Path $tempDir "BlenderAddonBuild_$addonName"
$stagingAddonDir = Join-Path $stagingRoot $addonName
$stagingLibDir   = Join-Path $stagingAddonDir "Lib"

Clear-Host
Write-Host "=== BUDOWANIE DODATKU: $addonName ===" -ForegroundColor Cyan
Write-Host "Folder zrodlowy: $sourceDir"

try {
    # 0. DIAGNOSTYKA: Sprawdzamy czy pliki istnieją
    if (-not (Test-Path (Join-Path $sourceDir "__init__.py"))) {
        throw "BRAK PLIKU: Nie znaleziono __init__.py w folderze skryptu!"
    }
    
    # Sprawdzamy folder Lib (lub lib - Windows nie rozróżnia wielkości liter, ale skrypt musi wiedzieć)
    if (-not (Test-Path (Join-Path $sourceDir "Lib"))) {
        # Próba sprawdzenia małej litery 'lib'
        if (-not (Test-Path (Join-Path $sourceDir "lib"))) {
             throw "BRAK FOLDERU: Nie znaleziono folderu 'Lib' ani 'lib'!"
        }
    }

    # 2. Sprzątanie starych plików
    Write-Host "Sprzatanie..." -ForegroundColor Gray
    if (Test-Path $stagingRoot) { Remove-Item $stagingRoot -Recurse -Force -ErrorAction SilentlyContinue }
    if (Test-Path $zipPath) { Remove-Item $zipPath -Force -ErrorAction SilentlyContinue }

    # 3. Tworzenie struktury
    New-Item -ItemType Directory -Path $stagingLibDir -Force | Out-Null

    # 4. Kopiowanie plików
    Write-Host "Kopiowanie plikow..." -ForegroundColor Gray
    
    # Kopiuj __init__.py
    Copy-Item (Join-Path $sourceDir "__init__.py") -Destination $stagingAddonDir
    
    # Kopiuj folder Lib (niezależnie czy nazywa się Lib czy lib)
    if (Test-Path (Join-Path $sourceDir "Lib")) {
        Copy-Item (Join-Path $sourceDir "Lib\*.json") -Destination $stagingLibDir
    } elseif (Test-Path (Join-Path $sourceDir "lib")) {
        Copy-Item (Join-Path $sourceDir "lib\*.json") -Destination $stagingLibDir
    }

    # 5. Pakowanie
    Write-Host "Pakowanie ZIP..." -ForegroundColor Gray
    Compress-Archive -Path $stagingAddonDir -DestinationPath $zipPath -Force

    Write-Host "----------------------------------------"
    Write-Host "SUKCES!" -ForegroundColor Green
    Write-Host "Plik gotowy: $zipPath"
    Write-Host "----------------------------------------"
}
catch {
    Write-Host "----------------------------------------"
    Write-Host "BLAD KRYTYCZNY:" -ForegroundColor Red
    Write-Host $_.Exception.Message -ForegroundColor Red
    Write-Host "----------------------------------------"
}
finally {
    # Sprzątanie folderu tymczasowego
    if (Test-Path $stagingRoot) { Remove-Item $stagingRoot -Recurse -Force -ErrorAction SilentlyContinue }
    
    # === TO ZATRZYMA OKNO ===
    Write-Host "Nacisnij dowolny klawisz, aby zamknac..."
    $null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
}