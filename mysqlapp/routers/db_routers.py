class MysqlRouter:
    route_app_labels = { 'auth', 'contenttypes', 'sessions', 'admin', 'mysqlapp' }
    
    def db_for_read(self, model, **hints):
        """[Functions for read from the database]

        Args:
            model: [Database Model name]
            hints: [hints as Dictionary arguments]
        """
        if model._meta.app_label in self.route_app_labels:
            return 'mysql_db'
        return None

    def db_for_write(self, model, **hints):
        """[Functions for to write in the database]

        Args:
            model: [Database Model name]
            hints: [hints as Dictionary arguments]
        """
        if model._meta.app_label in self.route_app_labels:
            return 'mysql_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """[Function to create Model Relationship buildint]

        Args:
            obj1 ([type]): [model]
            obj2 ([type]): [model]
        """

        if (
            obj1._meta.app_label in self.route_app_labels or
            obj2._meta.app_label in self.route_app_labels
        ):
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):

        if app_label in self.route_app_labels:
            return db == 'mysql_db'
        return None