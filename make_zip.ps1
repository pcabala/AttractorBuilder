# make_zip.ps1
# Skrypt do budowania paczki ZIP dla Blendera
# Uruchamiać z folderu głównego dodatku

# 1. Ustalanie ścieżek
# $PSScriptRoot to folder, w którym leży ten skrypt (czyli Twój folder AttractorBuilder)
$sourceDir = $PSScriptRoot
$addonName = "AttractorBuilder"
$zipName   = "attractor_builder.zip"
$zipPath   = Join-Path $sourceDir $zipName

# Używamy folderu tymczasowego systemu, żeby nie śmiecić w projekcie
$tempDir     = [System.IO.Path]::GetTempPath()
$stagingRoot = Join-Path $tempDir "BlenderAddonBuild_$addonName"
$stagingAddonDir = Join-Path $stagingRoot $addonName
$stagingLibDir   = Join-Path $stagingAddonDir "Lib"

Write-Host "Rozpoczynam budowanie $zipName..." -ForegroundColor Cyan

try {
    # 2. Sprzątanie
    if (Test-Path $stagingRoot) {
        Remove-Item $stagingRoot -Recurse -Force -ErrorAction SilentlyContinue
    }
    if (Test-Path $zipPath) {
        Remove-Item $zipPath -Force -ErrorAction SilentlyContinue
    }

    # 3. Tworzenie struktury katalogów (aby ZIP miał folder nadrzędny AttractorBuilder)
    New-Item -ItemType Directory -Path $stagingLibDir -Force | Out-Null

    # 4. Kopiowanie plików (Cherry-picking - wybieramy tylko to, co potrzebne)
    # Kopiuj __init__.py
    Copy-Item (Join-Path $sourceDir "__init__.py") -Destination $stagingAddonDir
    
    # Kopiuj zawartość folderu Lib (pliki json)
    Copy-Item (Join-Path $sourceDir "Lib\*.json") -Destination $stagingLibDir

    # Opcjonalnie: Jeśli masz inne pliki .py w głównym folderze, odkomentuj linię niżej:
    # Copy-Item (Join-Path $sourceDir "*.py") -Destination $stagingAddonDir

    # 5. Pakowanie do ZIP
    # Kompresujemy folder ze strefy tymczasowej do folderu projektu
    Compress-Archive -Path $stagingAddonDir -DestinationPath $zipPath -Force

    Write-Host "SUKCES!" -ForegroundColor Green
    Write-Host "Gotowy plik: $zipPath"
}
catch {
    Write-Host "BŁĄD: $_" -ForegroundColor Red
}
finally {
    # 6. Sprzątanie po sobie (usuwamy folder tymczasowy)
    if (Test-Path $stagingRoot) {
        Remove-Item $stagingRoot -Recurse -Force -ErrorAction SilentlyContinue
    }
}