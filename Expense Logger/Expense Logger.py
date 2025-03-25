# Step 1: Open the file in append mode
with open("expenses.txt", "a") as file:
    while True:
        try:
            # Step 2: Get expense details
            expense_name = input("Enter expense name (or type 'exit' to stop): ")

            if expense_name.lower() == "exit":
                print("Exiting... Your expenses are saved in 'expenses.txt'.")
                break  # Stop the loop

            expense_amount = float(input("Enter expense amount: "))  # Convert to float

            # Step 3: Save the entry
            file.write(f"{expense_name}: ${expense_amount}\n")
            print("Expense recorded successfully!\n")

        except ValueError:
            print("Error: Please enter a valid number for the expense amount.")

        except Exception as e:
            print(f"An unexpected error occurred: {e}")

        finally:
            print("Logging attempt completed.")  # Always prints after each attempt