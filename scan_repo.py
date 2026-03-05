# scan_repo.py
import os

# --- Configuration ---
# Files and directories to ignore. Add more if needed.
IGNORE_DIRS = {
    '.git', '__pycache__', 'node_modules', '.vscode', '.idea', 
    'venv', 'env', 'dist', 'build', 'target', '.next', 'coverage'
}
IGNORE_FILES = {
    '.DS_Store', 'scan_repo.py', 'package-lock.json', 'yarn.lock'
}
# File extensions to include. We focus on text-based source files.
INCLUDE_EXTENSIONS = {
    '.py', '.js', '.jsx', '.ts', '.tsx', '.java', '.go', '.rs', '.c', '.cpp', '.h',
    '.md', '.txt', '.json', '.yaml', '.yml', '.toml', '.xml', '.sh', '.sql',
    '.html', '.css', '.scss', '.vue', '.svelte'
}
# --- End of Configuration ---

def scan_repository(root_dir='.'):
    """
    Walks through the repository and concatenates the content of relevant files.
    """
    output = []
    for root, dirs, files in os.walk(root_dir):
        # Remove ignored directories from the walk
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]

        for file in files:
            if file in IGNORE_FILES:
                continue

            file_path = os.path.join(root, file)
            _, ext = os.path.splitext(file)

            if ext in INCLUDE_EXTENSIONS:
                try:
                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                        content = f.read()
                        # Add a clear header for each file
                        output.append(f"\n{'='*80}\n")
                        output.append(f"FILE: {file_path}\n")
                        output.append(f"{'='*80}\n")
                        output.append(content)
                except Exception as e:
                    print(f"Could not read file {file_path}: {e}")
    
    return "".join(output)

if __name__ == "__main__":
    print("Scanning repository... This may take a moment for large projects.")
    repo_content = scan_repository()
    
    # Save to a file to avoid terminal output limits
    with open("repo_contents.txt", "w", encoding="utf-8") as f:
        f.write(repo_content)
        
    print("\n✅ Done! The repository content has been saved to 'repo_contents.txt'.")
    print("📋 Please copy the entire contents of that file and paste it for me.")
