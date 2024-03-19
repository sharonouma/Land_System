from flask_table import Table, Col, LinkCol

class LandOwners(Table):
    user_id = Col('Id', show=False)
    user_name = Col('Name')
    user_email = Col('Email')
    phone_number = Col('Mobile')
    user_password = Col('Password', show=False)
    edit = LinkCol('Edit', 'main.edit_view', url_kwargs=dict(id='user_id'))
    add_title_deed = LinkCol('Add Title Deed', 'main.add_title_deed_view', url_kwargs=dict(id='user_id'))
    delete = LinkCol('Delete', 'main.delete_user', url_kwargs=dict(id='user_id'))
    

class TitleDeeds(Table):
    owner_id = Col('Id', show=False)
    location = Col('Location')
    area = Col('Area')
    plot_number = Col('Plot No')
    serial_no = Col('Serial No')
    documentation_number = Col('Documentation No')
    nature_of_title = Col('Nature of Title')
    issue_date= Col('Issue Date')