#TDLR Watched around 3 hours of Powershell videos just to find out it was because my powershell wasnt letting me run the file lol

New-Item -ItemType Directory -Name "Pears"
New-Item -ItemType Directory -Name "Bears"
New-Item -ItemType Directory -Name "Stairs"

Set-Location -Path "./Pears"

New-Item -ItemType Directory -Name "Pice"
New-Item -ItemType Directory -Name "Bice"
New-Item -ItemType Directory -Name "Sice"

Set-Location -Path ".."

Remove-Item -Recurse -Force "./Bears"
Remove-Item -Recurse -Force "./Stairs"
