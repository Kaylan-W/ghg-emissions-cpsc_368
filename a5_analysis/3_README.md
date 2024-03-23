The SQL file can be accessed from Michal Sanocki’s Oracle account. Prior to use, please log into the CS remote server. Login information is included below:

dsn = oracledb.makedsn("localhost", 1522, service_name="stu")
connection = oracledb.connect(user="ora_msan99", password="a85263259", dsn=dsn)

When developing our linear regression model, we applied one-hot encoding to create categorical variables and split the relevant dataset into 70-30 training and testing data. We then used the Ridge linear model and tuned hyperparameter alpha.

Our linear model to predict greenhouse gas emissions by households uses province and year as predictors. Our linear model for durable and non-durable manufacturing industries uses province, year, and durable as predictors. Durable is a binary variable classifying industries as durable/non-durable manufacturers.
