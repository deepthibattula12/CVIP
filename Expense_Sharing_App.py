class ExpenseSharingApp:
    def __init__(self):
        self.friends = []
        self.expenses = []
    
    def add_friend(self, friend_name):
        self.friends.append(friend_name)
    
    def add_expense(self, description, amount, paid_by, split_between):
        expense = {
            'description': description,
            'amount': amount,
            'paid_by': paid_by,
            'split_between': split_between
        }
        self.expenses.append(expense)
    
    def calculate_balances(self):
        balances = {friend: 0 for friend in self.friends}
        
        for expense in self.expenses:
            total_split = len(expense['split_between'])
            split_amount = expense['amount'] / total_split
            
            for friend in expense['split_between']:
                if friend != expense['paid_by']:
                    balances[friend] -= split_amount
                    balances[expense['paid_by']] += split_amount
        
        return balances
    
    def display_balances(self):
        balances = self.calculate_balances()
        for friend, balance in balances.items():
            if balance > 0:
                print(f"{friend} should receive {balance:.2f}")
            elif balance < 0:
                print(f"{friend} owes {-balance:.2f}")
            else:
                print(f"{friend} is settled up")

a = ExpenseSharingApp()    
while True:
    print("\nOptions:")
    print("1. Add a friend")
    print("2. Add an expense")
    print("3. Show balances")
    print("4. Exit")   
    ch = input("Choose an option: ")   
    if ch == '1':
        friend_name = input("Enter friend's name: ")
        a.add_friend(friend_name)
    elif ch == '2':
        description = input("ENTER THE PURPOSE OF THE MONEY PAID: ")
        amount = float(input("ENTER THE AMOUNT PAID:"))
        paid_by = input("ENTER THE FRIEND WHO PAID IT:")
        split_between = input("ENTER THE FRIENDS TO BE SPLIT AMONG THE FRIENDS:").split(',')
        split_between = [friend.strip() for friend in split_between]
        a.add_expense(description, amount, paid_by, split_between)
    elif ch == '3':
        a.display_balances()
    elif ch == '4':
        break
    else:
        print("Invalid choice")
