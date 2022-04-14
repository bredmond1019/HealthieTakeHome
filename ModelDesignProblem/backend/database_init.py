'''
This function is used to initialize the database with a bunch of data. 
If you are using the SQLite database provided in my config, 
This function will provide all the data to the database. 

If you connect your own PostgreSQL Database to the application, 
You will need to either 

1) run the application once to initilialize the data, 
then comment out the IF statement in the __init__.py file
In the BACKEND directory. 

2) Comment out that IF statement before running and 
create your own data. 

*** If you use your own database and do not comment out the code
after the first run, the application will try to create all the 
data again and their will be an error. 
'''




def create_database_entries(db):
    from .models import Provider, Client, Plan, ClientProvider, JournalEntry
    
    db.create_all()

    # Providers
    chiro = Provider(name="Chiro", email="chiro@gmail.com")
    doctor = Provider(name="Doctor", email="doctor@gmail.com")
    nurse = Provider(name="Nurse", email="nurse@gmail.com")
    physical_therapist = Provider(name='Physical Therapist', email="physical.therapy@gmail.com")


    # Clients
    brandon = Client(name="Brandon", email="bredmond1019@gmail.com")
    felipe = Client(name="Felipe", email="felipe@gmail.com")
    lee = Client(name="Lee", email="lee@gmail.com")
    david = Client(name="David", email="david@gmail.com")


    # Plans
    basic = Plan(plan_type="basic")
    premium = Plan(plan_type="premium")


    # Journal Entry
    b_entry = JournalEntry(entry="Brandon loves Healthie!")
    b_entry2 = JournalEntry(entry="Brandon loves to rock climb")
    brandon.journal_entries.extend([b_entry, b_entry2])

    f_entry = JournalEntry(entry="Felipe loves Brazil!")
    felipe.journal_entries.append(f_entry)

    l_entry = JournalEntry(entry="Lee loves his dog Jude!")
    lee.journal_entries.append(l_entry)

    d_entry = JournalEntry(entry="David loves code!")
    david.journal_entries.append(d_entry)
    

    # Association Table
    assoc1 = ClientProvider(client=brandon, provider=chiro, plan=basic)
    assoc2 = ClientProvider(client=brandon, provider=physical_therapist, plan=basic)
    assoc3 = ClientProvider(client=brandon, provider=doctor, plan=basic)

    assoc4 = ClientProvider(client=felipe, provider=chiro, plan=basic)
    assoc5 = ClientProvider(client=felipe, provider=doctor, plan=premium)
    assoc6 = ClientProvider(client=felipe, provider=nurse, plan=basic)

    assoc7 = ClientProvider(client=lee, provider=doctor, plan=premium)
    assoc8 = ClientProvider(client=lee, provider=nurse, plan=premium)
    assoc9 = ClientProvider(client=lee, provider=physical_therapist, plan=premium)

    assoc10 = ClientProvider(client=david, provider=physical_therapist, plan=basic)
    assoc11 = ClientProvider(client=david, provider=chiro, plan=premium)
    assoc12 = ClientProvider(client=david, provider=nurse, plan=basic)
    


    db.session.add_all([
        chiro, 
        doctor, 
        nurse, 
        physical_therapist,
        brandon,
        felipe, 
        lee, 
        david,
        basic, 
        premium, 
        b_entry,
        assoc1,
        assoc2,
        assoc3,
        assoc4,
        assoc5,
        assoc6,
        assoc7,
        assoc8,
        assoc9,
        assoc10,
        assoc11,
        assoc12,
        ])

    db.session.commit()






    # entry2 = JournalEntry(entry="This is test entry number 2")
    # brandon.journal_entries.append(entry2)
    # db.session.add(entry2)
    # db.session.commit()


