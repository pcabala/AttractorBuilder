# make_zip.ps1 - WERSJA STABILNA
# Używa systemowego Pythona, aby stworzyć ZIP kompatybilny z Mac/Linux (forward slashes)

# Zabezpieczenie przed znikającym oknem
$ErrorActionPreference = 'Stop'

try {
    # 1. Ustalanie ścieżek
    $sourceDir = $PSScriptRoot
    $addonName = "AttractorBuilder"
    $zipName   = "attractor_builder.zip"
    $zipPath   = Join-Path $sourceDir $zipName

    # Folder tymczasowy
    $tempDir     = [System.IO.Path]::GetTempPath()
    $stagingRoot = Join-Path $tempDir "BlenderAddonBuild_$addonName"
    $stagingAddonDir = Join-Path $stagingRoot $addonName
    $stagingLibDir   = Join-Path $stagingAddonDir "lib"

    Clear-Host
    Write-Host "=== BUDOWANIE DODATKU (CROSS-PLATFORM) ===" -ForegroundColor Cyan
    Write-Host "Katalog zrodlowy: $sourceDir"

    # 2. Sprawdzenie interpretera Pythona
    $pythonCmd = "python"
    try {
        $result = & $pythonCmd --version 2>&1
        Write-Host "Znaleziono Python: $result" -ForegroundColor Green
    } catch {
        # Jeśli nie ma 'python', próbujemy 'py' (Launcher)
        try {
            $pythonCmd = "py"
            $result = & $pythonCmd --version 2>&1
            Write-Host "Znaleziono Python Launcher: $result" -ForegroundColor Green
        } catch {
            throw "NIE ZNALEZIONO PYTHONA! Zainstaluj Python i dodaj do PATH, aby ten skrypt zadzialal."
        }
    }

    # 3. Sprzątanie
    Write-Host "Czyszczenie..." -ForegroundColor Gray
    if (Test-Path $stagingRoot) { Remove-Item $stagingRoot -Recurse -Force -ErrorAction SilentlyContinue }
    if (Test-Path $zipPath) { Remove-Item $zipPath -Force -ErrorAction SilentlyContinue }

    # 4. Tworzenie struktury
    New-Item -ItemType Directory -Path $stagingLibDir -Force | Out-Null

    # 5. Kopiowanie plików
    Write-Host "Kopiowanie plikow do tymczasowego folderu..." -ForegroundColor Gray
    
    # __init__.py
    $initPath = Join-Path $sourceDir "__init__.py"
    if (-not (Test-Path $initPath)) { throw "Brak pliku __init__.py!" }
    Copy-Item $initPath -Destination $stagingAddonDir

    # JSONy
    if (Test-Path (Join-Path $sourceDir "Lib")) {
        Copy-Item (Join-Path $sourceDir "Lib\*.json") -Destination $stagingLibDir
    } elseif (Test-Path (Join-Path $sourceDir "lib")) {
        Copy-Item (Join-Path $sourceDir "lib\*.json") -Destination $stagingLibDir
    } else {
        throw "Nie znaleziono folderu Lib lub lib z plikami JSON!"
    }

    # 6. Generowanie skryptu Pythona do pakowania
    Write-Host "Generowanie skryptu pakujacego..." -ForegroundColor Gray
    $pyScriptPath = Join-Path $tempDir "zipper_temp.py"
    
    # Kod Pythona - używa 'os.walk' i wymusza '/' w archiwum
    $pyCode = @"
import zipfile
import os
import sys

# Pobieramy sciezki z argumentow (bezpieczniej niz wklejac w string)
src_path = sys.argv[1]
zip_path = sys.argv[2]

print(f'Pakuje folder: {src_path}')
print(f'Do pliku: {zip_path}')

try:
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zf:
        count = 0
        for root, dirs, files in os.walk(src_path):
            for file in files:
                abs_path = os.path.join(root, file)
                # Relatywna sciezka (np. AttractorBuilder/lib/file.json)
                rel_path = os.path.relpath(abs_path, src_path)
                # KLUCZOWE: Zamiana backslash na slash dla ZIPa
                rel_path = rel_path.replace('\\', '/')
                
                print(f'  Dodaje: {rel_path}')
                zf.write(abs_path, arcname=rel_path)
                count += 1
        print(f'Spakowano {count} plikow.')
except Exception as e:
    print(f'BLAD PYTHONA: {e}')
    sys.exit(1)
"@
    Set-Content -Path $pyScriptPath -Value $pyCode -Encoding UTF8

    # 7. Uruchomienie pakowania
    Write-Host "Uruchamianie Python Zipper..." -ForegroundColor Yellow
    
    # Przekazujemy ścieżki jako argumenty (bez cudzysłowów wewnątrz komendy, PS to ogarnie)
    & $pythonCmd $pyScriptPath $stagingRoot $zipPath

    # 8. Weryfikacja
    if (Test-Path $zipPath) {
        Write-Host "`n----------------------------------------"
        Write-Host "SUKCES! ZIP utworzony poprawnie." -ForegroundColor Green
        Write-Host "Sciezka: $zipPath"
        Write-Host "----------------------------------------"
    } else {
        throw "Plik ZIP nie powstal! Sprawdz bledy powyzej."
    }

}
catch {
    Write-Host "`n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!" -ForegroundColor Red
    Write-Host "WYSTAPIL BLAD:" -ForegroundColor Red
    Write-Host $_.Exception.Message -ForegroundColor Red
    Write-Host "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
}
finally {
    # Sprzątanie skryptu pythona i folderu staging
    if (Test-Path $pyScriptPath) { Remove-Item $pyScriptPath -Force -ErrorAction SilentlyContinue }
    if (Test-Path $stagingRoot) { Remove-Item $stagingRoot -Recurse -Force -ErrorAction SilentlyContinue }

    # PAUZA NA KONIEC - żebyś widział co się stało
    Write-Host "`nNacisnij ENTER aby zamknac..."
    $null = Read-Host
}