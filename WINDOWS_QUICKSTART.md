# WINDOWS QUICK START - YOUR EXACT COMMANDS

Based on your path: `G:\PythonPractice\python practice.py\guvi\claude code\second`

---

## IMMEDIATE FIX (Choose One Method)

### METHOD 1: Double-Click Setup (EASIEST) ⭐

```
1. Double-click: SETUP_WINDOWS.bat
2. Wait for completion
3. Done!
```

This automatically:
- Sets UTF-8 encoding
- Fixes all Python files
- Runs complete setup

---

### METHOD 2: PowerShell Commands (Your Current Setup)

```powershell
# Step 1: Fix encoding once
cd "G:\PythonPractice\python practice.py\guvi\claude code\second"
python FIX_ALL_WINDOWS.py

# Step 2: Run setup
python setup.py

# Step 3: Run other scripts (no more errors!)
python content_creator_system.py
python job_hunting_system.py
python run_daily.py
```

---

### METHOD 3: Set Console Encoding First

```powershell
# Every time before running Python scripts
chcp 65001

# Then run normally
python setup.py
python content_creator_system.py
```

---

## YOUR COMPLETE WORKFLOW

### ONE-TIME SETUP (5 minutes):

```powershell
# Navigate to your project
cd "G:\PythonPractice\python practice.py\guvi\claude code\second"

# Activate virtual environment (optional)
myenv\Scripts\Activate.ps1

# Fix Windows encoding (ONE TIME!)
python FIX_ALL_WINDOWS.py

# Run all setups (ONE TIME!)
python setup.py
python content_creator_system.py
python job_hunting_system.py

# Fill your profile (IMPORTANT!)
notepad data\your_profile.json
```

---

### DAILY USAGE (15 minutes):

```powershell
# Navigate to project
cd "G:\PythonPractice\python practice.py\guvi\claude code\second"

# Run daily automation
python run_daily.py

# Open dashboard
start content_creator_dashboard.html

# Create post (in dashboard)
# Post to LinkedIn manually
# Send 2-3 job applications
```

---

## WHAT EACH FILE DOES

```
FIX_ALL_WINDOWS.py       ⭐ Run FIRST - fixes encoding
SETUP_WINDOWS.bat        ⭐ Double-click for auto setup
setup.py                 Creates all folders & files
content_creator_system.py Sets up content sources
job_hunting_system.py    Sets up job hunting templates
run_daily.py             Daily automation
```

---

## FILE LOCATIONS (YOUR ACTUAL PATHS)

```
Project Root:
G:\PythonPractice\python practice.py\guvi\claude code\second\

After Setup Creates:
├── data\
│   ├── your_profile.json          ⭐ EDIT THIS!
│   ├── email_templates.json       ⭐ Email templates
│   ├── application_tracker.json   ⭐ Track jobs
│   └── target_companies.json      Companies list
│
├── generated_posts\               Auto-generated drafts
├── logs\                          Activity logs
├── drafts\                        Your drafts
│
└── content_creator_dashboard.html ⭐ Main interface
```

---

## ERROR YOU SAW - NOW FIXED ✅

**Before:**
```
UnicodeEncodeError: 'charmap' codec can't encode character '\U0001f4a1'
```

**Solution Applied:**
All Python files now use `encoding='utf-8'` in file operations.

**How to Prevent:**
Run `python FIX_ALL_WINDOWS.py` before first use.

---

## VERIFICATION CHECKLIST

After running FIX_ALL_WINDOWS.py and setup.py:

```powershell
# Check folders exist
dir
# Should see: data, logs, drafts, generated_posts

# Check data files
dir data
# Should see: your_profile.json, email_templates.json, etc.

# Test daily script
python run_daily.py
# Should run without errors

# Test dashboard
start content_creator_dashboard.html
# Should open in browser
```

✅ If all above work, you're ready!

---

## YOUR TASK SCHEDULER SETUP

### Create Windows Scheduled Task:

1. **Win + R** → `taskschd.msc`

2. **Create Basic Task:**
   - Name: `AI ML Daily Automation`
   - Trigger: `Daily at 7:00 AM`

3. **Program Settings:**
   ```
   Program:
   C:\Users\OWNER\AppData\Local\Programs\Python\Python313\python.exe
   
   Arguments:
   "G:\PythonPractice\python practice.py\guvi\claude code\second\run_daily.py"
   
   Start in:
   G:\PythonPractice\python practice.py\guvi\claude code\second
   ```

4. **Test:** Right-click task → Run

---

## DAILY COMMANDS (Copy-Paste Ready)

```powershell
# Morning routine
cd "G:\PythonPractice\python practice.py\guvi\claude code\second"
python run_daily.py
start content_creator_dashboard.html

# Evening routine
notepad data\application_tracker.json
type data\target_companies.json
type data\email_templates.json
```

---

## QUICK REFERENCE

```powershell
# View files
type data\your_profile.json
type data\email_templates.json
type data\target_companies.json
type linkedin_recruiter_searches.txt

# Edit files
notepad data\your_profile.json
notepad data\application_tracker.json

# Run scripts
python run_daily.py              # Daily automation
python run_daily.py --review     # Weekly review

# Open dashboard
start content_creator_dashboard.html
```

---

## NEXT STEPS

1. ✅ Run: `python FIX_ALL_WINDOWS.py` (ONE TIME)
2. ✅ Run: `python setup.py`
3. ✅ Run: `python content_creator_system.py`
4. ✅ Run: `python job_hunting_system.py`
5. ✅ Edit: `data\your_profile.json` (ADD YOUR INFO!)
6. ✅ Test: `python run_daily.py`
7. ✅ Create your first post!

---

## PERMANENT FIX (Optional)

To never worry about encoding again:

```powershell
# Run PowerShell as Administrator
[System.Environment]::SetEnvironmentVariable('PYTHONIOENCODING', 'utf-8', 'User')

# Restart PowerShell
# All future Python scripts will use UTF-8
```

---

**Your system is now Windows-compatible and ready to use!** 🚀

**Just run: `python FIX_ALL_WINDOWS.py` once, then everything works!**
