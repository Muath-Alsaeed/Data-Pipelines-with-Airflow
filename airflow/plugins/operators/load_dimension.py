from airflow.hooks.postgres_hook import PostgresHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults

class LoadDimensionOperator(BaseOperator):

    ui_color = '#80BD9E'

    @apply_defaults
    def __init__(self,
                 
                 redshift_conn_id = ''
                 sql_command = '' ,
                 table = '',
                 truncate=False,
                 *args, **kwargs):

        super(LoadDimensionOperator, self).__init__(*args, **kwargs)
        self.redshift_conn_id = redshift_conn_id
        self.sql_command = sql_command
        self.table = table
        self.truncate = truncate
        

    def execute(self, context):
        self.log.info(f'loading {self.table} start !')
        
        redshift = PostgresHook (postgres_conn_id = redshift_conn_id)
        if self.truncate:
            self.log.info(f"truncate table: {self.table}")
        redshift.run(self.sql_command)
        self.log.info(f"finsh  loading {self.table} table  into Redshift")
