import jinja2, os
from pathlib import Path
from faker import Faker
from faker.providers import file

fake = Faker()
fake.add_provider(file)


class MetaDataTable:

    def __init__(self, template, app, file) -> None:
        self.template = template
        self.app = app
        self.file = file
        self.columns_types = os.environ.get('CREATE_COUNT_METADATA_DATABASE_COLUMNS_TYPES', 'Char').replace(' ', '').split(',')
        self.count_columns = os.environ.get('CREATE_COUNT_METADATA_DATABASE_COLUMNS', 0)
        self.cont_fk = os.environ.get('CREATE_COUNT_METADATA_DATABASE_COLUNNS_FK', 0)
        self.count_tables = os.environ.get('CREATE_COUNT_METADATA_DATABASE', 0)
        self.count_views = os.environ.get('CREATE_COUNT_METADATA_DATABASE_VIEWS', 0)
        self.count_views_table = os.environ.get('CREATE_COUNT_METADATA_DATABASE_VIEWS_TABLE', 2)
        self.count_views_table_col = os.environ.get('CREATE_COUNT_METADATA_DATABASE_VIEWS_TABLE_COLUMNS', -1)

    def resource_path(self, *relative_path):
        """ Get absolute path to resource"""
        return Path(os.getcwd(), *relative_path)


    def render_template(self, context):
        templateLoader = jinja2.FileSystemLoader(searchpath="./templates/")
        environment = jinja2.Environment(loader=templateLoader)
        results_template = environment.get_template(self.template)
        with open(Path(self.resource_path("app"), self.app, "models.py").__str__(), mode="w", encoding="utf-8") as results:
            results.write(results_template.render(context))

    ## CREATE META MODELS

    def column_types_generator(self, type_list):
        #t = os.environ.get('CREATE_COUNT_METADATA_DATABASE_COLUMNS_TYPES', '').replace(' ', '').split(',')
        for type in type_list:
            yield type


    def column_generator(self):
        column_types = self.column_types_generator(self.columns_types)
        for c in range(int(self.count_columns)):
            try:
                column_type = next(column_types)
            except StopIteration:
                column_types = self.column_types_generator(self.columns_types)
                column_type = next(column_types)

            yield {
                "name": f"col_{c}_" + fake.file_name(extension='').replace('.', '_') ,
                "type": column_type
            }

    def table_generator(self):
        for _ in range(int(self.count_tables)):
            yield {
                    "table": str( str(fake.name().replace(' ', '').replace('.', '')) + "Model"), 
                    "columns": list(self.column_generator())
            }  

    def meta_table_table_generator(self, meta):
        for i, item in enumerate(meta):
            yield i, item.get("table")

    def meta_table_column_generator(self, meta):
        for i, item in enumerate(meta):
            yield i, item.get("name")

    def generate_view(self, meta):
        return meta

    def generate_table(self):
        meta = list(self.table_generator())
        meta_tables = self.meta_table_table_generator(meta)
        count_fk = int(self.cont_fk)
        offsets = 0
        parent_table_index, parent_table_name = next(meta_tables)
        print("FK COUNT", count_fk)
        while count_fk > 0:
            try:
                print("PARENT", parent_table_index, parent_table_name)
                fk_table_index, fk_table_name = next(meta_tables)
                for _ in range(offsets):
                    parent_table_index, parent_table_name = next(meta_tables)
                print("FK", fk_table_index, fk_table_name)
                meta_columns_fk = self.meta_table_column_generator(meta[fk_table_index]["columns"])
                try:

                    col_inex_fk, col_name_fk = next(meta_columns_fk)                    
                    print("FKCOL", col_inex_fk, col_name_fk)
                    print("FKMETA", meta[fk_table_index]["columns"][col_inex_fk])
                    meta[fk_table_index]["columns"][col_inex_fk + offsets]["fk"] = parent_table_name
                    count_fk = count_fk - 1
                    print("CHINK", count_fk, offsets)
                except StopIteration:
                    print("FK StopIteration")
                    pass
                parent_table_index, parent_table_name = [fk_table_index, fk_table_name ]
            except StopIteration:
                offsets = offsets + 1
                meta_tables = self.meta_table_table_generator(meta)

        return meta

    def generate(self):
        meta = self.generate_table()
        meta = self.generate_view(meta)
        self.render_template({"meta": meta})


if __name__ == "__main__":
    gen = MetaDataTable("database.model", "faker_meta_db", "models.py")
    gen.generate()