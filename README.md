# **Python Containerized Covid Api**

This project is an API program that serve information about Corona Virus Desease in Indonesia.

---
## **Usage**
* ### **Local**
    1. Clone  
        `git clone https://github.com/Croazt/containerized-covid-api`
    2. Install required python module  
        `pip install -r requirements/requirements.txt`
    3. Run  
        `python app.py` 
    4. Access endpoint  
        `http://127.0.0.1:8080`  
        <br>
* ### **Docker**
    1. Pull image  
        `docker pull muhammadfachry/containerized-covid-api-id`
    2. Run container  
        `docker run -p 8080:8080 --[your container name] covid-api  muhammadfachry/containerized-covid-api-id`
    3. Access endpoint  
        `http://localhost:8080`
---
## **Docs**
**Access** :  
1. ` http://<host>:<port>/openapi.json`  
2. ` http://<host>:<port>/docs`  
3. ` http://<host>:<port>/redoc`  
---
## **Routes**
* `[GET] http://<host>:<port>/`   
    Provide general covid case summary in Indonesia

* `[GET] http://<host>:<port>/yearly`  
    Provide yearly cumulative data of total covid cases. 
    >**Query Params :**
    > - since : \<year>    
     Control since when [year] the data will be returned. By default is the year since first case detected.  
    ***example**: ?since=2021*
    >- upto : \<year>   
     A parameter that control up to when [year] the data will be returned. By default is up to current year.  
    ***example**: ?upto=2021*
* `[GET] http://<host>:<port>/yearly/<year>`  
    Provide data of total covid cases at exact given \<year>. 
* `[GET] http://<host>:<port>/monthly`  
    Provide monthly cumulative data of total covid cases. 
    >**Query Params :**
    > - since : \<year>.\<month>    
     A parameter that control since when [year, month] the data will be returned. By default since month the first cases detected.  
    ***example**: ?since=2021.1 or ?since=2021.01*
    >- upto : \<year>.\<month>   
     A parameter that control up to when [year, month] the data will be returned. By default up to current month.  
    ***example**: ?upto=2022.1 or ?upto=2022.01*
* `[GET] http://<host>:<port>/monthly/<year>`  
    Provide monthly cumulative data of total covid cases in the year provided in \<year>. 
    >**Query Params :**
    > - since : \<month>   
     A parameter that control since when [year, month] the data will be returned. By default since first month of the year.   
    ***example**: ?since=1 or ?since=01*
    >- upto : \<month>   
     A parameter that control up to when [year, month] the data will be returned. By default up to the last month of the year.  
    ***example**: ?upto=1 or ?upto=01*
    >> *The \<year> section at query params that instructed in API contract, removed due to redundant parameter because of given \<year> param at the URL path.*      
* `[GET] http://<host>:<port>/monthly/<year>/<month>`  
    Provide monthly data of total covid cases in the exact given \<month> and \<year> .   
* `[GET] http://<host>:<port>/daily`  
    Provide daily cumulative data of total covid cases.  
    >**Query Params :**
    > - since : \<year>.\<month>.\<date>    
     A parameter that control since when [year, month, date] the data will be returned. By default since first day of the year.  
    ***example**: ?since=2020.3.1 or ?since=2020.03.01*
    >- upto : \<year>.\<month>.\<date>   
     A parameter that control up to when [year, month, date] the data will be returned. By default up to the last day of the year.  
    ***example**: ?upto=2022.3.1 or ?upto=2022.03.01*
* `[GET] http://<host>:<port>/daily/<year>`  
    Provide daily cumulative data of total covid cases in the year provided in \<year>. 
    >**Query Params :**
    > - since : \<month>.\<date>   
     A parameter that control since when [year, month, date] the data will be returned. By default since first day cases detected.  ***example**: ?since=2020.3.1 or ?since=2020.03.01*
    >- upto : \<month>.\<date>   
     A parameter that control up to when [year, month, date] the data will be returned. By default up to today.   
    ***example**: ?upto=2022.3.1 or ?upto=2022.03.01*
    >> *The \<year> section at query params that given in API contract, removed due to redundant parameter because of given \<year> param at the URL path.*  
* `[GET] http://<host>:<port>/daily/<year>/<month>`  
    Provide daily cumulative data of total covid cases in the year and month provided in \<year> and \<month>. 
    >**Query Params :**
    > - since : \<date>   
     A parameter that control since when [year, month, date] the data will be returned. By default since first day cases detected.  ***example**: ?since=3.1 or ?since=03.01*
    >- upto : \<date>   
     A parameter that control up to when [year, month, date] the data will be returned. By default up to today.   
    ***example**: ?upto=3.1 or ?upto=03.01*
    >> *The \<year> and \<month> section at query params that given in API contract, removed due to redundant parameter because of given \<year> and \<month> param at the URL path.*  
* `[GET] http://<host>:<port>/daily/<year>/<month>/<date>`  
    Provide daily data of total covid cases in the exact date provided in \<year>, \<month>, \<date>. 
---

