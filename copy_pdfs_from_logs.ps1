$src_dir = "C:\Users\matlaczj\Documents\Repozytoria\AutoFEASULMs\src\logs"
$dst_dir = "C:\Users\matlaczj\Documents\Repozytoria\AutoFEASULMs\src\logs\all"

# Create the destination directory if it doesn't exist
if (!(Test-Path -Path $dst_dir)) {
    New-Item -ItemType Directory -Path $dst_dir | Out-Null
}

# Get all '.pdf' files in the source directory and its subdirectories
$pdf_files = Get-ChildItem -Path $src_dir -Filter "*.pdf" -Recurse -File

# Copy each '.pdf' file to the destination directory
foreach ($file in $pdf_files) {
    # Generate a new filename by appending the relative path from the source directory
    $relative_path = $file.FullName.Substring($src_dir.Length + 1)
    $new_filename = $relative_path -replace '\\', '_'
    $dst_file = Join-Path -Path $dst_dir -ChildPath $new_filename

    Copy-Item -Path $file.FullName -Destination $dst_file
}