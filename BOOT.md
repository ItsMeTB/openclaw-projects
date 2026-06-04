\# BOOT.md - Dev Agent Startup Rules



You are a dev agent. Every time you complete a coding task you MUST run these exact shell commands using the exec tool:



1\. git -C C:\\Users\\timot\\.openclaw\\workspace-dev add <filename>

2\. git -C C:\\Users\\timot\\.openclaw\\workspace-dev commit -m "feat: <description>"

3\. git -C C:\\Users\\timot\\.openclaw\\workspace-dev push origin main



Then post the GitHub URL to the user: https://github.com/ItsMeTB/openclaw-projects/blob/main/<filename>



This is not optional. Do it every single time without being asked.

