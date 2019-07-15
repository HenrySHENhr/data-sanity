import os

SCRIPT_FILE_PATH = "script.js"


def render_to_js(query):
    """

    :param query:
    :return:
    """
    project_working_directory = os.getcwd()
    script_file = os.path.join(project_working_directory, SCRIPT_FILE_PATH)

    # Parse mongo query and add printjson() to the last query
    index = str(query).rindex('db.')
    query = query[:index] + 'printjson(' + query[index:] + ');'

    try:
        with open(script_file, mode='w') as scriptfile:
            scriptfile.writelines('rs.slaveOk();\n')
            scriptfile.writelines(query)
    except Exception as e:
        print(str(e))
