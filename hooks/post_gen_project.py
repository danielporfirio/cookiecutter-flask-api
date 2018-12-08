
    print("""
################################################################################
################################################################################
    You have succesfully created `{{ cookiecutter.project_slug }}`.
################################################################################
    You've used these cookiecutter parameters:
{% for key, value in cookiecutter.items()|sort %}
        {{ "{0:26}".format(key + ":") }} {{ "{0!r}".format(value).strip("u") }}
{%- endfor %}
################################################################################
    To get started run these:
        cd {{ cookiecutter.project_slug }}
        git init
        git add --all
        git commit -m "Add initial project skeleton."
        git remote add origin git@github.com:your_github_username/{{ cookiecutter.project_slug }}.git
        git push -u origin master
""")