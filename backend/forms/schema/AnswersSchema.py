from forms.schema.AnswersFields import field_schemas

schema = {
	'sections' : {
		'type' : 'list',
		'required' : True,
		'schema' : {
			'type' : 'list',
			'required' : True,
			'schema' : {
				'type' : 'dict',
				'anyof_schema' : field_schemas
			}
		}
	}
}