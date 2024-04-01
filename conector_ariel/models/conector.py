from odoo import _, api, fields, models
import sys
import os
import csv
import psycopg2
import psycopg2.extras
import openpyxl
serverdb = "35.226.101.146"
userdb = "odoo15"
pwddb = "odoo15*"
portdb = 5432
db = "gstr-gstr-20032024-test-12340518"
user = "admin"
password = "IZI4asJr2RI98Ll2"

class ConectorAriel (models.Model):
    _name="conector.ariel"
    
    def vincular_parroquia(self):

        connection = psycopg2.connect(host=serverdb, database=db, user=userdb, password=pwddb, port=5432)
        cursor = connection.cursor()
        print ("Conexion correcta")

        sql = "select product_id ,quantity from  stock_valuation_layer pp  where quantity  =1;"
        #Validar id con el de app ariel
        cursor.execute(sql)
        parish_list = cursor.fetchall()
        print(parish_list, "FIN >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")