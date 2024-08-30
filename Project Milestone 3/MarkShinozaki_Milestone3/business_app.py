import psycopg2
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QComboBox, QListWidget, QTableWidget, QTableWidgetItem, QLineEdit, QLabel, QGridLayout, QGroupBox

class BusinessApp(QWidget):
    def __init__(self):
        super().__init__()

        self.conn = psycopg2.connect(
            dbname="milestone1DB",
            user="postgres",
            password="jn&!!8tCK6H",
            host="localhost"
        )
        self.cursor = self.conn.cursor()

        self.initUI()
        self.selected_zipcode = None  # Track the selected zipcode

    def initUI(self):
        mainLayout = QVBoxLayout()
        grid = QGridLayout()

        # Location Selection
        locationGroup = QGroupBox("Select Location")
        locationLayout = QVBoxLayout()

        self.zipcodeInput = QLineEdit()
        self.zipcodeInput.setPlaceholderText("Enter Zipcode...")
        self.zipcodeInput.returnPressed.connect(self.onZipcodeSearch)
        locationLayout.addWidget(QLabel("Enter Zipcode:"))
        locationLayout.addWidget(self.zipcodeInput)
        
        locationLayout.addWidget(QLabel("OR"))

        self.stateComboBox = QComboBox()
        self.stateComboBox.activated[str].connect(self.onStateChanged)
        locationLayout.addWidget(QLabel("Select State:"))
        locationLayout.addWidget(self.stateComboBox)
        
        self.cityComboBox = QComboBox()
        self.cityComboBox.activated[str].connect(self.onCityChanged)
        locationLayout.addWidget(QLabel("Select City:"))
        locationLayout.addWidget(self.cityComboBox)
        
        self.zipcodeList = QListWidget()
        self.zipcodeList.clicked.connect(self.onZipcodeSelected)
        locationLayout.addWidget(QLabel("Select Zipcode:"))
        locationLayout.addWidget(self.zipcodeList)
        
        locationGroup.setLayout(locationLayout)
        locationGroup.setStyleSheet("background-color: #FFEBEE;")
        grid.addWidget(locationGroup, 0, 0)

        # Zipcode Statistics
        statsGroup = QGroupBox("Zipcode Statistics")
        statsLayout = QVBoxLayout()
        
        self.numBusinessesLabel = QLabel("# of Businesses: N/A")
        self.totalPopulationLabel = QLabel("Total Population: N/A")
        self.avgIncomeLabel = QLabel("Average Income: N/A")
        
        statsLayout.addWidget(self.numBusinessesLabel)
        statsLayout.addWidget(self.totalPopulationLabel)
        statsLayout.addWidget(self.avgIncomeLabel)
        
        statsGroup.setLayout(statsLayout)
        statsGroup.setStyleSheet("background-color: #E8F5E9;")
        grid.addWidget(statsGroup, 0, 1)

        # Top Categories
        categoriesGroup = QGroupBox("Top Categories")
        categoriesLayout = QVBoxLayout()
        
        self.categoriesTable = QTableWidget()
        categoriesLayout.addWidget(self.categoriesTable)
        
        categoriesGroup.setLayout(categoriesLayout)
        categoriesGroup.setStyleSheet("background-color: #FFFDE7;")
        grid.addWidget(categoriesGroup, 0, 2)

        mainLayout.addLayout(grid)

        # Filter on Categories
        filterGroup = QGroupBox("Filter on Categories")
        filterLayout = QVBoxLayout()
        
        self.categoryComboBox = QComboBox()
        self.categoryComboBox.currentIndexChanged.connect(self.onCategoryChanged)
        filterLayout.addWidget(QLabel("Select Category:"))
        filterLayout.addWidget(self.categoryComboBox)
        
        filterGroup.setLayout(filterLayout)
        filterGroup.setStyleSheet("background-color: #E3F2FD;")
        mainLayout.addWidget(filterGroup)

        # Business Details Table
        self.businessTable = QTableWidget()
        mainLayout.addWidget(self.businessTable)

        # Popular and Successful Businesses
        bottomLayout = QHBoxLayout()
        
        self.popularBusinessesTable = QTableWidget()
        popularGroup = QGroupBox("Popular Businesses (in zipcode)")
        popularLayout = QVBoxLayout()
        popularLayout.addWidget(self.popularBusinessesTable)
        popularGroup.setLayout(popularLayout)
        popularGroup.setStyleSheet("background-color: #F3E5F5;")
        bottomLayout.addWidget(popularGroup)
        
        self.successfulBusinessesTable = QTableWidget()
        successfulGroup = QGroupBox("Successful Businesses (in zipcode)")
        successfulLayout = QVBoxLayout()
        successfulLayout.addWidget(self.successfulBusinessesTable)
        successfulGroup.setLayout(successfulLayout)
        successfulGroup.setStyleSheet("background-color: #E0F2F1;")
        bottomLayout.addWidget(successfulGroup)
        
        # Best Business
        self.bestBusinessTable = QTableWidget()
        bestGroup = QGroupBox("Best Business (in zipcode)")
        bestLayout = QVBoxLayout()
        bestLayout.addWidget(self.bestBusinessTable)
        bestGroup.setLayout(bestLayout)
        bestGroup.setStyleSheet("background-color: #FFF3E0;")
        bottomLayout.addWidget(bestGroup)

        mainLayout.addLayout(bottomLayout)

        self.setLayout(mainLayout)

        self.loadStates()

    def loadStates(self):
        self.cursor.execute("SELECT DISTINCT state FROM business ORDER BY state;")
        states = self.cursor.fetchall()
        self.stateComboBox.addItem("Select State")
        for state in states:
            self.stateComboBox.addItem(state[0])

    def onStateChanged(self, state):
        self.cityComboBox.clear()
        self.cityComboBox.addItem("Select City")
        self.cursor.execute("SELECT DISTINCT city FROM business WHERE state=%s ORDER BY city;", (state,))
        cities = self.cursor.fetchall()
        for city in cities:
            self.cityComboBox.addItem(city[0])
        self.zipcodeList.clear()
        self.businessTable.clear()
        self.clearStatistics()
        self.categoryComboBox.clear()
        self.categoriesTable.clear()
        self.popularBusinessesTable.clear()
        self.successfulBusinessesTable.clear()
        self.bestBusinessTable.clear()
        self.selected_zipcode = None  # Reset selected zipcode

    def onCityChanged(self, city):
        self.zipcodeList.clear()
        state = self.stateComboBox.currentText()
        self.cursor.execute("SELECT DISTINCT zipcode FROM business WHERE city=%s AND state=%s ORDER BY zipcode;", (city, state))
        zipcodes = self.cursor.fetchall()
        for zipcode in zipcodes:
            self.zipcodeList.addItem(zipcode[0])
        self.businessTable.clear()
        self.clearStatistics()
        self.categoryComboBox.clear()
        self.categoriesTable.clear()
        self.popularBusinessesTable.clear()
        self.successfulBusinessesTable.clear()
        self.bestBusinessTable.clear()
        self.selected_zipcode = None  # Reset selected zipcode

    def onZipcodeSelected(self):
        selected_zipcode = self.zipcodeList.currentItem().text()
        if self.selected_zipcode != selected_zipcode:
            self.selected_zipcode = selected_zipcode
            self.updateAllData()
        else:
            self.clearStatistics()
            self.categoriesTable.clear()
            self.businessTable.clear()
            self.popularBusinessesTable.clear()
            self.successfulBusinessesTable.clear()
            self.bestBusinessTable.clear()

    def onZipcodeSearch(self):
        entered_zipcode = self.zipcodeInput.text()
        if not entered_zipcode.isdigit() or len(entered_zipcode) != 5:
            self.zipcodeInput.setText("")
            self.zipcodeInput.setPlaceholderText("Invalid Zipcode! Enter a 5-digit Zipcode.")
            return
        self.selected_zipcode = entered_zipcode
        self.stateComboBox.setCurrentIndex(0)
        self.cityComboBox.clear()
        self.zipcodeList.clear()
        self.updateAllData()

    def onCategoryChanged(self):
        self.updateCategoryData()

    def updateCategoryData(self):
        self.loadBusinesses()
        self.loadPopularBusinesses()
        self.loadSuccessfulBusinesses()
        self.loadBestBusiness()

    def updateAllData(self):
        self.loadZipcodeStats()
        self.loadTopCategories()
        self.updateCategoryData()

    def loadZipcodeStats(self):
        zipcode = self.selected_zipcode
        self.cursor.execute("""
            SELECT COUNT(business.*), SUM(zipcodedata.population), AVG(zipcodedata.meanincome)
            FROM business
            JOIN zipcodedata ON business.zipcode = zipcodedata.zipcode
            WHERE business.zipcode=%s;
        """, (zipcode,))
        stats = self.cursor.fetchone()
        self.numBusinessesLabel.setText(f"# of Businesses: {stats[0]}")
        self.totalPopulationLabel.setText(f"Total Population: {stats[1]}")
        self.avgIncomeLabel.setText(f"Average Income: {stats[2]}")

    def loadTopCategories(self):
        zipcode = self.selected_zipcode
        self.cursor.execute("""
            SELECT category, COUNT(*)
            FROM business, unnest(categories) AS category
            WHERE zipcode=%s
            GROUP BY category
            ORDER BY COUNT(*) DESC;
        """, (zipcode,))
        categories = self.cursor.fetchall()

        self.categoriesTable.setRowCount(len(categories))
        self.categoriesTable.setColumnCount(2)
        self.categoriesTable.setHorizontalHeaderLabels(["Category", "# of Businesses"])

        for i, category in enumerate(categories):
            self.categoriesTable.setItem(i, 0, QTableWidgetItem(category[0]))
            self.categoriesTable.setItem(i, 1, QTableWidgetItem(str(category[1])))

        self.categoryComboBox.clear()
        self.categoryComboBox.addItem("All Categories")
        for category in categories:
            self.categoryComboBox.addItem(category[0])

    def loadBusinesses(self):
        self.businessTable.clear()
        zipcode = self.selected_zipcode
        selected_category = self.categoryComboBox.currentText()

        query = """
            SELECT name, address, city, state, stars, reviewcount, numcheckins, businessacceptscreditcards, goodforkids, bikeparking, outdoorseating, 
                   restaurantspricerange2, restaurantsgoodforgroups, hastv, caters, wifi, restaurantsattire, restaurantsreservations, restaurantstableservice, 
                   restaurantstakeout, restaurantsdelivery, alcohol, noiselevel, goodformeal_breakfast, goodformeal_brunch, goodformeal_dessert, 
                   goodformeal_dinner, goodformeal_latenight, goodformeal_lunch, ambience_romantic, ambience_intimate, ambience_classy, 
                   ambience_hipster, ambience_divey, ambience_touristy, ambience_trendy, ambience_upscale, ambience_casual, businessparking_garage, 
                   businessparking_street, businessparking_validated, businessparking_lot, businessparking_valet, categories, hours 
            FROM business 
            WHERE zipcode=%s
        """
        params = [zipcode]

        if selected_category and selected_category != "All Categories":
            query += " AND %s = ANY(categories)"
            params.append(selected_category)

        query += " ORDER BY name;"
        self.cursor.execute(query, tuple(params))
        businesses = self.cursor.fetchall()

        headers = ["Name", "Address", "City", "State", "Stars", "Review Count", "Num Checkins", "Accepts Credit Cards", "Good for Kids", "Bike Parking", 
                   "Outdoor Seating", "Price Range", "Good for Groups", "Has TV", "Caters", "WiFi", "Attire", "Reservations", "Table Service", "Takeout", 
                   "Delivery", "Alcohol", "Noise Level", "Good for Breakfast", "Good for Brunch", "Good for Dessert", "Good for Dinner", 
                   "Good for Late Night", "Good for Lunch", "Ambience Romantic", "Ambience Intimate", "Ambience Classy", "Ambience Hipster", 
                   "Ambience Divey", "Ambience Touristy", "Ambience Trendy", "Ambience Upscale", "Ambience Casual", "Parking Garage", "Parking Street", 
                   "Parking Validated", "Parking Lot", "Parking Valet", "Categories", "Hours"]

        self.businessTable.setRowCount(len(businesses))
        self.businessTable.setColumnCount(len(headers))
        self.businessTable.setHorizontalHeaderLabels(headers)

        for i, business in enumerate(businesses):
            for j, value in enumerate(business):
                self.businessTable.setItem(i, j, QTableWidgetItem(str(value)))

    def loadPopularBusinesses(self):
        self.popularBusinessesTable.clear()
        zipcode = self.selected_zipcode
        selected_category = self.categoryComboBox.currentText()

        query = """
            SELECT b.name, b.address, b.city, b.state, b.numcheckins, COUNT(r.review_id) AS review_count,
                   (0.7 * b.numcheckins + 0.3 * COUNT(r.review_id)) AS popularity_score
            FROM business b
            LEFT JOIN reviewtable r ON b.business_id = r.business_id
            WHERE b.zipcode = %s
        """
        params = [zipcode]

        if selected_category and selected_category != "All Categories":
            query += " AND %s = ANY(b.categories)"
            params.append(selected_category)

        query += """
            GROUP BY b.business_id
            ORDER BY popularity_score DESC
            LIMIT 10;
        """
        self.cursor.execute(query, tuple(params))
        businesses = self.cursor.fetchall()

        headers = ["Name", "Address", "City", "State", "Num Checkins", "Review Count", "Popularity Score"]
        self.popularBusinessesTable.setRowCount(len(businesses))
        self.popularBusinessesTable.setColumnCount(len(headers))
        self.popularBusinessesTable.setHorizontalHeaderLabels(headers)

        self.popular_business_ids = set()
        for i, business in enumerate(businesses):
            self.popular_business_ids.add(business[0])  # Collect business IDs to exclude from successful businesses
            for j, value in enumerate(business):
                self.popularBusinessesTable.setItem(i, j, QTableWidgetItem(str(value)))

    def loadSuccessfulBusinesses(self):
        self.successfulBusinessesTable.clear()
        zipcode = self.selected_zipcode
        selected_category = self.categoryComboBox.currentText()

        query = """
            SELECT b.name, b.address, b.city, b.state, b.stars, MIN(r.date) AS start_date, ROUND(AVG(r.stars), 2) AS avg_rating,
                   (0.5 * (CURRENT_DATE - MIN(r.date)) + 0.5 * ROUND(AVG(r.stars), 2)) AS success_score
            FROM business b
            LEFT JOIN reviewtable r ON b.business_id = r.business_id
            WHERE b.zipcode = %s
        """
        params = [zipcode]

        if selected_category and selected_category != "All Categories":
            query += " AND %s = ANY(b.categories)"
            params.append(selected_category)

        query += """
            GROUP BY b.business_id
            ORDER BY success_score DESC
            LIMIT 10;
        """
        self.cursor.execute(query, tuple(params))
        businesses = self.cursor.fetchall()

        headers = ["Name", "Address", "City", "State", "Stars", "Start Date", "Avg Rating", "Success Score"]
        self.successfulBusinessesTable.setRowCount(len(businesses))
        self.successfulBusinessesTable.setColumnCount(len(headers))
        self.successfulBusinessesTable.setHorizontalHeaderLabels(headers)

        if len(businesses) == 0:  # If no successful businesses, fallback to popular businesses
            self.cursor.execute("""
                SELECT b.name, b.address, b.city, b.state, b.stars, MIN(r.date) AS start_date, ROUND(AVG(r.stars), 2) AS avg_rating,
                       (0.5 * (CURRENT_DATE - MIN(r.date)) + 0.5 * ROUND(AVG(r.stars), 2)) AS success_score
                FROM business b
                LEFT JOIN reviewtable r ON b.business_id = r.business_id
                WHERE b.zipcode = %s
                GROUP BY b.business_id
                ORDER BY popularity_score DESC
                LIMIT 1;
            """, tuple(params))
            fallback_business = self.cursor.fetchone()
            if fallback_business:
                self.successfulBusinessesTable.setRowCount(1)
                for j, value in enumerate(fallback_business):
                    self.successfulBusinessesTable.setItem(0, j, QTableWidgetItem(str(value)))
        else:
            row = 0
            for i, business in enumerate(businesses):
                if business[0] not in self.popular_business_ids:  # Exclude businesses already classified as popular
                    for j, value in enumerate(business):
                        self.successfulBusinessesTable.setItem(row, j, QTableWidgetItem(str(value)))
                    row += 1

    def loadBestBusiness(self):
        self.bestBusinessTable.clear()
        zipcode = self.selected_zipcode
        selected_category = self.categoryComboBox.currentText()

        query = """
            SELECT b.name, b.zipcode,
                   (0.7 * b.numcheckins + 0.3 * COUNT(r.review_id)) AS popularity_score,
                   (0.5 * (CURRENT_DATE - MIN(r.date)) + 0.5 * ROUND(AVG(r.stars), 2)) AS success_score
            FROM business b
            LEFT JOIN reviewtable r ON b.business_id = r.business_id
            WHERE b.zipcode = %s
        """
        params = [zipcode]

        if selected_category and selected_category != "All Categories":
            query += " AND %s = ANY(b.categories)"
            params.append(selected_category)

        query += """
            GROUP BY b.business_id
            HAVING (0.7 * b.numcheckins + 0.3 * COUNT(r.review_id)) > 0 AND (0.5 * (CURRENT_DATE - MIN(r.date)) + 0.5 * ROUND(AVG(r.stars), 2)) > 0
            ORDER BY popularity_score DESC, success_score DESC
            LIMIT 1;
        """
        self.cursor.execute(query, tuple(params))
        business = self.cursor.fetchone()

        headers = ["Name", "Zipcode", "Popularity Score", "Success Score"]
        self.bestBusinessTable.setRowCount(1)
        self.bestBusinessTable.setColumnCount(len(headers))
        self.bestBusinessTable.setHorizontalHeaderLabels(headers)

        if business:
            for j, value in enumerate(business):
                self.bestBusinessTable.setItem(0, j, QTableWidgetItem(str(value)))

    def clearStatistics(self):
        self.numBusinessesLabel.setText("# of Businesses: N/A")
        self.totalPopulationLabel.setText("Total Population: N/A")
        self.avgIncomeLabel.setText("Average Income: N/A")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = BusinessApp()
    ex.setWindowTitle('CptS 451 - Business Analytics by Mark S')
    ex.show()
    sys.exit(app.exec_())
