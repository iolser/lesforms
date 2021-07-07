date_schema = {
	'field_type' : {'type' : 'string', 'allowed' : ['date'], 'required' : True},
	'answer' : {'type' : 'string'}
}

datetime_schema = {
	'field_type' : {'type' : 'string', 'allowed' : ['datetime'], 'required' : True},
	'answer' : {'type' : 'string'}
}

longtext_schema = {
	'field_type' : {'type' : 'string', 'allowed' : ['longtext'], 'required' : True},
	'answer' : {'type' : 'string'}
}

shorttext_schema = {
	'field_type' : {'type' : 'string', 'allowed' : ['shorttext'], 'required' : True},
	'answer' : {'type' : 'string'}
}

multiplechoice_schema = {
	'field_type' : {'type' : 'string', 'allowed' : ['multiplechoice'], 'required' : True},
	'answer' : {'type' : ['integer', 'string']}
}

selectboxes_schema = {
	'field_type' : {'type' : 'string', 'allowed' : ['selectboxes'], 'required' : True},
	'answer' : {'type' : 'list', 'schema': {'type': ['integer', 'string'], 'required' : True}}
}

number_schema = {
	'field_type' : {'type' : 'string', 'allowed' : ['number'], 'required' : True},
	'answer' : {'type' : 'number'}
}

phone_schema = {
	'field_type' : {'type' : 'string', 'allowed' : ['phone'], 'required' : True},
	'answer' : {'type' : 'number'}
}

nif_schema = {
	'field_type' : {'type' : 'string', 'allowed' : ['nif'], 'required' : True},
	'answer' : {'type' : 'number'}
}

email_schema = {
	'field_type' : {'type' : 'string', 'allowed' : ['email'], 'required' : True},
	'answer' : {'type' : 'string'}
}

exposition_schema = {
	'field_type' : {'type' : 'string', 'allowed' : ['text_exposition', 'youtube_exposition'], 'required' : True}
}

field_schemas = [date_schema, datetime_schema, longtext_schema, shorttext_schema, multiplechoice_schema, selectboxes_schema, number_schema, nif_schema, phone_schema, email_schema, exposition_schema]