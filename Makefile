run:
	 @python manage.py runserver
shell:
	@python manage.py shell
cleanmigrations:
	@python manage.py runscript cleanmigrations
initdev:
	@python manage.py runscript initdev
migrate:
	@python manage.py migrate
app:
    ifeq ($(name),)
	$(info usage: make app name=<app_name>)
    else
	$(info App $(name) created)
	@python manage.py startapp $(name)
	@mv $(name) apps/
    endif
	@:
getlocalsettings:
    ifeq ($(config),)
	$(info usage: make getlocalsettings config=<config_path>)
    else
	@curl https://raw.githubusercontent.com/freezmeinster/configtemplate/master/local_settings.py > $(config)/local_settings.py
   endif
	@:
