from offline_mode import run_offline_mode
from online_mode import run_online_mode
print("\n===== Meeting Intelligence System =====\n")
print("1. Offline Meeting")
print("2. Online Meeting")
choice = input("\nEnter Choice: ")
if choice == "1":
    run_offline_mode()
elif choice == "2":
    run_online_mode()
else:
    print("Invalid Choice")