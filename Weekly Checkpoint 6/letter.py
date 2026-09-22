def main():
    friends = ["Mario","Luigi","Daisy","Yoshi","Toad","Princess Peach","Bowser"]
    for reciever in friends:
        if reciever != "Princess Peach":
            print(f"""
+~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
       Dear {reciever},

       You are cordially invited to a ball at
       Peach's Castle this evening, 7:00 PM.

       Sincerely,
       {friends[5]}
+~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
        """)




if __name__=="__main__":
    main()
