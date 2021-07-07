date_schema = {
	'field_type' : {'type' : 'string', 'allowed' : ['date'], 'required' : True},
	'default' : {'type' : 'string'},
	'begin' : {'type' : 'string'},
	'end' : {'type' : 'string', 'greater_than_equal' : 'begin'},
}

datetime_schema = {
	'field_type' : {'type' : 'string', 'allowed' : ['datetime'], 'required' : True},
	'default' : {'type' : 'string'},
	'begin' : {'type' : 'string'},
	'end' : {'type' : 'string', 'greater_than_equal' : 'begin'},
}

longtext_schema = {
	'field_type' : {'type' : 'string', 'allowed' : ['longtext'], 'required' : True},
	'default' : {'type' : 'string'},
	'placeholder' : {'type' : 'string'},
	'min_length' : {'type' : 'integer'},
	'max_length' : {'type' : 'integer', 'greater_than_equal' : 'min_length'},
	'default_lines' : {'type' : 'integer'}
}

shorttext_schema = {
	'field_type' : {'type' : 'string', 'allowed' : ['shorttext'], 'required' : True},
	'default' : {'type' : 'string'},
	'placeholder' : {'type' : 'string'},
	'min_length' : {'type' : 'integer'},
	'max_length' : {'type' : 'integer', 'greater_than_equal' : 'min_length'},
	#'sensitive' : {'type' : 'boolean'}
}

multiplechoice_schema = {
	'field_type' : {'type' : 'string', 'allowed' : ['multiplechoice'], 'required' : True},
	'default' : {'type' : 'integer'},
	'options' : {'type' : 'list', 'schema': {
								'type': 'dict', 
								'schema' : {
												'id' : {'type' : 'integer', 'required' : True},
												'question' : {'type' : 'string', 'required' : True},
												'default' : {'type' : 'boolean'}
								}
							}, 'required' : True
	},
	'style' : {'type': 'string', 'allowed' : ['radio', 'dropdown'], 'required' : True},
	'allowed_other' : {'type' : 'boolean', 'dependencies' : {'style' : 'radio'}}, #, 'dependencies' : 'other_string'
	'other_string' : {'type' : 'string', 'dependencies' : {'allowed_other' : True}},
	'placeholder' : {'type' : 'string', 'dependencies' : {'allowed_other' : True}},
	'min_length' : {'type' : 'integer', 'dependencies' : {'allowed_other' : True}},
	'max_length' : {'type' : 'integer', 'greater_than_equal' : 'min_length', 'dependencies' : {'allowed_other' : True}}
}

selectboxes_schema = {
	'field_type' : {'type' : 'string', 'allowed' : ['selectboxes'], 'required' : True},
	'default' : {'type' : 'list', 'schema': {'type': 'integer'}},
	'options' : {'type' : 'list', 'schema': {
								'type': 'dict', 
								'schema' : {
												'id' : {'type' : 'integer', 'required' : True},
												'question' : {'type' : 'string', 'required' : True},
												'default' : {'type' : 'boolean'}
								}
							}, 'required' : True
	},
	'min_selected' : {'type' : 'integer', 'min' : 1},
	'max_selected' : {'type' : 'integer', 'greater_than_equal' : 'min_selected'},
	'allowed_other' : {'type' : 'boolean'}, #, 'dependencies' : 'other_string'
	'max_other' : {'type' : 'integer', 'dependencies' : {'allowed_other' : True}},
	'other_string' : {'type' : 'string', 'dependencies' : 'allowed_other'},
	'placeholder' : {'type' : 'string', 'minlength' : 1, 'dependencies' : {'allowed_other' : True}},
	'min_length' : {'type' : 'integer', 'dependencies' : {'allowed_other' : True}},
	'max_length' : {'type' : 'integer', 'greater_than_equal' : 'min_length', 'dependencies' : {'allowed_other' : True}},
}

number_schema = {
	'field_type' : {'type' : 'string', 'allowed' : ['number'], 'required' : True},
	'default' : {'type' : 'number'},
	'placeholder' : {'type' : 'string'},
	'min' : {'type' : 'integer'},
	'max' : {'type' : 'integer', 'greater_than_equal' : 'min'},
	'decimal_places' : {'type' : 'integer'},
	'prefix' : {'type' : 'string'},
	'suffix' : {'type' : 'string'},
	'style' : {'type': 'string', 'allowed' : ['text', 'slider'], 'required' : True},
}

phone_schema = {
	'field_type' : {'type' : 'string', 'allowed' : ['phone'], 'required' : True},
	'default' : {'type' : 'integer'},
	'placeholder' : {'type' : 'string'},
}

nif_schema = {
	'field_type' : {'type' : 'string', 'allowed' : ['nif'], 'required' : True},
	'default' : {'type' : 'integer'},
	'placeholder' : {'type' : 'string'},
}

email_schema = {
	'field_type' : {'type' : 'string', 'allowed' : ['email'], 'required' : True},
	'default' : {'type' : 'string'},
	'placeholder' : {'type' : 'string'},
}

# EXPOSITION

exposition_schema = {
	'field_type' : {'type' : 'string', 'allowed' : ['text_exposition', 'youtube_exposition'], 'required' : True},
	'content' : {'type' : 'string'} 
}


field_schemas = [date_schema, datetime_schema, longtext_schema, shorttext_schema, multiplechoice_schema, selectboxes_schema, number_schema, nif_schema, phone_schema, email_schema, exposition_schema]