if (Test-Path -Path "./new_folder") {
    # Create 'if_folder' if 'new_folder' exists
    New-Item -ItemType Directory -Path "./if_folder"
}

# Check if 'if_folder' exists
if (Test-Path -Path "./if_folder") {
    # If it exists, create 'hyperionDev'
    New-Item -ItemType Directory -Path "./hyperionDev"
} else {
    # Otherwise, create 'new-projects'
    New-Item -ItemType Directory -Path "./new-projects"
}
