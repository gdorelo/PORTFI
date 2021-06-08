<h1 align="center">
PORTFI
Your portfolio and risk analysis software._
</h1>

Portfi provides a detailed analisis on a customizable stock portfolio provided by the user. Our application offers some of the most relevant tools that high price applications offer while being free to use and maintaining a nice user-friendly experience.

### Inspiration

More and more people are everyday thinking of a way to live with passive income. Investing in big companies has always been a low-risk go to strategy for this, but the problem we found is that the tools to make do this are very expensive and don't even provide user-friendly UIs, which makes investing in these markets a very discouraging experience. Our goal is to be able to provide a free tool that everybody can use to start building a portfolio with a decent investment strategy.

### Features
- Ability to add main equities, stock, and ETF, traded in NYSE and NASDAQ markets.
- Historic analysis of the stocks provided by the user.
- Comparison of portfolios against main ratios and market benchmarks. 
- Visualization of traditional metrics such as risk, correlations, volatility, max drawdown, return, sharp (efficiency), and all in different time frames.
- User friendly graphic representations of these metrics and actives.
- Portfolio optimization according to the investor profile.
- Analysis with tools such as positioning and valuation of shares (P/E).

### Technology

PORTFI uses a number of open source projects to work properly:

- [Python](https://www.python.org/) - interpreted high-level general-purpose programming language.
- [Flask](https://flask.palletsprojects.com/en/2.0.x/) - micro web framework written in Python.
- [ReactJS](https://reactjs.org/) - open-source front-end JavaScript library. 
- [Material UI](https://material-ui.com/) - react component library built by Google.
- [MySQL](https://www.mysql.com/) - open-source relational database management system.
- [pandas](https://pandas.pydata.org/) - open source data analysis and manipulation tool.



### Installation

PORTFI requires several technologies to be installed in order to run, this is why we recommend you to use it on our deployed live version here.

If you still would like to run it for yourself, you can run a script with the commands below:

- Install the necessary software:

``` 
#!/bin/bash
sudo apt-get update
sudo apt-get install emacs -y
sudo apt-get install git -y
sudo apt-get install python3 -y
sudo apt install python3-pip -y
sudo pip3 install Flask
echo 'deb http://repo.mysql.com/apt/ubuntu/ trusty mysql-5.7-dmr' | sudo tee -a /etc/apt/sources.list
sudo apt-get install mysql-server-5.7 -y
sudo apt-get install python3-dev -y
sudo apt-get install libmysqlclient-dev -y
sudo apt-get install zlib1g-dev -y
sudo pip3 install mysqlclient==1.3.10 
sudo pip3 install SQLAlchemy==1.2.5
sudo pip3 install pathlib2
sudo apt-get install -y python3-lxml -y
sudo pip3 install flask_cors
sudo pip3 install flasgger
sudo apt-get install python3-pandas -y
sudo pip3 install pandas-datareader
sudo curl -fsSL https://deb.nodesource.com/setup_16.x | sudo -E bash -
sudo apt-get install -y nodejs
```

After all of the above dependancies are installed:
- Clone this repository ```git clone https://github.com/gdorelo/PORTFI.git ```
- ``` cd``` into the PORTFI folder
- Run ```npm install``` to install React dependancies
- Export the Flask global variable ```export FLASK_APP=api.web.app```
- Run the back-end ```flask run```
- Run the front-end ```npm start```

NPM should automatically open a new browser page on localhost:3000/ where PORTFI is running. If this page isn't opened, just copy and paste localhost:3000/ into your browser and press enter.

### Authors
**Gianluca Dorelo** https://github.com/gdorelo
**Martin Saavedra** https://github.com/martinmsaavedra/
**Matias Zappino** https://github.com/matiaszappino/

### License

MIT

**It's free!**



