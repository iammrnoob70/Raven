#====================================================================================================
# START - Testing Protocol - DO NOT EDIT OR REMOVE THIS SECTION
#====================================================================================================

# THIS SECTION CONTAINS CRITICAL TESTING INSTRUCTIONS FOR BOTH AGENTS
# BOTH MAIN_AGENT AND TESTING_AGENT MUST PRESERVE THIS ENTIRE BLOCK

# Communication Protocol:
# If the `testing_agent` is available, main agent should delegate all testing tasks to it.
#
# You have access to a file called `test_result.md`. This file contains the complete testing state
# and history, and is the primary means of communication between main and the testing agent.
#
# Main and testing agents must follow this exact format to maintain testing data. 
# The testing data must be entered in yaml format Below is the data structure:
# 
## user_problem_statement: {problem_statement}
## backend:
##   - task: "Task name"
##     implemented: true
##     working: true  # or false or "NA"
##     file: "file_path.py"
##     stuck_count: 0
##     priority: "high"  # or "medium" or "low"
##     needs_retesting: false
##     status_history:
##         -working: true  # or false or "NA"
##         -agent: "main"  # or "testing" or "user"
##         -comment: "Detailed comment about status"
##
## frontend:
##   - task: "Task name"
##     implemented: true
##     working: true  # or false or "NA"
##     file: "file_path.js"
##     stuck_count: 0
##     priority: "high"  # or "medium" or "low"
##     needs_retesting: false
##     status_history:
##         -working: true  # or false or "NA"
##         -agent: "main"  # or "testing" or "user"
##         -comment: "Detailed comment about status"
##
## metadata:
##   created_by: "main_agent"
##   version: "1.0"
##   test_sequence: 0
##   run_ui: false
##
## test_plan:
##   current_focus:
##     - "Task name 1"
##     - "Task name 2"
##   stuck_tasks:
##     - "Task name with persistent issues"
##   test_all: false
##   test_priority: "high_first"  # or "sequential" or "stuck_first"
##
## agent_communication:
##     -agent: "main"  # or "testing" or "user"
##     -message: "Communication message between agents"

# Protocol Guidelines for Main agent
#
# 1. Update Test Result File Before Testing:
#    - Main agent must always update the `test_result.md` file before calling the testing agent
#    - Add implementation details to the status_history
#    - Set `needs_retesting` to true for tasks that need testing
#    - Update the `test_plan` section to guide testing priorities
#    - Add a message to `agent_communication` explaining what you've done
#
# 2. Incorporate User Feedback:
#    - When a user provides feedback that something is or isn't working, add this information to the relevant task's status_history
#    - Update the working status based on user feedback
#    - If a user reports an issue with a task that was marked as working, increment the stuck_count
#    - Whenever user reports issue in the app, if we have testing agent and task_result.md file so find the appropriate task for that and append in status_history of that task to contain the user concern and problem as well 
#
# 3. Track Stuck Tasks:
#    - Monitor which tasks have high stuck_count values or where you are fixing same issue again and again, analyze that when you read task_result.md
#    - For persistent issues, use websearch tool to find solutions
#    - Pay special attention to tasks in the stuck_tasks list
#    - When you fix an issue with a stuck task, don't reset the stuck_count until the testing agent confirms it's working
#
# 4. Provide Context to Testing Agent:
#    - When calling the testing agent, provide clear instructions about:
#      - Which tasks need testing (reference the test_plan)
#      - Any authentication details or configuration needed
#      - Specific test scenarios to focus on
#      - Any known issues or edge cases to verify
#
# 5. Call the testing agent with specific instructions referring to test_result.md
#
# IMPORTANT: Main agent must ALWAYS update test_result.md BEFORE calling the testing agent, as it relies on this file to understand what to test next.

#====================================================================================================
# END - Testing Protocol - DO NOT EDIT OR REMOVE THIS SECTION
#====================================================================================================



#====================================================================================================
# Testing Data - Main Agent and testing sub agent both should log testing data below this section
#====================================================================================================

user_problem_statement: |
  Upgrade Raven Assistant with:
  1. Bengali Voice (Voice Out) - Replace pyttsx3 with edge-tts using 'bn-BD-NabanitaNeural' voice
  2. Better Hearing (Voice In) - Improved ambient noise adjustment and pause threshold
  3. Computer Control - Smart WhatsApp messaging with contacts dictionary and enhanced search
  4. Modern UI - Floating, draggable, semi-transparent window with glow effects
  5. Banglish Personality - Mix of Bengali and English in all responses

backend:
  - task: "Core Logic Upgrade (raven_core.py)"
    implemented: true
    working: "NA"
    file: "raven_core.py"
    stuck_count: 0
    priority: "high"
    needs_retesting: true
    status_history:
      - working: "NA"
        agent: "main"
        comment: |
          Upgraded raven_core.py with:
          - Replaced pyttsx3 with edge-tts (Bengali voice 'bn-BD-NabanitaNeural')
          - Added pygame for audio playback
          - Enhanced speech recognition with 1.0s ambient noise adjustment and pause_threshold
          - Smart WhatsApp command with contacts dictionary
          - Enhanced search command
          - Banglish personality in all responses
          - All system commands updated with Banglish responses

frontend:
  - task: "Modern GUI Upgrade (raven_gui.py)"
    implemented: true
    working: "NA"
    file: "raven_gui.py"
    stuck_count: 0
    priority: "high"
    needs_retesting: true
    status_history:
      - working: "NA"
        agent: "main"
        comment: |
          Upgraded raven_gui.py with:
          - Borderless floating window (overrideredirect)
          - Semi-transparent background (0.9 opacity)
          - Always on top functionality
          - Draggable window support
          - Enhanced glow effects for different states (Emerald Green, Electric Violet, Soft Blue)
          - Modern control buttons with Consolas font
          - Rounded corners and sleek design
          - Chat bubble styling improvements

metadata:
  created_by: "main_agent"
  version: "1.0"
  test_sequence: 0
  run_ui: false

test_plan:
  current_focus:
    - "Core Logic Upgrade (raven_core.py)"
    - "Modern GUI Upgrade (raven_gui.py)"
  stuck_tasks: []
  test_all: false
  test_priority: "high_first"

agent_communication:
  - agent: "main"
    message: |
      RAVEN ASSISTANT - FINAL ENHANCEMENTS COMPLETE!
      
      All upgrades have been implemented:
      
      1. ✅ Bengali Voice - edge-tts with 'bn-BD-NabanitaNeural' voice installed
      2. ✅ Better Hearing - Enhanced ambient noise adjustment (1.0s) and pause_threshold (1.0)
      3. ✅ Computer Control - Smart WhatsApp with contacts dictionary, enhanced search
      4. ✅ Modern UI - Floating, draggable, semi-transparent window with glow effects
      5. ✅ Banglish Personality - All responses in Banglish mix
      
      NEW FINAL IMPROVEMENTS (v2.1):
      6. ✅ Language Logic - Switch between English/Banglish modes, persists across restarts
      7. ✅ Always Listening - Continuous Listen-Respond-Listen loop when Voice Toggle ON
      8. ✅ UI Continuity - Window always on top, language mode saved in memory
      9. ✅ WhatsApp Reliability - 2-second auto-send delay for reliable messaging
      10. ✅ Idle Personality - Witty Banglish messages after 30s of silence
      
      NEXT STEPS:
      - User should add their contacts to CONTACTS dictionary in raven_core.py (line 34-40)
      - Run the application: python raven_assistant.py
      - Say "English" to switch to English mode, speak Bengali to return to Banglish
      - Test continuous voice listening with Voice Toggle ON
      - Test WhatsApp commands: "Open WhatsApp" or "Send message to [contact]"
      - Verify window stays on top and language mode persists after restart
  
  - agent: "main"
    message: |
      IMPLEMENTATION DETAILS:
      
      Modified Files:
      - /app/raven_core.py: Added language_mode state, updated memory system, 2s WhatsApp delay
      - /app/raven_gui.py: Enhanced voice loop, idle timeout with witty messages
      
      Key Features:
      - Language switching: Say "English" or speak Bengali to switch modes
      - Memory persistence: language_mode saved in history.json
      - Continuous listening: No interruption between voice responses
      - Smart WhatsApp: Direct "Open WhatsApp" command, 2s auto-send
      - Idle messages: Random witty Banglish phrases after 30s silence
      - Always on top: Window stays visible over other apps
      
      See /app/RAVEN_IMPROVEMENTS.md for complete documentation