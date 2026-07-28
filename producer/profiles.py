from common.models import UserProfile

USERS = [
    UserProfile(
    user_id="U001",
    age=25,
    occupation="Software Engineer",
    city="Pune",
    state="Maharashtra",
    monthly_income=90000,
    average_transaction=900,
    transaction_std_dev=200,
    max_normal_transaction=8000,
    preferred_start_hour=8,
    preferred_end_hour=23,
    device_id="DEV001",
    device_type="Samsung Galaxy S24",
    operating_system="Android",
    network_provider="Jio",
    preferred_merchants=[
        ("Amazon", "E-commerce"),
        ("Swiggy", "Food Delivery"),
        ("Uber", "Transport"),
        ("Netflix", "Entertainment"),
        ("Zepto", "Groceries")
    ]
                    ),

    UserProfile(
    user_id="U002",
    age=21,
    occupation="College Student",
    city="Mumbai",
    state="Maharashtra",
    monthly_income=15000,
    average_transaction=300,
    transaction_std_dev=100,
    max_normal_transaction=2500,
    preferred_start_hour=9,
    preferred_end_hour=23,
    device_id="DEV002",
    device_type="Redmi Note 13",
    operating_system="Android",
    network_provider="Airtel",
    preferred_merchants=[
        ("Swiggy", "Food Delivery"),
        ("Blinkit", "Groceries"),
        ("BookMyShow", "Entertainment"),
        ("Amazon", "E-commerce"),
        ("Spotify", "Entertainment")
    ]
        ),    

    UserProfile(
    user_id="U003",
    age=25,
    occupation="MBA Student",
    city="Thiruvananthapuram",
    state="Kerala",
    monthly_income=12000,
    average_transaction=350,
    transaction_std_dev=120,
    max_normal_transaction=3000,
    preferred_start_hour=7,
    preferred_end_hour=23,
    device_id="DEV003",
    device_type="Nothing Phone 2",
    operating_system="Android",
    network_provider="Jio",
    preferred_merchants=[
        ("Amazon", "E-commerce"),
        ("Swiggy", "Food Delivery"),
        ("IRCTC", "Travel"),
        ("BookMyShow", "Entertainment"),
        ("Zepto", "Groceries")
    ]
),    

    UserProfile(
    user_id="U004",
    age=24,
    occupation="Graphic Designer",
    city="Kochi",
    state="Kerala",
    monthly_income=45000,
    average_transaction=650,
    transaction_std_dev=180,
    max_normal_transaction=5000,
    preferred_start_hour=8,
    preferred_end_hour=22,
    device_id="DEV004",
    device_type="Nothing Phone 3",
    operating_system="Android",
    network_provider="Vi",
    preferred_merchants=[
        ("Myntra", "Fashion"),
        ("Amazon", "E-commerce"),
        ("Swiggy", "Food Delivery"),
        ("Spotify", "Entertainment"),
        ("Uber", "Transport")
    ]
),  

    UserProfile(
    user_id="U005",
    age=24,
    occupation="Business Owner",
    city="Patna",
    state="Bihar",
    monthly_income=50000,
    average_transaction=700,
    transaction_std_dev=250,
    max_normal_transaction=6000,
    preferred_start_hour=6,
    preferred_end_hour=23,
    device_id="DEV005",
    device_type="Samsung Galaxy S25",
    operating_system="Android",
    network_provider="Jio",
    preferred_merchants=[
        ("Amazon", "E-commerce"),
        ("Indian Oil", "Fuel"),
        ("HP Fuel", "Fuel"),
        ("LIC", "Insurance"),
        ("MakeMyTrip", "Travel")
    ]
), 

    UserProfile(
    user_id="U006",
    age=24,
    occupation="College Student",
    city="Mumbai",
    state="Maharashtra",
    monthly_income=10000,
    average_transaction=250,
    transaction_std_dev=80,
    max_normal_transaction=1800,
    preferred_start_hour=8,
    preferred_end_hour=23,
    device_id="DEV006",
    device_type="ASUS ROG Phone",
    operating_system="Android",
    network_provider="Jio",
    preferred_merchants=[
        ("Blinkit", "Groceries"),
        ("Swiggy", "Food Delivery"),
        ("Steam", "Gaming"),
        ("Amazon", "E-commerce"),
        ("Rapido", "Transport")
    ]
),   
    UserProfile(
    user_id="U007",
    age=29,
    occupation="Doctor",
    city="Bengaluru",
    state="Karnataka",
    monthly_income=180000,
    average_transaction=1800,
    transaction_std_dev=600,
    max_normal_transaction=20000,
    preferred_start_hour=7,
    preferred_end_hour=22,
    device_id="DEV007",
    device_type="iPhone 15",
    operating_system="iOS",
    network_provider="Jio",
    preferred_merchants=[
        ("Apollo Pharmacy", "Healthcare"),
        ("Uber", "Transport"),
        ("Amazon", "E-commerce"),
        ("MakeMyTrip", "Travel"),
        ("Swiggy", "Food Delivery")
    ]
),  
    UserProfile(
    user_id="U008",
    age=34,
    occupation="Teacher",
    city="Nagpur",
    state="Maharashtra",
    monthly_income=55000,
    average_transaction=700,
    transaction_std_dev=220,
    max_normal_transaction=7000,
    preferred_start_hour=6,
    preferred_end_hour=21,
    device_id="DEV008",
    device_type="Moto Edge 50",
    operating_system="Android",
    network_provider="Airtel",
    preferred_merchants=[
        ("Amazon", "E-commerce"),
        ("BigBasket", "Groceries"),
        ("IRCTC", "Travel"),
        ("BookMyShow", "Entertainment"),
        ("Flipkart", "E-commerce")
    ]
),  
    UserProfile(
    user_id="U009",
    age=40,
    occupation="Shop Owner",
    city="Ahmedabad",
    state="Gujarat",
    monthly_income=90000,
    average_transaction=1200,
    transaction_std_dev=400,
    max_normal_transaction=15000,
    preferred_start_hour=6,
    preferred_end_hour=23,
    device_id="DEV009",
    device_type="OnePlus 13",
    operating_system="Android",
    network_provider="Vi",
    preferred_merchants=[
        ("Amazon", "E-commerce"),
        ("Indian Oil", "Fuel"),
        ("HP Fuel", "Fuel"),
        ("LIC", "Insurance"),
        ("Flipkart", "E-commerce")
    ]
),

    UserProfile(
    user_id="U010",
    age=27,
    occupation="Chartered Accountant",
    city="Delhi",
    state="Delhi",
    monthly_income=140000,
    average_transaction=1500,
    transaction_std_dev=500,
    max_normal_transaction=18000,
    preferred_start_hour=8,
    preferred_end_hour=22,
    device_id="DEV010",
    device_type="Samsung Galaxy S25",
    operating_system="Android",
    network_provider="Jio",
    preferred_merchants=[
        ("Amazon", "E-commerce"),
        ("Uber", "Transport"),
        ("IRCTC", "Travel"),
        ("LIC", "Insurance"),
        ("Swiggy", "Food Delivery")
    ]
),  
    UserProfile(
    user_id="U010",
    age=27,
    occupation="Chartered Accountant",
    city="Delhi",
    state="Delhi",
    monthly_income=140000,
    average_transaction=1500,
    transaction_std_dev=500,
    max_normal_transaction=18000,
    preferred_start_hour=8,
    preferred_end_hour=22,
    device_id="DEV010",
    device_type="Samsung Galaxy S25",
    operating_system="Android",
    network_provider="Jio",
    preferred_merchants=[
        ("Amazon", "E-commerce"),
        ("Uber", "Transport"),
        ("IRCTC", "Travel"),
        ("LIC", "Insurance"),
        ("Swiggy", "Food Delivery")
    ]
),
    UserProfile(
    user_id="U011",
    age=36,
    occupation="Farmer",
    city="Nashik",
    state="Maharashtra",
    monthly_income=35000,
    average_transaction=450,
    transaction_std_dev=150,
    max_normal_transaction=4500,
    preferred_start_hour=5,
    preferred_end_hour=20,
    device_id="DEV011",
    device_type="Redmi Note 14",
    operating_system="Android",
    network_provider="BSNL",
    preferred_merchants=[
        ("BigBasket", "Groceries"),
        ("Amazon", "E-commerce"),
        ("Indian Oil", "Fuel"),
        ("Bharat Petroleum", "Fuel"),
        ("Jio Recharge", "Telecom")
    ]
),

    UserProfile(
        user_id="U012",
        age=31,
        occupation="Freelancer",
        city="Hyderabad",
        state="Telangana",
        monthly_income=85000,
        average_transaction=1000,
        transaction_std_dev=350,
        max_normal_transaction=12000,
        preferred_start_hour=9,
        preferred_end_hour=1,
        device_id="DEV012",
        device_type="Google Pixel 9",
        operating_system="Android",
        network_provider="Jio",
        preferred_merchants=[
            ("Amazon", "E-commerce"),
            ("Uber", "Transport"),
            ("Swiggy", "Food Delivery"),
            ("Spotify", "Entertainment"),
            ("MakeMyTrip", "Travel")
        ]
    ),

    UserProfile(
        user_id="U013",
        age=45,
        occupation="Government Officer",
        city="Lucknow",
        state="Uttar Pradesh",
        monthly_income=95000,
        average_transaction=1100,
        transaction_std_dev=350,
        max_normal_transaction=12000,
        preferred_start_hour=8,
        preferred_end_hour=21,
        device_id="DEV013",
        device_type="Samsung Galaxy A56",
        operating_system="Android",
        network_provider="Airtel",
        preferred_merchants=[
            ("Amazon", "E-commerce"),
            ("IRCTC", "Travel"),
            ("LIC", "Insurance"),
            ("BigBasket", "Groceries"),
            ("Uber", "Transport")
        ]
    ),

    UserProfile(
        user_id="U014",
        age=22,
        occupation="College Student",
        city="Chennai",
        state="Tamil Nadu",
        monthly_income=12000,
        average_transaction=250,
        transaction_std_dev=80,
        max_normal_transaction=1800,
        preferred_start_hour=9,
        preferred_end_hour=23,
        device_id="DEV014",
        device_type="Realme GT 7",
        operating_system="Android",
        network_provider="Jio",
        preferred_merchants=[
            ("Swiggy", "Food Delivery"),
            ("BookMyShow", "Entertainment"),
            ("Amazon", "E-commerce"),
            ("Rapido", "Transport"),
            ("Blinkit", "Groceries")
        ]
    ),

    UserProfile(
        user_id="U015",
        age=38,
        occupation="Lawyer",
        city="Kolkata",
        state="West Bengal",
        monthly_income=160000,
        average_transaction=1700,
        transaction_std_dev=500,
        max_normal_transaction=20000,
        preferred_start_hour=8,
        preferred_end_hour=22,
        device_id="DEV015",
        device_type="iPhone 14",
        operating_system="iOS",
        network_provider="Vi",
        preferred_merchants=[
            ("Amazon", "E-commerce"),
            ("Uber", "Transport"),
            ("MakeMyTrip", "Travel"),
            ("LIC", "Insurance"),
            ("Swiggy", "Food Delivery")
        ]
    ),

    UserProfile(
        user_id="U016",
        age=42,
        occupation="Sales Manager",
        city="Jaipur",
        state="Rajasthan",
        monthly_income=85000,
        average_transaction=950,
        transaction_std_dev=300,
        max_normal_transaction=10000,
        preferred_start_hour=7,
        preferred_end_hour=22,
        device_id="DEV016",
        device_type="OnePlus Nord 5",
        operating_system="Android",
        network_provider="Airtel",
        preferred_merchants=[
            ("Amazon", "E-commerce"),
            ("Flipkart", "E-commerce"),
            ("Uber", "Transport"),
            ("Indian Oil", "Fuel"),
            ("Swiggy", "Food Delivery")
        ]
    ),

    UserProfile(
        user_id="U017",
        age=26,
        occupation="Data Analyst",
        city="Pune",
        state="Maharashtra",
        monthly_income=70000,
        average_transaction=850,
        transaction_std_dev=250,
        max_normal_transaction=9000,
        preferred_start_hour=8,
        preferred_end_hour=23,
        device_id="DEV017",
        device_type="Nothing Phone 3",
        operating_system="Android",
        network_provider="Jio",
        preferred_merchants=[
            ("Amazon", "E-commerce"),
            ("Zepto", "Groceries"),
            ("Uber", "Transport"),
            ("Netflix", "Entertainment"),
            ("Swiggy", "Food Delivery")
        ]
    ),

    UserProfile(
        user_id="U018",
        age=50,
        occupation="Business Owner",
        city="Surat",
        state="Gujarat",
        monthly_income=220000,
        average_transaction=3000,
        transaction_std_dev=1000,
        max_normal_transaction=40000,
        preferred_start_hour=6,
        preferred_end_hour=23,
        device_id="DEV018",
        device_type="iPhone 16 Pro",
        operating_system="iOS",
        network_provider="Jio",
        preferred_merchants=[
            ("Amazon", "E-commerce"),
            ("MakeMyTrip", "Travel"),
            ("Indian Oil", "Fuel"),
            ("LIC", "Insurance"),
            ("Taj Hotels", "Hospitality")
        ]
    ),

    UserProfile(
        user_id="U019",
        age=28,
        occupation="Mechanical Engineer",
        city="Indore",
        state="Madhya Pradesh",
        monthly_income=65000,
        average_transaction=750,
        transaction_std_dev=250,
        max_normal_transaction=8000,
        preferred_start_hour=8,
        preferred_end_hour=22,
        device_id="DEV019",
        device_type="Samsung Galaxy S24 FE",
        operating_system="Android",
        network_provider="Vi",
        preferred_merchants=[
            ("Amazon", "E-commerce"),
            ("Uber", "Transport"),
            ("Blinkit", "Groceries"),
            ("BookMyShow", "Entertainment"),
            ("Indian Oil", "Fuel")
        ]
    ),

    UserProfile(
        user_id="U020",
        age=30,
        occupation="Nurse",
        city="Kochi",
        state="Kerala",
        monthly_income=50000,
        average_transaction=600,
        transaction_std_dev=180,
        max_normal_transaction=6000,
        preferred_start_hour=6,
        preferred_end_hour=22,
        device_id="DEV020",
        device_type="Vivo V50",
        operating_system="Android",
        network_provider="Jio",
        preferred_merchants=[
            ("Apollo Pharmacy", "Healthcare"),
            ("Amazon", "E-commerce"),
            ("Uber", "Transport"),
            ("BigBasket", "Groceries"),
            ("Swiggy", "Food Delivery")
        ]
    ),
    
        UserProfile(
        user_id="U021",
        age=39,
        occupation="Police Officer",
        city="Bhopal",
        state="Madhya Pradesh",
        monthly_income=80000,
        average_transaction=900,
        transaction_std_dev=250,
        max_normal_transaction=9000,
        preferred_start_hour=5,
        preferred_end_hour=21,
        device_id="DEV021",
        device_type="Samsung Galaxy S24",
        operating_system="Android",
        network_provider="Jio",
        preferred_merchants=[
            ("Indian Oil", "Fuel"),
            ("Amazon", "E-commerce"),
            ("Swiggy", "Food Delivery"),
            ("IRCTC", "Travel"),
            ("Apollo Pharmacy", "Healthcare")
        ]
    ),

    UserProfile(
        user_id="U022",
        age=41,
        occupation="Bank Manager",
        city="Chandigarh",
        state="Punjab",
        monthly_income=125000,
        average_transaction=1500,
        transaction_std_dev=450,
        max_normal_transaction=18000,
        preferred_start_hour=8,
        preferred_end_hour=21,
        device_id="DEV022",
        device_type="iPhone 15 Pro",
        operating_system="iOS",
        network_provider="Airtel",
        preferred_merchants=[
            ("Amazon", "E-commerce"),
            ("Uber", "Transport"),
            ("LIC", "Insurance"),
            ("MakeMyTrip", "Travel"),
            ("Swiggy", "Food Delivery")
        ]
    ),

    UserProfile(
        user_id="U023",
        age=32,
        occupation="Civil Engineer",
        city="Bhubaneswar",
        state="Odisha",
        monthly_income=72000,
        average_transaction=850,
        transaction_std_dev=250,
        max_normal_transaction=8500,
        preferred_start_hour=7,
        preferred_end_hour=22,
        device_id="DEV023",
        device_type="Google Pixel 8a",
        operating_system="Android",
        network_provider="Jio",
        preferred_merchants=[
            ("Amazon", "E-commerce"),
            ("Uber", "Transport"),
            ("Indian Oil", "Fuel"),
            ("BigBasket", "Groceries"),
            ("BookMyShow", "Entertainment")
        ]
    ),

    UserProfile(
        user_id="U024",
        age=28,
        occupation="Pharmacist",
        city="Visakhapatnam",
        state="Andhra Pradesh",
        monthly_income=65000,
        average_transaction=750,
        transaction_std_dev=220,
        max_normal_transaction=7500,
        preferred_start_hour=8,
        preferred_end_hour=22,
        device_id="DEV024",
        device_type="Vivo X200",
        operating_system="Android",
        network_provider="Airtel",
        preferred_merchants=[
            ("Apollo Pharmacy", "Healthcare"),
            ("Amazon", "E-commerce"),
            ("Swiggy", "Food Delivery"),
            ("Uber", "Transport"),
            ("PharmEasy", "Healthcare")
        ]
    ),

    UserProfile(
        user_id="U025",
        age=46,
        occupation="Restaurant Owner",
        city="Amritsar",
        state="Punjab",
        monthly_income=140000,
        average_transaction=1800,
        transaction_std_dev=550,
        max_normal_transaction=20000,
        preferred_start_hour=6,
        preferred_end_hour=23,
        device_id="DEV025",
        device_type="Samsung Galaxy Z Fold 7",
        operating_system="Android",
        network_provider="Jio",
        preferred_merchants=[
            ("Amazon", "E-commerce"),
            ("Indian Oil", "Fuel"),
            ("MakeMyTrip", "Travel"),
            ("Swiggy", "Food Delivery"),
            ("LIC", "Insurance")
        ]
    ),

    UserProfile(
        user_id="U026",
        age=35,
        occupation="Homemaker",
        city="Kanpur",
        state="Uttar Pradesh",
        monthly_income=30000,
        average_transaction=450,
        transaction_std_dev=150,
        max_normal_transaction=4000,
        preferred_start_hour=8,
        preferred_end_hour=21,
        device_id="DEV026",
        device_type="Redmi Note 14",
        operating_system="Android",
        network_provider="BSNL",
        preferred_merchants=[
            ("BigBasket", "Groceries"),
            ("Zepto", "Groceries"),
            ("Amazon", "E-commerce"),
            ("Flipkart", "E-commerce"),
            ("Apollo Pharmacy", "Healthcare")
        ]
    ),

    UserProfile(
        user_id="U027",
        age=58,
        occupation="Retired Government Employee",
        city="Coimbatore",
        state="Tamil Nadu",
        monthly_income=45000,
        average_transaction=500,
        transaction_std_dev=180,
        max_normal_transaction=5000,
        preferred_start_hour=6,
        preferred_end_hour=20,
        device_id="DEV027",
        device_type="Samsung Galaxy A35",
        operating_system="Android",
        network_provider="BSNL",
        preferred_merchants=[
            ("Apollo Pharmacy", "Healthcare"),
            ("LIC", "Insurance"),
            ("BigBasket", "Groceries"),
            ("Amazon", "E-commerce"),
            ("IRCTC", "Travel")
        ]
    ),

    UserProfile(
        user_id="U028",
        age=29,
        occupation="Startup Founder",
        city="Gurugram",
        state="Haryana",
        monthly_income=250000,
        average_transaction=2800,
        transaction_std_dev=900,
        max_normal_transaction=35000,
        preferred_start_hour=8,
        preferred_end_hour=1,
        device_id="DEV028",
        device_type="iPhone 16 Pro",
        operating_system="iOS",
        network_provider="Jio",
        preferred_merchants=[
            ("Amazon", "E-commerce"),
            ("Uber", "Transport"),
            ("MakeMyTrip", "Travel"),
            ("Swiggy", "Food Delivery"),
            ("Netflix", "Entertainment")
        ]
    ),

    UserProfile(
        user_id="U029",
        age=35,
        occupation="Marketing Executive",
        city="Noida",
        state="Uttar Pradesh",
        monthly_income=78000,
        average_transaction=950,
        transaction_std_dev=280,
        max_normal_transaction=9500,
        preferred_start_hour=8,
        preferred_end_hour=22,
        device_id="DEV029",
        device_type="OnePlus 12",
        operating_system="Android",
        network_provider="Airtel",
        preferred_merchants=[
            ("Amazon", "E-commerce"),
            ("Flipkart", "E-commerce"),
            ("Uber", "Transport"),
            ("Swiggy", "Food Delivery"),
            ("BookMyShow", "Entertainment")
        ]
    ),

    UserProfile(
        user_id="U030",
        age=30,
        occupation="Chartered Accountant",
        city="Mumbai",
        state="Maharashtra",
        monthly_income=145000,
        average_transaction=1600,
        transaction_std_dev=500,
        max_normal_transaction=18000,
        preferred_start_hour=8,
        preferred_end_hour=22,
        device_id="DEV030",
        device_type="iPhone 15",
        operating_system="iOS",
        network_provider="Vi",
        preferred_merchants=[
            ("Amazon", "E-commerce"),
            ("LIC", "Insurance"),
            ("Uber", "Transport"),
            ("IRCTC", "Travel"),
            ("Swiggy", "Food Delivery")
        ]
    )
]