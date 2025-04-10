import os
import subprocess

# Path to your main 'code' directory
code_dir = os.getcwd()  # Current working directory

print(code_dir)


# List of possible virtual environment folder names
folders = [
    f for f in os.listdir(code_dir)
    if os.path.isdir(os.path.join(code_dir, f)) and not f.startswith('.')
]


for folder in folders:
    project_path = os.path.join(code_dir, folder)
    print(f"\n🔍 Checking project: {folder}")


 # Search for a virtual environment folder ending with .env
    venv_folder = None
    for item in os.listdir(project_path):
 
        item_path = os.path.join(project_path, item)
        if os.path.isdir(item_path) and item.endswith('.env'):
            venv_folder = item_path
            break

    if not venv_folder:
        print("⚠️ No virtual environment (*.env) found.")
        continue

    activate_script = os.path.join(venv_folder, 'Scripts', 'activate.bat')
    if not os.path.exists(activate_script):
        print("❌ activate.bat not found in env.")
        continue

    print(f"✅ Found env: {venv_folder}")
    print(f"📜 Activating: {activate_script}")


    # Command to activate and run pip freeze
    command = f'"{activate_script}" && pip freeze > requirements.txt'

    print(f"🛠️ Running command: {command}")


    # try:
    #     result = subprocess.run(command, shell=True, capture_output=True, text=True)

    #     if result.returncode == 0:
    #         requirements_path = os.path.join(project_path, 'requirements.txt')
    #         with open(requirements_path, 'w') as f:
    #             f.write(result.stdout)
    #         print(f"📦 Saved pip packages to: {requirements_path}")
    #     else:
    #         print(f"❌ pip freeze failed:\n{result.stderr}")

    # except Exception as e:
    #     print(f"🚨 Exception: {e}")


    try:
        # result = subprocess.run(command, shell=True, capture_output=True, text=True)
        result = subprocess.run(command, shell=True, capture_output=True, text=True, cwd=project_path)


        if result.returncode == 0:
            # Save requirements.txt in the project folder
            requirements_path = os.path.join(project_path, 'requirements.txt')
            with open(requirements_path, 'w') as f:
                f.write(result.stdout)
            print(f"📦 Saved: {requirements_path}")
        else:
            print(f"❌ pip freeze failed:\n{result.stderr}")

    except Exception as e:
        print(f"🚨 Exception: {e}")