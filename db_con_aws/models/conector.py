from odoo import _, api, fields, models
import subprocess
import boto3

class ConectorDatabase (models.Model):
    _name="conector.database.aws"
    
    def conexion_aws(self):
        #Credenciales USR 1
        # aws_access_key_id = 'AKIAQOR5FLNKE44WCA6X'
        # aws_secret_access_key = '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'
        # region_name = 'us-west-1'
        
        #Credenciales USR 2
        aws_access_key_id = 'AKIAQOR5FLNKMXGCJVXI'
        aws_secret_access_key = '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'
        region_name = 'us-west-1'   
        
        querty_a = "SELECT name FROM purchase_order WHERE state not like ('cancel');"

        # Ejecutar el comando SQL
        subprocess.run(f'psql -c "{querty_a}" humanytek-gser-prod-4491709 > /home/odoo/arieldata/orders_odoo.txt', shell=True)
        print("Creo archivo en odoo .sh>>>>>>>>>>>>>>>>>>>>>>>>")
        subprocess.run('en', shell=True)
        
        # Conecta a tu instancia de base de datos RDS
        client = boto3.client('rds', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name=region_name)
        print("Conecta a tu instancia de base de datos RDS >>>>>>>>>>>>>>>>>>>>>>>>") 
        # Copia el archivo a un bucket de Amazon S3
        s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name=region_name)
        s3.upload_file('/home/odoo/arieldata/orders_odoo.txt', 'odoofiles', 'orders_odoo.txt')
        print("Copia el archivo a un bucket de Amazon S3 >>>>>>>>>>>>>>>>>>>>>>>>")

        querty_b = """WITH productos_activos AS (
    SELECT 
        sq.product_id, 
        SUM(sq.quantity) AS total_quantity
    FROM 
        stock_quant sq
    JOIN 
        stock_location sl ON sq.location_id = sl.id
    WHERE 
        sl.usage = 'internal'
    GROUP BY 
        sq.product_id
)
SELECT 
    pp.product_tmpl_id, 
    pt.default_code AS reference, 
    pt.name AS product_name, 
    COALESCE(pa.total_quantity, 0) AS product_quantity,
    pt.uom_id AS Unit_measure
FROM 
    product_product pp
LEFT JOIN 
    productos_activos pa ON pp.id = pa.product_id
JOIN 
    product_template pt ON pp.product_tmpl_id = pt.id;"""

        # Ejecutar el comando SQL
        subprocess.run(f'psql -c "{querty_b}" humanytek-gser-prod-4491709 > /home/odoo/arieldata/cant_prod.txt', shell=True)
        print("Creo archivo en odoo .sh>>>>>>>>>>>>>>>>>>>>>>>>")
        subprocess.run('en', shell=True)
        
        # Conecta a tu instancia de base de datos RDS
        client = boto3.client('rds', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name=region_name)
        print("Conecta a tu instancia de base de datos RDS >>>>>>>>>>>>>>>>>>>>>>>>") 
        # Copia el archivo a un bucket de Amazon S3
        s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name=region_name)
        s3.upload_file('/home/odoo/arieldata/cant_prod.txt', 'odoofiles', 'cant_prod.txt')
        print("Copia el archivo a un bucket de Amazon S3 >>>>>>>>>>>>>>>>>>>>>>>>")
        
